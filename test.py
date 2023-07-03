import requests

BASE = 'http://127.0.0.1:5000/'

data = [{"likes": 10, "name": "bob", "views": 100},\
        {"likes": 20, "name": "shelly", "views": 200},\
        {"likes": 30, "name": "trish", "views": 400},\
        {"likes": 10, "name": "tim", "views": 1000}]

for i in range(len(data)):
    headers = {'accept': 'application/json'}
    response = requests.post(BASE + 'video/' + str(i), json=data[i])
    if response.status_code == 201:
        print(f"Video {i} created successfully")
    else:
        print(f"Failed to create video {i}. Status code {response.status_code}")
    print("Response content: ", response.content)
    # print(response.json())

# response = requests.delete(BASE + 'video/0')
# print(response)
# input()
response = requests.get(BASE + 'video/2')
if response.status_code == 200:
    print("Video retrieved successfully")
    print("Response content: ", response.content)
else:
    print("Failed to retrieve video. Status code:", response.status_code)
# print(response.json())
