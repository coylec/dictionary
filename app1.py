import json

data = json.load(open("data.json"))

def describe(word):
    return data[word]

word = input("Enter word: ")

print(describe(word))