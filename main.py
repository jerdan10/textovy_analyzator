#textovy analyzator
uzivatele = {
    "jmeno":"heslo",
    "uziv123":"heslo123"
}

username = input("Zadej uziv. jmeno: ")
password = input("Zadej sve heslo: ")

#1. varianta přihlášení
if username in uzivatele.keys() and uzivatele[username] == password:
    print("Jste přihlášeni. Vyberte si prosím text")
else:
    print("Chybné heslo nebo jméno")
    
# 2. varianta přihlášení
# if uzivatele.get(username) == password:
#     print("Jste přihlášeni. Vyberte si prosím text")
# else:
#     print("Chybné heslo nebo jméno")

# 3. varianta přihlášení
# for jmeno, heslo in uzivatele.items():
#     if jmeno == username and heslo == password:
#         print("Jste přihlášeni. Vyberte si prosím text")
#         break
# else:
#     print("Chybné heslo nebo jméno.")


    

        
    
    
    
