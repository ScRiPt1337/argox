from socket import gethostbyname, gethostbyaddr
import asyncio
import subprocess
import dns.resolver

from cprint import *


class DnsEnum:
    def __init__(self, host):
        self.url = host.replace("http://","").replace("https://","")
        self.x = []

    async def getnamebyip(self):
        host = ""
        try:
            try:
                new = dns.resolver.query(self.url.replace("http://", "").replace("https://", ""), "A")
                for A in new:
                    host = A.to_text()
            except:
                pass
            if host:
                name = gethostbyaddr(host)
            else:
                name = gethostbyaddr(self.url)
            try:
                domain = subprocess.check_output("nslookup -querytype=PTR " + host, shell=True)
                name = str(name) + "\n"+str(domain)
            except Exception as e:
                cprint.err(e)
            return name
        except Exception as e:
            cprint.err(e)
            return "1"

    async def get_records(self):
        ids = [
            "NONE",
            "A",
            "NS",
            "MD",
            "MF",
            "CNAME",
            "SOA",
            "MB",
            "MG",
            "MR",
            "NULL",
            "WKS",
            "PTR",
            "HINFO",
            "MINFO",
            "MX",
            "TXT",
            "RP",
            "AFSDB",
            "X25",
            "ISDN",
            "RT",
            "NSAP",
            "NSAP-PTR",
            "SIG",
            "KEY",
            "PX",
            "GPOS",
            "AAAA",
            "LOC",
            "NXT",
            "SRV",
            "NAPTR",
            "KX",
            "CERT",
            "A6",
            "DNAME",
            "OPT",
            "APL",
            "DS",
            "SSHFP",
            "IPSECKEY",
            "RRSIG",
            "NSEC",
            "DNSKEY",
            "DHCID",
            "NSEC3",
            "NSEC3PARAM",
            "TLSA",
            "HIP",
            "CDS",
            "CDNSKEY",
            "CSYNC",
            "SPF",
            "UNSPEC",
            "EUI48",
            "EUI64",
            "TKEY",
            "TSIG",
            "IXFR",
            "AXFR",
            "MAILB",
            "MAILA",
            "ANY",
            "URI",
            "CAA",
            "TA",
            "DLV",
        ]

        for a in ids:
            try:
                answers = dns.resolver.query(self.url, a)
                for rdata in answers:
                    self.x.append(str(a + ":" + rdata.to_text()))
            except:
                pass

    async def run(self):
        domain = await self.getnamebyip()
        txt = await self.get_records()
        self.x.append(domain)
        return self.x