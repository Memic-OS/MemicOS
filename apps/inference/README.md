#### memicos 🧠🔍 inference server

- [what this is](#what-this-is)
- [repo status](#repo-status)
- [setup + run - non-docker](#setup--run---non-docker)
  - [customizing the inference server (different models, SAEs, etc)](#customizing-the-inference-server-different-models-saes-etc)
  - [loading specific saes from saelens](#loading-specific-saes-from-saelens)
  - [developing the inference client](#developing-the-inference-client)
- [setup + run - docker](#setup--run---docker)
- [setup + run - kubernetes](#setup--run---kubernetes)
- [usage examples](#usage-examples)
  - [get activations for a single feature and prompt](#get-activations-for-a-single-feature-and-prompt)
  - [get cosine similarities](#get-cosine-similarities)
  - [steering example gpt2-small res-jb](#steering-example-gpt2-small-res-jb)

## what this is

python server that supports memicos's inference capabilities - steering, testing activations, search via inference, etc.

it can be a standalone server. it does not require memicos to run.

it optionally uses [saelens](https://github.com/jbloomAus/SAELens) to pre-load saes into memory and perform inference.

saelens is not required. it can also just load models and perform inference using steering vectors that are passed into the request.

as much as possible, we try to use classes/types from the `packages/python/memicos-inference-client`, which is autogenerated from the openapi spec under `openapi/schemas/openapi/inference-server.yaml`

## repo status

- we would like to move toward supporting `nnsight` in addition to `saelens`/`transformerlens` would like to collaborate with ndif on this

> ⚠️ **warning:** this is _draft_ documentation. we expect to either have better readmes or use a hosted documentation website.

## setup + run - non-docker

this loads the `gpt2-small` model and the `res-jb` saes through saelens:

```
poetry lock && poetry install
poetry run python start.py
```

### customizing the inference server (different models, SAEs, etc)

open the `start.py` script to see the flags that memicos reads either from the arguments or from the environment variables.

### loading specific saes from saelens

example of loading model `gemma-2-2b` and a gemmascope sae using arguments

```
poetry run python start.py \
  --model_id gemma-2-2b \
  --sae_sets gemmascope-res-16k \
  --model_dtype bfloat16 \
  --sae_dtype bfloat16
```

you'll notice we use the `model_id` and `sae_sets` flags to set which SAE to load from saelens.

you can run the following to get the currently supported models and saes

```
poetry run python start.py --list_models
```

the `model_id` is the model id from the [transformerlens model table](https://transformerlensorg.github.io/TransformerLens/generated/model_properties_table.html) and `sae_sets` is the text after the layer number and hyphen in a memicos source ID - for example, if you have a memicos feature at url `http://memicos.org/gpt2-small/0-res-jb/123`, the `0-res-jb` is the source ID, and the `sae_sets` is `res-jb`.

you can also find memicos source IDs in the saelens [pretrained saes yaml file](https://github.com/jbloomAus/SAELens/blob/main/sae_lens/pretrained_saes.yaml) or by clicking into models in the [memicos datasets exports](https://memicos-datasets.s3.us-east-1.amazonaws.com/index.html?prefix=v1/) directory.

### developing the inference client

if you are making changes to the openapi spec (new/updated endpoints) and want to test those changes locally, generate your client and use the following command to point to the local inference client:

```
# switch to local inference client
poetry remove memicos-inference-client && poetry add ../../packages/python-inference-client/

# switch back to pypi/production inference client
poetry remove memicos-inference-client && poetry add memicos-inference-client`
```

## setup + run - docker

1. ensure you are in the monorepo root directory (not this directory)
2. build
   1. CPU: `docker build --platform=linux/amd64 -t memicos-inference:cpu -f apps/inference/Dockerfile --build-arg BUILD_TYPE=nocuda .`
   2. GPU: `docker build --platform=linux/amd64 -t memicos-inference:gpu -f apps/inference/Dockerfile --build-arg BUILD_TYPE=cuda .`
3. run
   1. CPU

```

docker run \
 -p 5002:5002 \
 -e SECRET=secret \
 -e MODEL_ID=gpt2-small \
 -e SAE_SETS='["res-jb"]' \
 memicos-inference:cpu

```

2. GPU

```

docker run \
 --gpus all \
 -p 5002:5002 \
 -e SECRET=secret \
 -e MODEL_ID=gpt2-small \
 -e SAE_SETS='["res-jb"]' \
 memicos-inference:gpu

```

4. tag and push to a repo (google cloud example)

```

# tag + push cpu

docker tag memicos-inference:cpu gcr.io/$(gcloud config get-value project)/memicos-inference:cpu
   docker push gcr.io/$(gcloud config get-value project)/memicos-inference:cpu

# tag + push gpu

docker tag memicos-inference:gpu gcr.io/$(gcloud config get-value project)/memicos-inference:gpu
   docker push gcr.io/$(gcloud config get-value project)/memicos-inference:gpu

```

## setup + run - kubernetes

see `./k8s/README.md` for our current kubernetes setup on google cloud.

## usage examples

all endpoints are documented under `schemas/openapi/inference-server.yaml`. some usage examples below:

### get activations for a single feature and prompt

```bash
curl -X POST http://127.0.0.1:5002/v1/activation/single \
-H "Content-Type: application/json" \
-d '{
 "prompt": "this is about dogs!",
 "model": "gemma-2-2b",
 "source": "20-gemmascope-res-16k",
 "index": 12082
}'
```

you'll get the following response

```json
{
  "activation": {
    "values": [0, 0, 0, 0, 70.5, 48.25],
    "max_value": 70.5,
    "max_value_index": 4,
    "dfa_values": null,
    "dfa_max_value": null,
    "dfa_target_index": null
  },
  "tokens": ["<bos>", "this", " is", " about", " dogs", "!"]
}
```

### get cosine similarities

```bash
curl -X POST http://127.0.0.1:5002/v1/util/sae-topk-by-decoder-cossim \
  -H "Content-Type: application/json" \
  -d '{
    "feature": {
      "model": "gemma-2-2b",
      "source": "20-gemmascope-res-16k",
      "index": 12082
    },
    "model": "gemma-2-2b",
    "source": "20-gemmascope-res-16k",
    "num_results": 10
  }'
```

### steering example gpt2-small res-jb

dog feature

```bash
curl -X POST http://127.0.0.1:5002/v1/steer/completion \
  -H "Content-Type: application/json" \
  -d '{
     "prompt": "I often think about",
     "model": "gpt2-small",
     "features": [
       {
         "model": "gpt2-small",
         "source": "7-res-jb",
         "index": 5919,
         "strength": 27
       }
     ],
     "types": [
       "STEERED"
     ],
     "n_completion_tokens": 16,
     "temperature": 0.5,
     "strength_multiplier": 1.5,
     "freq_penalty": 1,
     "seed": 16,
     "steer_method": "SIMPLE_ADDITIVE",
     "normalize_steering": false
   }'
```

## Testing, Linting, and Formatting

This project uses [pytest](https://docs.pytest.org/en/stable/) for testing, [pyright](https://github.com/microsoft/pyright) for type-checking, and [Ruff](https://docs.astral.sh/ruff/) for formatting and linting.

If you add new code, it would be greatly appreciated if you could add tests in the `tests` directory. You can run the tests with:

```bash
make test
```

Before commiting, make sure you format the code with:

```bash
make format
```

Finally, run all CI checks locally with:

```bash
make check-ci
```

If these pass, you're good to go! Open a pull request with your changes.
