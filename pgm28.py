def length(words):
    return max(len(word)for word in words)
word_list=input("enter a list of word separated by space:").split()
print("length of the longest word:",length(word_list))