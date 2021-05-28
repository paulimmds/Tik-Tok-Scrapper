# Tik-Tok-Scrapper

Tik-Tok Crawler/Scrapper with Python + Selenium WebDriver.

Extracts some video data from a target profile on Tik-Tok.
  - Date of Post
  - Time of Post
  - Tik-Tok Profile
  - Link of Post
  - Hashtags used in the post
  - Post Views Count
  - Post Like Count
  - Post Comments Count
  - Post Share Count
 
## Requiriments
 Tik-Tok Bot was developed using Python 3.
 
Before you can run the bot, you will need to install a few Python dependencies.
 - Selenium `pip install Selenium`
 - ChromeDriver `https://sites.google.com/a/chromium.org/chromedriver/downloads`
 
## Run
To change the link of the profile you want to scrape, follow these steps:
  - Access the file `bot.py`
  - Go to the function `open_driver`
  - In `self.driver.get('...')`, inser your link in place of the three dots. (Don´t forget to leave the link in quotes)

Make sure you are in the correct folder and run the following command in the terminal: `python main.py`

The Browser will open, and you will be asked to input a number of Count of Posts. Put the number of how many posts you want to scrape.

**Feel free to contact me and ask questions.**

**Feel free to contribute.**
