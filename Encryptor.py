from os import urandom, getenv
from dotenv import load_dotenv

from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend

from tkinter import *
from tkinter.filedialog import askopenfilename

import smtplib
from email.mime.multipart import MIMEMultipart as MM
from email.mime.text import MIMEText
from email.mime.application import MIMEApplication

load_dotenv()
root = Tk()
root.geometry('600x350')
block_size = 16


class Encryptor:
    def __init__(self, key):
        self.key = key
        self.create_gui()

    def fun(self):
        lab = Label(self.enc_frame, text='')
        lab.place(x=180, y=215)
        if len(self.enc_mail_ent1.get()) > 0:
            Button(self.enc_frame, text='Browse file',
                   command=self.encrypt_file).place(x=240, y=215)
        else:
            print('cam')
            lab.config(text='Enter a proper email address', fg='red')
            lab.after(400, lambda: lab.destroy())

    def encrypt_gui(self):
        self.frame.destroy()

        self.enc_frame = Frame(root)
        self.enc_frame.place(x=0, y=0, width=600, height=350)

        Label(self.enc_frame, text='Python Encrypt file',
              font=('Arial', 30), bg='green', fg='white').place(x=150, y=30)

        Label(self.enc_frame, text='Enter your email: ',
              font=('Arial', 25)).place(x=180, y=100)
        self.enc_mail_ent1 = Entry(self.enc_frame)
        self.enc_mail_ent1.place(x=180, y=140)
        self.btn1 = Button(self.enc_frame, text='Submit',
               command=self.fun)
        self.btn1.place(x=250, y=180)

    def create_gui(self):
        self.frame = Frame(root, width=600, height=350)
        self.frame.place(x=0, y=0)

        Label(self.frame, text='Python Encrypt file',
              font=('Arial', 30), bg='green', fg='white').place(x=160, y=30)

        Button(self.frame, text='Encrypt file',
               command=self.encrypt_gui).place(x=250, y=100)

        mainloop()

    def send(self, file):
        FromAddress = 'cokelele465@gmail.com'
        app_specific_pwd = getenv("APP_SPECIFIC_PWD")
        ToAddress = self.enc_mail_ent1.get()
        msg = MM()
        msg['Subject'] = 'Greetings, you have a task!'
        msg['From'] = FromAddress
        msg['To'] = ToAddress

        body = MIMEText("""Hello, This is a encrypted python file, decrypt it to view it.""")
        msg.attach(body)

        with open(file, 'rb') as f:
            att = MIMEApplication(f.read(), _subtype='enc')

        att.add_header('Content-Disposition', 'attachment',
                       filename=file.split('/')[-1])
        msg.attach(att)
        try:
            with smtplib.SMTP('smtp.gmail.com', 587) as s:
                s.starttls()
                s.login(FromAddress, app_specific_pwd)
                s.sendmail(FromAddress, ToAddress, msg.as_string())
            print("Email sent successfully!")
        except Exception as e:
            print(f"Error sending email: {e}")

    def encrypt(self, message, key):
        # Generate a random nonce (IV) for GCM
        nonce = urandom(12)

        # Create an AES-GCM cipher
        cipher = Cipher(algorithms.AES(key), modes.GCM(nonce),backend=default_backend())
        encryptor = cipher.encryptor()
    
        # Encrypt the image data
        ciphertext = encryptor.update(message) + encryptor.finalize()
    
        # Get the authentication tag
        tag = encryptor.tag

        # Write the encrypted data and authentication tag to a new file
        return nonce + tag + ciphertext

    def encrypt_file(self):
        try:
            file = askopenfilename(parent=root)

            with open(file, 'rb') as fo:
                plaintext = fo.read()
            enc = self.encrypt(plaintext, self.key)
            with open(file.split('/')[-1].split('.')[0]+ "-encrypted.enc", 'wb') as fo:
                fo.write(enc)
            # self.btn1.config(text='Send', command=lambda: self.send(
            #     file.split('/')[-1].split('.')[0]+".enc"))
            print("Encrypted file successfully")
        except Exception as e:
            print('some error occured while encrypting the file')
            print(e)

key = b'sliekoDf(#545*#w'

li = Encryptor(key)