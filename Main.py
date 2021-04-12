import CountingWords
import WordCount

print('Practica 1 SD\n')

numPalabras=CountingWords.contar_palabras_fichero('ficheroPrueba.txt')
print(numPalabras)
print('\n')

diccionario = WordCount.contar_palabras('ficheroPrueba.txt')
WordCount.ver_palabras(diccionario)