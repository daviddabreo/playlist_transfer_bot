from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import json

#Program takes in a list of song names with their artists and adds them to a playlist on spotify

#find the webdriver file
driver = webdriver.Chrome("D:\\Applications\\chromedriver-win64\\chromedriver.exe")
driver.implicitly_wait(150)
driver.get('https://www.jiosaavn.com/s/playlist/0f9be21a3c2551567bfee0725f9217e8/david/ZJwM8EdFBRQGSw2I1RxdhQ__')
time.sleep(50)
print("finding elements")
song_names = driver.find_elements(By.XPATH,'//*[@class="u-color-js-gray"]')
#print("names", song_names)
artist_names = driver.find_elements(By.XPATH,'//*[@class="u-centi u-ellipsis u-color-js-gray u-margin-right@sm u-margin-right-none@lg"]')
#print("artists", artist_names)
song_list = []
artist_list = []

print("found elements")
print("song names" ,len(song_names), "\nartist names", len(artist_names))

for i in range (len(artist_names)):
    song_list.append(song_names[i].text)
    artist_list.append(artist_names[i].text)


print("song list length: ",len(song_list),"\n", song_list)
print("artist list length: ",len(artist_list),"\n", artist_list)

final_list = []
for i in range (len(song_list)):
    final_list.append(song_list[i] + " "+ artist_list[i])

with open('D:\VsCode\Python\Projects\extracted_songs.json', 'w') as file1:

    json.dump(final_list,file1)

print("complete")
time.sleep(400)
driver.close()


