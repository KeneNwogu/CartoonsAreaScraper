from bs4 import BeautifulSoup
from urllib.request import urlopen
import re

link = f"https://eng.cartoonsarea.xyz/English-Dubbed-Series/A-Dubbed-Series/"
handle = urlopen(link)
obj = BeautifulSoup(handle)
img = obj.find_all(src=re.compile("/USER-DATA/Images/"))
# div = obj.find_all("class"=re.compile("Singamda"))
tags = [i.parent for i in img]
# names = [i.parent for i in tags]


jpg_name = [name["src"].split("/")[5] for name in img]
names = [name.split('.')[0] for name in jpg_name]
for name in names:
    print(names.index(name))
# names = [f'{splitter[0]}, {img.index(name)}'  for name in img]
# print(names)
# print("")


# for name in tags:
#     print(name)