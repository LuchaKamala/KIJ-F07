def binaryToString(data):
	r=[]
	result=[]
	for i in range(0, len(data), 8):
		num=data[i:i+8]
		r.append(num)
	for num in r:
		text = chr(int(num, 2))
		result.append(text)
	return ''.join(result)

result=binaryToString('0110100101110010011001100110000101101110')
print result