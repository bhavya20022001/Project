import random
ls=["Strong woman Do Bong Soon","The Sound of Magic","Hotel Del Luna","Business Proposal",
"Twenty Five Twenty One","Welcome to Wakiki","Fight for my way","Itaewon classes"]

i=0
x=input("Do you want me to pick a drama for you? yes/no : ").lower()
if x== "yes":

        i=random.randint(0,len(ls))
        print(ls[i])

if x!="yes":
    print("maybe next time then !")


