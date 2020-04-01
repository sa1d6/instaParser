#!/usr/bin/python3
from selenium import webdriver
import time



end = 10000 #Необходимое число постов
pers=[]
mass = []
hesh_List=[ 'едаялюблютебя', 'едаеда', 'едадляжизни', 'едатопливо', 'пища',
           'пищабогов', 'едадолжнабытьвкусной', 'блюдо', 'блюда', 'блюдодня',
           'кушать', 'кушатьподано', 'кушатьхочется', 'жрать', 'жратва', 'вкусно',
           'вкусняшка', 'вкусняшки', 'вкуснятина', 'вкусности', 'вкусноиполезно',
           'вкуснота', 'вкусный', 'вкуснаяеда', 'вкуснотища', 'этовкусно', 'еда'] #Список тегов по которым будет осуществлятся поиск
hesh=0

print('Введите логин')
login=input(str())
print('Введите пароль')
password=input(str())


browser = webdriver.Chrome('./chromedriver') # путь до драйвера для GOOGLE
browser.get("https://www.instagram.com")

#Авторизация

browser.get("https://www.instagram.com/accounts/login")
time.sleep(2)
browser.find_element_by_xpath("//section/main/div/article/div/div[1]/div/form/div[2]/div/label/input").send_keys(login)
browser.find_element_by_xpath("//section/main/div/article/div/div[1]/div/form/div[3]/div/label/input").send_keys(password)
browser.find_element_by_xpath("//section/main/div/article/div/div[1]/div/form/div[4]/button").click()
time.sleep(2)

#Функция плавной пролистки списка лайков
def Scroll():
    element = browser.find_element_by_xpath("/html/body/div[5]/div/div[2]/div")

    browser.execute_script("arguments[0].scrollTop = arguments[0].scrollHeight%s" % 6, element)
    time.sleep(0.1)
    browser.execute_script("arguments[0].scrollTop = arguments[0].scrollHeight%s" % 5, element)
    time.sleep(0.1)
    browser.execute_script("arguments[0].scrollTop = arguments[0].scrollHeight%s" % 4, element)
    time.sleep(0.1)
    browser.execute_script("arguments[0].scrollTop = arguments[0].scrollHeight%s" % 3, element)
    time.sleep(0.1)
    browser.execute_script("arguments[0].scrollTop = arguments[0].scrollHeight%s" % 2, element)
    time.sleep(0.1)
    browser.execute_script("arguments[0].scrollTop = arguments[0].scrollHeight%s" % 1, element)
    time.sleep(0.1)
    browser.execute_script("arguments[0].scrollTop = arguments[0].scrollHeight", element)
    time.sleep(0.1)





while hesh<=len(hesh_List) and len(mass)<end:
    teg = hesh_List[hesh-1]
    href = ("https://www.instagram.com/explore/tags/%s/?hl=ru"%teg)
    hesh +=1
    post_y = 0

    while len(mass )<end and post_y<3:
        post_x = 0
        post_y += 1
        while post_x < 3:
            browser.get(href)
            time.sleep(3)
            post_x = post_x + 1

            try:

                time.sleep(3)
                link = browser.find_element_by_xpath("//section/main/article/div[1]/div/div/div[1]/div[3]/a")
                link=link.get_attribute('href')
                print(link)
                browser.find_element_by_xpath(
                    "//section/main/article/div[1]/div/div/div[%(y)s]/div[%(x)d]/a/div/div[2]" % {"y": post_y,
                                                                                                  "x": post_x}).click()

                time.sleep(2)
                predel = int(browser.find_element_by_xpath(
                    "/html/body/div[4]/div[2]/div/article/div[2]/section[2]/div/div/button/span").text)

                browser.find_element_by_xpath("/html/body/div[4]/div[2]/div/article/div[2]/section[2]/div/div").click()
                time.sleep(3)
                pers = []
                while len(pers) < predel:
                    Scroll()

                    for i in browser.find_elements_by_xpath("//div/a[@title]"):
                        pers.append(str(i.get_attribute('href')))
                        pers.append(link + '////////////////////////////////////////////////////////////////////////')
                pers = set(pers)
                mass += pers
                print(len(mass))
            except:
                post_x += 1

mass=set(mass)
#вывод в списка в фаил list.txt
with open('/home/said/crypto/Desktop/ап/list.txt', 'w') as file:
    for line in mass:
        file.write(line +'\n')









