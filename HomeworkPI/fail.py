import requests

url = 'https://api.tracker.yandex.net/v2/issues'

headers = {
    'Authorization': 'Bearer your_access_token',
    'Content-Type': 'application/json'
}


data = {
    'queue': 'TeamCity Build Fails',
    'summary': 'Build failed',
    'description': 'Please fix it.',
    'assignee': 'Daria190404@yandex.ru' 
}


response = requests.post(url, headers=headers, json=data)

if response.status_code == 201:
    print('Task created successfully in Yandex Tracker')
else:
    print('Failed to create task in Yandex Tracker')
