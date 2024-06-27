import json

import boto3
from botocore.exceptions import ClientError

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

try:
    # Invoke the model with the request
    response = client.invoke_model(modelId=model_id, body=request)

except (ClientError, Exception) as e:
    print(f"ERROR: Can't invoke '{model_id}'. Reason: {e}")
    exit(1)

# Decode the response body.
model_response = json.loads(response["body"].read())

# Extract and print the response text.
response_text = model_response["content"][0]["text"]
print(response_text)
