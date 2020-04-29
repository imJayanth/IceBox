import sqlite3, easygui, pyautogui, sys
from signup import *
from sendmail import *
import re
regex = '^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,3})+$'
connection = sqlite3.connect("signup.db")
crsr = connection.cursor()
def record():
    name=str(ui.name.text())
    email=str(ui.email.text())
    try:
        if(re.search(regex,email)):
            print("")
        else:
            pyautogui.alert("Email Not Correct Try Again", "Error")
            return 'error'
    except:
        pass
    phno=str(ui.phno.text())
    uname=str(ui.username.text())
    try:
        sql_command="SELECT * FROM userdata where username =  "
        sql_command=sql_command+'\''+uname+'\''
        crsr.execute(sql_command)
        ans= crsr.fetchone()
        if(len(ans)!= None):
            pyautogui.alert("Username Exist Try Another Username", "Error")
            return 'error'
    except:
        pass
    pwd=str(ui.password.text())
    OTP='A'
    myvar=''
    if(email!=''):
            pyautogui.alert("Wait for the OTP Box to appear\n( Press OK )", "ALERT")
            OTP=sendotp(email)
            myvar = easygui.enterbox("Enter Your OTP Sent to Your Email")
            sql_command=str("INSERT INTO userdata VALUES (?,?,?,?,?);")
            if(myvar==OTP):
                crsr.execute(sql_command,(name,email,phno,uname,pwd))
                connection.commit()
                connection.close()
                pyautogui.alert("Registeration done!", "Information")
                sys.exit(app.exec_())
            else:
                pyautogui.alert("WRONG OTP Press SignUp Button Again to Recieve New OTP", "Error")
if __name__ == "__main__":
    sql_command = """CREATE TABLE userdata (name varchar(100),email varchar(100), phno varchar(100), username VARCHAR(20),password VARCHAR(30));"""
    try:
        crsr.execute(sql_command)
    except:
        pass
    app = QtWidgets.QApplication(sys.argv)
    SignupWindow = QtWidgets.QMainWindow()
    ui = Ui_SignupWindow()
    ui.setupUi(SignupWindow)
    SignupWindow.show()
    ui.signup.clicked.connect(record)
    sys.exit(app.exec_())

