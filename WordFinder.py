
def UserPrompt():

    UserWord = input("Enter your word: ")
    TextToSearch = input("Enter the text to search within: ")

    if UserWord.replace(" ","") == "" or TextToSearch.replace(" ", "") =="" :
        print("You must enter valid data")
        return UserPrompt()
    else:
        return UserWord, TextToSearch


Word, str2 = UserPrompt() 
wordFound = False
# casefold() string method ignores the case of the string
str2 = str2.casefold() 
Word = Word.casefold()

previousIndex = -1 # placeholder for the index in str2,
                   # which was were a previous letter in Word was found in str2
for i in range(0, len(Word)): # start 0 till the length of the Word
    
    if str2.find(Word[i]) == -1:
        #if the 1st letter in Word is not found in str2 then set wordFound to False
        # and break out of the iteration
       wordFound = False
       break
    if i ==0 and Word[i] in str2:
        # if the first letter in the Word was found in str2
        # then set wordFound bool to True
        # also assign the previous Index value the index where this letter in
        # Word was found in the string str2 and then go to next iteration
        wordFound = True
        previousIndex = str2.find(Word[i])
        continue
    if i > 0 and Word[i] in str2:
        # if a letter after the first letter is found in str2
        # look for the letter starting after the str2 index
        # where the previous letter in word was found

        #look for the letter at the i index of Word in str2 starting after the
        # index in str2 where the previous letter in order was found.
        currentIndex = str2.find(Word[i],previousIndex+1)
       
        if currentIndex == -1:
            #if the letter at the i index of Word is not found in str2
            # then assign a False value to the wordFound variable
            # and break out of the iteration
            wordFound = False
            break
        else:
            #assign the previousInex to be the currentIndex
            # to be used in the next iteration
            previousIndex = currentIndex
            


if wordFound:
    print("Word found")
else:
    print("Word not found")

"""
    Test data:
        input: donor
                Nabucodonosor
        Output: Yes

        input: donut
                Nabucodonosor

        Output: No
"""
        
