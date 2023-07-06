import itertools

string = input("String a ser permutada: ")

resultado = itertools.permutations(string,len(string))

for char in resultado:
    print(''.join(char))