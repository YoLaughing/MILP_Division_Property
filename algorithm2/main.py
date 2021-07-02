# Algorithm 2 presented in paper "Applyint MILP Method to Searching Integral 
# Distinguishers based on Division Property for 6 Lightweight Block Ciphers"
# Regarding to the paper, please refer to https://eprint.iacr.org/2016/857
# For more information, feedback or questions, pleast contact at xiangzejun@iie.ac.cn

# Implemented by Xiang Zejun, State Key Laboratory of Information Security, 
# Institute Of Information Engineering, CAS


from sbox import Sbox

if __name__ == "__main__":
    # PRESENT Sbox
    # cipher = "PRESENT"
    # sbox = [0xc, 0x5, 0x6, 0xb, 0x9, 0x0, 0xa, 0xd, 0x3, 0xe, 0xf, 0x8, 0x4, 0x7, 0x1, 0x2]
    # present = Sbox(sbox)
    # filename = cipher + "_DivisionTrails.txt"
    # present.PrintfDivisionTrails(filename)

    cipher_example = "sbox1"
    sbox1 = [0xc, 0xd, 0xb, 0x9, 0x6, 0x0, 0x5, 0xa, 0x3, 0x2, 0x8, 0x4, 0xf, 0x7, 0xe, 0x1]
    sbox2 = [0xc, 0xb, 0xe, 0xf, 0x1, 0x7, 0xd, 0x9, 0xa, 0x0, 0x2, 0x4, 0x3, 0x8, 0x5, 0x6]
    L = [0x0, 0x2, 0xe, 0xc, 0xf, 0xd, 0x1, 0x3, 0x7, 0x5, 0x9, 0xb, 0x8, 0xa, 0x6, 0x4]
    present = Sbox(sbox1)
    filename = cipher_example + "_DivisionTrails.txt"
    present.PrintfDivisionTrails(filename)
