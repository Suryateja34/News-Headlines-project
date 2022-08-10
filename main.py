from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
import pandas as pd
from datetime import datetime
import os
import sys

application_path = os.path.dirname(sys.executable)
# The above command will run and store the csv file in the same folder as the executable file is located. This is because sometimes the file may or may not be exported to the folder.

now = datetime.now()
month_day_year =now.strftime("%m%d%y") # This strftime is used to convert time into string format
# The format is MMDDYYYY

website = "https://www.thesun.co.uk/sport/football/"
path = "/Users/Lakshmi/Downloads/chromedriver/chromedriver.exe"
#Headless-mode
options = Options()
options.headless = True

service = Service(executable_path=path)
driver = webdriver.Chrome(service = service, options = options)
driver.get(website)

containers = driver.find_elements(by="xpath", value='//div[@class="teaser__copy-container"]')


titles = []
subtitles = []
links = []
for container in containers:
    title = container.find_element(by="xpath", value='./a/h2').text
    subtitle = container.find_element(by="xpath", value='./a/p').text
    link = container.find_element(by="xpath", value='./a').get_attribute("href")
    titles.append(title)
    subtitles.append(subtitle)
    links.append(link)

my_dict = {'titles': titles, 'subtitles': subtitles, 'links': links}
file_name = f'headlines-{month_day_year}.csv'
final_path = os.path.join(application_path,file_name)

df_headline = pd.DataFrame(my_dict)
df_headline.to_csv(final_path)

driver.quit()

# The difference between the find_element and find_elements is that the first method returns a single value and the second value returns a list which makes it the iterable
# xpath for the news headline == //div[@class="teaser__copy-container"]

# Find this xpath using console in the inspect page and extract the all the headlines using the class and the attribute of the wanted thing
#xpath for the title of the news is == //div[@class="teaser__copy-container"]/a/h2 This is to extract the title of the news
#xpath for the subtitle == //div[@class="teaser__copy-container"]/a/p