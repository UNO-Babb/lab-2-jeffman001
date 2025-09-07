#Magic8Ball.py
#Name:
#Date:
#Assignment:

#We will need random for this program, import to use this package.
import random

def main():
  #Create a list of your responses.
  print("Magic 8 Ball")
  #Prompt the user for their question.
question = input ("what will you ask today?:  ")
  #Answer question randomly with one of the options from your earlier list.
answers = [ "okay, sure", "mayhaps", "why are you even asking ME that?", "nope", "maybe that's something you should ask yourself", "why??", "not right now",
           "lemme finish this game real quick", "you better not", "if you want me to lose a bet, sure", "there's an easy solution to this, throw me", "maybe think about that more",
            "Insert answer 13 here", "how would I know that?", "Ha, I'd like to see you try", "I mean its not impossible", "RUN", "Bop It!", "you know what go do it! just leave me over here beforehand though",
             "sooner is better than later, or was it the other way around?", "cry about it" ]
length=len(answers)
r=random.random() * length
r = int(r) #cuts off decimal
print (r)
response=answers[r]
print (response)
if __name__ == '__main__':
  main()
