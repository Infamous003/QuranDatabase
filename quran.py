import mysql.connector

def introduce():
  print("_______________________________________________________________________________________\n")
  print("\tHi there! This is a simple CLI application that retrieves verses from the Quran.\n")
  print("\tThis application uses MySQL database to store and retrieve verses.")
  print("\tYou can use the following options to interact with the application:\n")
  print("________________________________________________________________________________________")

def menu():
  print("1. Show a verse.")
  print("2. Show a random verse.")
  print("3. Show an entire chapter(surah).")
  print("4. Show first N verses of a chapter.")
  print("5. EXIT")

  choice = int(input("Your choice? "))
  return choice

def getInput():
  chapter = int(input("Enter chapter number: "))
  verse = int(input("Enter verse number: "))
  return [chapter, verse]

def executeQuery(cursor, query):
  cursor.execute(query)
  result = cursor.fetchall()

  print("##########################################################\n\n")
  for row in result:
    print(f"{row[3]} ({row[1]}:{row[2]})")
  print("\n\n##########################################################")

def main():
  try:
    mydb = mysql.connector.connect(
        host="localhost",     # enter IP address if the database is not locally hosted
        user="",              # Username of the datbase
        password="",          # Password of the database server
        database=""           # Name of the database
    )
    mycursor = mydb.cursor()
    while True:
      choice = menu()
      if choice == 1:
        [chapter, verse] = getInput()
        query = f"SELECT * FROM `english_yusuf_ali` WHERE `sura`={chapter} AND `verse`={verse};"
        executeQuery(mycursor, query)

      elif choice == 2:
        query = "SELECT * FROM `english_yusuf_ali` ORDER BY RAND() LIMIT 1;"
        executeQuery(mycursor, query)

      elif choice == 3:
        chapter = int(input("Enter chapter number: "))
        query = f"SELECT * FROM `english_yusuf_ali` WHERE `sura`={chapter};"
        executeQuery(mycursor, query)

      elif choice == 4:
        chapter = int(input("Enter chapter number: "))
        numberOfVerse = int(input("Enter number of verses to be shown: "))
        query = f"SELECT * FROM `english_yusuf_ali` WHERE `sura`={chapter} LIMIT {numberOfVerse};"
        executeQuery(mycursor, query)

      elif choice == 5:
        print("Salam...")
        break

      else:
        print("Astagfirullah, NO!")
        continue

  except mysql.connector.Error as err:
    print("Error connection :?/".format(err))

  finally:
    if mydb.is_connected():
      mydb.close()


introduce()
main()