from scrapers import cartoons_area

print("FInd ANime From SCraper")
dubbed_or_sub = int(input("Choose language: Japanese{0} or English{1}: "))

scraper = cartoons_area.Scraper(dubbed_or_sub)
print(f"link to scrape: {scraper.selected_link}")

name = input("Enter Name Of Anime: ")
scraper.search_anime_by_name(scraper.selected_link, name.lower())
print(scraper.get_season_link())



# print(scraper)