
# each line of user input removes the spaces
UserText1 = (input("Enter your first text: ")).replace(" ", "")
UserText2 = (input("Enter your second text:")).replace(" ", "")


if UserText1 == "" or UserText2 == "": # If there are only spaces in the two strings
    print("Not Anagrams")

else:
    isAnagram = False # bool for holding the Anagram condition
    for char in UserText1: # traverse each character in the UserText1
        if UserText1.count(char) == UserText2.count(char):
            # if number of time is character is in text1 is the same at text 2 then its a Anagram
            isAnagram = True 
        else:
            # its not a Anagram so no need to iterate further in the string
            isAnagram = False
            break
    
    if isAnagram == True:
        print("Anagrams")
    else:
        print("Not Anagrams")

