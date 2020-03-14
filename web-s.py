from selenium import webdriver
#from BeautifulSoup4 import BeautifulSoup4 as BeautifulSoup
import pandas as pd

driver = webdriver.Chrome("/usr/lib/chromium-browser/chromedriver")
products = []
prices = []
ratings = []
driver.get("<a href=\"https://www.flipkart.com/laptops/\">https://www.flipkart.com/laptops/</a>~buyback-guarantee-on-laptops-/pr?sid=6bo%2Cb5g&uniq")
