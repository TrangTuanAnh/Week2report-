
text="Ru rg dviv mlg uli olev, gsv dliow dlfow yv ufoo lu sfig, szgv, wvhgifxgrlm zmw lgsvi yzw gsrmth."

def atbash_cipher(text): # Mã này mã hóa và giải mã dùng chung hàm này 
    result = ''
    for char in text:
        if char.isalpha():
            # Mã hóa hoặc giải mã cắc kí tự là chữ cái
            new_char = chr(90 - (ord(char.upper()) - 65))
            result+=new_char
        else:
            # Giữ nguyên các ký tự không phải chữ cái (số, khoảng trắng, dấu câu)
            result+=char
    return result

if __name__=="__main__":
    print(atbash_cipher(text))