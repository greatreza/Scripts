from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
PATH = "directory path to your chromeDriver"
driver = webdriver.Chrome(PATH)


driver.get("link to page with all the links :) ")

links = []
link_count = 0
elems = driver.find_elements_by_xpath("//a[@href]")

for elem in elems:
   
    links.append(elem.get_attribute("href"))
    link_count += 1
    
print("link count is", link_count)#this tells us how many links it gathered


with open('yourFile.txt', 'w') as f:#puts all the links in a .txt file ready for download :)
    for item in links:
        f.write("%s\n" % item)
        


time.sleep(10)#waits 10 sec in case job is'nt already done

driver.quit()#closes chrome window