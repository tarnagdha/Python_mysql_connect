import mysql.connector as mc
from mysql.connector import Error
from config import connection_parameters
print(connection_parameters)
search="'%Faible%'"
request="SELECT * FROM utilisateur WHERE income_group LIKE " + search
print(request)
try :
    connection=mc.connect(**connection_parameters)
    if connection.is_connected():
        cursor = connection.cursor()
        cursor.execute(request)
        results = cursor.fetchall()
        print(results)
        cursor.close()
        connection.close()

except Error as e :
    print("la connection a échoué", e)  


