import requests
import json
import os


def get_connection():
    protocol = os.getenv('RAI_PROTOCOL', default='http')
    host = os.getenv('RAI_HOST', default='localhost')
    port = os.getenv('RAI_PORT', default='7076')

    return "{protocol}://{host}:{port}".format(
        protocol=protocol,
        host=host,
        port=port
    )


def make_rpc(payload):
    rsp = requests.post(
        url=get_connection(),
        json=payload
    )
    return json.loads(
        rsp.content.decode('utf-8')
    )
