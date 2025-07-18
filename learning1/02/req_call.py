# pip install requests
import requests
import json
import os

from common.project_env import setup_environment
setup_environment()

url = os.getenv('OPENAI_BASE_URL') + "/chat/completions"
#print(os.getenv('OPENAI_BASE_URL'))
payload = json.dumps({
    "model": "gpt-4o",
    "messages": [
        {"role": "system", "content": "assistant"},
        {"role": "user", "content": "Hello"}
    ]
})
headers = {
    'Content-Type': 'application/json',
    'Authorization': 'Bearer ' + os.getenv('OPENAI_API_KEY'),
}
response = requests.request("POST", url, headers=headers, data=payload)
print(response.text)
