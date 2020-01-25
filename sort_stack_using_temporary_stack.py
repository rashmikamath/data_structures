#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jan 25 20:06:11 2020

@author: rkamath
"""

def sortStack(stack):
    tempStack = createStack()
    while(isEmpty(stack)==False):
        #pop the first element from stack
        tmp = top(stack)
        pop(stack)
        #while temporary stack is not empty and top of temporary stack is greater than tmp
        while((isEmpty(tempStack)==False )and (int(top(tempStack)) > int(tmp))):
            #pop the element from temporary stack and push it to input stack
            push(stack,top(tempStack))
            pop(tempStack)
        #push tmp to temporary stack
        push(tempStack,tmp)
    return tempStack
def createStack():
    stack = []
    return stack

def isEmpty(stack):
    return len(stack)==0

def push(stack,item):
    return stack.append(item)

def pop(stack):
    if isEmpty(stack):
        print("Stack Underflow")
        exit()
    return stack.pop()

def top(stack):
    p = len(stack)
    return stack[p-1]

def prints(stack): 
    for i in range(len(stack)-1, -1, -1): 
        print(stack[i], end = ' ') 
    print() 
        
stack = createStack() 
push( stack, str(34) ) 
push( stack, str(3) ) 
push( stack, str(31) ) 
push( stack, str(98) ) 
push( stack, str(92) ) 
push( stack, str(23) ) 
  
print("Sorted numbers are: ") 
sortedst = sortStack ( stack ) 
prints(sortedst) 
  