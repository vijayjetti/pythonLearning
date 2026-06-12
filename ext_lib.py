#  External Libraries
#  ================
#  This module contains external libraries that are used by the project. 
# It is not intended to be imported by other modules in the project.

#  get_json function fetches JSON data from a specified URL and saves it to a file named 'data.json'.

import json

import requests

def get_json(url):
    """Fetches JSON data from the specified URL."""
    response = requests.get(url)
    print(f'Response Status Code: {response.status_code}')  # Debugging statement to check the status code
    if response.status_code == 200:
        print('Successfully fetched data from the URL.')  # Debugging statement to confirm successful fetch
    else:
        print(f'Failed to fetch data. Status Code: {response.status_code}')  # Debugging statement for failed fetch
    response.raise_for_status()  # Raise an error for bad status codes
    return response.json()

url = "https://api.github.com/users/vijayjetti"  # Example URL to fetch data from GitHub API
try:
    data = get_json(url)
    with open('data.json', 'w') as f:
        json.dump(data, f, indent=4)  # Save the fetched data to a JSON file
except requests.exceptions.RequestException as e:
    print(f"An error occurred: {e}")  # Debugging statement to check for any request exceptions
else:
    print("Data fetched and saved successfully.")  # Debugging statement to confirm successful operation

# Regular Expressions

import re

text = "The rain in Spain stays mainly in the plain."
matches = re.findall(r'\b\w+ain\b', text)  # Find all words that end with 'ain'

print(matches)  # Prints the list of words ending with 'ain' in the text

# Multithreading

import threading

def print_numbers():
    for i in range(5):
        print(i)

# Create two threads
thread1 = threading.Thread(target=print_numbers)
thread2 = threading.Thread(target=print_numbers)

# Start the threads
thread1.start()
thread2.start()

# Wait for both threads to complete
thread1.join()
thread2.join()