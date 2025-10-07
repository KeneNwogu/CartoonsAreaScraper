## Introduction

This project provides Python scripts to scrape cartoonsarea.xyz, designed to bypass ads and redirects. It allows you to find and potentially download anime content from the website.

## Installation

1.  **Clone the repository:**

    ```bash
    git clone https://github.com/KeneNwogu/CartoonsAreaScraper.git
    cd CartoonsAreaScraper
    ```

2.  **Install the required packages:**

    ```bash
    pip install -r requirements.txt
    ```

## Usage

1.  **Run the main script:**

    ```bash
    python main.py
    ```

2.  **Choose your language preference:** The script will prompt you to select either Japanese (0) or English (1) dubbed anime.

3.  **Enter the first letter of the anime:**  You will be prompted to enter the first letter of the anime you are searching for.

4.  **Select an anime from the list:** The script will display a list of anime matching your search. Enter the corresponding index number to select an anime.

    ```python
    from scrapers import cartoons_area
    from downloader.download import download

    print("FInd ANime From SCraper")
    dubbed_or_sub = int(input("Choose language: Japanese{0} or English{1}: "))

    scraper = cartoons_area.Scraper(dubbed_or_sub)
    print(f"link to scrape: {scraper.selected_link}")

    letter = input("Enter First Letter Of Anime: ")
    print(scraper.find_anime_by_letter(letter))

    index = int(input("Choose an index in the list of anime: "))
## Features

*   Scraping of cartoonsarea.xyz to extract anime information.
*   Language selection (Japanese or English dubbed).
*   Anime search by the first letter.
*   Download functionality (partially implemented in `downloader/download.py`).
*   Avoidance of ads and redirects.

## Contributing

This project is open to contributions.  If you would like to contribute, please follow these steps:

1.  **Fork the repository.**
2.  **Create a new branch** for your feature or bug fix.
3.  **Make your changes** and commit them with clear and concise messages.
4.  **Submit a pull request** to the main repository.