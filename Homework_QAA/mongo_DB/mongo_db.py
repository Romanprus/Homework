import pymongo


class BaseDB:
    def __init__(self, host: str, port: int, database: str):
        self._host = host
        self._port = port
        self._database = database
        self._client = pymongo.MongoClient(
            f'{self._host}:{self._port}/?directConnection=true&serverSelectionTimeoutMS=2000&appName=mongosh+1.6.1')
        self._db = self._client[self._database]
        self._collection = self._db['test_team']

    def insert_one(self, **kwargs):
        self._collection.insert_one(kwargs)

    def insert_many(self, *dicts):
        self._collection.insert_many(dicts)

    def find_all(self):
        result = self._collection.find()
        return result

    def find_one(self, **kwargs):
        result = self._collection.find_one(kwargs)
        return result

    def delete_one(self, **kwargs):
        self._collection.delete_one(kwargs)

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


Collection().insert_one(Trainee='Bohdan D')
Collection().insert_one(Lead='Roman P', Salary=1000)
Collection().insert_many({'QA':'Leha z rayonu'}, {'PM': 'Baba Halya', 'Salary': '1000'})
cursor = list(Collection().find_all())
print(cursor)
cursor = list(Collection().find_one(Trainee='Bohdan D'))
print(cursor)
Collection().update_one('Vasul P')
cursor = list(Collection().find_all())
print(cursor)
Collection().delete_one(Lead='Roman P')
cursor = list(Collection().find_all())
print(cursor)
Collection().delete_many()
cursor = list(Collection().find_all())
print(cursor)
