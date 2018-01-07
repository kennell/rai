import requests
import json


CONNECTION = 'http://localhost:7076'


def make_rpc(payload):
    rsp = requests.post(
        url=CONNECTION,
        json=payload
    )
    return json.loads(
        rsp.content.decode('utf-8')
    )
