# IceBox Password Manager
IceBox is a software containing
  - PasswordProtector
  - FileSafe (to store confidential files in encrypted format)
  - SecretNotes (to store confidential information)

### How to use
> Install the required packages using  **```pip install -r requirements```**

Open _IceBoxPasswordManager.pyw_ to get to the login screen. 

If you don't have an account, click the signup option, enter your details (name, username, mail ID, phone number and password) and enter the OTP sent via mail to create an account.

Now you can login to your account by entering your username and password. 

If you forgot your password, click _forgot password_ , enter username, mail ID and enter the OTP sent via mail to create a new password.

## PasswordProtector
> Passwords here are stored safely.
**Create Password:** Enter the website for which you are creating the password and it suggests a strong password or else you can use your custom password.
**Edit Password:** Enter the website for which you are editing the password and enter the new password.
**Delete Password:** Enter the website for which you are deleting the password.
**Show Passwords:** Shows all websites with their respective passwords.
**Use Password:** Enter the website for which you have to use the password and place the cursor in the field where you have to use the password and press _ok_ to autofill the password.

## FileSafe
The files you store here will be encrypted and stored safe using 3-file encryption module and script that uses AES256-CBC to encrypt/decrypt files using passwords and binary streams.
**Add file:** Choose the file to be uploaded and enter a password for encryption. The list of available files are shown by default
**View file:** Select the file to be viewed, click _view selected file_ and enter the password to view the file.
**Delete file:** Select the file to be deleted, click _delete selected file_ and enter the password to delete the file.
