import json
from difflib import get_close_matches

data = json.load(open("data.json"))

def describe(word):
    word = word.lower()
    if word in data:
        return data[word]
    elif len(get_close_matches(word, data.keys())) > 0:
        confirm = input("Did you mean %s? Enter Y for yes or N for no: " % get_close_matches(word, data.keys())[0])
        if confirm == "Y":
            return data[get_close_matches(word, data.keys())[0]]
        elif confirm == "N":
            return "The word does not exist, please double check it."
        else:
            return "We do not understand your entry."
    else:
        return "The word does not exist."

word = input("Enter word: ")

output = describe(word)

if type(output) == list:
    for item in output:
        print(item)
else:
    print(output)