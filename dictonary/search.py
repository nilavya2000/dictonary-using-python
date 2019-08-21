import json
import difflib
from difflib import get_close_matches

data=json.load(open("data.json"))

def search(w):
	if w in data:
		return data[w]
	elif len(get_close_matches(w, data.keys()))>0:
		y=input("did you mean %s ? if yes press Y or if no press N : " %get_close_matches(w, data.keys())[0])
		yn=y.lower()
		if yn =="y":
			return data[get_close_matches(w, data.keys())[0]]
		elif yn=="n":
			return "NOT FOUND.!!"
		else:
			return "can't get you"
	else:
		return "word doesn't exist. do check the word."

i=input("enter the word : ")
a=i.lower()
out=search(a)
if type(out)==list:
	for i in out:
		print(i)
else:
	print(out)
