from selenium import webdriver
import pandas as pd
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from webdriver_manager.chrome import ChromeDriverManager


driver = webdriver.Chrome(ChromeDriverManager().install())
#go on YouTube and search for desired query
driver.get("https://www.youtube.com/results?search_query=Math&sp=EgIQAQ%253D%253D")

#appends all youtube links from query to links array
#for more results, scroll down with the browser opened from driver and then run
user_data = driver.find_elements_by_xpath('//*[@id="video-title"]')
links = []
for i in user_data:
    links.append(i.get_attribute("href"))

print(len(links))

df_math = pd.DataFrame(columns = ['link', 'title', 'description', 'category'])

wait = WebDriverWait(driver, 10)
v_category = "math"

for x in links:
    if isinstance(x, str):
        #grabs the link
        driver.get(x)
        #strips the end of url
        v_id = x.strip('https://www.youtube.com/watch?v=')
        #grabs title
        v_title = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR,"h1.title yt-formatted-string"))).text
        #grabs descrption (doesn't seem to work at the moment)
        v_description = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR,"div#description yt-formatted-string"))).text
        #adds it to the dataframe 
        df_math.loc[len(df_math)] = [v_id, v_title, v_description, v_category]


print(df_math.to_string())