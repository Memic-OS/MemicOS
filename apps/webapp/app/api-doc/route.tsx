import { getApiDocs } from '@/lib/swagger';
import { ApiReference } from '@scalar/nextjs-api-reference';

const spec = await getApiDocs();

export const GET = ApiReference({
  spec: { content: spec },
  theme: 'alternate',
  tagsSorter: 'alpha',
  operationsSorter: 'alpha',
  hideDownloadButton: true,
  metaData: {
    title: 'MemicOS API Reference',
    description: 'API reference for the MemicOS API',
    ogDescription: 'API reference for the MemicOS API',
    ogTitle: 'MemicOS API Reference',
  },
  hiddenClients: {
    c: true,
    clojure: true,
    crystal: true,
    csharp: true,
    kotlin: true,
    objc: true,
    ocaml: true,
    php: true,
    r: true,
  },
  defaultHttpClient: {
    targetKey: 'python',
    clientKey: 'requests',
  },
  hideModels: true,
  defaultOpenAllTags: true,
});
