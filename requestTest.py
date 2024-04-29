import requests
import json
from uuid import uuid4

url1 = "https://apps-demo-screening.sonar.thetaray.cloud/security/accessToken"


response1 = requests.post(url1,  json={"clientSecret": "thetaray"})
print(response1)

data = json.loads(response1.text)
token = data["token"]

url = "https://apps-demo-screening.sonar.thetaray.cloud/screening/customer/check"

requestId = str(uuid4())
id = str(uuid4())

with open('userdata.json', 'r') as j:
  contents = json.loads(j.read())

fullname = (contents["Full Name"])
yob = (contents["DOB"])
location = (contents["Location"])
birthloc = (contents["Birth Location"])

print (fullname, yob, location, birthloc)

payload = json.dumps({
  "requestId": str(requestId),
  "requestData": {
    "type": "individual",
    "id": str(id),
    "fullName": str(fullname),
    "addresses": [
      str(location)
    ],
    "dateOfBirth": str(yob),
    "placeOfBirth": str(birthloc),
    "nationalities": [
      str(birthloc)
    ]
  }
})

s = 'Bearer {}'.format(token)

headers = {
  'Authorization': str(s),
  'Content-Type': 'application/json'
}

response = requests.request("POST", url, headers=headers, data=payload)

print(response.text)
f = open("response.json", 'w')
f.write(response.text)
f.close
