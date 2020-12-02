from bs4 import BeautifulSoup
from urllib.request import urlopen
from urllib.error import URLError
import re

"""
   Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope Process
   py -3 -m venv .venv
  .venv/scripts/activate

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
        """
        letter = letter.upper()
        print("finding....")
        try:
            if self.selected_link == self.options[1]:
                link = f"https://eng.cartoonsarea.xyz/English-Dubbed-Series/{letter}-Dubbed-Series/"
                handle = urlopen(link)
                self.obj = BeautifulSoup(handle, features="html.parser")

                tags = self.obj.find_all("a", {"href": re.compile(".+/English-Dubbed-Series/.-Dubbed-Series/")})
                self.links = ["https:" + tag['href'] for tag in tags]
                print("self.links ", self.links)
                names = [tag.contents for tag in tags]
                # print(tags)
                # print(self.links)
                # print(names)
            else:
                link = f"http://cartoonsarea.xyz/Japanese-Dubbed-Videos/{letter}-Subbed-Series/"
                handle = urlopen(link)
                self.obj = BeautifulSoup(handle, features="html.parser")
                tags = self.obj.find_all("a", {"href": re.compile(".+/Japanese-Dubbed-Videos/.-Subbed-Series/")})
                self.links = ["https:" + tag['href'] for tag in tags]
                # print("self.links ", self.links)
                names = [tag.contents for tag in tags]
        except URLError:
            print("Retrying...")
            self.find_anime_by_letter(letter)
        else:
            print("names", [name[0] for name in names])
            self.names = [name[0].lower() for name in names]
            return self.names

    def get_season_link(self, index):
        selected_anime = self.links[index]
        self.selected_anime = selected_anime
        self.selected_name = self.names[index]
        pattern = selected_anime.split(':')[1]
        print("selected anime", selected_anime)
        handle = urlopen(selected_anime)
        obj = BeautifulSoup(handle, features="html.parser")
        tags = obj.find_all("a", {"href": re.compile(pattern)})
        self.season_links = ["https:" + tag['href'] for tag in tags]
        print("Season links", self.season_links)
        return self.season_links

    def get_episodes_from_season(self, index):
        season = self.season_links[index]
        pattern = season.split(':')[1]

        handle = urlopen(season)
        obj = BeautifulSoup(handle, features="html.parser")
        tags = obj.find_all("a", {"href": re.compile(pattern)})
        pages = obj.find_all('a', {"href": re.compile(".+/?page.")})

        if pages:
            index = int(input(f"{len(pages)} pages were found. Select page to get episodes from: "))
            page_ = season + pages[index]['href']
            print('page', page_)
            handle = urlopen(page_)
            obj = BeautifulSoup(handle, features="html.parser")
            tags = obj.find_all("a", {"href": re.compile(pattern)})
            self.episode_links = ["https:" + tag['href'] for tag in tags]
            sp = [link.split("/")[7].replace("%20", " ") for link in self.episode_links]
            # name = [link[0][len(link - 1)].replace("%20", " ") for link in sp]
            print(sp)
            return self.episode_links

        self.episode_links = ["https:" + tag['href'] for tag in tags]
        sp = [link.split("/")[7].replace("%20", " ") for link in self.episode_links]
        print(sp)
        return self.episode_links

    def dowload_episodes(self, string):
        episode_to_download = string.split(",")
        start = int(episode_to_download[0])
        stop = int(episode_to_download[1])
        self.start, self.stop = start, stop
        self.download_links = []

        self.episodes = self.episode_links[start: stop]
        for episode in self.episodes:
            handle = urlopen(episode)
            obj = BeautifulSoup(handle.read(), features="html.parser")
            tags = obj.find_all("a", {"href": re.compile(".+/.+mp4")})
            self.download_links.append(["https:" + tag['href'].replace(" ", "%20") for tag in tags])
        print(self.download_links)
        return self.episodes

    def get_media_links(self):
        self.media_links = []
        for episode in self.download_links:
            handle = urlopen(episode[0])
            obj = BeautifulSoup(handle, features="html.parser")
            tags = obj.find_all("a", {"class": "download-btn"})
            self.media_links.append(["https://cartoonsarea.xyz" + tag['href'].replace(" ", "%20") for tag in tags])
        print("media_links", self.media_links)
        return self.media_links
