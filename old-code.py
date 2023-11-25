# from cryptography.fernet import Fernet
from Crypto import Random
from Crypto.Cipher import AES
from tkinter import *
from tkinter.filedialog import askopenfile, askopenfilename
import smtplib
import mimetypes

from email.mime.multipart import MIMEMultipart as MM
import email
import email.mime.application
from email.mime.text import MIMEText

root = Tk()
root.geometry('600x350')


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

    def decrypt_gui(self):
        try:
            enc_frame.destroy()
        except:
            print("there is no such frame to destroy")
        try:
            frame.destroy()
        except:
            print('there no frame to destroy')
        root.geometry('400x200')
        global dec_frame
        dec_frame = Frame(root, width=400, height=200)
        dec_frame.place(x=0, y=0)
        Label(dec_frame, text='Decrypt file',
              font=('Arial', 30), bg='green', fg='white').place(x=115, y=30)
        Button(dec_frame, text='browse file to decrypt', command=decrypt_file).place(x=115, y=100)

    def create_gui(self):
        self.frame = Frame(root, width=600, height=350)
        self.frame.place(x=0, y=0)

        Label(self.frame, text='Python Encrypt file',
              font=('Arial', 30), bg='green', fg='white').place(x=160, y=30)

        Button(self.frame, text='encrypt file',
               command=self.encrypt_gui).place(x=250, y=100)
        lab1 = Label(self.frame, text='OR')
        lab1.place(x=270, y=150)

        Button(self.frame, text='Decrypt file',
               command=self.decrypt_gui).place(x=250, y=200)

        mainloop()

    def pad(self, s):
        return s + b"\0" * (AES.block_size - len(s) % AES.block_size)

    def send(self, file):
        From = 'vijaysainagavamsi@gmail.com'
        pwd = 'hbczblhainoreuzo'
        msg = MM()
        msg['Subject'] = 'Greetings'
        msg['From'] = From
        msg['To'] = self.enc_mail_ent1.get()

        body = MIMEText("""Hello, These is a encrypted python file, decrypt
        the file.""")
        msg.attach(body)

        with open(file, 'rb') as f:
            att = email.mime.application.MIMEApplication(
                f.read(), _subtype='py')

        att.add_header('Content-Disposition', 'attachment',
                       filename=file.split('/')[-1])
        msg.attach(att)
        s = smtplib.SMTP('smtp.gmail.com', '587')
        s.starttls()
        s.login(From, pwd)
        s.sendmail(From, From, msg.as_string())
        s.quit()

    def encrypt(self, message, key):
        message = self.pad(message)
        iv = Random.new().read(AES.block_size)
        cipher = AES.new(key, AES.MODE_CBC, iv)
        return iv + cipher.encrypt(message)

    def encrypt_file(self):
        try:
            file = askopenfilename(parent=root)

            with open(file, 'rb') as fo:
                plaintext = fo.read()
            enc = self.encrypt(plaintext, self.key)
            with open(file.split('/')[-1].split('.')[0]+"_enc" + ".py", 'wb') as fo:
                fo.write(enc)
            self.btn1.config(text='Send', command=lambda: self.send(
                file.split('/')[-1].split('.')[0]+"_enc" + '.py'))
        except Exception as e:
            print('some error occured while encrypting the file')
            print(e)

    def decrypt(self, ciphertext, key):
        iv = ciphertext[:AES.block_size]
        cipher = AES.new(key, AES.MODE_CBC, iv)
        plaintext = cipher.decrypt(ciphertext[AES.block_size:])
        return plaintext.rstrip(b"\0")

    def decrypt_file(self):
        file = askopenfilename(parent=root)
        with open(file, 'rb') as fo:
            ciphertext = fo.read()
        dec = self.decrypt(ciphertext, self.key)
        with open(file.replace('_enc.py', '')+'_dec.py', 'wb') as fo:
            fo.write(dec)


key = b'sliekoDf(#545*#w'

li = Encryptor(key)