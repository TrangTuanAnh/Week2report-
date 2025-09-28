from collections import Counter
import string

# Known English letter frequencies (from most frequent to least frequent)
english_frequencies = 'ETAOINSHRDLCUMWFGYPBVKJXQZ'

cipher_text = ("◔◆●□⊟ ◕◇⊟ ◓⊟◍⊟∆◔⊟ ◐⊠ ◕◇⊟ ⊠◆◓◔◕ ●◐✦⊟◍, ◇∆◓◓✪ ◑◐◕◕⊟◓ ∆●⊞ ◕◇⊟ ◑◇◆◍◐◔◐◑◇⊟◓'◔ ◔◕◐●⊟, ◐● 26 ◉★●⊟ 1997, ◕◇⊟ ⊡◐◐○◔ ◇∆✦⊟ ⊠◐★●⊞ ◆◎◎⊟●◔⊟ ◑◐◑★◍∆◓◆◕✪ ∆●⊞ □◐◎◎⊟◓□◆∆◍ ◔★□□⊟◔◔ ✧◐◓◍⊞✧◆⊞⊟. ◕◇⊟✪ ◇∆✦⊟ ∆◕◕◓∆□◕⊟⊞ ∆ ✧◆⊞⊟ ∆⊞★◍◕ ∆★⊞◆⊟●□⊟ ∆◔ ✧⊟◍◍ ∆◔ ✪◐★●◈⊟◓ ◓⊟∆⊞⊟◓◔ ∆●⊞ ∆◓⊟ ✧◆⊞⊟◍✪ □◐●◔◆⊞⊟◓⊟⊞ □◐◓●⊟◓◔◕◐●⊟◔ ◐⊠ ◎◐⊞⊟◓● ◍◆◕⊟◓∆◕★◓⊟,[3][4] ◕◇◐★◈◇ ◕◇⊟ ⊡◐◐○◔ ◇∆✦⊟ ◓⊟□⊟◆✦⊟⊞ ◎◆✩⊟⊞ ◓⊟✦◆⊟✧◔ ⊠◓◐◎ □◓◆◕◆□◔ ∆●⊞ ◍◆◕⊟◓∆◓✪ ◔□◇◐◍∆◓◔. ∆◔ ◐⊠ ⊠⊟⊡◓★∆◓✪ 2023, ◕◇⊟ ⊡◐◐○◔ ◇∆✦⊟ ◔◐◍⊞ ◎◐◓⊟ ◕◇∆● 600 ◎◆◍◍◆◐● □◐◑◆⊟◔ ✧◐◓◍⊞✧◆⊞⊟, ◎∆○◆●◈ ◕◇⊟◎ ◕◇⊟ ⊡⊟◔◕-◔⊟◍◍◆●◈ ⊡◐◐○ ◔⊟◓◆⊟◔ ◆● ◇◆◔◕◐◓✪, ∆✦∆◆◍∆⊡◍⊟ ◆● ⊞◐✫⊟●◔ ◐⊠ ◍∆●◈★∆◈⊟◔. ◕◇⊟ ◍∆◔◕ ⊠◐★◓ ⊡◐◐○◔ ∆◍◍ ◔⊟◕ ◓⊟□◐◓⊞◔ ∆◔ ◕◇⊟ ⊠∆◔◕⊟◔◕-◔⊟◍◍◆●◈ ⊡◐◐○◔ ◆● ◇◆◔◕◐◓✪, ✧◆◕◇ ◕◇⊟ ⊠◆●∆◍ ◆●◔◕∆◍◎⊟●◕ ◔⊟◍◍◆●◈ ◓◐★◈◇◍✪ 2.7 ◎◆◍◍◆◐● □◐◑◆⊟◔ ◆● ◕◇⊟ ★●◆◕⊟⊞ ○◆●◈⊞◐◎ ∆●⊞ 8.3 ◎◆◍◍◆◐● □◐◑◆⊟◔ ◆● ◕◇⊟ ★●◆◕⊟⊞ ◔◕∆◕⊟◔ ✧◆◕◇◆● ◕✧⊟●◕✪-⊠◐★◓ ◇◐★◓◔ ◐⊠ ◆◕◔ ◓⊟◍⊟∆◔⊟. ◆◕ ◇◐◍⊞◔ ◕◇⊟ ◈★◆●●⊟◔◔ ✧◐◓◍⊞ ◓⊟□◐◓⊞ ⊠◐◓ ⊡⊟◔◕-◔⊟◍◍◆●◈ ⊡◐◐○ ◔⊟◓◆⊟◔ ⊠◐◓ □◇◆◍⊞◓⊟●.")

def rules (x):
    return not x.isalnum() and not x.isspace() and x!='[' and x!=']' and x!="'" and x!='.' and x!='-' and x!=','


# Count letter frequencies in the ciphertext (ignoring non-alphabet characters)
cipher_counts = Counter(filter(rules, cipher_text))

# Sort the ciphertext letters by frequency (most frequent first)
sorted_cipher = ''.join([item[0] for item in cipher_counts.most_common()])

# Create an initial mapping from ciphertext letters to the English frequency order
mapping = {}
for i in range(min(len(sorted_cipher), len(english_frequencies))):
    mapping[sorted_cipher[i]] = english_frequencies[i]

print("\nInitial mapping (special characters -> English letters):")
for cipher_char, eng_char in mapping.items():
    print(f"'{cipher_char}' -> '{eng_char}'")

# Optional manual adjustments to improve decryption quality
mapping["◐"] = "O"
mapping["●"] = "N"
mapping["⊠"] = "F"
mapping["◕"] = "T"
mapping["◇"] = "H"
mapping["∆"] = "A"
mapping["◑"] = "P"
mapping["◍"] = "L"
mapping["◓"] = "R"
mapping["◔"] = "S"
mapping["◆"] = "I"
mapping["⊞"] = "D"
mapping["⊡"] = "B"
mapping["○"] = "K"
mapping["◎"] = "M"
mapping["✧"] = "W"
mapping["✫"] = "Z"

def print_key_mapping_table(mapping):
    plain_letters = list(string.ascii_uppercase)
    reverse_map = {v: k for k, v in mapping.items()}
    row1 = " ".join(f"{letter:2}" for letter in plain_letters)
    row2 = " " + "--" + "+--"*(len(plain_letters)-1) + " "
    row3 = " ".join(f"{reverse_map.get(letter,'--'):2}" for letter in plain_letters)
    print("\n" + row3)
    print(row2)
    print(row1)


# Display the final mapping using the desired table format
print_key_mapping_table(mapping)

# Decrypt the ciphertext using the mapping
decrypted_text = []
for char in cipher_text:
    if char in mapping:   # nếu ký tự có trong mapping (ký tự đặc biệt)
        decrypted_text.append(mapping[char])
    else:
        decrypted_text.append(char)  # giữ nguyên (số, dấu cách, dấu câu...)
decrypted_text = ''.join(decrypted_text)

print("\nDecrypted Text:")
print(decrypted_text)
