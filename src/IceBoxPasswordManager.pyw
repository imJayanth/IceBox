from login import *
from signup import *
from signup import *
from sendmail import *
import pyautogui, easygui
import sqlite3, sys, os
import re
regex = '^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,3})+$'
connection = sqlite3.connect("signup.db")
crsr = connection.cursor()
logincount=0
def importt():
    os.system('signupprogram.pyw')

def forgotpassword():
    email=easygui.enterbox("Enter Your Email ( used during registration )")
    if(re.search(regex,email)):
        print("")
    else:
        pyautogui.alert("Email Not Correct Try Again", "Error")
        return 'error'
    username=easygui.enterbox("Enter Your UserName ( used during registration )")
    crsr.execute("SELECT * FROM userdata where email =  ? and username= ? ",(email,username))
    ans= crsr.fetchall()
    if(len(ans)==0):
        pyautogui.alert("Given Email Does Not Exist in Our Database", "Error")
    else:
        pyautogui.alert("Please Wait for the OTP Box to appear\n ( press OK )", "ALERT")
        OTP=sendotp(email)
        enterotp=easygui.enterbox("Enter The OTP Sent to your Email")
        if(OTP==enterotp):
            pyautogui.alert("Your Credentials will be sent to your Email\nPlease Check Your Email", "ALERT")
            sendpassword(email,str(ans[0][3]),str(ans[0][4]))
        else:
            pyautogui.alert("Wrong OTP Try again", "ERROR")
            return 'error'

            
def checklogin():
    string=str(ui.username.text())+'\n'+str(ui.password.text())+'\n'
    uname=str(ui.username.text())
    pwd=str(ui.password.text())
    crsr.execute("SELECT * FROM userdata where username =  ?",(uname,))
    ans= crsr.fetchall()
    connection.commit()
    print(ans)
    if(len(ans)==0):
        pyautogui.alert("Username Doesn’t Exist Try Again", "Error")
    else:
        if(ans[0][4]!=pwd):
            pyautogui.alert("Wrong Password Try Again", "Error")
        else:
            file=open("name",'w')
            file.write(ans[0][3])
            file.close()
            os.system('passmanagerprogram.pyw')
            connection.close()
            sys.exit(app.exec_())
if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    LoginWindow = QtWidgets.QMainWindow()
    ui = Ui_LoginWindow()
    ui.setupUi(LoginWindow)
    LoginWindow.show()
    pyautogui.alert('Welcome to IceBox Pssword Manager\n-This Project contains\n\to Password Protector\n\to FileSafe(to store confidencial files in encrypted format)\n\to SecretNotes (for storing confidential information)\nThis Project was done as a part of DBMS Package by:-\n\to Deepan.N (18pt43)\n\to Jayanth.S.K(18pt42)','Information')
    ui.loginbutton.clicked.connect(checklogin)
    ui.signupbutton.clicked.connect(importt)
    ui.forgotpass.clicked.connect(forgotpassword)
    sys.exit(app.exec_())
