import scrapy
import re

class StatSpider(scrapy.Spider):
  name = "stat"
  start_urls = [
    'https://www.ngdc.noaa.gov/nndc/struts/results?bt_0=1965&st_0=2016&type_17=EXACT&query_17=None+Selected&op_12=eq&v_12=&type_12=Or&query_14=None+Selected&type_3=Like&query_3=&st_1=&bt_2=&st_2=&bt_1=&bt_4=5.5&st_4=&bt_5=&st_5=&bt_6=&st_6=&bt_7=1&st_7=&bt_8=&st_8=&bt_9=&st_9=&bt_10=&st_10=&type_11=Exact&query_11=&type_16=Exact&query_16=&bt_18=&st_18=&ge_19=&le_19=&type_20=Like&query_20=&display_look=1&t=101650&s=1&submit_all=Search+Database'
  ]

  def parse(self, response):
    table = response.css('table')[2]
    tr = table.css('tr')[3:]
    for r in tr:
      td = r.css('td::text').extract()
      print(td)
      yield {
        'date': "{}/{}/{}".format(td[1], td[2], td[0]),
        'year': int(td[0]),
        'time': "{}:{}".format(td[3], td[4]),
        'country': td[6],
        'lat': float(td[7]),
        'lng': float(td[8]),
        'depth': float(td[9]),
        'magnitude': float(td[10]),
        'deaths': int(td[11].strip()),
      }
