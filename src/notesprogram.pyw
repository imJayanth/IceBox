from notes import *
import sqlite3, sys, pyautogui
from datetime import date,datetime
import os

def start():
    ui.choosefile.clear()
    data = db_select_all_notes()  
    for d in data:
        ui.choosefile.addItem(str(d[3]))
def textformat(liste):
    text='Note ID: '+str(liste[0])+'<br/>'+'Date: '+liste[1]+'<br/>'+'Time: '+liste[2]+'<br/>'+'Title: '+liste[3]+'<br/>'+'Content: '+liste[4]+'<br/>'
    front="<html><head/><body><p align=\"center\"><span style=\" font-size:14pt; font-weight:600; color:#ffffff;\">"
    back='</span></p></body></html>'
    text=front+text+back
    return text

def notext():
    front="<html><head/><body><p align=\"center\"><span style=\" font-size:14pt; font-weight:600; color:#ffffff;\">"
    back='</span></p></body></html>'
    text=front+'Empty !'+back
    return text
def timenow():
    now = datetime.now()
    atime=str(now.strftime("%H:%M:%S"))
    return atime 

def db_insert_note(note_id,username, title, note):
    mycursor = conn.cursor()
    d= date.today()
    mycursor.execute("INSERT INTO {tn} (note_id,username,note_date,title, note,time) VALUES(?,?,?, ?, ?,?)".format(tn="tb_notes"),(note_id,username,d,title, note,timenow()))
    conn.commit()
    
def db_select_all_notes():
    mycursor = conn.cursor()
    mycursor.execute("SELECT * from tb_notes")
    return mycursor.fetchall()

def db_select_specific_note(username, title):
    mycursor = conn.cursor()
    mycursor.execute('SELECT note_id,note_date,time,title,note FROM tb_notes WHERE title = ? and username = ?',(title,username))
    return mycursor.fetchone()


def db_delete_note(title):
    mycursor = conn.cursor()
    mycursor.execute("DELETE FROM {tn} WHERE title = ? and username= ?".format(tn="tb_notes"),(title,username))
    conn.commit()

def save():
    noteid=0
    text=str(ui.content.toPlainText())
    title=str(ui.title.text())
    if(text!='' and title!=''):
        while 1:
            try:
                db_insert_note(noteid,username,title, text)
                break
            except:
                noteid=noteid+1
    else:
        pyautogui.alert('Note Empty !','ALERT')
    ui.choosefile.clear()
    data = db_select_all_notes()  
    for d in data:
        ui.choosefile.addItem(str(d[3]))

def shownote():
    try:
        notename=str(ui.choosefile.currentText())
        dbs=db_select_specific_note(username, notename)
        ui.shownote.setText(textformat(dbs))
    except:
        pass
def deletenote():
    try:
        notename=str(ui.choosefile.currentText())
        db_delete_note(notename)
        ui.shownote.setText(notext())
        start()
    except:
        pass
##            print(str(sys.exc_info()))    
    
if __name__ == "__main__":
    username='asd'   # for test purpose
    file=open('name','r')
    username=str(file.read())
    file.close()
    os.remove('name')
    conn = sqlite3.connect("notes.db")
    mycursor = conn.cursor()
    query = "CREATE TABLE IF NOT EXISTS tb_notes (note_id INT PRIMARY KEY,username varchar(255),note_date date, title VARCHAR(255) NOT NULL,note VARCHAR(2000) NOT NULL,time varchar(255))"
    mycursor.execute(query)
    app = QtWidgets.QApplication(sys.argv)
    Notes = QtWidgets.QMainWindow()
    ui = Ui_Notes()
    ui.setupUi(Notes)
    Notes.show()
    pyautogui.alert('Here you can save your notes securely\nYou can also use this as a secret diary as date and time are stored accurately','Information')
    start()
    ui.savebutton.clicked.connect(save)
    ui.viewnotebutton.clicked.connect(shownote)
    ui.deletenote.clicked.connect(deletenote)
    sys.exit(app.exec_())
