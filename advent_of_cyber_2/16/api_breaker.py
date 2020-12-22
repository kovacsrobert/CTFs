import requests


for i in range(1, 99, 2):
	print(f'attempt {i}')
	html = requests.get('http://10.10.210.215:8000/api/' + str(i))
	data = str(html.text)
	print('html' + data)
	if "Error" not in data:
		print("Found key: " + str(i))
		break;
