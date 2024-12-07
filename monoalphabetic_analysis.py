from collections import Counter

plaintext_letter_frequency_ordered = [
    'E', 'T', 'H', 'A', 'S', 'R', 'I', 'N', 'O', 'D', 'L', 'U', 'Y', 'W', 'B', 'G', 'F', 'M', 'C', 'P', 'V', 'K'
]

def get_letter_frequency(ciphertext):
    letter_counts = Counter(char for char in ciphertext if char.isalpha())
    total_letters = sum(letter_counts.values())
    return {letter: (count / total_letters) * 100 for letter, count in letter_counts.items()}

def map_letters_by_exact_frequency(ciphertext_freq):
    sorted_ciphertext_letters = sorted(ciphertext_freq, key=ciphertext_freq.get, reverse=True)
    return dict(zip(sorted_ciphertext_letters, plaintext_letter_frequency_ordered))

def decrypt_with_mapping(ciphertext, letter_mapping):
    return ''.join(letter_mapping.get(char.upper(), char) for char in ciphertext)

def frequency_analysis_attack(ciphertext):
    ciphertext_freq = get_letter_frequency(ciphertext)
    letter_mapping = map_letters_by_exact_frequency(ciphertext_freq)
    decrypted_text = decrypt_with_mapping(ciphertext, letter_mapping)
    
    print("Decrypted Text:", decrypted_text)
    return decrypted_text


if __name__ == "__main__":

    ciphertext = ("BUEW BNIUJLX RUJNXTUJL GJ HJLIUJ IFRUJNLJ, XSNX XSJUJZV ZJNTXV'L UELJ WIQSX FJOJU HIJ, ZTX NL XSJ UIPJU LSETMH ZV XIWJ HJRJNLJ, SIL XJFHJU SJIU WIQSX ZJNU SIL WJWEUV: ZTX XSET REFXUNRXJH XE XSIFJ EGF ZUIQSX JVJL, BJJH'LX XSV MIQSX'L BMNWJ GIXS LJMB-LTZLXNFXINM BTJM, WNCIFQ N BNWIFJ GSJUJ NZTFHNFRJ MIJL, XSV LJMB XSV BEJ, XE XSV LGJJX LJMB XEE RUTJM: XSET XSNX NUX FEG XSJ GEUMH'L BUJLS EUFNWJFX, NFH EFMV SJUNMH XE XSJ QNTHV LPUIFQ, GIXSIF XSIFJ EGF ZTH ZTUIJLX XSV REFXJFX, NFH XJFHJU RSTUM WNC'LX GNLXJ IF FIQQNUHIFQ: PIXV XSJ GEUMH, EU JMLJ XSIL QMTXXEF ZJ, XE JNX XSJ GEUMH'L HTJ, ZV XSJ QUNOJ NFH XSJJ. GSJF BEUXV GIFXJUL LSNMM ZJLIJQJ XSV ZUEG, NFH HIQ HJJP XUJFRSJL IF XSV ZJNTXV'L BIJMH, XSV VETXS'L PUETH MIOJUV LE QNKJH EF FEG, GIMM ZJ N XNXXJUJH GJJH EB LWNMM GEUXS SJMH: XSJF ZJIFQ NLCJH, GSJUJ NMM XSV ZJNTXV MIJL, GSJUJ NMM XSJ XUJNLTUJ EB XSV MTLXV HNVL; XE LNV GIXSIF XSIFJ EGF HJJP LTFCJF JVJL, GJUJ NF NMM-JNXIFQ LSNWJ, NFH XSUIBXMJLL PUNILJ.")
    best_decryption = frequency_analysis_attack(ciphertext)