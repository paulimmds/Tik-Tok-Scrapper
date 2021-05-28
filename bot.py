import csv, json
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import ElementClickInterceptedException, NoSuchElementException, TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.proxy import Proxy, ProxyType
from random_user_agent.user_agent import UserAgent
from random_user_agent.params import SoftwareName, OperatingSystem
from time import sleep
from datetime import datetime

class Bot():
    def __init__(self) :
        #Configurando Opções do Chrome
        options = Options()

        #Rotate UA
        software_names = [SoftwareName.CHROME.value]
        operating_systems = [OperatingSystem.WINDOWS.value, OperatingSystem.LINUX.value]
        user_agent_rotator = UserAgent(software_names=software_names, operating_systems=operating_systems, limit=100)

        options.add_argument(f'user-agent={user_agent_rotator.get_random_user_agent()}')

        #Rotate Proxy
        #proxy = ''
        #options.add_argument(f'--proxy-server={proxy}')

        #Automated Browser setting off:
        options.add_experimental_option("useAutomationExtension", False)
        options.add_experimental_option("excludeSwitches", ["enable-automation"])

        #Headless Browser:
        #options.headless = True
        #options.add_argument("--no-sandbox")
        #options.add_argument("--window-size=1920x1080")
        #options.add_argument("--disable-gpu")
        #options.add_argument('--ignore-certificate-errors')
        #options.add_argument('--allow-running-insecure-content')
        #options.add_argument("--disable-extensions")
        #options.add_argument("--start-maximized")
        #options.add_argument('--disable-dev-shm-usage')
        #options.add_argument('--remote-debuggin-port=9222')

        self.driver = webdriver.Chrome(executable_path=r'./chromedriver.exe', options=options)

        self.date_of_post = []
        self.time_of_post = []
        self.tiktok_profile = []
        self.tiktok_headline = []
        self.link_of_post = []
        self.hashtags = []
        self.views = []
        self.likes = []
        self.comments = []
        self.shares = []

    def open_driver(self):
        self.driver.get('https://www.tiktok.com/@theamazonbadger')
        sleep(2)
        self.lock_captcha()
    
    def get_posts_links(self): 
        #Link of Post scrape
        link_of_post = WebDriverWait(self.driver,10).until(EC.presence_of_element_located((By.XPATH,"//div[@class='jsx-2529870817 link-container']"))).text
        link_of_post = link_of_post.split('&')
        link_of_post = link_of_post[0] + link_of_post[1]
        self.link_of_post.append(link_of_post)
        
    def get_data(self):
        dic = WebDriverWait(self.driver,10).until(EC.presence_of_element_located((By.ID,"__NEXT_DATA__"))).get_attribute('innerHTML')
        dic = json.loads(dic)
        try:
            dic2 = dic['props']['pageProps']['items'][0]

            #DateTime and Time of Post scrap
            createtime = dic2['createTime']
            self.convert_datetime(createtime)

            #Username scrape
            self.tiktok_profile.append(dic2['author']['uniqueId'])

            #Hashtags scrape
            hashtags = []
            for item in dic2['textExtra']:
                hashtags.append(item['hashtagName'])
            
            self.hashtags.append(hashtags)

            #Views Count scrape
            self.views.append(dic2['stats']['playCount'])

            #Likes Count scrape
            self.likes.append(dic2['stats']['diggCount'])

            #Comments Count scrape
            self.comments.append(dic2['stats']['commentCount'])
            
            #Shares Count scrape
            self.shares.append(dic2['stats']['shareCount'])
        
        except:
            #DateTime and Time of Post scrap
            createtime = dic['props']['pageProps']['itemInfo']['itemStruct']['createTime']
            self.convert_datetime(createtime)

            #Username scrape
            self.tiktok_profile.append(dic['props']['pageProps']['itemInfo']['itemStruct']['author']['uniqueId'])

            #Hashtags scrape
            hashtags = []
            for item in dic['props']['pageProps']['itemInfo']['itemStruct']['textExtra']:
                hashtags.append(item['hashtagName'])
            
            self.hashtags.append(hashtags)

            #Views Count scrape
            self.views.append(dic['props']['pageProps']['itemInfo']['itemStruct']['stats']['playCount'])

            #Likes Count scrape
            self.likes.append(dic['props']['pageProps']['itemInfo']['itemStruct']['stats']['diggCount'])

            #Comments Count scrape
            self.comments.append(dic['props']['pageProps']['itemInfo']['itemStruct']['stats']['commentCount'])
            
            #Shares Count scrape
            self.shares.append(dic['props']['pageProps']['itemInfo']['itemStruct']['stats']['shareCount'])

    def convert_datetime(self,unix_code):
        # if you encounter a "year is out of range" error the timestamp
        # may be in milliseconds, try `ts /= 1000` in that case

        unix_code = int(unix_code)

        try:
           self.date_of_post.append(datetime.utcfromtimestamp(unix_code).strftime('%Y-%m-%d'))
           self.time_of_post.append(datetime.utcfromtimestamp(unix_code).strftime('%H:%M:%S'))
        except:
            unix_code /= 1000
            self.date_of_post.append(datetime.utcfromtimestamp(unix_code).strftime('%Y-%m-%d'))
            self.time_of_post.append(datetime.utcfromtimestamp(unix_code).strftime('%H:%M:%S'))
    
    def print_five(self):
        print(self.date_of_post[:5])
        print(self.time_of_post[:5])
        print(self.tiktok_profile[:5])
        print(self.link_of_post[:5])
        print(self.hashtags[:5])
        print(self.views[:5])
        print(self.likes[:5])
        print(self.comments[:5])
        print(self.shares[:5])
    
    def next_post(self):
        button_next = WebDriverWait(self.driver,10).until(EC.element_to_be_clickable((By.XPATH,"//img[@class='jsx-650941325 control-icon arrow-right']"))).click()

    def open_first_post(self):
         #Open the first post to iterate
        first_post = WebDriverWait(self.driver,10).until(EC.element_to_be_clickable((By.XPATH,"//div[@class='jsx-1036923518 card-footer normal no-avatar']"))).click()

    def lock_captcha(self):
        try:
            button_close = WebDriverWait(self.driver,5).until(EC.visibility_of_element_located((By.XPATH,"//a[@id='verify-bar-close']"))).click()
        except:
            pass

    def import_data(self):
        try:
            with open('data.csv','r') as f:
                pass
        except:
            with open('data.csv','a+',encoding='utf-8') as f:
                writer = csv.writer(f, delimiter=';')
                header = ['Date of Post','Time of Post','Profile Username','Link of Post','Hashtags','Views','Likes','Comments','Shares']
                writer.writerow(header)
        
        with open('data.csv','a+', newline='', encoding='utf-8') as f:
            writer = csv.writer(f, delimiter=';')
            for i in range(len(self.date_of_post)):
                writer.writerow([self.date_of_post[i],self.time_of_post[i],self.tiktok_profile[i],self.link_of_post[i],self.hashtags[i],self.views[i],self.likes[i],self.comments[i],self.shares[i]])

