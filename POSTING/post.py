

from instabot import Bot 
from remove import imageremove
import time
bot = Bot() 

bot.login(username = "____gene____", 
		password = "gene@8654")
bot.upload_photo("D:\\INSTA\\space.jpeg", 
		caption = "provide the caption that you want to display on the post here")

time.sleep(60)

imageremove.remove("D:\\INSTA\\space.jpeg.REMOVE_ME") 



