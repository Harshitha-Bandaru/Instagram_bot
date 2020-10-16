from selenium import webdriver
import time 
tags = ["quoteoftheday", "musings"]
driver = webdriver.Chrome(executable_path="C://Users/Harshitha/Downloads/chromedriver.exe")
driver.get("https://www.instagram.com")
time.sleep(2)
driver.find_element_by_name("username").send_keys("harshi__bandaru")
driver.find_element_by_name("password").send_keys("Pragna@4547")
#driver.find_element_by_xpath("\\button[@type=\"submit\"]").click() # to click on login button, it is of type submit
driver.find_element_by_xpath("//button[contains(.,'Log In')]").click() #another way to click on login 
time.sleep(3)
driver.find_element_by_xpath("//*[contains(@class, 'sqdOP  L3NKy   y3zKF     ')]").click() #to access the save info
time.sleep(3)
driver.find_element_by_xpath("//*[contains(@class, 'aOOlW   HoLwm ')]").click() #to click on not now for turn on notifications
time.sleep(2)
for tag in tags:
    driver.get(f"https://www.instagram.com/explore/tags/{tag}/") #to open a spectific hashtag on insta
    time.sleep(3)
    driver.find_element_by_xpath("//*[contains(@class, 'eLAPa')]").click() #to open the first post
    for i in range(0, 3):
        time.sleep(4)
        #driver.find_element_by_xpath("//*[contains(@class, 'QBdPU ')]").click()
        #driver.find_element_by_xpath("//*[contains(@class, 'wpO6b ')]").click() #to like the posts
        #driver.find_element_by_xpath("//*[contains(@class, '/html/body/div[3]/div[2]/div/article/div[2]/section[1]/span[1]/button/span')]").click()
        driver.find_element_by_css_selector("[aria-label='Like']").click()
        time.sleep(4)
        driver.find_element_by_xpath("//*[contains(@class, ' _65Bje  coreSpriteRightPaginationArrow')]").click() #to open next post
    time.sleep(4)