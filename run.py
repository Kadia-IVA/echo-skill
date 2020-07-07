import json

with open('speech.json') as file:
    text = file.read()
with open('output.txt', 'w') as file:
    print(text, file=file)
