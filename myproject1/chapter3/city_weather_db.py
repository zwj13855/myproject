import pymongo

class HefengDb():
    def __init__(self):
        self.client=pymongo.MongoClient('localhost',27017)
        self.book_weather=self.client['weather']
        self.sheet_weather=self.book_weather['sheet_weather_3']

    def save(self,date):
        self.sheet_weather=
if __name__=="__main__":
    client=pymongo.MongoClient('localhost',27017)
    book_weather=client['weather']
    sheet_weather=book_weather['sheet_weather_3']
    print(sheet_weather)
    sheet_weather.insert_one({"name":"zhanwenjuan","class":"net19049"})