import json

with open('speech.json') as file:
    text = json.load(file)['raw']
with open('output.txt', 'w') as file:
    print(text, file=file)
