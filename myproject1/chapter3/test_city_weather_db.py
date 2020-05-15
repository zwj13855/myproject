import unittest

from chapter3.city_weather import mongodb

class TestCityWeatherDbCase(unittest.TestCase):

    def test_save(self):
        hefengDb = HefengDb()
        hefengDb.save({"name": "zhanwenjuan", "class": "net19049"})
        hefengDb.show_all()
        results=hefengDb.find({"name":"zhanwenjuan"})
        for each in results:
            self.assertEqual("zhanwenjuan",each['name'])
            self.assertEqual("net19049",each['class'])
            hefengDb.delete()
            #print(each)
        #self.assertEqual(4,hefengDb.find_all())

    def test_save_all(self):
        hefeng=HeFeng()
        #codes=hefeng.get_city_code()
        #for each in codes:
        #    print(next(codes))
        each=hefeng.get_weather("CN101010200")
        print(each)
        hefengDb=HefengDb()

if __name__=='__main__':
    unittest.main()