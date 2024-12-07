from collections import Counter

plaintext_letter_frequency_ordered = [
    'E', 'N', 'R', 'I', 'D', 'S', 'T', 'H', 'G', 'A', 'U', 'L', 'C', 'W', 'B', 'M', 'O', 'F', 'Z', 'V', 'K', 'Ü', 'Ö', 'Ä', 'P', 'ß', 'J'
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

    ciphertext = ("MNI QUI OVLÖIOWUI TUOUI TÜIOVLUI TYP CIO MUPHULPCIR, QXHYW QYU PNOU QUP OVLÖILUYW IYUHXAO OWUPEU, QNVL TUII QUP PUYGUPU QCPVL QYU BUYW MUPRULUI ONAA, HÖRU OUYI BXPWUP UPEU OUYI XIQUIJUI WPXRUI: QNVL QC, XI QUYIU UYRUIUI LUAAUI XCRUI RUECIQUI, IÄLPOW QYU GAXHHU QUYIUO AYVLWO HYW UYRUIUH EPUIIOWNGG, HXVLOW UYIU LCIRUPOINW, TN ÜEUPGACOO AYURW, QC OUAEOW QUYI GUYIQ, BC QUYIUH OÜOOUI OUAEOW BC RPXCOXH: QC, QUP QC ICI QUP GPYOVLU OVLHCVJ QUP TUAW EYOW, CIQ UYIBYRUP MUPJÜIQUP QUO FPÄVLWYRUI GPÜLAYIRO, MUPRPÄEOW YI QUYIUP UYRUIUI JINOFU QUYI RAÜVJ, CIQ HXVLOW, RUYBYRUP LCAQYRUP, MUPOVLTUIQCIR QCPVL OFXPOXHJUYW: UPEXPHU QYVL QUP TUAW, NQUP OUY QYUOUP MYUAGPXOO, QUP QXO PUVLW QUP TUAW MUPOVLAYIRW, QCPVL QXO RPXE CIQ QYVL. TUII MYUPBYR TYIWUP QUYIU OWYPI EUAXRUPI TUPQUI, CIQ WYUGU RPÄEUI YI QXO GUAQ QUYIUP OVLÖILUYW RPXEUI, QXO OWNABU RUTXIQ QUYIUP SCRUIQ, SUWBW ON EUTCIQUPW, TYPQ UYI BUPACHFWUP PUOW MNI RUPYIRUH TUPW OUYI: QXII, RUGPXRW, TN XAA QUYIU OVLÖILUYW RUEAYUEUI YOW, TN XAA QUP OVLXWB QUYIUP AUELXGWUI WXRU; BC OXRUI, YI QUYIUI WYUG MUPOCIJUIUI XCRUI, TÄPU UYIU XAAUOMUPBULPUIQU OVLXIQU CIQ CIGPCVLWEXPUP PCLH.")
    best_decryption = frequency_analysis_attack(ciphertext)