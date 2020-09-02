

from instabot import Bot 
from remove import imageremove
import time
bot = Bot() 

bot.login(username = "____spacebot____", 
		password = "gene@8654")
bot.upload_photo("D:\\INSTA\\output.jpg", 
		caption = "Information taken from spacedaily.com , for more info visit the site. copyrights @____spacebot____")

time.sleep(60)

imageremove.remove("D:\\INSTA\\output.jpg.REMOVE_ME") 



