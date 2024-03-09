# Cassandre Hamel, 20210863
# Viviane Binet, 20244728

import math
import sys


def read_problem(input_file="input.txt"):

    # lecture du fichier/file reading
    file = open(input_file, "r")
    lines = file.readlines()
    file.close()


    nbJours=int(lines[0].removesuffix('\n'))

    ligneW = (lines[1].removesuffix("\n")).split()
    W=[None]*len(ligneW)
    for i in range (len(ligneW)):
        W[i]=int(ligneW[i])

    return [nbJours, W]


def write(fileName, content):
    """Écrire la sortie dans un fichier/write output in file"""
    file = open(fileName, "w")
    file.write(content)
    file.close()


def main(args):
    """Fonction main/Main function"""
    input_file = args[0]
    output_file = args[1]

    info = read_problem(input_file)
    nbJours = info[0]
    W = info[1]

    # find max[W]:
    def max(array):
        max = array[0]
        for i in range (1, len(array)):
            if array[i]>max:
                max = array[i]
        return max
    
    maxW = max(W)

    # number of days the wood would last if we burn x logs/day
    def daysLasting(x):
        total = 0
        for i in range (len(W)):
            total+= math.ceil(W[i]/x)
        return total
    

    if (len(W) == nbJours):
        B = maxW

    else:
        minB = math.ceil(sum(W)/nbJours)

        # binary search between minB and maxW
        i = minB
        j = maxW
        x = j
        while i != j:
            x = (i+j)//2
            if daysLasting(x) == nbJours:
                j = x

            elif daysLasting(x)<nbJours:
                j = x

            elif daysLasting(x)>nbJours:
                i = x + 1

        B = i

    write(output_file, str(B))


# NE PAS TOUCHER
# DO NOT TOUCH
if __name__ == "__main__":
    main(sys.argv[1:])
