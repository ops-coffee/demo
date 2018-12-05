import binascii
from Cryptodome.PublicKey import RSA
from Cryptodome.Cipher import PKCS1_v1_5


class RsaCrypto():
    '''RSA 加解密'''

    def __init__(self):
        self.private_key = '''-----BEGIN PRIVATE KEY-----
        MIIEvAIBADANBgkqhkiG9w0BAQEFAASCBKYwggSiAgEAAoIBAQCf3UyOFvAxeYwj
        gtgImSj+2HViCX5M2X6+jgukEiIzOkc39/2lxNTICby1609l5LYLQdXpmvRqcaRT
        tRmB2FeC7z1eGvMwrJbipXSvgo+mzqGMkBjzybY9VV9UNAtr4NzuRBFch8DONI+Q
        A3FYGUs1vQDT8AANGGC83FYu5PGeAlwk85pGMZPNWmEMrp/4WbmbDir2kALaOOR+
        1tjP9TWXQEHfQUWeZAqWdmaRgBL9CxpCDdHSgBNcxEs+Er2ldhkyfKVyzrtBUftg
        U+/TTp/D+ep+48I4WJCG87qYLxJZW9afSBDSATsm/P0hF0j71tW7+HSGYFRXX4Tp
        CFa8JmMxAgMBAAECggEAIwZSq/zVkhldvTgBCd04kKEvEpQe4kpyjOBFJ6S7bnrR
        uK7yGRwHPG55tGfCJQJXah759Wz4KMwOIzLVzE9wWOT+jnwcFOlzQ2PZrUxPGc5C
        sa+ub9cdQNHQCXw/llqVPPSX0yyA7wyv+W7vqcwc4MCwij6WXEgfhbFGho6tax8j
        VMA1npL0/4sB/u6TIM6HM4TM0yGQj6Seb3Tm0ZJNubPcoH73mDKNdcsCJVToY4NP
        xXX2NbdttOJZ/XHv1v5gfygSKedJN5IScU5A+2ucpPQ9vabVpGzWBNvyKyw1o4jE
        +lrLrpJs+9d0eJMnsC5Kv8pouH9jHGK3/Ro4ioXqWQKBgQC7OD9yLNVfjzuCNF+m
        DoyGu/A/DHhlujn//1omfJcSp+TI2yZlB1W7S7z8YB/gCCTOLmAMTMDbaGBXQk+O
        RXGKFSYFefGAr2qGDG4qwvdfTfv3dZJsd4ey9IprP2MTvvfNkz8lFDU5F3oGut/u
        5/6agoNZoJWJNT/iUmw6GwQiLQKBgQDamFOWWXs8BCPaYTw1wAQhVfK9+pPIElyw
        vRSxtgXwcVSRJDRoNGL+1Oac4k+4kd0sKGaqdGD+Ki4TWTutqQY8MxInu5PMGBcU
        a2STFekn1CijR5EfWg7Speh+Z6IE5r7rVR7gd4Dm1vDUQYM8q9auc+zj3FT1aQh+
        vvimysrblQKBgBoMI1ehQTaAWQkufDhAQfDk6PH8rCuLE1K4ljRQlTw1O7FuPBNG
        R/k8+lgqj4S93VEKRravXw2noe/B/AuRQdCyTI3qf10mCq4HwLQWWBBcazfslaid
        oLWXLELrmL9AjH1/hQOFojoFOCcDjPBSOqwIiHnJy8RBMlgsm34iEBspAoGAYFWV
        MMNKjg59BnanpEB1EYPhMFxH2HpPIwyRHChNwcMQM86y0eGUZx3IbAdIfty5jgZY
        CHK1dA1+tMQ0irncp5cSPzRpVB6hvTv+3NthH05egma9zAVSVv8K0Po26tYN+YRP
        0TiZNCIxjDk67vgD6mnoUhr9zhF1zvW2ezsP32kCgYAlvAItpOUNgVpncGXVCI+4
        nGWGex/h1PEFbWxBiXznG+tgcTLx7Q4E/eYFVpFG72vjc3611+SAZ/TQRiKRcJIQ
        fXa5BhVYMa+Mt7MaBY3bl1KGffOXSfbNLa4BP2NLfC1HEVgxJuCrcArtsEAmzola
        xTMEjsJTgkX9X1Gw/r4/5g==
        -----END PRIVATE KEY-----'''

        self.public_key = '''-----BEGIN PUBLIC KEY-----
        MIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEAn91MjhbwMXmMI4LYCJko
        /th1Ygl+TNl+vo4LpBIiMzpHN/f9pcTUyAm8tetPZeS2C0HV6Zr0anGkU7UZgdhX
        gu89XhrzMKyW4qV0r4KPps6hjJAY88m2PVVfVDQLa+Dc7kQRXIfAzjSPkANxWBlL
        Nb0A0/AADRhgvNxWLuTxngJcJPOaRjGTzVphDK6f+Fm5mw4q9pAC2jjkftbYz/U1
        l0BB30FFnmQKlnZmkYAS/QsaQg3R0oATXMRLPhK9pXYZMnylcs67QVH7YFPv006f
        w/nqfuPCOFiQhvO6mC8SWVvWn0gQ0gE7Jvz9IRdI+9bVu/h0hmBUV1+E6QhWvCZj
        MQIDAQAB
        -----END PUBLIC KEY-----'''

    def encrypt(self, plaintext):
        '''加密方法'''
        try:
            recipient_key = RSA.import_key(self.public_key)
            cipher_rsa = PKCS1_v1_5.new(recipient_key)

            en_data = cipher_rsa.encrypt(plaintext.encode('utf-8'))
            hex_data = binascii.hexlify(en_data).decode('utf-8')

            return {'state': 1, 'message': hex_data}
        except Exception as err:
            return {'state': 0, 'message': str(err)}

    def decrypt(self, hex_data):
        '''解密方法'''
        try:
            private_key = RSA.import_key(self.private_key)
            cipher_rsa = PKCS1_v1_5.new(private_key)

            en_data = binascii.unhexlify(hex_data.encode('utf-8'))
            data = cipher_rsa.decrypt(en_data, None).decode('utf-8')

            return {'state': 1, 'message': data}
        except Exception as err:
            return {'state': 0, 'message': str(err)}


if __name__ == '__main__':
    print(RsaCrypto().encrypt())
