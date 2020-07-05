import json

with open('speech.json') as file:
    speech = json.load(file)

with open('output.txt', 'w') as file:
    print(speech['raw'], file=file)
