from selenium import webdriver
import time 
tags = ["quoteoftheday"]
driver = webdriver.Chrome(executable_path="/path/to/chromedriver")
driver.get("https://www.instagram.com")
time.sleep(2)
driver.find_element_by_name("username").send_keys("harshi__bandaru")
driver.find_element_by_name("password").send_keys("Harshi@123")
driver.find_element_by_xpath("\\button[@type=\"submit\"]").click()
time.sleep(3)
driver.find_element_by_xpath("//*[contains(@class, '')]").click() # to access the save info
time.sleep(3)
driver.find_element_by_xpath("//*[contains(@class, '')]").click() # to click on not now for turn on notifications
time.sleep(2)
for tag in tags:
    driver.get(f"https://www.instagram.com/explore/tags/{tag}/") # to open a spectific hashtag on insta
    time.sleep(3)
    driver.find_element_by_xpath("//*[contains(@class, '')]").click() # to open the first post
    for i in range(0, 3):
        time.sleep(4)
        driver.find_element_by_xpath("//*[contains(@class, '')]").click() # to like the posts
        time.sleep(4)
        driver.find_element_by_xpath("//*[contains(@class, '')]").click() #  to open next post
    time.sleep(4)