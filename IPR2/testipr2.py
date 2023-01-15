import unittest

import rsa



class TestStringMethods(unittest.TestCase):

    def test_rsa_1(self):
        public_key, private_key = rsa.generate_rsa_key_pair(13, 17)


        normal_text ="qwerty! des3"

        encrypted_text = rsa.rsa_encrypt(public_key, normal_text)

       # print(''.join(map(lambda x: str(x), encrypted_text)))

        decrypted_text = rsa.rsa_decrypt(private_key, encrypted_text)


        self.assertEqual(normal_text, decrypted_text)

    def test_rsa_2(self):
        public_key, private_key = rsa.generate_rsa_key_pair(13, 17)

        normal_text = "Hello my Friend!!!"

        encrypted_text = rsa.rsa_encrypt(public_key, normal_text)

        #print(''.join(map(lambda x: str(x), encrypted_text)))

        decrypted_text = rsa.rsa_decrypt(private_key, encrypted_text)

        self.assertEqual(normal_text, decrypted_text)


if __name__ == '__main__':
    unittest.main()