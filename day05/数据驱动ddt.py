import ddt
import requests
import unittest

url = 'https://www.lagou.com/jobs/positionAjax.json?needAddtionalResult=false'

def getHeader():
    headers = {
        'Content-Type':'application/x-www-form-urlencoded; charset=UTF-8',
        'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36',
        'Cookie':'_ga=GA1.2.2045471023.1548125216; user_trace_token=20190122104637-f04ffaab-1def-11e9-b733-5254005c3644; LGUID=20190122104637-f0500254-1def-11e9-b733-5254005c3644; sensorsdata2015jssdkcross=%7B%22distinct_id%22%3A%22168737437ae434-0c32dacc5e9b33-b781636-2073600-168737437af8d3%22%2C%22%24device_id%22%3A%22168737437ae434-0c32dacc5e9b33-b781636-2073600-168737437af8d3%22%7D; LG_LOGIN_USER_ID=135fcd869c5bf54528adb2891adec074f841e6b9dbd4b047; WEBTJ-ID=20190329213004-169c9a4a6a09e1-0d541aeec71856-7a1437-2073600-169c9a4a6a1a72; Hm_lvt_4233e74dff0ae5bd0a3d81c6ccf756e6=1553866206; JSESSIONID=ABAAABAAADEAAFI93478353CA8D7C48D55DA0A852B19539; index_location_city=%E5%85%A8%E5%9B%BD; TG-TRACK-CODE=index_search; X_MIDDLE_TOKEN=77d9266f390cbaf1882649f5d697e7da; _gat=1; Hm_lpvt_4233e74dff0ae5bd0a3d81c6ccf756e6=1554079402; _gid=GA1.2.1545609527.1554079402; LGSID=20190401084238-0ccfdbd0-5417-11e9-bba5-5254005c3644; PRE_UTM=; PRE_HOST=; PRE_SITE=https%3A%2F%2Fwww.lagou.com%2Futrack%2FtrackMid.html%3Ff%3Dhttps%253A%252F%252Fwww.lagou.com%252Fjobs%252Flist_%2525E8%252587%2525AA%2525E5%25258A%2525A8%2525E5%25258C%252596%2525E6%2525B5%25258B%2525E8%2525AF%252595%2525E5%2525B7%2525A5%2525E7%2525A8%25258B%2525E5%2525B8%252588%253Fcity%253D%2525E5%252585%2525A8%2525E5%25259B%2525BD%2526cl%253Dfalse%2526fromSearch%253Dtrue%2526labelWords%253D%2526suginput%253D; PRE_LAND=https%3A%2F%2Fwww.lagou.com%2Fjobs%2Flist_%25E8%2587%25AA%25E5%258A%25A8%25E5%258C%2596%25E6%25B5%258B%25E8%25AF%2595%25E5%25B7%25A5%25E7%25A8%258B%25E5%25B8%2588%3Fcity%3D%25E5%2585%25A8%25E5%259B%25BD%26cl%3Dfalse%26fromSearch%3Dtrue%26labelWords%3D%26suginput%3D; LGRID=20190401084238-0ccfddfd-5417-11e9-bba5-5254005c3644; SEARCH_ID=2b402c967bb14edd95d43a2692088bb9',
        'Referer':'https://www.lagou.com/jobs/list_%E8%87%AA%E5%8A%A8%E5%8C%96%E6%B5%8B%E8%AF%95%E5%B7%A5%E7%A8%8B%E5%B8%88?city=%E5%85%A8%E5%9B%BD&cl=false&fromSearch=true&labelWords=&suginput='
    }
    return headers

@ddt.ddt
class Lagou(unittest.TestCase):

    @ddt.data((1,), (2,), (3,))
    @ddt.unpack
    def test_lagou(self, page):

        positions = []
        r = requests.post(url=url,
                          headers=getHeader(),
                          data={'first':False, 'pn':page,'kd':'自动化测试工程师'})
        self.assertEqual(r.json()['success'], True)


if __name__ == "__main__":
    unittest.main(verbosity=2)