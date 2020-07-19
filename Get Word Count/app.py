def count_words(sentence):
    # Strip all commas
    sentence = sentence.replace(',','')
    # Separate each word into an element in a list
    listOfWords = [x.strip() for x in sentence.split(' ')]
    # Return the number of elements in the list
    return len(listOfWords)

sentence = input("enter a sentence: ")

print(count_words(sentence))
