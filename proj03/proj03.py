# Name:Zeke
# Date:7/12/17



#proj 03: Guessing Game

#Generate a random number between 1 and 9 (including 1 and 9).
#Ask the user to guess the number, then tell them whether they guessed too low, too high,
#or exactly right. Keep the game going until the user types exit.
#Keep track of how many guesses the user has taken, and when the game ends, print this out.
import random
variable_name = random.randint(1,9)
loop_control = True
guesses = 4
user = int(raw_input('I am thinking of a number 1-9. Can you guess it? :'))
while user != variable_name and guesses != 1:
    guesses = guesses - 1
    print 'you have'
    print guesses
    print 'guesses left'
    if user > variable_name:
        print 'That is to high '
        loop_control = True
        user = int(raw_input('I am thinking of a number between 1-9. Can you guess it? :'))
    elif user < variable_name :
        print 'That is too low! '
        user = int(raw_input('I am thinking of a number 1-9. Can you guess it? :'))
if user == variable_name:
    print 'Congratulations you guessed my number!!!! '
else:
    print "Sorry you're out of guesses... But don't take it out on me. It's not MY fault you suck at this game."


#     loop_control == False
#         loop_control = False
#     print 'Congratulations you guessed my number!'
# elif guesses == 0 :
#     while loop_control == False :
#         loop_control = False
# else :
#     print 'Sorry, try again.'
#     while loop_control == True :
#         loop_control = True
#     guesses = guesses - 1
#     print 'You only have'
#     print guesses
#     print 'left.'




