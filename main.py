from bot import *

bot = Bot()

bot.open_driver()

count = int(input("Count of Posts: "))

bot.open_first_post()

for i in range(1,count+1):
    bot.get_posts_links()
    bot.next_post()

for link in bot.link_of_post:
    bot.driver.get(link)
    bot.lock_captcha()
    bot.get_data()

sleep(1)

bot.print_five()

bot.import_data()