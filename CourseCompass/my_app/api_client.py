import requests

def get_external_data():
    url = "https://github.com/quantum-bits/iChair"
    headers = {
        "Accept": "application/json"
    }
    
    response = requests.get(url, headers=headers)
    
    if response.status_code == 200:
        return response.json()  # or .text for raw
    else:
        return {"error": f"API call failed with status {response.status_code}"}
