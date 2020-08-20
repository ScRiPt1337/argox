import asyncio
import aiohttp
from bs4 import BeautifulSoup, SoupStrainer
from cprint import *


class WebSpider():
    def __init__(self, url):
        if url.endswith("/"):
            self.url = url[:-1]
        else:
            self.url = url
        self.withoutwww = self.url.replace("http","").replace("https://","").replace("www.","")
        self.linkx = []

    async def spider(self, response):
        for link in BeautifulSoup(response, features="html.parser", parse_only=SoupStrainer(['a', 'img', 'script','link'])):
            if link.has_attr('href'):
                if link["href"] in self.linkx:
                    continue
                elif self.withoutwww not in link['href'] and link['href'].startswith("http"):
                    continue
                else:
                    if link['href'].startswith("http"):
                        self.linkx.append(link['href'])
                    elif link["href"].startswith("#"):
                        continue
                    elif len(link["href"]) == 1:
                        continue
                    else:
                        if self.url + link['href'] in self.linkx:
                            continue
                        else:
                            self.linkx.append(str(self.url + link['href']))

    async def fetch(self,url,session):
        try:
            async with session.get(url, ssl=False) as response:
                txt = await response.text()
                await self.spider(txt)
        except:
            pass
            
    async def run(self):
        async with aiohttp.ClientSession() as session:
            await asyncio.gather(*[self.fetch(self.url,session)])
            return self.linkx
        
