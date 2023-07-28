import requests as requests
import json

def listar_nombre_paises(url):
    paises = requests.get(url)
    paises = paises.json()

    for pais in paises:
        print(f"NOMBRE OFICIAL EN ESPAÑOL:{pais['translations']['spa']['official']}")
        print(f"POBLACIÓN:{pais['population']}")
        print(f"ÁREA:{pais['area']}")

        poblacion_max = max(paises, key=lambda pais:pais['population'])
        print("PAÍS CON MAYOR POBLACIÓN :",poblacion_max['translations']['spa']['official'],"con una polacion",poblacion_max['population'])

        area_max = max(paises, key=lambda pais:pais['area'])
        print("PAÍS CON MAYOR ÁREA", area_max['translations']['spa']['official'], " area:", area_max['area'])


        total = sum(pais['population'] for pais in paises)
        print("POBLACIÓN TOTAL:",total)

        media = total/ len(paises)
        print("MEDIA DE LA POBLACIÓN:",media)

        mediana = paises[len(paises) //2] ['population']
        print("MEDIANA DE LA POBLACIÓN:",mediana)

        moda = max(pais['population'] for pais in paises)
        print("MODA DE LA POBLACIÓN",moda)




url = 'https://restcountries.com/v3.1/all'
listar_nombre_paises(url)