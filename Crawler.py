#============================================================
# Create Time:			2020-01-01 15:00:33
# Last modify:			2020-01-27 23:28:26
# Writer:			Wenhao	1795902848@qq.com
# File Name:			Crawer.py
# File Type:			PY Source File
# Tool:				Windows -- vim & python
# Information:                  学习强国新闻爬虫。
#============================================================
import requests
import json
import MysqlOperator

class XuexiCrawer:
    def __init__(this):
        this.urls = [
            'https://www.xuexi.cn/lgdata/1ajhkle8l72.json?_st=26297694', #综合新闻
            'https://www.xuexi.cn/lgdata/1jscb6pu1n2.json?_st=26297944', #重要新闻
            'https://www.xuexi.cn/lgdata/35il6fpn0ohq.json?_st=26297951', #学习重点
            'https://www.xuexi.cn/lgdata/tuaihmuun2.json?_st=26297968', #新闻发布厅
            'https://www.xuexi.cn/lgdata/slu9169f72.json?_st=26297974', #中宣部发布
            'https://www.xuexi.cn/lgdata/1ap1igfgdn2.json?_st=26298241', #学习时评
            'https://www.xuexi.cn/lgdata/1crqb964p71.json?_st=26298245' #头条新闻
        ]
        this.headers = {
            'Host':'www.xuexi.cn',
            'Accept':'application/json',
            'User-Agent':'Mozilla/5.0 (Windows NT 10.0: Win64: x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.88 Safari/537.36',
            'Sec-Fetch-Site':'same-origin',
            'Sec-Fetch-Mode':'cors',
            'Referer':'https://www.xuexi.cn/7097477a9643eacffe4cc101e4906fdb/9a3668c13f6e303932b5e0e100fc248b.html',
            'Accept-Encoding':'gzip, deflate, br',
            'Accept-Language':'zh,zh-TW:q=0.9,en-US:q=0.8,en:q=0.7,zh-CN:q=0.6',
            'Cookie':'__UID__=1ce3f4f0-faca-11e9-b605-0f97eea8a7d8',
            'Connection':'keep-alive'
        }
        this.db = MysqlOperator.MysqlOperator()
        return None

    def crawl(this):
        for url in this.urls:
            r = requests.get(url=url, headers=this.headers, verify=True)
            txt = r.content.decode("utf-8")
            json_content = json.loads(txt)
            for item in json_content:
                publishTime = item.get("publishTime")
                title = item.get('title')
                source = item.get('showSource')
                if(publishTime == "" or title == "" or source == ""):
                    continue
                this.db.insertOneLine(
                        date=publishTime, title=title, editor=source)
        this.db.commit()
        return None

class YangshiCrawler(object):
    """央视网新闻爬虫"""
    def __init__(this):
        """""jsonUrl中的数字为1，2，3，...
        jsonUrl是国内新闻url
        """
        super(YangshiCrawler, this).__init__()
        this.jsonUrl = 'http://news.cctv.com/2019/07/gaiban/cmsdatainterface/page/china_%d.jsonp?cb=t&cb=china'
        return None

class ChinaYouthCrawler(object):
    """docstring for ChinaYouthCrawler
    http://www.youth.cn/
    """
    def __init__(this, arg):
        super(ChinaYouthCrawler, this).__init__()
        this.arg = arg
        return None

class ChinaNewsCrawler(object):
    """docstring for ChinaNewsCrawler
    http://www.chinanews.com/china/
    """
    def __init__(this, arg):
        super(ChinaNewsCrawler, this).__init__()
        this.arg = arg
        return None

if __name__ == '__main__':
    c = XuexiCrawer()
    c.crawl()
