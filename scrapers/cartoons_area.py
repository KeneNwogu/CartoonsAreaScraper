from bs4 import BeautifulSoup
from urllib.request import urlopen
from urllib.error import URLError
import re

"""
   Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope Process
   py -3 -m venv .venv
  .venv\scripts\activate

"""
# http://cartoonsarea.xyz/Japanese-Dubbed-Videos/A-Subbed-Series/ -example link
# https://eng.cartoonsarea.xyz/English-Dubbed-Series/A-Dubbed-Series/

class Scraper():
    """
    The CartoonsArea Scraper Class.
    english_ and japanese_ represent languages
    english and japanese represent links for languages

    """
    # english_ = "English"
    # japanese_ = "Japanese"
    japanese = "http://cartoonsarea.xyz/Japanese-Dubbed-Videos/"
    english = "http://cartoonsarea.xyz/English-Dubbed-Series/"
    options = [japanese, english]
    def __init__(self, num):
        self.selected_link = self.options[num]
        return None

    def find_anime_by_letter(self, letter):
        """
        img = obj.find_all(src=re.compile("/USER-DATA/Images/"))
        tags = [i.parent for i in img]
        names = [i.parent for i in tags]

        for name in img:
            print(name["src"].split("/"))
            print("")
        """
        letter = letter.upper()
        try:
            if self.selected_link == self.options[1]:
                link = f"https://eng.cartoonsarea.xyz/English-Dubbed-Series/{letter}-Dubbed-Series/"
                handle = urlopen(link)
                self.obj = BeautifulSoup(handle, features="html.parser")
                img = self.obj.find_all(src=re.compile("/USER-DATA/Images/")) #find all child image tags under links
                tags = [i.parent for i in img]
                self.links = [tag['href'] for tag in tags]
                jpg_name = [name["src"].split("/")[5] for name in img]
                names = [name.split('.')[0] for name in jpg_name]
            else:
                link = f"https://eng.cartoonsarea.xyz/Japanese-Dubbed-Series/{letter}-Dubbed-Series/"
                handle = urlopen(link)
                self.obj = BeautifulSoup(handle)
                img = self.obj.find_all(src=re.compile("/USER-DATA/Images/")) #find all child image tags under links
                tags = [i.parent for i in img]
                self.links = [tag['href'] for tag in tags]
                jpg_name = [name["src"].split("/")[5] for name in img]
                names = [name.split('.')[0] for name in jpg_name]
        except URLError as error:
            print("Retrying...")
            self.find_anime_by_letter(letter)
        else:    
            return [name.lower() for name in names]
    

    def search_anime_by_name(self, url, name):
        letter = name[0]
        names = self.find_anime_by_letter(letter)
        print(names)
        if name not in names:
            return f"{name} does not Exist on CartoonsArea.xyz. Try Searching For Another anime / name"
        else:
            # i for index
            i = names.index(name)
            self.anime_link = self.links[i]
            return self.anime_link

    def get_season_link():
        link = self.anime_link
        handle = urlopen(link)
        obj = BeautifulSoup(handle, features="html.parser")
        tags = obj.find_all('a')
                


