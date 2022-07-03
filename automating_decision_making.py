import random
ls=[["Strong woman Do Bong Soon","gives strength","16 episodes","series"],["The Sound of Magic","escape reality","6 episodes","short series"],["Hotel Del Luna","try something new","16 episodes","drama"],["Business Proposal","romantic","16 episodes","drama"],
["Welcome to Wakiki","jolly and comedy","20 episodes","series"],["Fight for my way","real and inspiring","16 episodes","drama"]]
i=0
x=input("Do you want me to pick a drama for you? yes/no : ").lower()

if x== "yes":

        i=random.randint(0,len(ls))
        print(ls[i])
else :
    print("maybe next time then !")


