import requests

# url="https://zullkit-backend.buildwithangga.id/api/login"
# r = requests.post(url, data={'email': 'admin@email.co', 'password': 'password'})

url="http://10.64.26.210/trusted"
r = requests.post(url, data={'username': 'tableau.ioh_b2b'})
# r = requests.post(url, data={'username': 'tableau.ioh_b2b', 'target_site': 'IOH'})

print r.status_code
print r.text
