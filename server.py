# -*- coding: utf-8 -*-

'''
Created on 2021. 6. 25.
@author: jangh@vmware.com
'''

from pygics import rest, server
import requests

TOKEN = 'TOKEN HERE'
PROXY_LISTEN_PORT = 80

url = 'https://api.opsgenie.com/v2/alerts'
headers = {
    'Content-Type': 'application/json',
    'Authorization': 'GenieKey ' + TOKEN
}

@rest('POST', '/v2/alerts')
def alerts(req):
    requests.post(url, headers=headers, json=req.data, verify=False)
    return 'OK'

if __name__ == '__main__':
    server('0.0.0.0', PROXY_LISTEN_PORT)