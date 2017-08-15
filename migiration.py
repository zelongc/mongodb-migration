from pymongo import MongoClient
import argparse
import datetime

ap = argparse.ArgumentParser()
ap.add_argument("-f", "--fromaddress", required=True)
ap.add_argument("-t", "--toaddress", required=True)
ap.add_argument("-d", "--DB", required=True)
ap.add_argument("-c", "--Collection", required=True)


args = vars(ap.parse_args())

# Parse the arguments
from_address = args["toaddress"]
to_address = args["fromaddress"]
db=args["DB"]
collection=["Collection"]


class db_client(object):
    def __init__(self):
        self.from_client = MongoClient('mongodb://%s:27017/' % from_address)
        self.from_db = self.from_client['%s' % db]
        self.from_collection = self.from_db['%s' % collection]

        self.to_client = MongoClient('mongodb://%s:27017/' % to_address)
        self.to_db = self.to_client["%s" % db]
        self.to_collection = self.to_db["%s" % collection]

    def run(self):
        try:
            data = self.from_collection.find_one_and_delete()
            data2 = self.to_collection.insert_one(data)
        except Exception as e:
            with open('mongodb_log', 'a') as f:  # a -> append to the bottom line
                f.write("[" + datetime.datetime.now().__str__() + "]" + '\n')
                f.write(str(e) + '\n')


if __name__ == "__main__":
    Client = db_client()
    Client.run()