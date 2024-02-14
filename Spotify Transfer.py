from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import json

#Program takes in a list of song names with their artists and adds them to a playlist on spotify

#find the webdriver file
driver = webdriver.Chrome("D:\\Applications\\chromedriver-win64\\chromedriver.exe")
driver.implicitly_wait(150)
driver.get('https://open.spotify.com/search/')


#Clicks on the login button, enters username and password
Login_button = driver.find_element(By.XPATH, '//*[@id="main"]/div/div[2]/div[1]/header/div[5]/button[2]')
Login_button.click() 


email = driver.find_element(By.XPATH,'//*[@id="login-username"]')
email.send_keys('email')


pwd = driver.find_element(By.XPATH,'//*[@id="login-password"]') 
pwd.send_keys('password')


Login_button = driver.find_element(By.XPATH, '//*[@id="login-button"]/span[1]')
Login_button.click()


with open('D:\VsCode\Python\Projects\extracted_songs.json', 'r') as file1:

    list1 = json.load(file1)

for i in range(19,250):
    try:
        search = driver.find_element(By.XPATH, '/html/body/div[4]/div/div[2]/div[2]/nav/div[1]/ul/li[2]/a')
        search.click()
        
        search_bar = driver.find_element(by=By.XPATH, value = '//*[@id="main"]/div/div[2]/div[1]/header/div[3]/div/div/form/input')
        search_bar.send_keys(list1[i])
        search_bar.send_keys(Keys.ENTER)

        song = driver.find_element(By.XPATH, '//*[@id="searchPage"]/div/div/section[2]/div[2]/div/div/div/div[2]/div[1]/div/div[1]/div[2]/a/div')
        song.click()
        
        options = driver.find_element(By.CSS_SELECTOR,'#main > div > div.ZQftYELq0aOsg6tPbVbV > div.jEMA2gVoLgPQqAFrPhFw > div.main-view-container > div.os-host.os-host-foreign.os-theme-spotify.os-host-resize-disabled.os-host-scrollbar-horizontal-hidden.main-view-container__scroll-node.os-host-transition.os-host-overflow.os-host-overflow-y > div.os-padding > div > div > div.main-view-container__scroll-node-child > main > section > div.os-host.os-host-foreign.os-theme-spotify.os-host-resize-disabled.os-host-scrollbar-horizontal-hidden.os-host-scrollbar-vertical-hidden.os-host-transition > div.os-padding > div > div > div > div > button:nth-child(3) > span > svg')
        options.click()

        add_to_playlist = driver.find_element(By.CSS_SELECTOR,'#context-menu > ul > li:nth-child(1) > button')                         
        add_to_playlist.click()

        playlist_david = driver.find_element(By.XPATH, '/html/body/div[17]/div/ul/li[1]/div/ul/div/li[3]/button')

        
        playlist_david.click()
        print("added song number ", i+1)
    except:
        dont_add = driver.find_element(By.XPATH,'/html/body/div[9]/div/div/div/div/button[2]/span')
        dont_add.click()
        print("exception cleared")



time.sleep(20)
driver.close()



