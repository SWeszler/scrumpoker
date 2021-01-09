import websocket
import json

ws = websocket.WebSocket()

ws.connect('ws://localhost:5000/ws/pol-data/')

for i in range(10):
    ws.send(json.dumps({
        'value': f'{i}'
    }))