# Nom, Matricule
# Nom, Matricule

import math
import sys


def read_problem(input_file="input.txt"):
    """Fonctions pour lire/écrire dans les fichier. Vous pouvez les modifier,
    faire du parsing, rajouter une valeur de retour, mais n'utilisez pas
    d'autres librairies.
    Functions to read/write in files. you can modify them, do some parsing,
    add a return value, but don't use other librairies"""

    # lecture du fichier/file reading
    file = open(input_file, "r")
    lines = file.readlines()
    file.close()




    info = (lines[0].removesuffix("\n")).split()

    nbPiliers = int(info[3])

    piliers = [None]*nbPiliers

    for i in range (nbPiliers):
        piliers[i]=int(lines[i+1].removesuffix("\n"))
        


    return [info, piliers]




def write(fileName, content):
    """Écrire la sortie dans un fichier/write output in file"""
    file = open(fileName, "w")
    file.write(content)
    file.close()


def main(args):
    """Fonction main/Main function"""
    input_file = args[0]
    output_file = args[1]

    input = read_problem(input_file)
    info = input[0]
    length = int(info[0])
    minDist = int(info[1])
    endsMinDist = int(info[2])
    nbPiliers = int(info[3])

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

    

    write(output_file,str(possible))


# NE PAS TOUCHER
# DO NOT TOUCH
if __name__ == "__main__":
    main(sys.argv[1:])
