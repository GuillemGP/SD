def contar_palabras(ruta):
   texto = open(ruta, "r")

   diccionario = dict()

   for linea in texto:
      # Quitamos de la linea los saltos 
      linea = linea.strip()

      # Convertimos toda la linea en letras minúsculas
      linea = linea.lower()

      # Reemplazamos los paréntesis que puedan aparecer en el texto
      linea = linea.replace("(", "").replace(")", "")

      # Convertimos la linea a diccionario de palabras
      palabras = linea.split(" ")

      for palabra in palabras:
	     # Si la palabra ya se encuentra en diccionario
         if palabra in diccionario:
	        # La palabra suma uno
            diccionario[palabra] += 1

	    # Si aún no se encuentra
         else:
            diccionario[palabra] = 1

   return diccionario


def ver_palabras(diccionario):
   for palabra in list(diccionario.keys()):
      print(palabra, ":", diccionario[palabra])