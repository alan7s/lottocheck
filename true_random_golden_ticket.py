import requests

#True Random Golden Ticket
#Version v0.1 by alan7s
#Settings
API = "YOUR_RANDOM.ORG_API"
MAX_NUMBER = 6
MIN_RANGE = 1
MAX_RANGE = 60

def randomdotorg(n, min, max):
    url = "https://api.random.org/json-rpc/4/invoke"
    headers = {"Content-Type": "application/json"}

    data = {
        "jsonrpc": "2.0",
        "method": "generateIntegers",
        "params": {
            "apiKey": API,
            "n": n,
            "min": min,
            "max": max
        },
        "id": 1
    }

    try:
        response = requests.post(url, json=data, headers=headers)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as err:
        print(f"Request error: {err}")
        if hasattr(response, 'status_code'):
            print(f"Status Code: {response.status_code}, Response: {response.text}")
    return None

ticket = []

print("Running....")

while len(ticket) < MAX_NUMBER:
    my_range = randomdotorg(2, MIN_RANGE, MAX_RANGE)
    if not my_range:
        break
    numbers = sorted(my_range["result"]["random"]["data"])
    number = randomdotorg(1, numbers[0], numbers[1])
    if not number:
        break
    ticket.add(number["result"]["random"]["data"][0])

print("Your golden ticket:", sorted(ticket))

#Running....
#Your golden ticket: [6, 17, 32, 44, 49, 57]
