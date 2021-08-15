#Magazyn Moduł 5 
#1commit f exit program ma ie włczyć 
#import sys


def exit(a):
    while a != 'exit':
        print("wpisałeś coś innego niż exit ")
        break
    print('by by')
    exit(0)

if __name__== '__main__':
    a=input("na razie wpisz tylko exit")
    exit(a)