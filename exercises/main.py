from random import randint
from os import remove, rename
from p import P
import constant

def getUserScore(userName):
    try:
        input = open('userScores.txt', 'r')
        for line in input:
            content = line.split(',')
            if content[0] == userName:
                input.close()
                return content[1]
        input.close()
        return "-1"
    except IOError:
        print ("\nFile userScores.txt not found. A new file will be created.")
        input = open('userScores.txt', 'w')
        input.close()
        return "-1"

if __name__ == '__main__':
    print(getUserScore('Carol'))

    x = P(name='Alex', alias='amen')
    x.who()

    print(constant.PI)
    print(constant.GRAVITY)