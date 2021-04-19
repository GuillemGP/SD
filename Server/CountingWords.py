def contar_palabras_fichero(fname):

    with open(fname,'r') as f:
        words = [word for line in f
                for word in line.strip().split()]

    numPalabras=len(words)
    return(numPalabras)