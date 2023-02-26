# -*- coding: utf-8 -*-
"""
Created on Mon Feb 20 08:24:20 2023

@author: Juan Brasdefer, Fabian Pawelczyk
"""


def TowerOfHanoi(n , from_rod, to_rod, aux_rod):
    
    #our base case should be when we only have one disk left in our source rod
    #this means that it triggers when n==1

    #however, since it's recursive, this 'source rod' is not a fixed location
    #but rather an idea to be executed at the micro level
    if n == 1:
        print ("Move disk 1 from source",from_rod,"to destination",to_rod)
        return
    
    #in any other situation, the code moves around the order of
    #the rods in recursion, so that destination goal changes in micro moves

    #sorry, i really don't know how else to explain!! :))
    
    else:
        TowerOfHanoi(n-1, from_rod, aux_rod, to_rod)
        print ("Move disk",n,"from source",from_rod,"to destination",to_rod)
        TowerOfHanoi(n-1, aux_rod, to_rod, from_rod)
         


TowerOfHanoi(3,'A','B','C')