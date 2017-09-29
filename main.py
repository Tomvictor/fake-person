import urllib.request
import json

print("Fake person starting...")
data = ""

with urllib.request.urlopen('https://uinames.com/api/?ext&gender=female&region=England') as f:
	print("checking API...\n")
	# print(f.read(300))
	# saving response as byte
	data =f.read()

# decoding data in utf-8 format
response = data.decode('utf-8')

data = json.loads(response)
print(data)
print("\n")
print(data["name"])
print(data["surname"])
print(data["gender"])
print(data["age"])
print(data["birthday"]["dmy"])
print(data["phone"])
print(data["email"])
print(data["photo"])
print(data["region"])



