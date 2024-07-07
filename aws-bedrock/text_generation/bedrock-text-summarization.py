import json

import boto3

from botocore.exceptions import ClientError

# Create a Bedrock runtime client in the AWS of your choice
client = boto3.client("bedrock-runtime", region_name="us-east-1")

# Set the Model ID, e.g, Claude Instant
model_id = "anthropic.claude-instant-v1"

# Define a prompt for the model
prompt = """
Please provide a summary of the following text. Do not add any information that is not mentioned in the text below.

<text> The Eiffel Tower is a wrought-iron lattice tower on the border of France and Italy, lying atop the Paris 
region on the northern edge of France. It is named after the engineer Gustave Eiffel, whose company design and built 
this tower. The tower is structured in a style similar to that of a cathedral, with a dome and a cupola. The tower is 
324 meters (1,296 ft) tall, about the same height as the top of the Eiffel Tower in Paris, and is the tallest 
structure in the Paris region. The tower is open to the public and is a must-see attraction in Paris. 
</text>
"""

# Format the request payload using the model's native structure
request_body = {
    "anthropic_version": "bedrock-2023-05-31",
    "max_tokens": 4096,
    "messages": [
        {
            "role": "user",
            "content": [{"type": "text", "text": prompt}],
        }
    ],
}

# Convert the native request to JSON
request = json.dumps(request_body)

try:
    # Invoke the model with the request
    response = client.invoke_model(modelId=model_id, body=request)

except (ClientError, Exception) as e:
    print(f"ERROR: Can't invoke '{model_id}'. Reason: {e}")
    exit(1)

model_response = json.loads(response["body"].read())

# Extract and print the response text.
response_text = model_response["content"][0]["text"]
print(response_text)

