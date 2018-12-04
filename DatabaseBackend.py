from pymongo import MongoClient


class DB(object):
    def __init__(self):
        self.client = MongoClient(connection_uri)

    def __del__(self):
        self.close()
        return

    def close(self):
        if self.client is None:
            return
        self.client.close()
        self.client = None
        return

    def _Read(self, db_name, coll_name, cuts = {}, projection = {}, sort=None, limit=0, onlyone=False):
        coll = self.client[db_name][coll_name]
        if onlyone:
            return coll.find_one(cuts, projection, sort=sort)
        else:
            return coll.find(cuts, projection=projection, sort=sort, limit=limit)

    def _Write(self, db_name, coll_name, doc):
        coll = self.client[db_name][coll_name]
        if isinstance(doc, (list, tuple)):
            if not all([isinstance(d, dict) for d in doc]):
                raise ValueError('Documents must be dicts')
            coll.insert_many(doc)
        elif isinstance(doc, dict):
            coll.insert_one(dict)
        else:
            raise ValueError('Don\'t know what to do with document type \'%s\'' % type(doc))
        return

    def _Update(self, db_name, coll_name, cuts = {}, update = {}, onlyone=False):
        coll = self.client[db_name][coll_name]
        if onlyone:
            coll.update_one(filter=cuts, update=update)
        else:
            coll.update_many(filter=cuts, update=update)
        return

    def FindOneAndUpdate(self, db_name, coll_name, cuts={}, update={}):
        return self._Update(db_name, coll_name, cuts=cuts, update=update, onlyone=True)

    def GetRoomSettings(self, room_id):
        pass

    def GetSensorSettings(self, room_id, sensor_id):
        pass

    def StoreReading(self, room_id, sensor_id, timestamp, value):
        pass

    def GetData(self, room_id, sensor_id, t_start, t_end=None):
        pass
