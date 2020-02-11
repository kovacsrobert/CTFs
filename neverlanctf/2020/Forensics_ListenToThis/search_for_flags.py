import requests

# <!-- flag{n3v3rl4nctf_s4ys_t3ll_us_4n0th3r_1_jack} -->

for index in range(60):
	print(" --- " + str(index) + " --- ")
	# https://darknetdiaries.com/episode/1/
	r = requests.get('https://darknetdiaries.com/episode/' + str(index))
	#print(r.status_code)
	startIndex = r.text.find('flag')
	endtIndex = r.text.find('}', startIndex) + len('} -->')
	print(r.text[startIndex:endtIndex])
