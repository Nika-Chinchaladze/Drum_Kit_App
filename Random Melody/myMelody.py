from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from random import randint
from time import sleep


class DrumKit:
    def __init__(self):
        self.my_service = Service("C:/Zoo_Development/chromedriver.exe")
        self.driver = webdriver.Chrome(service=self.my_service)

    def go_online(self):
        self.driver.get(url="https://nika-chinchaladze.github.io/Drum_Kit_App/")
        sleep(7)

    def beat_drum(self):
        tom1 = self.driver.find_element(By.CLASS_NAME, "w")
        tom2 = self.driver.find_element(By.CLASS_NAME, "a")
        tom3 = self.driver.find_element(By.CLASS_NAME, "s")
        tom4 = self.driver.find_element(By.CLASS_NAME, "d")
        crash = self.driver.find_element(By.CLASS_NAME, "k")
        snare = self.driver.find_element(By.CLASS_NAME, "j")
        kick = self.driver.find_element(By.CLASS_NAME, "l")
        my_melody = [tom1, tom2, tom3, tom4, crash, snare, kick]

        for i in range(100):
            num = randint(0, 6)
            my_melody[num].click()
            sleep(0.5)

        sleep(5)
        self.driver.quit()


a = DrumKit()
a.go_online()
a.beat_drum()
