import hashlib

str1 = "EVA{W31c0mE_To_zJuEV4_T3ch@TECHA}"
str2 = "EVA{W31c0mE_To_zJuEV4_T3ch@TECHB}"
str3 = "EVA{W31c0mE_To_zJuEV4_T3ch@00000}"

MD5_tb1 = hashlib.md5()
MD5_tb2 = hashlib.md5()
MD5_tb3 = hashlib.md5()
MD5_tb3.update(str3.encode("utf-8"))
print(MD5_tb3.hexdigest())
MD5_tb2.update(str2.encode("utf-8"))
print(MD5_tb2.hexdigest())
MD5_tb1.update(str1.encode("utf-8"))
print(MD5_tb1.hexdigest())
