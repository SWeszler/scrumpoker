from websocket import create_connection

ws = create_connection('ws://localhost:5000/ws/pol-data/')

for i in range(10):
    ws.send(f"Sending {i}...")

while True:
    result = ws.recv()
    print(result)
    entry = input()
    if entry == 'exit':
        ws.close()
        break
    else:
        ws.send(entry)