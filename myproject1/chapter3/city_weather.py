import requests

class HeFeng():
    def __init__(self):
        self.url="http://cdn.heweather.com/china-city-list.txt"


    def get_city_code(self):
        cities=self.get_citys()
        for each in cities:
            yield(each[2:13])

    def get_citys(self):
        html=requests.get(self.url)
        html.encoding='utf8'
        cities=html.text.split('\n')
        return cities[6:]
        #print(html.text)

if __name__ == '__main__':
    hefeng =HeFeng()
    #hefeng.get_city_code()
    #for each in hefeng.get_citys():
     #   print(each)
    code=hefeng.get_city_code()
    print(code.__next__())
    print(code.__next__())
    print(code.__next__())
