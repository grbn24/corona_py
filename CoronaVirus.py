from selenium import webdriver
class CoronaVirus():
    def __init__(self):
        self.driver = webdriver.Chrome("/usr/lib/chromium-browser/chromedriver")
        self.driver.get('https://www.worldometers.info/coronavirus/')
        table = self.driver.find_element_by_xpath('//*[@id="main_table_countries"]/tbody[1]')
        country_element = table.find_element_by_xpath("//td[contains(text(),'Netherlands')]")
        row = country_element.find_element_by_xpath("./..")
        data = row.text.split(" ")
        total_cases = data[1]
        new_cases = data[2]
        total_deaths = data[3]
        new_deaths = data[4]
        active_cases = data[5]
        total_recoverd = data[6]
        serious_critical = data[7]
        print(total_cases)
        # changed something
        # changed another thing
        