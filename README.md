# Saavn to Spotify Transfer

This project consists of two Python scripts: `Saavn_Scraper.py` and `Spotify_Transfer.py`. The scripts leverage the Selenium library with Python to automate tasks related to scraping song names from the music provider JioSaavn and transferring them to a Spotify playlist.

## Saavn Scraper

`Saavn_Scraper.py` is a Python script that scrapes song names from the music provider JioSaavn. It utilizes Selenium to automate the process of retrieving song names from the website. Please note that this script is dependent on the structure of the JioSaavn website, and any changes to the website's code may affect its functionality.

## Spotify Transfer

`Spotify_Transfer.py` is another Python script included in this project. This script is responsible for adding the songs scraped from JioSaavn to a Spotify playlist. It also utilizes Selenium to interact with the Spotify web interface. Similar to the Saavn Scraper, this script is dependent on the structure of the Spotify website and may require updates if there are changes to the website's code.

## Usage

To use these scripts:

1. Make sure you have Python installed on your system.
2. Install Selenium by running:
   ```
   pip install selenium
   ```

3. Download the appropriate ChromeDriver version for your operating system from the official ChromeDriver website: [ChromeDriver Downloads](https://sites.google.com/a/chromium.org/chromedriver/downloads).
   
4. Ensure the ChromeDriver executable is in your system's PATH or in the same directory as your Python scripts.

5. Run `Saavn_Scraper.py` to scrape song names from JioSaavn.
6. Run `Spotify_Transfer.py` to transfer the scraped songs to a Spotify playlist.

## Disclaimer

These scripts are provided as-is and may not be actively maintained. They are dependent on the structure of the websites they interact with (JioSaavn and Spotify). Any changes to the websites' code may affect the functionality of these scripts.



