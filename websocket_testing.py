from websocket import create_connection

ws = create_connection("ws://localhost:5000/ws/join-game/?token=authentication-token-here")

while True:
    result = ws.recv()
    print(result)
    entry = input()
    if entry == 'exit':
        ws.close()
        break
    else:
        ws.send(entry)