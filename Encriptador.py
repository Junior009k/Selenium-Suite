
from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
from Crypto.Util.Padding import pad, unpad
from Crypto.Hash import SHA256
from base64 import b64encode, b64decode

def derivar_clave(passphrase):
    return SHA256.new(passphrase.encode()).digest()

def desencriptar(iv_b64, cifrada_b64, passphrase):
    clave = derivar_clave(passphrase)
    try:
        iv = b64decode(iv_b64)
        cifrada = b64decode(cifrada_b64)
        cipher = AES.new(clave, AES.MODE_CBC, iv)
        descifrada = unpad(cipher.decrypt(cifrada), AES.block_size)
        return descifrada.decode()
    except Exception as e:
        return f"Error: {str(e)}"
    
