from passmanager import *
from passwordgen import *
import sqlite3, sys, os, easygui, pyautogui

connection = sqlite3.connect("pass.db")
crsr = connection.cursor()
sql_command = """CREATE TABLE passwords (name varchar(100),website varchar(100), password varchar(100));"""
try:
    crsr.execute(sql_command)
except:
    pass
username='asd'   # for test purpose
file=open('name','r')
username=str(file.read())
print(username)
file.close()
os.remove('name')

def typepassword(text):
    a=str(pyautogui.confirm('Place the cursor where you want your password'))
    if(a=='OK'):
        pyautogui.write(text)

def filesafe():
    file=open('name','w')
    file.write(username)
    file.close()
    os.system('filesafeprogram.pyw')
    
def secnotes():
    file=open('name','w')
    file.write(username)
    file.close()
    os.system('notesprogram.pyw')

def textedit(liste):
    if(len(liste)==0):
        a='No Passwords To Show !'
    else:
        a=[str(i) for i in liste]
        a='<br/>'.join(a)
    a='(Website,Password)<br/>'+a
    text="<html><head/><body><p align=\"center\"><span style=\" font-size:18pt; font-weight:600; color:#ffffff;\">"+a+"</span></p></body></html>"
    return text

def create():
    website=easygui.enterbox('Enter the Website for Which You Are Saving the Password')
    password=givepassword('pass')
    a=str(pyautogui.confirm('\tPress OK To use this strong pasword \nor Press Cancel to Enter your own Password \n\n PASSWORD suggested : ' + password,'ALERT'))
    if(a!='OK'):
        password=easygui.enterbox('Enter the Password')
        pyautogui.alert(teststrength(password),'Password Analysis')
    else:
        print('')
    command="INSERT INTO passwords VALUES (?,?,?);"
    sql_command = command
    try:
        crsr.execute(sql_command,(username,website,password))
        connection.commit()
        pyautogui.alert('Name : '+str(username)+'\n'+'Website : '+str(website)+'\n'+'Password : '+str(password)+'\n','Password Added !')
    except:
        pyautogui.alert(str(sys.exc_info()),'ERROR')

def use():
    try:
        website=easygui.enterbox('Enter the Website for Which You Want the Password')
        crsr.execute('SELECT password FROM passwords where website = ? and name= ?', (website,username))
        ans= crsr.fetchall()
        typepassword(str(ans[0][0]))
    except:
        pyautogui.alert('No passwords Exist fot That Website','ERROR')

def show():
    try:
        crsr.execute('SELECT website,password FROM passwords where name = ? ',(username,))
        ans= crsr.fetchall()
        ui.passpage.setText(textedit(ans))
        print(ans)
        connection.commit()
    except:
        pyautogui.alert(str(sys.exc_info()),'ERROR')

def delete(name):
    website=easygui.enterbox('Enter the Website for Which You Want To Delete The Password')
    try:
        crsr.execute("DELETE FROM passwords WHERE website = ? and name = ?; ",(website,username))
        connection.commit()
        pyautogui.alert('Deleted\n To see updated results, press Show All Passwords Button','Done')
    except:
        pyautogui.alert(str(sys.exc_info()),'ERROR')
        print(str(sys.exc_info()))

def edit():
    website=easygui.enterbox('Enter the Website for Which You Want to Update the Password')
    password=easygui.enterbox('Enter the Password')
    try:
        crsr.execute('UPDATE passwords SET password = ? WHERE website = ? and name = ?;',(password,website,username))
        connection.commit()
    except:
        pyautogui.alert(str(sys.exc_info()),'ERROR')

        
app = QtWidgets.QApplication(sys.argv)
PasswordManager = QtWidgets.QMainWindow()
ui = Ui_PasswordManager()
ui.setupUi(PasswordManager)
PasswordManager.show()
pyautogui.alert('All Your Passwords can be stored here safely\nTo use FileSafe or SecretNotes Press Respective buttons on the top right corner of this window','Information')
ui.createpass.clicked.connect(create)
ui.showpass.clicked.connect(show)
ui.usepass.clicked.connect(use)
ui.deletepass.clicked.connect(delete)
ui.editpass.clicked.connect(edit)
ui.usefilesafe.clicked.connect(filesafe)
ui.usenotes.clicked.connect(secnotes)
sys.exit(app.exec_())
