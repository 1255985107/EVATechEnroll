import hashlib

head_str = "EVA{W31c0mE_To_zJuEV4_T3ch@"
MD5_str = "94686c57e51234928b344924f992d9c9"

charset = "0123456789\
abcdefghijklmnopqrstuvwxyz\
ABCDEFGHIJKLMNOPQRSTUVWXYZ\
!@#$%^&*()_+-=<>?,./:\";\'|" # possible chars for '?'
fillin = ['', '', '', '', '']

def tryfill(pos: int):
	global fillin
	if pos == 5:
		code = head_str + "".join(fillin) + "}"
		# code = "".join(fillin)
		MD5_tb = hashlib.md5()
		MD5_tb.update(code.encode("utf-8"))
		MD5_tmp = MD5_tb.hexdigest()
		if MD5_tmp == MD5_str:
			print(code)
			return True
		else:
			return False
	for ch in charset:
		fillin[pos] = ch
		if tryfill(pos + 1):
			return True
	return False

if __name__ == "__main__":
	if tryfill(pos = 0) != True:
		print("No Answer Found.")