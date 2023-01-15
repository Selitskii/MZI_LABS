def add_zeros_items(data, k):
    if len(data) <= k:
        zeros_size = k - len(data)
        data2 = [0 for i in range(zeros_size)] + data
        return data2


class GOST:
    def __init__(self):
        self.TABLE_S = [
            [4, 10, 9, 2, 13, 8, 0, 14, 6, 11, 1, 12, 7, 15, 5, 3],
            [14, 11, 4, 12, 6, 13, 15, 10, 2, 3, 8, 1, 0, 7, 5, 9],
            [5, 8, 1, 13, 10, 3, 4, 2, 14, 15, 12, 7, 6, 0, 9, 11],
            [7, 13, 10, 1, 0, 8, 9, 15, 14, 4, 6, 12, 11, 2, 5, 3],
            [6, 12, 7, 1, 5, 15, 13, 8, 4, 10, 9, 14, 0, 3, 11, 2],
            [4, 11, 10, 0, 7, 2, 1, 13, 3, 6, 8, 5, 9, 12, 15, 14],
            [13, 11, 4, 1, 3, 15, 5, 9, 0, 10, 14, 7, 6, 8, 2, 12],
            [1, 15, 13, 0, 5, 7, 10, 4, 9, 2, 3, 14, 6, 11, 8, 12]
        ]

    def encrypt(self, data, key):
        key = add_zeros_items(key, 256)
        data = [1] + data
        m = ((len(data) // 64) + 1) * 64
        data = add_zeros_items(data, m)
        res = []
        keys = [key[i:i + 32] for i in range(0, len(key), 32)]

        for i in range(0, m, 64):
            block_data = data[i:i+64]
            N1 = block_data[:32]
            N2 = block_data[32:]

            block_keys = []
            for i in range(32):
                block_keys.append(keys[i % 8])

            for i in range(32):
                pod_key = block_keys[i]
                N1, N2 = self.transform(N1, N2, pod_key)

            res += N1 + N2
        return res

    def transform(self, l_i_prev, r_i_prev, key):
        r_i = l_i_prev
        l_i = [0 for _ in range(32)]

        l_part = int("".join(str(i) for i in l_i_prev), 2)
        k_part = int("".join(str(i) for i in key), 2)

        l_and_key_mod = (l_part + k_part) % (2 ** 32)
        l = add_zeros_items([int(i) for i in "{0:b}".format(l_and_key_mod)], 32)
        start_s_table = [l[i:i + 4] for i in range(0, 32, 4)]
        res = []
        for i in range(8):
            s_int = int("".join(str(i) for i in start_s_table[i]), 2)
            s_int = self.TABLE_S[i][s_int]
            start_s_table[i] = add_zeros_items([int(i) for i in "{0:b}".format(s_int)], 4)
            res += start_s_table[i]
        funck = res[11:] + res[:11]
        for i in range(32):
            l_i[i] = r_i_prev[i] ^ funck[i]
        return l_i, r_i

    def decrypt(self, data, key):
        result_data = []
        key = add_zeros_items(key, 256)
        keys = [key[i:i + 32] for i in range(0, len(key), 32)]

        for i in range(0, len(data), 64):
            block_data = data[i:i+64]
            N1 = block_data[:32]
            N2 = block_data[32:]

            block_keys = []
            for i in reversed(range(32)):
                block_keys.append(keys[i % 8])

            for i in range(32):
                pod_key = block_keys[i]
                N2, N1 = self.transform(N2, N1, pod_key)
            result_data += N1 + N2

        while result_data[0] != 1:
            result_data = result_data[1:]

        return result_data[1:]