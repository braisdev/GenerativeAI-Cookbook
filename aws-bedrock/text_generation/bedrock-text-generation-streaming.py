import json

import boto3

# Create a Bedrock runtime client in the AWS of your choice
client = boto3.client("bedrock-runtime", region_name="us-east-1")

# Set the model ID, e.g, Claude Instant
model_id = "anthropic.claude-instant-v1"

# Define a prompt for the model
prompt = """
Task: Compose an email from Alice, Head of Client Relations, to the client "Mark Taylor"
who expressed dissatisfaction with the technical support provided.
"""

# Format the request payload using the model's native structure
native_request = {
    "anthropic_version": "bedrock-2023-05-31",
    "max_tokens": 4096,
    "temperature": 0,
    "messages": [
        {
            "role": "user",
            "content": [{"type": "text", "text": prompt}],
        }
    ],
}

# Convert the native request to JSON.
request = json.dumps(native_request)

# Invoke the model with the request.
streaming_response = client.invoke_model_with_response_stream(
    modelId=model_id, body=request
)

# Extract and print the response text in real-time.
for event in streaming_response["body"]:
    chunk = json.loads(event["chunk"]["bytes"])
    if chunk["type"] == "content_block_delta":
        print(chunk["delta"].get("text", ""), end="")
