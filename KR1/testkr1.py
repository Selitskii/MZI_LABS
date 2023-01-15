import unittest

import Kr1



class TestStringMethods(unittest.TestCase):

    def test_kr1_1(self):
        key = "key_MZI_KR1"
        text = "MZI_KR1"
        self.assertEqual(Kr1.hmac(key,text), 'fbf9b2f2a7aefd31690193ca28674677e5cec19cc9591c06b35c6e621948daaf')

    def test_kr1_2(self):
        key = "Belarus"
        text = "I like my work!!"
        self.assertEqual(Kr1.hmac(key,text), '48f0460aa718d3b471090d5ded5132a8a4312eff08c8ca1f8d5a8978abd541f9')




if __name__ == '__main__':
    unittest.main()