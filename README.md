# EIEFSA

This Python project is designed for Applied Cryptography as part of the Masters of Science in Computer Science program.

## Steps to Run the Project

1. **Open a Terminal**: 

2. **Create a Virtual Environment**: 
    ```bash
    python -m venv myenv
    ```

3. **Activate the Virtual Environment**:

    - **On Windows**:
        ```bash
        myenv\Scripts\activate
        ```

    - **On macOS and Linux**:
        ```bash
        source myenv/bin/activate
        ```

4. **Install Required Packages**:
    ```bash
    pip install -r requirements.txt
    ```

## Encryption Process

1. **To Encrypt a File**:
    - Run the encryptor file:
        ```bash
        python Encryptor.py
        ```
    - A window will appear, click on "Encrypt File" button, enter your email, click submit, browse and select an image file (for convenience, an image named `Sunflower.jpeg` is provided in the current directory). Once selected, the image will be encrypted and stored in the same folder as the code with the name `Sunflower-encrypted.enc`. Close the window afterwards.

2. **To Decrypt a File**:
    - Run the decryptor file:
        ```bash
        python Decryptor.py
        ```
    - A window will appear, click on "Decrypt File" button, browse and select the encrypted file `Sunflower-encrypted.enc`. Once selected, the image will be decrypted and stored in the same folder as the code with the name `Sunflower-decrypted.jpeg`. Close the window afterwards.

    - You can attempt to open the file `Sunflower-decrypted.jpeg` to view the decrypted image in its original form.

## Deactivation

To deactivate the virtual environment, simply run:
```bash
deactivate
``` 

Ensure to perform this step after you have completed your work with the project.