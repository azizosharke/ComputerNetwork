# https://docs.python.org/3/library/selectors.html
# https://abdesol.medium.com/udp-protocol-with-a-header-implementation-in-python-b3d8dae9a74b
# https://medium.com/quick-code/aes-implementation-in-python-a82f582f51c2

import hashlib
from Crypto import Random
from Crypto.Cipher import AES
import selectors
import socket



sel = selectors.DefaultSelector()

def accept(socket):
    multi, address = socket.accept()
    print('accepted',  multi, 'from', address)
    multi.setblocking(False)
    sel.register(multi, selectors.EVENT_READ, transfer())

def transfer(multi):
    info = multi.recv(512)
    assert isinstance(info, object)
    if not info:
        return
    print('echoing', repr(info), 'to',multi)
    multi.send(info)

sock = socket.socket()
sock.listen(100)

class AESCipher():
    def __init__(self, key):
        self.block_size = AES.block_size
        self.key = hashlib.sha256(key.encode()).digest()

    def encrypt(self, aes_cipher):
        aes_feedback = Random.new().read(self.block_size)
        cipher = AES.new(self.key, AES.MODE_CFB, aes_feedback)
        return aes_feedback + cipher.encrypt(aes_cipher)

    def decrypt(self, encrypted_text):
        aes_feedback = encrypted_text[:self.block_size]
        aes = AES.new(self.key, AES.MODE_CFB, aes_feedback)
        return aes.decrypt(encrypted_text[self.block_size:])

    def cipher_block(self, plain_text):
        feedback = self.block_size - len(plain_text) % self.block_size
        cipher_block = chr(feedback)
        padding_str = feedback * cipher_block
        new_plain_text = plain_text + padding_str
        return new_plain_text



