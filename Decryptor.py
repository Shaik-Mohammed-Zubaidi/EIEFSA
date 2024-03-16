from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend

from tkinter import *
from tkinter.filedialog import askopenfile, askopenfilename

root = Tk()
root.geometry('600x350')


class Decryptor:
    def __init__(self, key):
        self.key = key
        self.create_gui()

    def decrypt_gui(self):
        try:
            self.enc_frame.destroy()
        except Exception as e:
            print("there is no such frame to destroy")
            print(e)
        try:
            self.frame.destroy()
        except:
            print('there is no frame to destroy')
        root.geometry('400x200')
        global dec_frame
        dec_frame = Frame(root, width=400, height=200)
        dec_frame.place(x=0, y=0)
        Label(dec_frame, text='Decrypt file',
              font=('Arial', 30), bg='green', fg='white').place(x=115, y=30)
        Button(dec_frame, text='browse file to decrypt', command=self.decrypt_file).place(x=115, y=100)

    def create_gui(self):
        self.frame = Frame(root, width=600, height=350)
        self.frame.place(x=0, y=0)

        Label(self.frame, text='Decrypt file',
              font=('Arial', 30), bg='green', fg='white').place(x=160, y=30)

        Button(self.frame, text='Decrypt file',
               command=self.decrypt_gui).place(x=250, y=100)

        mainloop()

    def decrypt(self, ciphertext, key, file_name):
        # Extract the nonce, tag, and ciphertext from the encrypted data
        nonce = ciphertext[:12]
        tag = ciphertext[12:28]
        ciphertext = ciphertext[28:]

        # Decrypt the data
        cipher = Cipher(algorithms.AES(key), modes.GCM(nonce, tag), backend=default_backend())
        decryptor = cipher.decryptor()

        # Decrypt the image data
        plain_text = decryptor.update(ciphertext) + decryptor.finalize()

        # Write the decrypted data to a new file
        output_path = f'{file_name}.png'
        with open(output_path, 'wb') as output_file:
            output_file.write(plain_text)

    def decrypt_file(self):
        try:
            file = askopenfilename(parent=root)
            file_name = file.split('/')[-1].split('.')[0]
            with open(file, 'rb') as fo:
                ciphertext = fo.read()
            self.decrypt(ciphertext, self.key, file_name)
            print("Decrypted file successfully")

        except Exception as e:
            print('some error occured while decrypting the file')
            print(e)


key = b'sliekoDf(#545*#w'

li = Decryptor(key)
