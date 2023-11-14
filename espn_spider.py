from typing import Iterable
import scrapy
from scrapy.http import Request

class EspnSpide(scrapy.Spider):
  name = "espn"

  def start_requests(self):
    urls = [
      "https://www.espn.com/nfl/lines",
      "https://www.espn.com/college-football/lines",
      "https://www.espn.com/nba/lines",
      "https://www.espn.com/nhl/lines",
      "https://www.espn.com/mlb/lines",
    ]

    for url in urls:
      yield scrapy.Request(url=url, callback=self.parse)

  def parse(self, response):
      for table in response.xpath('//tbody[@class="Table__TBODY"]'):
        for team in table.xpath('.//tr[@class="Table__TR Table__TR--sm Table__even"]'):
          yield {
            "sport": response.xpath('//a[@class="AnchorLink Nav__Secondary__Menu__Link clr-gray-01 flex items-center pl3 pr4"]/span[@class="Nav__Text"]/text()').get(),
            "team": team.xpath('.//text()').get(),
            "ML": team.xpath('.//td[4]/text()').get(),
            "BPI":team.xpath('.//td[5]/text()').get(),
          }