#!/usr/bin/python

# author: Zelong Cong
import argparse

import connect_mongo
from support import *

ap = argparse.ArgumentParser()
ap.add_argument("-t", "--tokens", required=True, help="The access tokens")
args = vars(ap.parse_args())


db_client = connect_mongo.db_client()

def FileSave(user_info):

    db_client.insert_new_user(content)

def find_and_insert

if __name__ == "__main__":
    while 1:
        harvest_friends()
