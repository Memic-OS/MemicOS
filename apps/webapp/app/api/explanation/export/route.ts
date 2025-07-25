import { RequestOptionalUser, withOptionalUser } from '@/lib/with-user';
import { NextResponse } from 'next/server';
import { object, string, ValidationError } from 'yup';

const querySchema = object({
  modelId: string().required(),
  saeId: string().required(),
});

/**
@swagger
{
  "/api/explanation/export": {
    "get": {
      "tags": [
        "Explanations"
      ],
      "summary": "Export Explanations",
      "security": [{
          "apiKey": []
      }],
      "description": "Exports all explanations for a specific SAE. Warning: This can be a large response (>3 megabytes).",
      "parameters": [
        {
          "in": "query",
          "name": "modelId",
          "required": true,
          "schema": {
            "type": "string",
            "default": "gpt2-small"
          },
          "description": "The model ID to that the SAE is for. For example, gpt2-small."
        },
        {
          "in": "query",
          "name": "saeId",
          "required": true,
          "schema": {
            "type": "string",
            "default": "6-res-jb"
          },
          "description": "The SAE ID to export explanations for. For example, 6-res-jb."
        }
      ],
      "responses": {
        "200": {
          "description": "OK",
          "content": {
            "application/json": {
              "schema": {
                "type": "array",
                  "items": {
                    "$ref": "#/components/schemas/Explanation"
                  }
              }
            }
          }
        }
      }
    }
  }
}
*/
export const GET = withOptionalUser(async (request: RequestOptionalUser) => {
  const url = new URL(request.url);
  const modelId = url.searchParams.get('modelId');
  const saeId = url.searchParams.get('saeId');

  try {
    const params = await querySchema.validate({ modelId, saeId });
    console.log(`Exporting explanations for modelId ${params.modelId} saeId ${params.saeId}`);
    const s3Url = `https://memicos-exports.s3.amazonaws.com/explanations-only/${params.modelId}_${params.saeId}.json`;
    const response = await fetch(s3Url, {
      method: 'HEAD',
    });
    if (response.ok) {
      // file exists, redirect user to it
      return NextResponse.redirect(s3Url);
    }
    // file does not exist, return error
    return NextResponse.json(
      {
        message:
          "We don't yet have an explanation export for this model and SAE. Please contact support@memicos.org if you need this now and we'll get it to you ASAP.",
      },
      { status: 404 },
    );
  } catch (error) {
    if (error instanceof ValidationError) {
      return NextResponse.json({ message: error.message }, { status: 400 });
    }
    return NextResponse.json(
      {
        message:
          "We don't yet have an explanation export for this model and SAE. Please contact support@memicos.org if you need this now and we'll get it to you ASAP. Alternatively, double-check the exports directory to see if it's there: https://memicos-exports.s3.amazonaws.com/index.html",
      },
      { status: 404 },
    );
  }
});
