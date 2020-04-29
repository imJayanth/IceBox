from filesafe import *
import sqlite3
import sys, easygui,pyautogui, shutil
import pyAesCrypt, os
def textedit(liste):
    if(len(liste)==0):
        a='No Files To Show !'
    else:
        a=[str(i[0]) for i in liste]
        a='<br/>'.join(a)
    a='List of Files Available<br/><br/>'+a
    text="<html><head/><body><p align=\"center\"><span style=\" font-size:18pt; font-weight:600; color:#499f7e;\">"+a+"</span></p></body></html>"
    return text

def start():
    pyautogui.alert("The Files you store here will be encrypted and stored safe using 3 file-encryption module and script that uses AES256-CBC to encrypt/decrypt files using passwords and binary streams",'Information')
    try:
        crsr.execute('SELECT filename FROM files WHERE username =?;',(username,))
        ans=crsr.fetchall()
        connection.commit()
        ui.filelist.setText(textedit(ans))
        ui.dropfile.clear()
        for i in ans:
            ui.dropfile.addItem(i[0])
    except:
        pass
        
def addfile():
    bufferSize = 64 * 1024
    try:
        os.mkdir('files')
    except:
        pass
    original=easygui.fileopenbox()
    if(original!=None):
        password = easygui.enterbox("Enter Password For File Encryption")
        dirlist=original.split('\\')
        filename=str(dirlist[len(dirlist)-1])
        target='files'+'\\'+filename
        shutil.copyfile(original, target)
        crypted=target+'.aes'
        pyAesCrypt.encryptFile(target,crypted, password, bufferSize)
        os.remove(target)
        try:
            crsr.execute('INSERT INTO files VALUES (?,?,?);',(username,filename,password))
            connection.commit()
        except:
            pass
##            print(str(sys.exc_info()))
    crsr.execute('SELECT filename FROM files WHERE username =?;',(username,))
    ans=crsr.fetchall()
    connection.commit()
    ui.filelist.setText(textedit(ans))
    ui.dropfile.clear()
    for i in ans:
        ui.dropfile.addItem(i[0])

def viewfile():
    try:
        bufferSize = 64 * 1024
        filename=str(ui.dropfile.currentText())
        password = easygui.enterbox("Enter Password Used During File Encryption")
        crsr.execute('SELECT password FROM files WHERE username =? and filename= ?;',(username,filename))
        ans=crsr.fetchall()
        connection.commit()
        if(password==ans[0][0]):
                cryptname='files'+'\\'+filename+'.aes'
                openname='files'+'\\'+filename
                pyAesCrypt.decryptFile(cryptname,openname, password, bufferSize)
                os.system(openname)
                a=str(pyautogui.confirm('Press OK After viewing the file'))
                if(a=='OK'):
                    os.remove(openname)
        else:
            pyautogui.alert("Wrong Password",'ALERT')
    except:
        pass
def deletefile():
    filename=str(ui.dropfile.currentText())
    password = easygui.enterbox("Enter Password Used During File Encryption")
    crsr.execute('SELECT password FROM files WHERE username =? and filename= ?;',(username,filename))
    ans=crsr.fetchall()
    connection.commit()
    if(password==ans[0][0]):
        cryptname='files'+'\\'+filename+'.aes'
        os.remove(cryptname)
        crsr.execute("DELETE FROM files WHERE filename = ? and username = ?; ",(filename,username))
        connection.commit()
        pyautogui.alert("Removed !",'ALERT')
    else:
            pyautogui.alert("Wrong Password",'ALERT')

if __name__ == "__main__":
    username='asd'   # for test purpose
    file=open('name','r')
    username=str(file.read())
    file.close()
    os.remove('name')
    connection = sqlite3.connect("files.db")
    crsr = connection.cursor()
    sql_command = """CREATE TABLE IF NOT EXISTS files (username varchar(100),filename varchar(100), password varchar(100));"""
    crsr.execute(sql_command)
    connection.commit()
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    start()
    ui.addfile.clicked.connect(addfile)
    ui.viewfile.clicked.connect(viewfile)
    ui.pushButton_2.clicked.connect(deletefile)
    sys.exit(app.exec_())
