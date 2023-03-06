web iOS android tablet and mobile

import requests
import json

# Your own API server URL
url = "http://www.aidriveone.com/api/v1/AiDriveGPT"

# Replace the credentials with your own API credentials
headers = {
    "Content-Type": "application/json",
    "Authorization": "Bearer YOUR_API_KEY"
}

# Function to send a message to the AiDriveGPT API and return the response
def send_message(message):
    payload = {
        "message": message
    }
    response = requests.post(url, headers=headers, data=json.dumps(payload))
    return response.json()

# Main loop to run the AiDriveGPT
while True:
    # Get user input
    user_input = input("You: ")

    # Send user input to the AiDriveGPT API
    response = send_message(user_input)

    # Get the AiDriveGPT response from the API
    AiDriveGPT_response = response["message"]

    # Print the AiDriveGPT response
    print("AiDriveGPT: " + AiDriveGPT_response)
    
    
    
    def send_message(message):
    payload = {
        "message": message
    }
    try:
        response = requests.post(url, headers=headers, data=json.dumps(payload))
        response.raise_for_status()
        return response.json()
    except requests.exceptions.HTTPError as error:
        print(f"HTTP error occurred: {error}")
        return None
    except requests.exceptions.ConnectionError as error:
        print(f"Connection error occurred: {error}")
        return None
    except requests.exceptions.Timeout as error:
        print(f"Timeout error occurred: {error}")
        return None
    except requests.exceptions.RequestException as error:
        print(f"An error occurred: {error}")
        return None

