import mysql.connector
from nltk.tokenize import RegexpTokenizer
#Tokeniser
tokenizer = RegexpTokenizer("[\w']+")
mydb = mysql.connector.connect(host='10.0.0.151',user='etl_readonly_V3',password='rdelTonlyEvVer3',db='ev_dw')
mycursor = mydb.cursor()
mycursor.execute("SELECT * FROM flat_ed_places WHERE key_id=50 ")
result = mycursor.fetchall()
for i in result:
    tokenizer.tokenize(print(i))
