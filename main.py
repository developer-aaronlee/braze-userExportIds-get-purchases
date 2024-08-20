import csv
import json
import requests
from requests.auth import HTTPBasicAuth

url = 'https://rest.iad-06.braze.com/users/export/ids'
API_KEY = 'Bearer api_key'
headers = {
    'Content-Type': 'application/json',
    'Authorization': API_KEY
}

alldata = []
with open('batch_test_10_result.csv', 'wb') as file:
    # str1 = ""
    with open('batch_test_10.csv') as csvfile:
        spamreader = csv.reader(csvfile, delimiter=' ', quotechar='|')
        for row in spamreader:
            if len(row) == 0:
                continue
            temp = row[0].split(",")
            if temp[0] == "external_id":
                continue
            body = json.dumps({"email_address": temp[0]
                             })
            response = requests.post(url, data=body, headers=headers)
            a = response.json()
            all = []

            if len(a['users']) == 0:
                continue
            if len(a['users']) != 0:
                all.append([a['users'][0]['email']])

            for x in a['users']:
                all.append([x['external_id']])
            if 'purchases' in a['users'][0]:
                for x in a['users'][0]['purchases']:
                    all.append([x['name']])
                    all.append([x['first']])
                    all.append([x['last']])
                    all.append([x['count']])
                else:
                    all.append('')

            alldata.append(all)
            print(all)

with open("batch_test_10_result.csv", "w") as csvfile:
    writer = csv.writer(csvfile)
    for x in alldata:
        writer.writerow(x)
