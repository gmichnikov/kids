import json
import requests

# Attempt to download the words dictionary
# this is a list of almost 400k words
try:
    response = requests.get("https://raw.githubusercontent.com/dwyl/english-words/master/words_dictionary.json")
    words_dict = response.json()
except Exception as e:
    print("Error downloading the words dictionary:", e)

    # Alternatively, if you have the file downloaded, you can load it locally:
    # with open('path_to_your_downloaded_file/words_dictionary.json') as file:
    #     words_dict = json.load(file)


# Attempt to download the list of words
# this is a list of around 25k words
try:
    response = requests.get('https://raw.githubusercontent.com/dolph/dictionary/master/popular.txt')
    # Split the content by newline to get a list of words
    words_list = response.text.split('\n')
except Exception as e:
    print("Error downloading the words list:", e)
    # Alternatively, if you have the file downloaded, you can load it locally:
    # with open('path_to_your_downloaded_file/popular.txt') as file:
    #     words_list = file.read().split('\n')


# Letters on the right side of a standard QWERTY keyboard
right_side_letters = "yhnujmiklopb"
right_side_letters = "yhnujmiklop"
right_side_letters = "qwertasdfgzxcvb"
right_side_letters = "qwertasdfgzxcvb"
right_side_letters = "qwertyuiop"
right_side_letters = "asdfghjkl"
right_side_letters = "zxcvbnm"
right_side_letters = "abcdefghijklm"
right_side_letters = "nopqrstuvwxyz"

# Function to check if a word consists entirely of letters from the right side of the keyboard
def is_right_side_word(word):
    return all(letter in right_side_letters for letter in word)

# Search for the longest word that meets the criteria
longest_word = ""
for word in words_list:
# for word in words_dict.keys():
    if len(word) > len(longest_word) and is_right_side_word(word):
    # if len(word) > 10 and is_right_side_word(word):
        print(f"Word: {word}, Length: {len(word)}")
        longest_word = word

# Print out the word and its length
print(f"Longest word: {longest_word}, Length: {len(longest_word)}")

# print(f"the list has {len(words_dict)} words")
print(f"the list has {len(words_list)} words")