from pymongo import MongoClient
import argparse
import datetime

ap = argparse.ArgumentParser()
ap.add_argument("-f", "--fromaddress", required=True)
ap.add_argument("-t", "--toaddress", required=True)
ap.add_argument("-d", "--DB", required=True)
ap.add_argument("-c", "--C", required=True)

args = vars(ap.parse_args())

# Parse the arguments
from_address = args["fromaddress"]
to_address = args["toaddress"]
db = args["DB"]
collection = args["C"]

print(from_address, to_address, db, collection)


class db_client(object):
    def __init__(self):
        self.from_client = MongoClient('mongodb://%s:27017/' % from_address)
        self.from_db = self.from_client[db]
        self.from_collection = self.from_db[collection]

        self.to_client = MongoClient('mongodb://%s:27017/' % to_address)
        self.to_db = self.to_client[db]
        self.to_collection = self.to_db[collection]

    def run(self):
        while self.from_collection.count()!=0:
            print(self.from_collection.count()," Left")
            try:
                data = self.from_collection.find_one_and_delete({"_id":{"$ne":None}})
                data2 = self.to_collection.insert_one(data)
            except Exception as e:
                with open('mongodb_log', 'a') as f:  # a -> append to the bottom line
                    print('duplication!')
                    f.write("[" + datetime.datetime.now().__str__() + "]" + '\n')
                    f.write(str(e) + '\n')



if __name__ == "__main__":
    Client = db_client()
    Client.run()
