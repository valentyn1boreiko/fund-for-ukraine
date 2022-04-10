from os import listdir
from os.path import isfile, join

mypath = 'receipts/'
files = [f for f in listdir(mypath) if isfile(join(mypath, f))]
print(files)

imgs = ""
for file in files:
	imgs+=f"<img src='receipts/{file}'>\n"

f = open("receipts.html", "w")
f.write(imgs)
f.close()

