
encrypt = lambda clear, key: "".join([hex(ord(clear[i]) * ord(key[i]))[2:] + '/' for i in range(4)])[:-1]

def encode(clear, key):
	ans = ""
	for i in range(4):
		tmpstr = hex(ord(clear[i]) * ord(key[i]))[2:0] # turn the prod into hex, trim "0x" away
		ans.join(tmpstr + "/") # add '/' and concat the answers
	return ans[:-1] # trim the trailing '/' away

if __name__ == "__main__":
	clear = input()
	key = input()
	public = encrypt(clear, key)
	print(public)