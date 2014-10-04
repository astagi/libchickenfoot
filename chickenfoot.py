import requests
import json

SERVER_URL = 'http://192.168.1.50:5000'

FORWARD = 'fwd'
BACK = 'back'
LEFT_FORWARD = 'leftfwd'
RIGHT_FORWARD = 'rightfwd'
LEFT_BACK = 'leftback'
RIGHT_BACK = 'rightback'

ON = 'on'
OFF = 'off'

def _send_post_request(action, data):
    requests.post('{}/{}'.format(SERVER_URL, action),
        data=json.dumps(data),
        headers={'Content-type': 'application/json'})

def move(tp, duration):
    _send_post_request('move', {'type':tp, 'duration':duration})

def set_lights(status):
    _send_post_request('lights', {'status':status})

def beep(duration):
    _send_post_request('beep', {'duration':duration})