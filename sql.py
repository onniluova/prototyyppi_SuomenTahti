import mysql.connector

yhteys = mysql.connector.connect(
         host='127.0.0.1',
         port= 3306,
         database='lentokonepeli',
         user='dbuser',
         password='sAL_a3ana',
         autocommit=True
         )

