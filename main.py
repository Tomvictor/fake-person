import urllib.request
import json

print("Fake person starting...")
data = ""

def faker():
	
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

		pic_name = "img/" + data["name"] + ".jpg"

		urllib.request.urlretrieve(data["photo"], pic_name)



for item in range(1,100):
	faker()
	print(item)



"""

{
   'title':'mrs',
   'age':31,
   'surname':'Ward',
   'photo':'https://uinames.com/api/photos/female/9.jpg',
   'credit_card':{
      'security':525,
      'number':'7992-3969-6718-4028',
      'expiration':'3/22',
      'pin':2880
   },
   'birthday':{
      'raw':509637629,
      'mdy':'02/24/1986',
      'dmy':'24/02/1986'
   },
   'region':'England',
   'name':'Gracie',
   'password':'Ward86%',
   'email':'gracie_ward@example.com',
   'gender':'female',
   'phone':'(193) 414 1016'
}


"""

