from selenium import webdriver
import time
import json
import random
import string
browser = webdriver.Chrome("/Users/neildeo/Downloads/chromedriver")
emails = []
first_name = []
last_name = []
email = ''
names = json.loads(open('list.json').read())
for name in names:
    namePlus = "".join(random.choice(string.digits))
    nameOne = random.choice(names)
    nameTwo = random.choice(names)
    first_name.append(nameOne)
    last_name.append(nameTwo)
    email = nameOne + nameTwo +str(namePlus) + '@hotmail.com'
    email = email.lower()
    print(email)
    emails.append(email)



for i in range(1,2):
    time.sleep(2)
    browser.get('https://www.change.org/p/state-of-california-have-schools-teach-python-from-4th-grade-onwards?recruiter=1039563348&utm_source=share_petition&utm_medium=copylink&utm_campaign=share_petition')
    time.sleep(3)
    inp = browser.find_element_by_xpath('''//*[@id="firstName"]''')

    inp.send_keys(first_name[i])

    time.sleep(2)
    inp2 = browser.find_element_by_xpath('''//*[@id="lastName"]''')

    inp2.send_keys(last_name[i])
    time.sleep(3)
    email = browser.find_element_by_xpath('''//*[@id="email"]''')

    email.send_keys(emails[i])
    time.sleep(3)
    buttClick = browser.find_element_by_xpath('''//*[@id="page"]/div[1]/div[3]/div[2]/div/div/div/div[2]/div[2]/form/button[2]''')

    buttClick.click()

    time.sleep(5)
    skip = browser.find_element_by_link_text('Sorry, I can’t do anything right now')
    skip.click()
    time.sleep(5)
    skip_two = browser.find_element_by_link_text('Skip for now')
    skip_two.click()
    time.sleep(5)
    see_news = browser.find_element_by_link_text('See news on the petition you signed')
    see_news.click()
