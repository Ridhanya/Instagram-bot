


from selenium import webdriver
from selenium.webdriver.chrome.options import *
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import autoit
import time
from selenium.webdriver.support import ui
from selenium.webdriver.support.ui import WebDriverWait

username = "____gene____"
passwd = "gene@8654"
driverpth = "D:\\chromedriver_win32\\chromedriver.exe"
photopath = "D:\\INSTA\\robo.jpg" #examp "C:\\Users\\alire\\PycharmProjects\\instagrambot2\\logo.png"
phototext = "Hi, Welcome to my instagram. I am a bot and I hope I will be helpful to you in providing knowledge from certain popular sites."

options = Options()
options.add_argument("--log-level=3")
options.add_argument("--silent")
#options.add_argument("--headless")
options.add_argument("--no-sandbox")
options.add_argument("--disable-logging")
options.add_argument("--mute-audio")
mobile_emulation = {"deviceName": "Nexus 5"}
options.add_experimental_option("mobileEmulation", mobile_emulation)
options.add_argument('--user-agent=Mozilla/5.0 (iPhone; CPU iPhone OS 10_3 like Mac OS X) AppleWebKit/602.1.50 (KHTML, like Gecko) CriOS/56.0.2924.75 Mobile/14E5239e Safari/602.1')
driver = webdriver.Chrome(executable_path=driverpth,options=options)
driver.get("https://www.instagram.com/accounts/login/?hl=tr")
time.sleep(3)
username_input = driver.find_element_by_css_selector("input[name='username']").send_keys(username)
time.sleep(0.5)
password_input = driver.find_element_by_css_selector("input[name='password']").send_keys(passwd)


time.sleep(0.5)
driver.find_element_by_xpath("//button[@type='submit']").click()
time.sleep(1.5)
WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//button[contains(.,'Şimdi Değil')]"))).click()
time.sleep(1.5)
WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//button[contains(.,'Cancel')]"))).click()

time.sleep(1)
driver.find_element_by_css_selector("svg[aria-label='New Post']").click()
        
    

autoit.win_active("Open") #open can change by your os language if not open change that
time.sleep(2)
autoit.control_send("Open", "Edit1", photopath)

time.sleep(1.5)
autoit.control_send("Open", "Edit1", "{ENTER}")
time.sleep(2)
#driver.find_element_by_xpath("//*[@id='react-root']/section/div[1]/header/div/div[2]/button").click()
WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//button[contains(.,'Next')]"))).click()
time.sleep(1)

driver.find_element_by_xpath("//*[@id='react-root']/section/div[2]/section/div[1]/textarea").send_keys(phototext)
		#driver.find_element_by_xpath("//*[@id='react-root']/section/div[2]/section[1]/div[1]/textarea").send_keys(phototext)
time.sleep(1)
driver.find_element_by_xpath("//*[@id='react-root']/section/div[1]/header/div/div[2]/button").click()
time.sleep(20)
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//button[contains(.,'Not Now')]"))).click()
time.sleep(5)
time.sleep(20)

driver.close()




        
