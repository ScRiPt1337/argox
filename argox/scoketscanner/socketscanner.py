import asyncio
from socket import gethostbyname
from cprint import *


class portscanner:
    def __init__(self, host,fullscan=False,debug=False):
        self.host = host
        self.fullscan = fullscan
        self.open = []
        self.debug = debug

    async def runner(self):
        if self.fullscan:
            x = 5000
            for i in range(14):
                if i >= 1 or i >= 2:
                    x = x + 5000
                task = [self.open_socket(ports) for ports in range(x - 5000 ,x)]
                await asyncio.gather(*task)
        else:
            task = [self.open_socket(ports) for ports in range(5000)]
            await asyncio.gather(*task)
            taskx = [self.open_socket(ports) for ports in range(5000,10000)]
            await asyncio.gather(*taskx)
            
    async def open_socket(self, port):
        if int(port) > 65535:
            return 1
        socket_connection = asyncio.open_connection(self.host, port, loop=self.loop)
        try:
            _, writer  = await asyncio.wait_for(socket_connection, timeout=5)
            writer.close()
            self.open.append(port)
        except Exception as e:
            if self.debug == True:
                cprint.err(e)
        
    async def main(self, loop):
        self.loop = loop
        await self.runner()
        return self.open

if __name__ == "__main__":
    pass
    
