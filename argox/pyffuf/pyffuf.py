import argparse
import asyncio
import sys
from datetime import datetime

import aiohttp
from bs4 import BeautifulSoup as bs
from clint.textui import puts, colored, indent

from argox.pyffuf.checker import CHECKER


class FUZZER:
    def __init__(self, urlx, wordlist):
        self.urlx = urlx
        self.wordlist = wordlist
        self.totalsend = 1
        self.totalsuc = 0
        self.total = 0

    async def checkpage(self, html):
        soup = bs(html, 'html.parser')
        try:
            chex = str(soup.select_one('title').text).upper()
            # print(chex)
            if "NOT FOUND" in chex or "404" in chex:
                return False
            else:
                return True
        except:
            pass

    async def printf(self, cldata, data, status_code="", responsex=""):
        try:
            with indent(4, quote='>>>'):
                if status_code != 404 and status_code != 403:
                    if await self.checkpage(responsex):
                        puts(colored.green(str(cldata)) + colored.green(data) +
                             colored.green(str(status_code)))
                        self.totalsuc = 1 + self.totalsuc
                        return str(data) + " " + str(status_code)
                    else:
                        print('>>> ' + colored.red(str(cldata)) + data, end="\r")
                else:
                    print('>>> ' + colored.red(str(cldata)) + data, end="\r")
        except KeyboardInterrupt:
            pass

    async def fetch(self, session, url):
        try:
            async with session.get(url, ssl=False) as response:
                txt = await response.text()
                data = await self.printf(f"[{self.totalsend}/{self.total}]" + " ", url + " > ", status_code=response.status,
                                  responsex=txt)
                self.totalsend = 1 + self.totalsend
                return data
        except Exception as e:
            await self.printf("Error : " + str(e), "")
            self.totalsend = 1 + self.totalsend

    async def readlist(self):
        try:
            async with aiohttp.ClientSession() as session:
                with open(self.wordlist, mode='r') as f:
                    tasks = [self.fetch(session, str(self.urlx.replace(
                        "PUFF", line).replace("\n", ""))) for line in f]
                    data = await asyncio.gather(*tasks)
                    return data
        except KeyboardInterrupt:
            self.done()
            return 0
        except UnicodeDecodeError:
            print('>>> ' + colored.red(str("There is a encoding error Please use a diffrent wordlist!")), end="\r")


    def done(self):
        with indent(4, quote='>>>'):
            puts(colored.red(str(">>>>>>>>>>>>>>>>>>>>>>>>>>>> DONE!")))
            puts(colored.red(str("Total Dir Found : ")) + str(self.totalsuc))
            puts(colored.red(str("End Time : ")) +
                 str(datetime.now().strftime('%H:%M:%S')))
            sys.exit()
        
    async def fucker(self,to):
        for i in to:
            yield i
    
    async def main(self):
        url = []
        ch = CHECKER(self.urlx, self.wordlist)
        self.total = ch.check()
        #self.fuzz()
        nicedata = await self.readlist()
        async for element in self.fucker(nicedata):
            if element != None:
                url.append(element)
            else:
                pass
        return url
