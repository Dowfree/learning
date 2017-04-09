#!usr/bin/env python
# -*-coding:utf-8 -*-
from urllib import request
from lxml import etree
weekday = []
weather = []
temperature = []
url = 'https://www.yahoo.com/news/weather/china/beijing/beijing-2151330'
with request.urlopen(url) as fp:
    data = fp.read().decode('utf-8')
    data_tree = etree.HTML(data)
    items = data_tree.xpath("//div[@class='BdB Bds(d) Bdbc(#fff.12) Fz(1.2em) Py(2px) O(0) Pos(r) forecast-item']")
    for item in items:
        weekday.append(item.xpath('./div/span/text()')[0])
        weather.append(item.xpath('./span[1]/img/@alt')[0])
        temperature.append(''.join(item.xpath('./span[3]//text()')[0:2]) + '-' + ''.join(item.xpath('./span[3]//text()')[2:]))

for i in range(8):
    print("%-20s%-25s%-20s" % (weekday[i], weather[i], temperature[i]))
