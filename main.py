#textovy analyzator
TEXTS = [
    '''Situated about 10 miles west of Kemmerer,
    Fossil Butte is a ruggedly impressive
    topographic feature that rises sharply
    some 1000 feet above Twin Creek Valley
    to an elevation of more than 7500 feet
    above sea level. The butte is located just
    north of US 30 and the Union Pacific Railroad,
    which traverse the valley.''',
    '''At the base of Fossil Butte are the bright
    red, purple, yellow and gray beds of the Wasatch
    Formation. Eroded portions of these horizontal
    beds slope gradually upward from the valley floor
    and steepen abruptly. Overlying them and extending
    to the top of the butte are the much steeper
    buff-to-white beds of the Green River Formation,
    which are about 300 feet thick.''',
    '''The monument contains 8198 acres and protects
    a portion of the largest deposit of freshwater fish
    fossils in the world. The richest fossil fish deposits
    are found in multiple limestone layers, which lie some
    100 feet below the top of the butte. The fossils
    represent several varieties of perch, as well as
    other freshwater genera and herring similar to those
    in modern oceans. Other fish such as paddlefish,
    garpike and stingray are also present.'''
]


uzivatele = {
    "jmeno":"heslo",
    "uziv123":"heslo123"
}

separator = "-" * 40
username = input("Zadej uziv. jmeno: ")
password = input("Zadej sve heslo: ")

#1. varianta přihlášení
if username in uzivatele.keys() and uzivatele[username] == password:
    print(f"username: {username}\npassword: {password}")
    print(separator)
    print("Welcome to the app, " + username)
else:
    print(f"username: {username}\npassword: {password}")
    print("unregistered user, terminating the program...")
    exit()


#Zadávání čísla textu uživatel a vrácení textu pro další analýzu
try:
    number_of_text = int(input("Enter a number btw. 1 and 3 to select: "))
    if number_of_text not in range(1,4):
        print("You entered wrong number. Program exits.")
        exit()
    else:
        text = TEXTS[number_of_text - 1]
    
except ValueError:
    print("You entered wrong number. Program exits.")
    exit()

#Analýza textu
split = text.split()
word_count = len(split)


i = 0
k = 0
l = 0
m = 0
sum = 0
list = []
numbers = []
for word in split:
    text = str(word)
    if word[0].isupper() and word[1].islower():   
        i += 1
    if word.isupper():
        k += 1
    if word.islower():
        l += 1
    if word.isdecimal():
        m += 1
        list.append(word)


for number in list:
    number = int(number)
    sum  += number


for word in split:
    strip_word = word.strip(".,")
    number_of_letters = len(strip_word)
    numbers.append(number_of_letters)

print(separator)
print(f"There are {word_count} words in the selected text.")
print(f"There are {i} titlecase words.")
print(f"There are {k} uppercase words.")
print(f"There are {l} lowercase words.")
print(f"There are {m} numeric strings.")
print(f"The sum of all the numbers {sum}")
print(f"There are {word_count} words in the selected text.")
print(separator)


list = []
for x in numbers:
    if x not in list:
        list.append(x)
        
list = sorted(list)


final = []
for x in list:
    pocet = numbers.count(x)
    final.append(pocet)
    
dictionary = dict(zip(list, final))

headers = ("LEN", "Occurences", "NR.")
title = " | ".join(headers)
print(title.center(40))


for key, item in dictionary.items():
    hvezdy = "*" * item
    line = f"{key:>2}|{hvezdy:<18}|{item:>2}"
    print(line.center(40))

    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    



    

        
    
    
    
