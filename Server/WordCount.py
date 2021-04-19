def contar_palabras(ruta):

   file=open(ruta, 'r')
   palabras={}
   result = ""
   for word in file.read().split():
      if word not in palabras:
         palabras[word] = 1
      else:
         palabras[word] += 1
   for k,v in palabras.items():
      result = result + str(k) + ":" + str(v) +" "
   return result


def ver_palabras(diccionario):
   for palabra in list(diccionario.keys()):
      print(palabra, ":", diccionario[palabra])