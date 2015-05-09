'''
Created on May 9, 2015

@author: niko
'''

import numpy as np
import random
from sets import Set

def simulatePrizedoor(nsim):
    prizeDoors = np.random.randint(3, size=nsim)
    return prizeDoors

def simulateGuess(nsim):
    guesses = np.random.randint(3, size=nsim)
    return guesses

def goatDoor(prizeDoors, guesses):
    revealedDoors = np.array([])
    for i in range(len(prizeDoors)):
        allDoors = np.asarray(range(3))
        prizeDoor = prizeDoors[i]      
        guess = guesses[i]
        doorsToRemove = list(set([prizeDoor, guess]))
        goatDoors = np.delete(allDoors, doorsToRemove)
        revealedDoor = random.sample(goatDoors, 1)[0]
        revealedDoors = np.append(revealedDoors, revealedDoor)
    return revealedDoors

def switchGuess(guesses, goatDoors):
    switchedDoors = np.array([])
    for i in range(len(guesses)):
        allDoors = set(range(3))
        guess = guesses[i]
        goat = goatDoors[i]
        switch = allDoors.difference([guess, goat])
        s = next(iter(switch))
        switchedDoors = np.append(switchedDoors, s)
    return switchedDoors

def winPercentage(guesses, prizeDoors):
    guessesCount = len(guesses)
    correctGuessesCount = 0
    for i in range(len(guesses)):
        if guesses[i] == prizeDoors[i]:
            correctGuessesCount += 1
    return correctGuessesCount*100.0/guessesCount

if __name__ == "__main__":
    nsim = 1000
    prizeDoors = simulatePrizedoor(nsim)
    guesses = simulateGuess(nsim)
    goatDoors = goatDoor(prizeDoors, guesses)
    switches = switchGuess(guesses, goatDoors)
    winPercentageNoSwitch = winPercentage(guesses, prizeDoors)
    winPercentageSwitch = winPercentage(switches, prizeDoors)
    
    print "In case of no switching the contestant won %.2f percents of %d games" % (winPercentageNoSwitch, nsim)
    print "In case of switching the contestant won %.2f percents of %d games"% (winPercentageSwitch, nsim)
        
        
        
        