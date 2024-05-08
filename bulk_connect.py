# -*- coding: utf-8 -*-
"""
Created on Sun Jul 28 18:16:01 2019

@author: SAFI
"""
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

linkedin_username = ''
linkedin_password = ''



driver = webdriver.Chrome('D:/chromedriver.exe')

driver.get('https:www.google.com')
sleep(3)

search_query = driver.find_element_by_name('q')
search_query.send_keys('site:linkedin.com/in/ AND "spring" AND "Tunisie"')
sleep(0.5)

search_query.send_keys(Keys.RETURN)
sleep(3)



last_page_content='afficher les résultats les plus pertinents'
last_page = False 
google_search_pages_list =[]
linkedin_urls=[]

while not last_page:
    
    linkedin_link_in_google_page = driver.find_elements_by_class_name('iUh30')
    linkedin_link_in_google_page = [url.text for url in linkedin_link_in_google_page]
    for linkedin_url in linkedin_link_in_google_page:
       linkedin_url=linkedin_url.replace("tn","www") 
       linkedin_urls.append(linkedin_url)
    next_page=''
    next_page = driver.find_element_by_xpath("//a[@id='pnnext']").get_attribute("href")
    google_search_pages_list.append(next_page)
    driver.get(next_page)
    
    
    sleep(0.3)
    elem = driver.find_element_by_xpath("//*")
    source_code = elem.get_attribute("outerHTML")
    
    #to iterate through all google result pages
    last_page=last_page_content in source_code
    
    # to force it just to parse the first page ( to delete it later and uncomment the previous line )
    #last_page=True
    
    

    
sleep(0.5)





driver = webdriver.Chrome('D:/chromedriver.exe')
driver.get('https://www.linkedin.com/login?trk=guest_homepage-basic_nav-header-signin')

username = driver.find_element_by_id('username')
username.send_keys(linkedin_username)
sleep(0.5)

password = driver.find_element_by_id('password')
password.send_keys(linkedin_password)
sleep(0.5)

sign_in_button = driver.find_element_by_xpath('//*[@type="submit"]')
sign_in_button.click()
sleep(0.5)






for profile in linkedin_urls:
    driver.get(profile)
    possible_buttons = driver.find_elements_by_xpath("//button[@type='button']")
    for item in possible_buttons:
        if not(item.get_attribute('aria-label')) is None and "Connect with" in item.get_attribute('aria-label'):
            print('New connection detected ==> Connect Action!')
            connect_button=item
            try:
                connect_button.click()
                send_now_button = driver.find_element_by_xpath("//button[@class='artdeco-button artdeco-button--3 ml1']")
                send_now_button.click()
            except:
                pass
        else:
            print('Skipped')



