import mysql.connector as mc

import pandas as pd

from mysql.connector import Error

from config import connection_parameters


search="'%Faible%'"

request="SELECT * FROM utilisateur WHERE income_group LIKE " + search

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
    
    print("Donnée generée sous le nom 'data'")

generateExcel(data, pd, "dataExcel.xlsx")


