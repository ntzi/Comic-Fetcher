import urllib.request
import requests
import random
import time
import sys
from os import listdir, remove
from os.path import isfile, join, getctime


class Comic:
    # Fetch new comic from https://xkcd.com/ every 1 hour. Save up to 2 comics in total in 'comics' directory.

    def __init__(self):
        self.comic_id = ''
        self.response = ''
        self.download_path = './comics'

    def find_comic_id(self):
        downloaded_comic_ids = []
        downloaded_comics = [f for f in listdir(self.download_path) if isfile(join(self.download_path, f))]
        for name in downloaded_comics:
            comic_id = name.split(' ')[-1]
            comic_id = comic_id.split('.')[0]
            # Skip hidden files (eg: .DS_Store)
            if not comic_id == '':
                downloaded_comic_ids.append(int(comic_id))

        self.comic_id = random.randint(1, 2362)
        while self.comic_id in downloaded_comic_ids:
            self.comic_id = random.randint(1, 2362)

    def make_request(self, test_comic_id=''):
        if not test_comic_id == '':
            self.comic_id = test_comic_id

        request_url = 'https://xkcd.com/{}/info.0.json'.format(self.comic_id)
        try:
            x = requests.get(request_url)
            x.raise_for_status()
            self.response = x.json()
        except requests.exceptions.RequestException as e:  # This is the correct syntax
            raise SystemExit(e)

    def download_new_comic(self):
        comic_url = self.response['img']
        comic_title = self.response['safe_title'] + ' ' + str(self.comic_id)
        save_name = '{}/{}.jpg'.format(self.download_path, comic_title)
        urllib.request.urlretrieve(comic_url, save_name)

    def delete_old_comic(self):
        #  Keep a maximum of 2 comics stored.
        #  Delete the oldest comic.

        list_of_files = listdir(self.download_path)
        full_path = ["{0}/{1}".format(self.download_path, x) for x in list_of_files]

        if len(list_of_files) > 2:
            oldest_file = min(full_path, key=getctime)
            remove(oldest_file)

    def fetch(self):
        while True:
            self.find_comic_id()
            self.make_request()
            self.download_new_comic()
            self.delete_old_comic()
            sys.stdout.write("\rNew comic downloaded!            \n")

            for remaining in range(60, 0, -1):
                sys.stdout.write("\r")
                sys.stdout.write("{:2d} minutes remaining until new comic arrives.".format(remaining))
                sys.stdout.flush()
                time.sleep(60)
