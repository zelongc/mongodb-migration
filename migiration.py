from pymongo import MongoClient
import argparse
import datetime

ap = argparse.ArgumentParser()
ap.add_argument("-f", "--fromaddress", required=True, help="The access tokens")
ap.add_argument("-d", "--toaddress", required=True, help="The access tokens")
ap.add_argument("-fd", "--FromDB", required=True)
ap.add_argument("-fc", "--FromCollection", required=True)
ap.add_argument("-td", "--ToDB", required=True)
ap.add_argument("-fc", "--ToCollection", required=True)

args = vars(ap.parse_args())

# Parse the arguments
from_address = args["toaddress"]
to_address = args["fromaddress"]
from_db = args["FromDB"]
to_db = args["ToDB"]
from_collection = args["FromCollection"]
to_collection = args["ToCollection"]


class db_client(object):
    def __init__(self):
        self.from_client = MongoClient('mongodb://%s:27017/' % from_address)
        self.from_db = self.from_client['%s' % from_db]
        self.from_collection = self.from_db['%s' % from_collection]

        self.to_client = MongoClient('mongodb://%s:27017/' % to_address)
        self.to_db = self.to_client["%s" % to_db]
        self.to_collection = self.to_db["%s" % to_collection]

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
    db_client.run()