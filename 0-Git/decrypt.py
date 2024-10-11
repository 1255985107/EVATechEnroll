
decrypt = lambda encrypted, key: "".join([chr(int(encrypted.split('/')[i], 16) // ord(key[i])) for i in range(4)])

def decode(encrypted, key):
	words = encrypted.split('/')
	ans = ""
	for i in range(4):
		num = int(words[i], 16)
		key0x = ord(key[i])
		clear0x = num // key0x
		ans += chr(clear0x)
	return ans

if __name__ == "__main__":
	encrypted = input()
	key = input()
	clear = decrypt(encrypted, key)
	print(clear)