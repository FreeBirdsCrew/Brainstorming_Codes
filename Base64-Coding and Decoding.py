import base64
data = base64.b64encode(bytes('Simran', 'cp500'))
print(data)
decoded = base64.b64decode(data)
print(decoded)
