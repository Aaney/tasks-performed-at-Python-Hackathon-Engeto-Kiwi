# task from: http://hack.engeto.com/combinatorics

import itertools
from math import factorial as f

def permute(l,m):
    # listToPermute = input("Please enter the list: ")
    # listToPermute = ['A', 'B', 'C', 'D']
    # repetition = "n"
    listToPermute = l
    repetition = m
    result = []
    if repetition == "y":
        c = 0
        k = itertools.product(listToPermute, repeat=len(listToPermute))
        for i in k:
            result.append((list(i)))
            c += 1
        print("Number of permutations with repetition of n elements=",len(listToPermute)," is n**n=",
              len(listToPermute)**len(listToPermute))
        print("There are", c, "permutations with repetition:")
        for i in result:
            print(i)
    if repetition == "n":
        # Number of permutations without repetition of n elements is n!
        c = 0
        k = itertools.permutations(listToPermute)
        for i in k:
            result.append((list(i)))
            c+=1
        print("Number of permutations without repetition of n elements =",len(listToPermute),"elements is n! =",
              f(len(listToPermute)))
        print("There are", c, "permutations without repetition:")
        for i in result:
            print(i)
#permute()

def combine(l,m):
    # listToPermute = ['A', 'B', 'C', 'D']
    # repetition = "n"
    listToPermute = l
    repetition = m
    result = []
    if repetition == "y":
        c = 0
        #k = itertools.product(listToPermute, repeat = len(listToPermute) - 1)
        k = itertools.combinations_with_replacement(listToPermute,len(listToPermute)-1)
        for i in k:
            result.append((list(i)))
            c += 1
        print("Number of combinations with repetition of k=", len(listToPermute)-1," elements is (n-1+k)!/((n-1)!k!)=",
              f(len(listToPermute) - 1+len(listToPermute) - 1) / (f(len(listToPermute) - 1)*f(len(listToPermute) - 1)))

        print("There are", c, "combinations  with repetition:")
        for i in result:
            print(i)
    if repetition == "n":
        c = 0
        k = itertools.combinations(listToPermute, len(listToPermute)-1)
        for i in k:
            result.append((list(i)))
            c += 1
        print("Number of combinations without repetition of k=", len(listToPermute)-1, " elements is n!/((n-k)!k!)=",
              f(len(listToPermute))/(f((len(listToPermute))-(len(listToPermute)-1))*f(len(listToPermute)-1)))
        print("There are", c, "combinations  without repetition:")
        for i in result:
            print(i)

def combine_or_permute(l):
    decide = input("Combine, permute, repeat or not (cy, cn, py, pn): ")
    if decide[0]=="c":
        combine(l,decide[1])
    if decide[0] == "p":
        permute(l,decide[1])
combine_or_permute(['A', 'B', 'C', 'D'])