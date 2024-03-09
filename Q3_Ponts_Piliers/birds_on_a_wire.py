
import math
import sys


def read_problem():

    info = input().split()

    nbPiliers = int(info[2])

    piliers = [None]*nbPiliers

    for i in range (nbPiliers):
        piliers[i]=int(input())
        

    return [info, piliers]


def main(args):

    input = read_problem()
    info = input[0]
    length = int(info[0])
    minDist = int(info[1])
    endsMinDist = 6
    nbPiliers = int(info[2])

    piliers = input[1]

    possible = 0

    if nbPiliers>0:

        # Trier piliers
        piliers.sort()


        # Calculer distances entre les piliers
        dist = [None]*(len(piliers)-1)

        for i in range (len(dist)):
            dist[i] = piliers[i+1]-piliers[i]

        # Calculer la distance entre les piliers aux extrémités et la limite où ils peuvent être
        endsDist = [piliers[0]-endsMinDist, length-piliers[-1]-endsMinDist]
    


        # piliers de plus entre les piliers existants
        for d in dist:
            if d >= 2*minDist:
                
                possible += d//minDist-1

        # piliers de plus aux extremites
        for d in endsDist:
            if d >= minDist:
                possible += d//minDist
 


    else:       # 0 piliers
        possible = (length-2*endsMinDist)//minDist+1
    

    print(possible)


if __name__ == "__main__":
    main(sys.argv[1:])