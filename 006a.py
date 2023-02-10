import sqlite3 as sql
import random
import time

#Opgaven:
#Indsæt random temperatur til random byer i sql database og vis dem.
#Vis temp i aarhus.
#Vis de 10 koldeste byer.

#Om der skal ryddes op være loop
cleanUp = False

#Hastighed i sekunder, hvis man ville have at while loopet skal kør hurtigher eller langsommer
hastighed = 2

#Tilslutter databasen og fjerner alt fra table city, kør fra ny
db = sql.connect('cityTemp.db')
db.cursor()
db.execute('drop table IF EXISTS city')
db.close()

#En liste af byer
cities = ['Aarhus', 'Tokyo', 'Delhi', 'Shanghai', 'Dhaka', 'Sao Paulo', 'Mexico City', 'Cairo', 'Beijing', 'Mumbai', 'Osaka', 'Chongqing', 'Karachi', 'Istanbul', 'Kinshasa', 'Lagos', 'Buenos Aires', 'Kolkata', 'Manila', 'Tianjin', 'Guangzhou', 'Rio De Janeiro', 'Lahore', 'Bangalore', 'Shenzhen', 'Moscow', 'Chennai', 'Bogota', 'Paris', 'Jakarta', 'Lima', 'Bangkok', 'Hyderabad', 'Seoul', 'Nagoya', 'London', 'Chengdu', 'Nanjing', 'Tehran', 'Ho Chi Minh City', 'Luanda', 'New York City', 'Wuhan', 'Xi An Shaanxi', 'Ahmedabad', 'Kuala Lumpur', 'Hangzhou', 'Surat', 'Suzhou', 'Hong Kong', 'Riyadh']

#Main while loop
while 1:
   #Tilslutter databasen igen og rydder table op, hvis cleanUp = True, danner ny table hvis ikke den findes
   db = sql.connect('cityTemp.db')
   db.cursor()
   if cleanUp:
      db.execute('drop table IF EXISTS city')

   db.execute('CREATE TABLE IF NOT EXISTS city (city TEXT, temperature INTEGER, dateTime DATETIME DEFAULT CURRENT_TIMESTAMP)')


   #Giver en prompt at følgende byer bliver bliver updateret
   print("\nUpdating cities...")
   for city in cities:
      currentRandomInt = random.randint(-40, 40)
      db.execute('INSERT INTO city (city, temperature) VALUES (?,?)', (city, currentRandomInt))
      print(f"{city}: {currentRandomInt}")
   db.commit()

   #Sortere byers tempaturer koldeste og printer ud
   tableSelectTemp10 = db.execute('SELECT * FROM city ORDER BY temperature ASC LIMIT 10')
   print("\nTop 10 koldeste lande/byer i øjeblikket:")
   for row in tableSelectTemp10:
      print(f"{row[0]}: {row[1]}C")

   #Finder den nyeste Aarhus row og printer ud
   tableSelectAarhus = db.execute('SELECT * FROM city WHERE city = "Aarhus" ORDER BY dateTime DESC LIMIT 1')
   print(f"\nTempaturen i Aarhus i øjeblikket: {tableSelectAarhus.fetchone()[1]}C")
   
   #Lukker databasen og venter lidt i programmet for while loopet
   db.close()
   time.sleep(hastighed)