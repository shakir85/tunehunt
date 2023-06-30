import os


def fetch_files(path):
    for dirpath, something, filenames in os.walk(path):
        # print(dirpath)
        print(something)
        for i in filenames:
            print(i)


fetch_files(path="../testing")
