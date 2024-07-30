import requests
import time

# Set your codespace URL
codespace_url = "https://solid-bassoon-g45rp759xx54395x.github.dev/"

# Set the interval in seconds (5 minutes in this case)
interval = 300

while True:
    try:
        # Send a GET request to your codespace
        response = requests.get(codespace_url)
        
        # Check if the request was successful
        if response.status_code == 200:
            print("Keep-alive signal sent successfully.")
        else:
            print("Failed to send keep-alive signal. Status code:", response.status_code)
    except requests.exceptions.RequestException as e:
        print("Error sending keep-alive signal:", e)

    # Wait for the specified interval before sending the next request
    time.sleep(interval)