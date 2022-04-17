welcome= input("Enter your Name : ")
print("Hey " + welcome + ", Welcome to the Quizz Game !")


playing=input("Do you want to play the game ? ")
print(playing)
if playing.lower() != "yes":
    quit()
print("Lets play !")
score= 0
answer=input("What does Ram stands for ? ")

if answer.lower() == ("random access memory").lower():
    print("Correct !")
    score +=1

else:
    print("Incorrect !")

answer = input("What does Rom stands for ? ")

if answer.lower() == ("Read Only Memory").lower():
    print("Correct !")
    score += 1

else:
    print("Incorrect !")

answer = input("What does SSD stands for ? ")

if answer.lower() == ("Solid State Drive").lower():
    print("Correct !")
    score += 1

else:
    print("Incorrect !")

answer = input("What does CPU stands for ? ")

if answer.lower() == ("Central processing unit").lower():
    print("Correct !")
    score += 1

else:
    print("Incorrect !")

print("You got " + str(score) + " questions correct !")