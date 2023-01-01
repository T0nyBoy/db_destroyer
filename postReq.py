import csv
import requests

# Open the CSV file
with open('payload.csv', 'r') as csv_file:
  # Create a CSV reader object
  reader = csv.DictReader(csv_file)
  
  # Set the endpoint URL
  url = input("Paste the endpoint: ")
  payloadUsername = input("Endpoint username: ")
  payloadPassword = input("Endpoint password: ") 
  
  # Iterate through the rows of the CSV file
  for row in reader:
    # Get the username and password from the current row
    username = row['Email']
    password = row['Password']
    
    # Set the payload with the username and password
    payload = {payloadUsername: username, payloadPassword: password}
    
    # Send a POST request to the endpoint with the payload
    response = requests.post(url, json=payload)
    
    # Print the payload, the response status code, the response error message (if there is one), and the response data (if there is any)
    print(f"Payload: {payload}")
    print(f"Status code: {response.status_code}")
    if response.status_code >= 400:
      print(f"Error message: {response.json()}")
    else:
      print(f"Response data: {response.json()}")