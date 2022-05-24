# Read text from a file, and count the occurence of words in that text
# Example:
# count_words("The cake is done. It is a big cake!") 
# --> {"cake":2, "big":1, "is":2, "the":1, "a":1, "it":1}

def read_file_content(filename):
    # [assignment] Add your code here 

    file = open(filename, 'r')
    file_text = file.read()

    return file_text


def count_words():
    text = read_file_content("./story.txt")
    # [assignment] Add your code here

    word_count = len(text.split()) #Get number of words in the string
    word_list = text.split() #Split string into individual words and store in a list

    word_dictionary = {} #Dictionary to store word occurrences

    for index in range(len(word_list)):
        word = word_list[index] #Pick word from the list
        if word in word_dictionary: #Check if word was already counted; If so, go to next word
            continue
        occurences = text.count(word) #Count the number of occurences of the word in the string
        word_dictionary[word] = occurences #Store word and word count in Dictionary


    return word_dictionary #Return Dictionary

dict = count_words() #Test the function
print(dict)