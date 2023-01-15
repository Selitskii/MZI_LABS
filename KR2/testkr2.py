import unittest

import KR2


class TestStringMethods(unittest.TestCase):
    
    def test_digital_signature(self):
        p = int(input("Enter a prime number (17, 19, 23, etc): "))
        q = int(input("Enter another prime number (Not one you entered above): "))

        print("Generating your public/private keypairs now . . .")
        public_key, private_key = KR2.generate_key_pair(p, q)

        print("Your public key is ", public_key, " and your private key is ", private_key)

        print("Reading text from file and hashing it")
        file_to_enc = open('to_enc', 'r')
        normal_text = file_to_enc.read()
        print("")

        hashed = KR2.hash_function(normal_text)

        print("Encrypting message with private key . . .")
        encrypted_msg = KR2.encrypt(private_key, hashed)
        print("Your encrypted hashed message is: ", ''.join(map(lambda x: str(x), encrypted_msg)), '\n')
        print("")

        print("Decrypting message with public key . . .")
        decrypted_msg = KR2.decrypt(public_key, encrypted_msg)
        print("Your decrypted message is:")
        print(decrypted_msg)
        print("")

        decrypted_file = open('decrypted.txt', 'w')
        decrypted_file.write(decrypted_msg)

        print("Verification process . . .")
        status = KR2.verify(decrypted_msg, normal_text)

        self.assertTrue(status)


if __name__ == '__main__':
    unittest.main()
