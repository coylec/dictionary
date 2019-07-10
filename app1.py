import json

data = json.load(open("data.json"))

def describe(word):
    word = word.lower()
    if word in data:
        return data[word]
    else:
        return "The word does not exist."

word = input("Enter word: ")

print(describe(word))