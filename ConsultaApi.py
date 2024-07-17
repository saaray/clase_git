# -*- coding: utf-8 -*-
"""
Created on Wed Jul 17 17:29:52 2024

@author: Saray
"""

import requests

url = "https://jsonplaceholder.typicode.com/comentarios"

respuesta= requests.get(url)

if respuesta.status_code ==200:
    print("solucitud exitosa")
    print("datos",respuesta.json())
else:
    print("error en la solicitud del recurso. Detalles:\n ",
          respuesta.text)
    


