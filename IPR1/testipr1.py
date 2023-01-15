import unittest
import  mainipr1

class TestIPR1(unittest.TestCase):

    def test_double_des_1(self):
        data ="Hello! Desk and Gost tasks. Task 1"
        key1 = 'KSIEH4'
        key2 = 'PFEV43'
        enc = mainipr1.get_enc_double_des(data,key1,key2)
        dec = mainipr1.get_dec_double_des(enc,key1,key2)
        self.assertEqual(dec,data)

    def test_double_des_2(self):
        data = "Hello! My friend!!!"
        key1 = 'KSIEH4'
        key2 = 'PFEV'
        enc = mainipr1.get_enc_double_des(data, key1, key2)
        dec = mainipr1.get_dec_double_des(enc, key1, key2)
        self.assertEqual(dec, data)

    def test_triple_des_1(self):
        data = "Hello! My friend!!!"
        key1 = 'KSIEH4'
        key2 = 'PFEV'
        enc = mainipr1.get_enc_triple_des(data, key1, key2)
        dec = mainipr1.get_dec_triple_des(enc, key1, key2)
        self.assertEqual(dec, data)

    def test_triple_des_2(self):
        data = "Hello! Desk and Gost tasks. Task 1"
        key1 = 'KSIEH4'
        key2 = 'PFEV43'
        enc = mainipr1.get_enc_triple_des(data, key1, key2)
        dec = mainipr1.get_dec_triple_des(enc, key1, key2)
        self.assertEqual(dec, data)

    def test_gost_des_1(self):
        data = "Hello! Desk and Gost tasks. Task 1"
        key1 = 'SDSDF45'
        enc = mainipr1.get_enc_gost_des(data, key1)
        dec = mainipr1.get_dec_gost_des(enc, key1)
        self.assertEqual(dec, data)

    def test_gost_des_2(self):
        data = "Hello! My friend!!!"
        key1 = 'SDSDFfsdgsgsfg34'
        enc = mainipr1.get_enc_gost_des(data, key1)
        dec = mainipr1.get_dec_gost_des(enc, key1)
        self.assertEqual(dec, data)

if __name__ == '__main__':
    unittest.main()