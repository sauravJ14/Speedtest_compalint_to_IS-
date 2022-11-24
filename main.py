from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time

DOWN=150
UP=10

driver_ser=Service(executable_path="D:\py prac\chromedriver.exe")

Twitter_ID="NILL"
Twitter_pass="NILL"

class InternetSpeedTwitterBot:
    def __init__(self):
        self.driver=webdriver.Chrome(service=driver_ser)
        self.up=0
        self.down=0

    def get_internet_speed(self):
        self.driver.get("https://www.speedtest.net/")
        go = self.driver.find_element(By.CLASS_NAME,"start-text")
        go.click()

        time.sleep(60)
        self.down=self.driver.find_element(By.XPATH,'//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div[1]/div/div[2]/span').text
        self.up=self.driver.find_element(By.XPATH,'//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div[2]/div/div[2]/span').text
        print(self.up)
    def tweet_at_provider(self):
        pass

bot=InternetSpeedTwitterBot()
bot.get_internet_speed()

pass