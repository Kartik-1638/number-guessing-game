import random
number=input('enter the number you want to be guessed :- ')
chances=0
while(chances<=2):
    guess=input('Enter your guessed number, I hope you lose :) :- ')
    if(guess==number):
        print('It was a wrong choice, SIKE you guessed it right')
        break
    chances=chances+1

if (chances==3):
    print('hehe all your guesses are incorrect BAHAHAHAHHAAHA, better luck next time though')


