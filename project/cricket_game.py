# Cricket Game
import random
import pyttsx3
import speech_recognition as sr 

from playsound import playsound 
engine =pyttsx3.init()
voices =engine.getProperty('voices')
engine.setProperty('voice',voices[0].id)
engine.setProperty('rate',150)
playsound("C:\\Users\\stc\\Downloads\\Ipl Sms Tone.mp3")
engine.say("""        WELL  COME  TO OUR CRIKET  GAME 

                 let's start the game 

      we have to follow some instructions:  how to play the game 

1. You have to select any random number from 1 to 6 after that the computer will also select a number.
2. While you  batting, if the number selected by you and computer is different, then your number  will  add to your runs.
   If the number selected by you and computer is same, then you will lose your wicket.
4. While bowling, if the number selected by you and computer is different, then the computer's number will add to its runs.
   If the number selected by you and computer is same, then the computer will lose its wicket.
5. Each player will get 2 wickets and 2 overs (12 balls) for batting and bowling.
6. The innings will end after either the three wickets fell or the overs end.
7. The player with maximum runs wins. 
 
""")
engine.runAndWait()
#speaking function
def Speak():
    global toss
    r= sr.Recognizer()
    with sr.Microphone() as source:
        
        audio=r.listen(source)
        try:
            text=r.recognize_google(audio,language='en-in')
            print("you said {}".format(text))
            return text
            
        except:
            engine.say("couldn't recognize, speak again")
            Speak()

# Toss 
 
print("\nHere comes the Toss")

engine.say("Here comes the Toss")
engine.runAndWait()

#toss = (input("Choose 1 for  head or 2 for tail: ")).lower()
engine.say("Choose    head    or    tail:  ")
engine.runAndWait()
toss=Speak()
 
random_toss = random.randint(1,2)         
random_opt = random.randint(1,2)            
print("In random_opt (1 = bat) and (2 = ball)")

 
u_opt = 0
c_opt = 0
 
if random_toss == 1 and toss == "head":
    print("You won! choose bat or bowl")
    engine.say('You won! choose bat or bowl')
    engine.runAndWait()
    u_opt=Speak()
 
elif random_toss == 2 and toss == "tel":
    print("\nYou won the toss")
    engine.say('You won! choose bat or bowl')
    engine.runAndWait()
    u_opt=Speak()   
  
else:
    engine.say('  You  lost the toss ')
    engine.runAndWait()
 
    if random_opt == 1:
        c_opt = "bat"
        print("Computer choose to",c_opt)
        engine.say("Computer choose to bat ")
        engine.runAndWait()
 
    elif random_opt == 2:
        c_opt = "ball"
        print("Computer choose to",c_opt)
        engine.say("Computer choose to ball ")
        engine.runAndWait()
 
# First Innings  

print("\n---------- First Innings Begins ----------")
engine.say("    ten \n   nine  \n eight \n  seven \n six \n  five \n four  \n  three \n   two \n  one \n let's  play  the first inning  ")
engine.runAndWait()
 
runs_1 = 0
wickets_1 = 0
balls_1 = 0
 
while wickets_1 != 2 and balls_1 != 12:
 
    u_choice = int(input("\nChoose any number from 1 to 6: "))
    c_choice = random.randint(1,6)
 
    if u_choice < 1 or u_choice > 6:
        print("\nPlease choose a value from 1 to 6.")
 
    else:
        print("Your choice: ",u_choice,"\nComputer's choice: ",c_choice)
 
        if u_choice == c_choice:
            wickets_1 += 1
            engine.say("   loss the  wicket  ")
            engine.runAndWait()

 
        else:
            if u_opt == "bat" or c_opt == "ball":
                Bat_first = "You"
                Ball_first = "Computer"
                runs_1 += u_choice
 
            elif u_opt == "ball" or c_opt == "bat":
                Bat_first = "Computer"
                Ball_first = "You"
                runs_1 += c_choice
 
        print("\nScore =",runs_1,"/",wickets_1)
 
        balls_1 += 1
 
        if balls_1 == 6:
            print("End of Over 1")
 
        elif balls_1 == 12:
            print("End of Over 2")
 
        print("Balls remaining: ",12 - balls_1)
 
print("\n---------- End of Innings ----------")
engine.say("  end the first innings  and the  final score is  "+str(runs_1)+ "at loss of" + str(wickets_1))
engine.runAndWait() 
print("\nFinal Score:")
print("Runs =",runs_1)
print("wickets =",wickets_1)
 
print("\n",Ball_first,"needs",runs_1 + 1,"runs to win.")
 
# Second Innings 
 
print("\n---------- Secound Innings Begins ----------")
engine.say(" let's  play  the secound  inning  ")
engine.runAndWait()

runs_2 = 0
wickets_2 = 0
balls_2 = 0
 
while wickets_2 != 2 and balls_2 != 12 and runs_2 <= runs_1:
 
    u_choice = int(input("\nChoose any number from 1 to 6: "))
    c_choice = random.randint(1,6)
 
    if u_choice < 1 or u_choice > 6:
        print("\nPlease choose a value from 1 to 6.")
 
    else:
        print("Your choice: ",u_choice,"\nComputer's choice: ",c_choice)
 
        if u_choice == c_choice:
            wickets_2 += 1
            engine.say("   loss the  wicket  ")
            engine.runAndWait()
 
        else:
            if Bat_first == "Computer": 
                runs_2 += u_choice
                Bat_second = "You"
 
            elif Bat_first == "You":
                runs_2 += c_choice
                Bat_second = "Computer"
 
        print("\nScore =",runs_2,"/",wickets_2)
 
        balls_2 += 1
 
        if balls_2 == 6:
            print("End of Over 1")
 
        elif balls_2 == 12:
            print("End of Over 2")
 
        if runs_2 <= runs_1 and balls_2 <= 11 and wickets_2 != 2:
            print("To win:",runs_1 - runs_2 + 1,"runs needed from",12 - balls_2,"balls.")
 
print("\n---------- End of Innings ----------") 
 
print("\nFinal Score:")
print("Runs =",runs_2)
print("wickets =",wickets_2)
 
# Result of Match 
 
print("\n~~ Result ~~")
 
if runs_1 > runs_2:
 
    if Bat_first == "You": 
        print("\nCongratulations! You won the Match by",runs_1 - runs_2,"runs.")
        engine.say("\nCongratulations! You won the Match by"+str(runs_1 - runs_2)+"runs.")
        engine.runAndWait()
 
    else:
        print("\nBetter luck next time! The Computer won the Match by",runs_1 - runs_2,"runs.") 
        engine.say("\nBetter luck next time! The Computer won the Match by"+str(runs_1 - runs_2)+"runs.") 
        engine.runAndWait()
 
elif runs_2 > runs_1:
 
    if Bat_second == "You": 
        print("\nCongratulations! You won the Match by",2 - wickets_2,"wickets.")
        engine.say("\nCongratulations! You won the Match by+"+str(2 - wickets_2)+"wickets.")
        engine.runAndWait()
    else:
        print("\nBetter luck next time! The Computer won the Match by",2 - wickets_2,"wickets.")
        engine.say("\nBetter luck next time! The Computer won the Match by"+str(2 - wickets_2)+"wickets.")
        engine.runAndWait()
 
else:
    print("The Match is a Tie.","\nNo one Wins.")
    engine.say("The Match is a Tie.","\nNo one Wins.")
    engine.runAndWait()
playsound("C:\\Python310\\Diwali ! Crackers ! Sound.mp3")