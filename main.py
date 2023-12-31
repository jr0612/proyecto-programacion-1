import info_basica
import cien_palabras
import frec_letras
import lon_palabras
import palabras_diferentes
import detectar_idioma
import stopwords
import epoca_del_texto
import lugares_y_personajes_2
import lugares_y_nombres
import personajes_principales
from tkinter import filedialog , Tk


opiton = None
opiton2 = None
texto = None
def abrir_archivo():
     ventana = Tk()
     ventana.withdraw()
     ventana.attributes('-topmost', True)
     ruta_archivo = filedialog.askopenfile(initialdir='/', title='Selecciona el texto',
                                           filetypes=(("Archivos de texto", '*.txt') ,('Todos los archivos' , '*.*')))
     if ruta_archivo:
          with open(ruta_archivo.name ,'r', encoding='utf-8' ) as archivo:
               texto = archivo.read()
               return texto
     ventana.destroy()

     
  
def mostrar_info_basica(texto):
    resultado = 'El texto tiene: ' +str(info_basica.contar_caracteres(texto)) +' caracteres\nEl texto tiene: '+ str(info_basica.contar_palabras(texto)) + ' palabras'
    return resultado

def mostrar_100_pals(texto):
     pals = cien_palabras.frec_palabras(texto)
     for pal in pals:
          print(pal)

def mostrar_no_stop_words(texto):
     idioma= detectar_idioma.detectar_idioma_2(texto)
     pals = stopwords.calcular_frecuencia(texto, idioma)
     for palabra, frecuencia in pals[:50]:
          print(f"{palabra}: {frecuencia}")

def menu_inicial():
     print('Recuerde tener instaladas las siguientes librerias para un completo funcionamiento:')
     print('unidecode')
     print('matplotlib')
     print('spacy\n')
     print('Tambien ejecutar el siguiente comando en el terminal:')
     print('python -m spacy download es_core_news_md\n')
     print("PROCESADOR DE INFORMACION TEXTUAL")
     print()

     

     print("1.Abrir archivo")
     print("2.Salir")
     option = int(input('Elije una opción: '))
     while True:
          if option == 1:
               texto = abrir_archivo()
               if texto:
                    print('\nTexto cargado con exito.')
                    menu_herramientas(texto)
               else:
                    print('\nEl archivo no fue cargado con exito\n')
                    menu_inicial()
                    break
               break
          elif option == 2:
               print('Hasta pronto.')
               break
          else:
               print()
               print()
               print('RESULTADO:')               
               print('opcion invalida, por elija una opcion valida.\n')
def menu_herramientas(texto):

     
     print("\nHERRAMIENTAS\n")
     print('1.Informacion basica')
     print('2.Histograma de frecuencia de letras')
     print('3.Histograma de longitud de palabras')
     print('4.Cien palabras mas frecuentes')
     print('5.Numero de palabras distintas')
     print('6.Identificar idioma')
     print('7.Cincuenta palabras mas frecuentes que no son stop words')
     print('8.Identificar personajes')
     print('9.Identificar personjes principales')
     print('10.Identificar lugares (solo para textos en español)')
     print('11.Identificar el tiempo en que transcurre el texto (solo para textos en español)')
     print('12.atras')
     option = int(input('Elije ulna opcion: '))
     while True:
          if option ==1:
               print()
               print()
               print('RESULTADO:')
               print(mostrar_info_basica(texto))
               menu_herramientas(texto)
               break
          if option == 2:
               print()
               print()
               print('RESULTADO:')               
               frec_letras.frec_letras(texto)
               menu_herramientas(texto)
               break
          if option == 3:
               print()
               print()
               print('RESULTADO:')
               lon_palabras.histograma_longitudes_palabras(texto)
               menu_herramientas(texto)
               break

          if option == 4:
               print()
               print()
               print('RESULTADO:')
               mostrar_100_pals(texto)
               menu_herramientas(texto)
               break
          if option == 5:
               print()
               print()
               print('RESULTADO:')
               print('Cantidad de palabras distintas en el texto: ' + str(palabras_diferentes.contar_palabras_diferentes(texto)))
               menu_herramientas(texto)
               break
          if option == 6:
               print()
               print()
               print('RESULTADO:')
               print('El texto se encuentra en el idioma '+ detectar_idioma.detectar_idioma_2(texto) + ".")
               menu_herramientas(texto)
               break
          if option == 7:
               print()
               print()
               print('RESULTADO:')
               mostrar_no_stop_words(texto)
               menu_herramientas(texto)
               break
          if option == 8:
               print()
               print()
               print('RESULTADO:')
               print(lugares_y_nombres.frec_personajes(lugares_y_personajes_2.lugares_libreria(texto,'personajes'),texto))
               menu_herramientas(texto)
               break
          if option == 9:
               print()
               print()
               print('RESULTADO:')
               print(personajes_principales.personajes_principales(lugares_y_nombres.frec_personajes(lugares_y_personajes_2.lugares_libreria(texto,'personajes'),texto)))
               menu_herramientas(texto)
               break
          if option == 10:
               print()
               print()
               print('1.Sin libreria')
               print('2.Con libreria')          
               option2 = int(input('Elije una opción: '))
               if option2 == 1:
                    print(lugares_y_nombres.lugares(lugares_y_nombres.nom_prop(texto),texto))
               elif option2 ==2:
                    print(lugares_y_personajes_2.lugares_libreria(texto, 'lugares'))
               else:
                    print('Opcion invalida')

               menu_herramientas(texto)
               break
          
          if option == 11:
               print()
               print()
               print('RESULTADO:')
               print(epoca_del_texto.determinar_periodo_tiempo(texto))
               menu_herramientas(texto)
               break
          elif option ==12:
               menu_inicial()
               break
          else:
               print('opcion invalida, por elija una opcion valida.\n')
               menu_herramientas(texto)
               break 




menu_inicial()   