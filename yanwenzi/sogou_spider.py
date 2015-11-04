# -*- coding:utf-8 -*-
import urllib
import urllib2
import json
import os

__author__ = 'https://github.com/kikoroc'

tag = {
    1: u'常用',
    2: u'高兴',
    3: u'卖萌',
    4: u'震惊',
    5: u'生气',
    6: u'无奈',
    7: u'晕',
    8: u'道歉',
    9: u'动物',
    10: u'害羞',
    11: u'哭',
    12: u'么么哒',
    13: u'睡啦',
    14: u'再见',
    15: u'傲娇',
    16: u'吃货',
    17: u'得意',
    18: u'害怕',
    19: u'囧',
    20: u'赞',
    21: u'难过',
    22: u'贱',
    23: u'其他'
}


def request(tag_id, page=1, recursive=True):
    data = {'tag_id': tag_id, 'type': 'tag', 'page': page}
    req = urllib2.Request(url='http://pinyin.sogou.com/dict/ywz/ajax/make_list.php', data=urllib.urlencode(data))
    response = urllib2.urlopen(req)
    ret = response.read()
    ret_json = json.loads(ret)
    parse(tag_id, ret_json)
    page = ret_json['page']
    if page > 1 and recursive:
        for p in range(2, page+1):
            request(tag_id, p, False) 		    


def parse(tag_id, ret_json):
    category = tag[tag_id]
    filename = './out/%s.txt' % category
    fh = open(filename, 'a')
    for entry in ret_json['data']:
        c = '%s\t%s\n' % (entry['tag'], entry['entry'])
        fh.write(c.encode('utf-8'))
    fh.close()


def clear(path):
    for f in os.listdir(path):
        txt = os.path.join(path, f)
        if os.path.isfile(txt):
            os.remove(txt)
 
if __name__ == '__main__':
    clear('./out/')
    for i in range(1, 24):
        request(i)
