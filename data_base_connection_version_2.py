import mysql.connector as mc

import pandas as pd

from mysql.connector import Error

from config import connection_parameters


search="'%Faible%'"

request="SELECT * FROM utilisateur WHERE income_group LIKE " + search


try :
    print("connection à la base de donnée en cours")
    connection=mc.connect(**connection_parameters)
    if connection.is_connected():
        print("connection à la base de donnée réussie")

        print("recuperation du curseur")
        cursor = connection.cursor()

        print("execution de la requete")
        cursor.execute(request)

        print("Recuperation du resultat")
        results = cursor.fetchall()
        
        print("intialisation du dataframe")
        dataframe=pd.DataFrame(results)

        print("importer les resultats sous format excel")
        dataframe.to_excel("data.xlsx")
        print("Donnée generée sous le nom 'data'")

        cursor.close()
        connection.close()
        
except Error as e :
    print("la connection a échoué", e)  


