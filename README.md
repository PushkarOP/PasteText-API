```markdown
# PasteText API

This is a simple Python API, built with Flask, that functions like Pastebin. It allows users to upload any text, which is then stored and can be accessed later via a unique link.

## Installation

Install the required Python packages:

```bash
pip install flask flask_sqlalchemy requests
```

## Running the API

Start the Flask development server:

```bash
python api.py
```

A SQLite database will be created in the system's memory to store posted text.

## Usage

### Posting Text

Use the following Python script with the `requests` library to interact with the API:

```python
import requests
import json

# URL of the API
url = 'http://localhost:5000/'

# Your text to send
my_text = '''This is my text. It can be as long as needed, 
and can span multiple lines like this.
'''

# Data to be sent
data = {'content': my_text}

# Headers
headers = {'Content-type': 'application/json', 'Accept': 'text/plain'}

# POST request
response = requests.post(url, data=json.dumps(data), headers=headers)

# If the POST request is successful, you will receive a response
if response.status_code == 200:
    print('Successfully uploaded.')
    print('Response:', response.json())
else:
    print('Failed to upload.')
```

### Retrieving Text

To retrieve the posted text, make a `GET` request:

```python
text_id = 'xyz'  # use the actual id you got from the POST response
get_url = url + 'text/' + text_id

response = requests.get(get_url)

if response.status_code == 200:
    print('Successfully retrieved.')
    print('Response:', response.text)
else:
    print('Failed to retrieve.')
```

Replace the `text_id` in the sample code with the ID received from the `POST` request. You can also view the uploaded text in your web browser using the same URL.
