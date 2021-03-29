import requests as r
from bs4 import BeautifulSoup as bs
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from config import url, headers, username
from auth_data import login, password
from file_loader import Loader
import time
import random
import json
import os

options = webdriver.FirefoxOptions()
# options.add_argument('')

browser = webdriver.Firefox(executable_path='/home/ilya/PycharmProjects/instagram_parser/firefoxdriver/geckodriver',
                            options=options
                            )
file_worker = Loader(username)


def wait(a, b):
    time.sleep(random.randrange(a, b))


# def login_instagram(url):
#     browser.get(url)
#     wait(4, 7)
#     login_input = browser.find_element_by_name('username')
#     login_input.clear()
#     login_input.send_keys(login)
#     wait(3, 6)
#     password_input = browser.find_element_by_name('password')
#     password_input.clear()
#     password_input.send_keys(password)
#     password_input.send_keys(Keys.ENTER)
#     return browser.get(f'{url}/{login}')


def find_all_photos(url):
    browser.get(url)
    wait(4, 7)
    login_input = browser.find_element_by_name('username')
    login_input.clear()
    login_input.send_keys(login)
    print('Успешно ввели логин')
    wait(3, 6)
    password_input = browser.find_element_by_name('password')
    password_input.clear()
    password_input.send_keys(password)
    print('Ввели пароль')
    wait(1, 2)
    password_input.send_keys(Keys.ENTER)
    print('Залогинились')
    wait(3, 5)
    browser.get(f'{url}')
    print('Зашли на страницу')
    wait(4, 8)
    photos = browser.find_elements_by_class_name('FFVAD')
    number_of_photos = len(photos)
    print(f'Создали список из {number_of_photos} фото')
    return photos


def get_all_links(photos):
    links = []
    for photo in photos:
        link = photo.get_attribute('src')
        print(f'Ссылка на фото: {link}', end='\n')
        links.append(link)
    return links


def get_links_from_instagram_page(url, username):
    try:
        photos = find_all_photos(url=f'{url}/{username}')
        wait(1, 3)
        links = get_all_links(photos=photos)
        file_worker.write_to_txt(links)

    except Exception as ex:
        print(ex)
        browser.close()
        browser.quit()
    finally:
        browser.close()
        browser.quit()


def main():
    get_links_from_instagram_page(url=url, username=username)
    file_worker.download_from_txt(f'./links/{username}_links.txt')


if __name__ == '__main__':
    main()
