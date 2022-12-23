import pymongo

class BaseDB:
    def __init__(self, host: str, port: int, database: str):
        self._host = host
        self._port = port
        self._database = database
        self._client = pymongo.MongoClient(f'{self._host}:{self._port}/?directConnection=true&serverSelectionTimeoutMS=2000&appName=mongosh+1.6.1')
        self._db = self._client[self._database]
        self._collection = self._db['test_team']

    def insert_one(self, key: str, value: str):
        self._collection.insert_one({key: value})

    def insert_many(self, key1: str, value1: str, key2: str, value2: str, key3: str, value3: str):
        self._collection.insert_many([{key1: value1}, {key2: value2}, {key3: value3}])

    def find_all(self):
        result = self._collection.find()
        return result

    def find_one(self, key: str, value: str):
        result = self._collection.find_one({key: value})
        return result

    def delete_one(self, key: str, value: str):
        self._collection.delete_one({key: value})

    def delete_many(self):
        self._collection.delete_many({})


class Collection(BaseDB):
    def __init__(self):
        super().__init__(host='mongodb://127.0.0.1',
                         port=27017,
                         database='QA')


    def update_one(self, new_value):
        data = {'Trainee': 'Bohdan D'}
        new_data = {'$set': {'Trainee': f'{new_value}'}}
        self._collection.update_one(data, new_data)


Collection().insert_one('Junior QA', 'Vova T')
Collection().insert_one('Middle QA', 'Tatiana Z')
Collection().insert_many('Trainee', 'Bohdan D', 'Lead', 'Roman P', 'Middle +', 'Dmytro D')
cursor = list(Collection().find_all())
print(cursor)
cursor = list(Collection().find_one('Middle +', 'Dmytro D'))
print(cursor)
Collection().update_one('Vasul P')
cursor = list(Collection().find_all())
print(cursor)
Collection().delete_one('Lead', 'Roman P')
cursor = list(Collection().find_all())
print(cursor)
Collection().delete_many()
cursor = list(Collection().find_all())
print(cursor)