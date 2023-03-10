from collections import Counter
from gost import add_zeros_items


class DES:
    def __init__(self):
        self.IP = [
            58, 50, 42, 34, 26, 18, 10, 2, 60, 52, 44, 36, 28, 20, 12, 4,
            62, 54, 46, 38, 30, 22, 14, 6, 64, 56, 48, 40, 32, 24, 16, 8,
            57, 49, 41, 33, 25, 17, 9, 1, 59, 51, 43, 35, 27, 19, 11, 3,
            61, 53, 45, 37, 29, 21, 13, 5, 63, 55, 47, 39, 31, 23, 15, 7
        ]
        self.E = [
            32, 1, 2, 3, 4, 5,
            4, 5, 6, 7, 8, 9,
            8, 9, 10, 11, 12, 13,
            12, 13, 14, 15, 16, 17,
            16, 17, 18, 19, 20, 21,
            20, 21, 22, 23, 24, 25,
            24, 25, 26, 27, 28, 29,
            28, 29, 30, 31, 32, 1
        ]
        self.S = [
            [
                [14, 4, 13, 1, 2, 15, 11, 8, 3, 10, 6, 12, 5, 9, 0, 7,],
                [0, 15, 7, 4, 14, 2, 13, 1, 10, 6, 12, 11, 9, 5, 3, 8,],
                [4, 1, 14, 8, 13, 6, 2, 11, 15, 12, 9, 7, 3, 10, 5, 0,],
                [15, 12, 8, 2, 4, 9, 1, 7, 5, 11, 3, 14, 10, 0, 6, 13],
            ],
            [
                [15, 1, 8, 14, 6, 11, 3, 4, 9, 7, 2, 13, 12, 0, 5, 10,],
                [3, 13, 4, 7, 15, 2, 8, 14, 12, 0, 1, 10, 6, 9, 11, 5,],
                [0, 14, 7, 11, 10, 4, 13, 1, 5, 8, 12, 6, 9, 3, 2, 15,],
                [13, 8, 10, 1, 3, 15, 4, 2, 11, 6, 7, 12, 0, 5, 14, 9],
            ],
            [
                [10, 0, 9, 14, 6, 3, 15, 5, 1, 13, 12, 7, 11, 4, 2, 8,],
                [13, 7, 0, 9, 3, 4, 6, 10, 2, 8, 5, 14, 12, 11, 15, 1,],
                [13, 6, 4, 9, 8, 15, 3, 0, 11, 1, 2, 12, 5, 10, 14, 7,],
                [1, 10, 13, 0, 6, 9, 8, 7, 4, 15, 14, 3, 11, 5, 2, 12],
            ], [
                [7, 13, 14, 3, 0, 6, 9, 10, 1, 2, 8, 5, 11, 12, 4, 15],
                [13, 8, 11, 5, 6, 15, 0, 3, 4, 7, 2, 12, 1, 10, 14, 9],
                [10, 6, 9, 0, 12, 11, 7, 13, 15, 1, 3, 14, 5, 2, 8, 4],
                [3, 15, 0, 6, 10, 1, 13, 8, 9, 4, 5, 11, 12, 7, 2, 14]
            ], [
                [2, 12, 4, 1, 7, 10, 11, 6, 8, 5, 3, 15, 13, 0, 14, 9],
                [14, 11, 2, 12, 4, 7, 13, 1, 5, 0, 15, 10, 3, 9, 8, 6],
                [4, 2, 1, 11, 10, 13, 7, 8, 15, 9, 12, 5, 6, 3, 0, 14],
                [11, 8, 12, 7, 1, 14, 2, 13, 6, 15, 0, 9, 10, 4, 5, 3]
            ], [
                [12, 1, 10, 15, 9, 2, 6, 8, 0, 13, 3, 4, 14, 7, 5, 11],
                [10, 15, 4, 2, 7, 12, 9, 5, 6, 1, 13, 14, 0, 11, 3, 8],
                [9, 14, 15, 5, 2, 8, 12, 3, 7, 0, 4, 10, 1, 13, 11, 6],
                [4, 3, 2, 12, 9, 5, 15, 10, 11, 14, 1, 7, 6, 0, 8, 13]
            ], [
                [4, 11, 2, 14, 15, 0, 8, 13, 3, 12, 9, 7, 5, 10, 6, 1],
                [13, 0, 11, 7, 4, 9, 1, 10, 14, 3, 5, 12, 2, 15, 8, 6],
                [1, 4, 11, 13, 12, 3, 7, 14, 10, 15, 6, 8, 0, 5, 9, 2],
                [6, 11, 13, 8, 1, 4, 10, 7, 9, 5, 0, 15, 14, 2, 3, 12]
            ], [
                [13, 2, 8, 4, 6, 15, 11, 1, 10, 9, 3, 14, 5, 0, 12, 7],
                [1, 15, 13, 8, 10, 3, 7, 4, 12, 5, 6, 11, 0, 14, 9, 2],
                [7, 11, 4, 1, 9, 12, 14, 2, 0, 6, 10, 13, 15, 3, 5, 8],
                [2, 1, 14, 7, 4, 10, 8, 13, 15, 12, 9, 0, 3, 5, 6, 11]
            ]
        ]
        self.P = [
            16, 7, 20, 21, 29, 12, 28, 17,
            1, 15, 23, 26, 5, 18, 31, 10,
            2, 8, 24, 14, 32, 27, 3, 9,
            19, 13, 30, 6, 22, 11, 4, 25
        ]
        self.C = [
            57, 49, 41, 33, 25, 17, 9, 1, 58, 50, 42, 34, 26, 18,
            10, 2, 59, 51, 43, 35, 27, 19, 11, 3, 60, 52, 44, 36,
        ]
        self.D = [
            63, 55, 47, 39, 31, 23, 15, 7, 62, 54, 46, 38, 30, 22,
            14, 6, 61, 53, 45, 37, 29, 21, 13, 5, 28, 20, 12, 4
        ]
        self.shift = [
            1, 1, 2, 2, 2, 2, 2, 2, 1, 2, 2, 2, 2, 2, 2, 1
        ]
        self.KP = [
            14, 17, 11, 24, 1, 5, 3, 28, 15, 6, 21, 10, 23, 19, 12, 4,
            26, 8, 16, 7, 27, 20, 13, 2, 41, 52, 31, 37, 47, 55, 30, 40,
            51, 45, 33, 48, 44, 49, 39, 56, 34, 53, 46, 42, 50, 36, 29, 32
        ]
        self.final_IP = [
            40, 8, 48, 16, 56, 24, 64, 32, 39, 7, 47, 15, 55, 23, 63, 31,
            38, 6, 46, 14, 54, 22, 62, 30, 37, 5, 45, 13, 53, 21, 61, 29,
            36, 4, 44, 12, 52, 20, 60, 28, 35, 3, 43, 11, 51, 19, 59, 27,
            34, 2, 42, 10, 50, 18, 58, 26, 33, 1, 41, 9, 49, 17, 57, 25
        ]

    def encrypt(self, data, key):
        data = [1] + data
        m = ((len(data) // 64) + 1) * 64
        data = add_zeros_items(data, m)
        res = []
        for block in range(0, m, 64):
            res += self.encrypt_64(data[block:block+64], key)
        return res

    def encrypt_64(self, data, key):
        len_block = 64
        key =add_zeros_items(key, 56)
        data_IP = []
        for i in range(len_block):
            data_IP.append(data[self.IP[i] - 1])
        left = data_IP[:len_block//2]
        right = data_IP[len_block//2:]
        for i in range(16):
            k_i = self.generate_k48(key, i)
            left, right = self.feistel_transform(left, right, k_i)
        new_data = left + right
        ans = [new_data[self.final_IP[i] - 1] for i in range(len_block)]
        return ans

    def generate_k48(self, k_56, iteration):
        k_64 = []
        for i in range(8):
            k_64 += k_56[i * 7:i * 7 + 7]
            if Counter(k_56[i * 7:i * 7 + 7])[1] % 2 == 0:
                k_64 += [1]
            else:
                k_64 += [0]
        cd_56 = [0 for i in range(56)]
        for i in range(28):
            cd_56[i] = k_64[self.C[i] - 1]
        j = 0
        for i in range(28, 56):
            cd_56[i] = k_64[self.D[j] - 1]
            j += 1
        k_48 = [0 for i in range(48)]
        for i in range(48):
            k_48[i] = cd_56[self.KP[i] - 1]
        self.C = self.C[self.shift[iteration]:] + self.C[:self.shift[iteration]]
        self.D = self.D[self.shift[iteration]:] + self.D[:self.shift[iteration]]
        return k_48

    def feistel_transform(self, left, right, k):
        L_i = right
        right_48_bit = [right[self.E[i] - 1] for i in range(48)]
        f_right = [right_48_bit[i] ^ k[i] for i in range(48)]
        s_boxes_32 = []
        for i in range(8):
            b_i = f_right[i * 6:i * 6 + 6]
            a = int(str(b_i[0]) + str(b_i[-1]), 2)
            str_b = ''.join([str(i) for i in b_i])
            b = int(str_b[1:-1], 2)
            s = self.S[i]
            b_4 = bin(s[a][b])[2:]
            if len(b_4) < 4:
                b_4 = '0' * (4 - len(b_4)) + b_4
            s_boxes_32 += [int(i) for i in b_4]
        function_r_k = [s_boxes_32[self.P[i] - 1] for i in range(32)]
        R_i = [left[i] ^ function_r_k[i] for i in range(32)]
        return L_i, R_i

    def decrypt(self, data, key):
        n = len(data)
        res = []
        for i in range(0, n, 64):
            res += self.decrypt_64(data[i:i+64], key)
        while res[0] != 1:
            res = res[1:]
        return res[1:]

    def decrypt_64(self, data, key):
        key = add_zeros_items(key, 56)
        len_n = 64
        data_IP = [data[self.IP[i] - 1] for i in range(len_n)]
        l_i = data_IP[:len_n//2]
        r_i = data_IP[len_n//2:]

        keys = []
        for i in range(16):
            k_i = self.generate_k48(key, i)
            keys.append(k_i)
        for i in reversed(range(16)):
            l_i, r_i = self.feistel_transform_dec(l_i, r_i, keys[i])
        data_IP = l_i + r_i
        ans = [data_IP[self.final_IP[i] - 1] for i in range(len_n)]
        return ans

    def feistel_transform_dec(self, left, right, k):
        R_i = left
        right_48_bit = [left[self.E[i] - 1] for i in range(48)]
        f_right = [right_48_bit[i] ^ k[i] for i in range(48)]
        s_boxes_32 = []
        for i in range(8):
            b_i = f_right[i * 6:i * 6 + 6]
            a = int(str(b_i[0]) + str(b_i[-1]), 2)
            str_b = ''.join([str(i) for i in b_i])
            b = int(str_b[1:-1], 2)
            s = self.S[i]
            b_4 = bin(s[a][b])[2:]
            if len(b_4) < 4:
                b_4 = '0' * (4 - len(b_4)) + b_4
            s_boxes_32 += [int(i) for i in b_4]
        function_r_k = [s_boxes_32[self.P[i] - 1] for i in range(32)]
        L_i = [right[i] ^ function_r_k[i] for i in range(32)]
        return L_i, R_i