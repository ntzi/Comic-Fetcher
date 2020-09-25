import sys
sys.path.insert(0, '../comic_fetcher')
from src.comic_fetcher import Comic
import unittest
from os import listdir
import time


class ComicTest(unittest.TestCase):
    # Run tests for comic().

    def test_find_comic_id(self):

        comic = Comic()
        comic.find_comic_id()
        comic_id = comic.comic_id
        condition = 2362 >= comic_id > 0
        with self.subTest():
            self.assertTrue(condition, 'Comic id is wrong')

    def test_delete_old_comic(self):
        comic = Comic()
        for i in range(3):
            comic.find_comic_id()
            comic.make_request()
            comic.download_new_comic()
            comic.delete_old_comic()
            time.sleep(5)

        list_of_files = listdir(comic.download_path)

        condition = len(list_of_files) == 2
        with self.subTest():
            self.assertTrue(condition, 'Old comics are not deleted properly')


if __name__ == '__main__':
    unittest.main()
