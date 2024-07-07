import json
import boto3
import base64


# Function to convert image to base64
def convert_image_to_base64(image_path):
    with open(image_path, "rb") as image_file:
        return base64.b64encode(image_file.read()).decode('utf-8')


# Path to your image
image_path = "/Users/brais.maneiro/Documents/z-personal/0-workspace/0-github/GenerativeAI-Cookbook/src/images/beach.jpg"

# Convert the image to base64
image_base64_string = convert_image_to_base64(image_path)

bedrock_runtime = boto3.client("bedrock-runtime", region_name="us-east-1")

modelId = "anthropic.claude-3-sonnet-20240229-v1:0"

prompt_config = {
    "anthropic_version": "bedrock-2023-05-31",
    "max_tokens": 4096,
    "messages": [
        {
            "role": "user",
            "content": [
                {
                    "type": "image",
                    "source": {
                        "type": "base64",
                        "media_type": "image/png",
                        "data": image_base64_string},
                },

                {
                    "type": "text",
                    "text": "Please describe the image"
                }
            ]
        }
    ]
}

body = json.dumps(prompt_config)

accept = "application/json"
contentType = "application/json"

response = bedrock_runtime.invoke_model(
    body=body,
    modelId=modelId,
    accept=accept,
    contentType=contentType
)

# Parse the response
response_body = json.loads(response.get("body").read())
results = response_body.get("content")[0].get("text")

# Print the result
print(results)
