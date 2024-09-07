import mysql.connector
import time
from rich import print
from rich.console import Console
console = Console()

def introduce():
  bold_white = '[bold white]'
  bold_white_end = '[/bold white]'

  intro_line1 = f"\t{bold_white}Hi, there!{bold_white_end}, This is a simple, {bold_white}CLI application{bold_white_end}, that {bold_white}retrieves{bold_white_end} verses from {bold_white}the Quran{bold_white_end}.\n"
  intro_line2 = f"\tThis application uses {bold_white}MySQL database{bold_white_end} to store and {bold_white}retrieve verses{bold_white_end}."
  intro_line3 = f"\tYou can use the {bold_white}following options{bold_white_end} to interact with the application:\n"
  border = "_______________________________________________________________________________________\n"

  for i in border:
    print(f"[bold white]{i}", end='', flush=True)
    time.sleep(0.008)
  print(intro_line1)
  print(intro_line2)
  print(intro_line3, end='', flush=True)
  for i in border:
    print(f"[bold white]{i}", end='', flush=True)
    time.sleep(0.008)
  

def menu():
  option_color = '[bold green1]'
  number_color = '[white]'
  print(f"{number_color}1. {option_color}Show a verse.")
  print(f"{number_color}2. {option_color}Show a random verse.")
  print(f"{number_color}3. {option_color}Show an entire chapter(surah).")
  print(f"{number_color}4. {option_color}Show first N verses of a chapter.")
  print(f"{number_color}5. {option_color}EXIT")
  print(f"[bold turquoise4]Your choice? ", end='', flush=True)
  choice = int(input())
  return choice

def getInput():
  print("[bold bright_white]Enter chapter number: ", end='', flush=True)
  chapter = int(input())
  print("[bold bright_white]Enter verse number: ", end='', flush=True)
  verse = int(input())
  return [chapter, verse]

def executeQuery(cursor, query):
  cursor.execute(query)
  result = cursor.fetchall()
  print("_____________________________________________________\n")
  for row in result:
    printVerse(row, row[2], row[3])
  print("_____________________________________________________")

def printVerse(verse, chapter, versenum):
  verseText = verse[4]
  verseText = list(verseText)
  for i in list(verseText):
    print(f"[bold green3]{i}", end='', flush=True)
    time.sleep(0.05)
  print(f"[bold bright_white] ({chapter}:{versenum})")

def main():
  try:
    mydb = mysql.connector.connect(
        host="localhost",     # enter IP address if the database is not locally hosted
        user="syed",              # replace with your database username
        password="itsokay03",          # replace with your DB password
        database="QURAN"           # Name of the database
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
        print("See ya...")
        break

      else:
        print("Okay, you're smart I get it -_-")
        continue

  except mysql.connector.Error as err:
    print(err)
    return

  finally:
    if mydb.is_connected():
      mydb.close()


introduce()
main()