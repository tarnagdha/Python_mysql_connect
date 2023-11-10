import mysql.connector

from config import connection_parameters
print(connection_parameters)
search="'%Faible%'"
request="SELECT * FROM utilisateur WHERE income_group LIKE " + search
print(request)