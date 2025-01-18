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

# Process the response
if response.status_code == 200:
    try:
        # Parse the response line by line
        lines = response.text.splitlines()
        content = ""  # Collect all 'content' values here
        
        for line in lines:
            # Parse each line as JSON
            parsed_line = json.loads(line)
            if "message" in parsed_line and "content" in parsed_line["message"]:
                content += parsed_line["message"]["content"]  # Append the content
        
        # Print the formatted content
        print("Formatted Content:\n")
        print(content)
    except json.JSONDecodeError as e:
        print(f"Error parsing response: {e}")
        print("Raw response:\n", response.text)
else:
    print(f"Request failed with status code: {response.status_code}")
    print(f"Response content: {response.text}")

# combined_data = []

# if response.status_code == 200:
#     try:
#         # Split the response content by lines
#         response_lines = response.text.splitlines()
        
#         for line in response_lines:
#             if line.strip():  # Ignore empty lines
#                 # Parse each JSON object separately
#                 data = json.loads(line)
#                 # print(data)  # Print each parsed JSON object
#                 combined_data.append(data)
#                 print(data)
                
#                 # Example access (adjust based on your response structure)
#                 if "content" in combined_data:
#                     print(combined_data["content"])
#     except json.JSONDecodeError as e:
#         print(f"Error decoding JSON: {e}")
# else:
#     print(f"Request failed with status code: {response.status_code}")


# print(f"Combined Data: {combined_data}")


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