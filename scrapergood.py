import csv
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver import Chrome
from webdriver_manager.chrome import ChromeDriverManager

WORD = "#hummus"

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get('https://twitter.com/explore')
driver.implicitly_wait(10)
search_input = driver.find_element_by_xpath('//input[@aria-label="Search query"]')
search_input.send_keys(WORD)
search_input.send_keys(Keys.RETURN)

tweets = driver.find_elements_by_xpath('//article[@data-testid="tweet"]')




tweet = tweets[1]

# content of the tweet
tweet_text = tweet.find_element_by_xpath('.//div/div/div/div[2]/div[2]/div[2]/div[1]/div').text
print(tweet_text)

input()