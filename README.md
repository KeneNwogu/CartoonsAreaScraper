# CartoonsAreaScraper

[![Python](https://img.shields.io/badge/Python-3.7+-blue.svg)](https://www.python.org/)

A collection of Python scripts designed to scrape cartoonsarea.xyz, providing a cleaner browsing experience by avoiding ads and redirects. This project allows users to easily find and download their favorite animated content.

## Introduction

CartoonsAreaScraper provides a set of Python scripts to interact with the cartoonsarea.xyz website. It aims to simplify the process of finding and downloading anime by bypassing intrusive ads and redirects. The project offers a command-line interface for searching and downloading anime.

## Features

*   **Anime Search:** Search for anime by the first letter of its name.
*   **Language Selection:** Choose between Japanese (original) or English dubbed anime.
*   **Download Functionality:** Downloads anime episodes.
*   **Ad and Redirect Avoidance:** Designed to bypass ads and redirects for a smoother user experience.

## Installation

1.  **Clone the repository:**

    ```bash
    git clone <repository_url>
    cd CartoonsAreaScraper
    ```

    (Replace `<repository_url>` with the actual URL of your repository.)

2.  **Install dependencies:**

    ```bash
    pip install -r requirements.txt
    ```

## Usage

1.  **Run the main script:**

    ```bash
    python main.py
    ```

2.  **Follow the prompts:**

    *   Choose the language preference (Japanese or English).
    *   Enter the first letter of the anime you are looking for.
    *   Select the anime from the list by entering its index.
    *   The script will then provide options for downloading the anime.

    Example:

    ```
    FInd Anime From SCraper
    Choose language: Japanese{0} or English{1}: 1
    link to scrape: https://eng.cartoonsarea.xyz/English-Dubbed-Series/A-Dubbed-Series/
    Enter First Letter Of Anime: A
    ['Attack on Titan', 'Assassination Classroom', ...]
    Choose an index in the list of anime: 0
    ```

## Contributing

Contributions are welcome! Please follow these guidelines:

1.  **Fork the repository.**
2.  **Create a new branch** for your feature or bug fix.
3.  **Make your changes** and commit them with clear, concise commit messages.
4.  **Submit a pull request.**

Please ensure your code adheres to the project's coding style (PEP 8).