# Numbers Processor

line = input("Enter a line of numbers - separate them with spaces:")
strings = line.split()
total = 0
substr =''
# print("strings is: ", strings)
try:
    for substr in  strings:
        total += float(substr)
    if len(strings) <= 0:
        print("There was nothing to total")
    else:    
        print(f"The total is: {total}")
except:
    print(f"{substr} is not a number")