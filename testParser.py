import requests
import json

# Set up the base URL for the local Ollama API
url = "http://localhost:11434/api/chat"

# Define the payload (your input prompt)
payload = {
    "model": "gameTest11",  # Replace with the model name you're using
    "messages": [{"content": "Start game!"}]
}

# Send the HTTP POST request with streaming disabled
response = requests.post(url, json=payload, stream=False)

if response.status_code == 200:
    try:
        # Split the response content by lines
        response_lines = response.text.splitlines()
        
        for line in response_lines:
            if line.strip():  # Ignore empty lines
                # Parse each JSON object separately
                data = json.loads(line)
                print(data)  # Print each parsed JSON object
                
                # Example access (adjust based on your response structure)
                if "content" in data:
                    print(data["content"])
    except json.JSONDecodeError as e:
        print(f"Error decoding JSON: {e}")
else:
    print(f"Request failed with status code: {response.status_code}")


# # Check the response status
# if response.status_code == 200:
#     print()
#     for line in response.iter_lines(decode_unicode=True):
#         if line:  # Ignore empty lines
#             try:
#                 # Parse each line as a JSON object
#                 json_data = json.loads(line)
#                 # Extract and print the assistant's message content
#                 if "message" in json_data and "content" in json_data["message"]:
#                     print(json_data["message"]["content"], end="")
#             except json.JSONDecodeError:
#                 print(f"\nFailed to parse line: {line}")
#     print()  # Ensure the final output ends with a newline
# else:
#     print(f"Error: {response.status_code}")
#     print(response.text)