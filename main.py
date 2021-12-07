import json
from difflib import get_close_matches

data = json.load(open("data.json"))


def translate(word):
    word = word.lower()
    if word in data:
        return data[word]
    elif len(get_close_matches(word, data.keys(), cutoff=0.75)) > 1:
        for i in range(len(get_close_matches(word, data.keys(), cutoff=0.75))):
            ans = input("Did you mean %s instead? Please enter Y for Yes and N for No: " % get_close_matches(word, data.keys())[i])
            if ans.lower() == "y":
                return data[get_close_matches(word, data.keys())[i]]
                break
            elif ans.lower() == "n":
                pass
            else:
                return "We didn't understand your input!"
            break
    else:
        return "The word doesn't exist. Please double check it."


while True:
    word = input("Enter a valid word: ")
    if type(translate(word)) == list:
        if len(translate(word)) >= 1:
            print(translate(word)[0])
        else:
            for _ in range(len(translate(word))):
                print(f"{_+1} definition: {translate(word)[_]}")
    else:
        print(translate(word))
    ans1 = input("Do you want to check another word? Please enter Y for Yes and N for No: ")
    if ans1.lower() == "y":
        pass
    elif ans1.lower() == "n":
        print("Thank you!")
        break
    else:
        print("Sorry we didn't understand the word!")
        break
