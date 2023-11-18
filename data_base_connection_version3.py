import mysql.connector as mc

import pandas as pd

import json

import os

from mysql.connector import Error

from config import connection_parameters

print("Ouvrons le fichier JSON")
with open("informations.json") as f :
    print("charger les données JSON")
    infoJson = json.load(f)

print("Créons un chemin de dossier")
pathDos = "C:/Users/HP/Desktop/result_request/sous_dos"

print("Créont le dossier avec ses sous dossiers s'il n'existe  pas avec la methode mkdir")
if not os.path.exists(pathDos):
    os.makedirs(pathDos, exist_ok=True)

search="'%Faible%'"

request="SELECT * FROM utilisateur WHERE income_group LIKE " + "'%" + infoJson["seach"] + "%'"

def dbconnection(mysql_connector, params_connection):
    try:
         
        print("connection à la base de donnée en cours")

        connection = mysql_connector.connect(**params_connection)

        if connection.is_connected():
            print("connection à la base de donnée réussie")
            return connection
    
    except Error as e:
    
        print("La connection a échoué")
        return None

object_connection = dbconnection(mc, connection_parameters)
print(object_connection)

def executeQuery(object_connection, query):       
    if object_connection == None :
        return [] 
    
    print("recuperation du curseur")
    cursor = object_connection.cursor()

    print("execution de la requete")
    cursor.execute(query)

    print("Recuperation du resultat")
    results = cursor.fetchall()

    return results

data = executeQuery(object_connection, request)
print(data)

def generateExcel(arrayresults, pandas_object, pathFile):
    
    print("intialisation du dataframe")
    dataframe = pandas_object.DataFrame(arrayresults)

    print("importer les resultats sous format excel")
    dataframe.to_excel(pathFile)
    
    print("Donnée generée sous le nom", infoJson["filename"])

generateExcel(data, pd, pathDos + "/"+infoJson["filename"])


