#Realizado con Python 3.8.10 64-bits en Ubuntu 20.04.2 LTS mediante WSL
#Importar las librerías panda, numpy y colorama
from colorama import Fore #Cambiar color del texto
import pandas as pd
import numpy as np
from sty import fg, bg, ef, rs, Style, RgbFg #Cambiar color del texto a naranja
#import os #Importar os para limpiar la pantalla
#os.system("clear")#Limpiar la pantalla con clear, si se está usando un sistema basado en UNIX
#Mostrar todas las filas
pd.set_option('display.max_rows', 100)
#Leer el archivo bd.xlsx
df = pd.read_excel('bd.xlsx')
#Determinar si la persona tiene COVID
df['¿Tiene COVID?']=np.where(df['Indicador']>=0.8, 'Sí', 'No')
si_covid=df[df['¿Tiene COVID?']=='Sí']
no_covid=df[df['¿Tiene COVID?']=='No']
#Imprimir la tabla
print(df)
#Imprimir la edad promedio de los contagiados
print("La edad promedio de los", len(si_covid),"contagiados es de", + si_covid['Edad'].mean().round(0), "años")
contagiados=len(si_covid)
#Evaluar semáforo epidemiológico
if contagiados==0:#Si no hay contagiados
    print(Fore.GREEN + 'Semáforo verde')
elif contagiados>=1 and contagiados<=30:#Si hay de 1 a 30 contagiados
    print(Fore.YELLOW + 'Semáforo amarrillo')
elif contagiados>=31 and contagiados<=70:#Si hay de 31 a 70 contagiados
    fg.orange = Style(RgbFg(255, 150, 50))#Código RBG del naranja
    #Cambiar el texto a naranja
    naranja = fg.orange + 'Semáforo naranja' + fg.rs
    print(naranja,'\n')#Imprimir el resultado
elif contagiados>=71 and contagiados<=100:#Si hay mas de 70 contagiados
    print(Fore.RED + 'Semáforo rojo')