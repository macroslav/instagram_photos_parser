import requests as r
import os


class Loader():

    def __init__(self, username):
        self.username = username

    def write_to_txt(self, links):
        for link in links:
            with open(f'./links/{self.username}_links.txt', 'a') as file:
                file.write(link + '\n')

    def read_from_txt(self, path):
        links = []
        print('Reading links from txt file...')
        with open(path, 'r') as file:
            links = file.readlines()
        print('Link have already read!')
        return links

    def download_img(self, link):
        img = r.get(link)
        img_id = link.split('/')[-1].split('_')[0]
        if not os.path.exists(f'./{self.username}_photos'):
            os.mkdir(f'./{self.username}_photos')
        else:
            with open(f"./photos/{self.username}_photos/{self.username}_{img_id}_img.jpg", 'wb') as img_file:
                img_file.write(img.content)

    def download_from_txt(self, path):
        try:
            links = self.read_from_txt(path)
            count = 0
            number_of_photos = len(links)
            for link in links:
                count += 1
                self.download_img(link)
                print(f'Photo {count}/{number_of_photos} downloaded!')
            print('Successfully download all images!')
        except Exception as ex:
            print(ex)