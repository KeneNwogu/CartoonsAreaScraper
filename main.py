from scrapers import cartoons_area
from downloader.download import download

print("FInd ANime From SCraper")
dubbed_or_sub = int(input("Choose language: Japanese{0} or English{1}: "))

scraper = cartoons_area.Scraper(dubbed_or_sub)
print(f"link to scrape: {scraper.selected_link}")

letter = input("Enter First Letter Of Anime: ")
print(scraper.find_anime_by_letter(letter))

index = int(input("Choose an index in the list of anime: "))
# print(scraper.get_season_link(index))

# scraper.search_anime_by_name(scraper.selected_link, name.lower())
seasons = scraper.get_season_link(index)
season_index = int(input(f"There are {len(seasons)} seasons: Enter Season To download from: "))

episodes = scraper.get_episodes_from_season(season_index)
episode_range = input(f"There are {len(episodes)} episodes. Enter range (start, end: Example: '1, 2') to download from: ")

scraper.dowload_episodes(episode_range)
media_links = scraper.get_media_links()

for item in media_links:
    download(item[0], scraper.selected_name)

# filename = os.path.join(main_path, scraper.selected_anime, "{} {}.mp4"
#                                     .format(scraper.selected_anime, i))
# downloader.download_mp4(item[0], filename)
# print(scraper)
