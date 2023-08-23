print("Welcome To My Computer Quiz")

playing = input("Do You want to Play? ")

if playing.lower() != "yes":
    quit()

print("Okay Let's Play :)")
score=0

answer = input("What does RAM Stand for? ")
if answer.lower()== "Random Access Memory":
    print('correct')
else:
    print('Incorrect')

answer = input("What does GPU Stand for? ")
if answer.lower()== "General Processing Unit":
    print('correct')
    score+=1
else:
    print('Incorrect')

answer = input("What does CPU Stand for? ")
if answer.lower()== "Central Processing Unit":
    print('correct')
    score+=1
else:
    print('Incorrect')

answer = input("What does LAN Stand for? ")
if answer.lower()== "Local Area Network":
    print('correct')
    score+=1
else:
    print('Incorrect')
print("You got "+str(score) +"Questions Correct!!") 
print("You got "+str((score/4)*100)+ "+.") 
