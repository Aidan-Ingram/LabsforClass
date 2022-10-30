'''
Aidan Ingram
3065803
10/26/2022
Lab 7
10/29/2022
Purpose: File can read into a given text file, count the words, and create two files;
one file has all words that appear once, the other has every word and it's count in the file
'''
def clean_word(word):
    """Function should read through lines in a file, and if a forbidden character
    is present, it should be replaced and returned"""
    forbiddenchar = ['!', '?', ':', ';', ',', '|', '.', '[', ']', '(', ')', '--']
    word = word.lower()
    word = word.strip()
    for letter in word:
        if letter in forbiddenchar:
            word = word.replace(letter, "")
    return word

def build_count(text):
    """Function specifically targets '--' since it's two characters, and can't be cleaned
    normally. From there, runs every word through the cleaner and puts it in a dict.
    If word appears more than once, adds to count of word in the dict., else makes it 1."""
    totaldict = {}
    for line in text:
        if '--' in line:
            newword = line.replace('--', ' ')
            line = newword
        else:
            line = line
        line = line.strip()
        line = line.split()
        for word in line:
            newword = clean_word(word)
            if newword in totaldict:
                totaldict[newword] += 1
            else:
                totaldict[newword] = 1
    return totaldict

def unique_words(word_counts):
    """Functions looks at the dict in build_count (in main) and if count = 1, adds the word
    to a list that is then separated by a newline, and printed without the count"""
    uniquedict = {}
    totaldict = word_counts
    for word, count in totaldict.items():
        if count == 1:
            uniquedict[word] = count
        else:
            totaldict = totaldict
    printedlist = list(uniquedict)
    returnedlist = '\n'.join(printedlist)
    returnedlist.split()
    return returnedlist

def main():
    """Main calls all functions mentioned. Starts by opening the user file given, reads in, and calls
    functions. There is a statement at the top of each new file made saying what is displayed,
    and the information is written in from the called functions. Functions are saved as unique_words and
    word_data"""
    print("========Welcome to the File-Word Counter!========")
    u_input = input("Enter a file name to have it's contents counted: ")
    """This part of the function is for the total words and count"""
    newworddata1 = open('word_data.txt', 'w')
    newworddata1.write("|Words that appear in file : Number of times they appear|\n")
    newworddata1.close()
    ufile = open(u_input, 'r')
    newdict = build_count(ufile)
    newworddata = open('word_data.txt', 'a')
    for key, value in newdict.items():
        newworddata.write(str(key) + ' : ' + str(value) +'\n')
    newworddata.close()
    """This part of the function is exclusively to open the unique file and create it"""
    ostatement = open('unique_words.txt', 'w')
    ostatement.write("|Here is a list of words that appear exactly one time in the Constitution:|\n")
    ostatement.close()
    uniquew = open(u_input, 'r')
    newfunc = build_count(uniquew)
    final = unique_words(newfunc)
    newfile = open('unique_words.txt', 'a')
    newfile.write(final)
    newfile.close()
    """Final piece here prints what the user sees when the program has run successfully"""
    print(f'The file {u_input} has been processed.')
    print("Output stored in word_data.txt and unique_words.txt")
    print("Closing...")
main()
