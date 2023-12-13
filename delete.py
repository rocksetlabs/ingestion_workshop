import os
import json
import requests

ROCKSET_API_KEY = os.getenv("ROCKSET_API_KEY", "")

def config():
    with open("./resources/config.json") as c:
        config = json.loads(c.read())
    region = config['region']
    workspace = config['workspace']
    collection = config['collection']
    return region, workspace, collection

def send_data(**kwargs):
    with open("./resources/delete.json") as f:
        data = json.loads(f.read())
    headers = {'Authorization': 'ApiKey {}'.format(ROCKSET_API_KEY)}
    for record in data:
        payload = {"data": [record]}
        r = requests.delete('https://{}/v1/orgs/self/ws/{}/collections/{}/docs'.format(kwargs["region"],
                                                                                    kwargs["workspace"],
                                                                                    kwargs["collection"]),
                            json=payload,
                            headers=headers)
        print(r.json())

def start_delete():
    region, workspace, collection = config()
    send_data(region = region,
                workspace = workspace,
                collection = collection)

if __name__ == "__main__":
    start_delete()
