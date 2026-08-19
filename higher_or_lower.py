from people import famous_people
 
print("Welcome to Higher or Lower Game")
print("In this game we will give you a name, description and country.")
print("You have to guess who has more followers.")
print("So let's get Started!!\n")
 
firstCounter = 0
secondCounter = 1
 
while secondCounter < len(famous_people):
    man1=famous_people[firstCounter]
    man2=famous_people[secondCounter]
    print(f"This is {man1['name']} from {man1['country']} works as {man1['what_they_do']}\n" )
    
    print(f"This is {man2['name']} from {man2['country']} works as {man2['what_they_do']}" )
    userChoice= int(input("Who have more follower first or second(chose 1/2) : "))
    if userChoice == 1 and man1['followers']>man2['followers']:
        secondCounter+=1
        print(f"Correct{man1['name']} have more follower from {man2['name']}")
    else:
        print("You Lose!")
        break