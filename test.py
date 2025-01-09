from zeep import Transport
from pathlib import Path
from plunetapi import PlunetAPI
from zeep.cache import SqliteCache, InMemoryCache
import time

if __name__ == '__main__':
    pc = PlunetAPI(base_url="https://test14.plunet.com", cache_wsdl=True)
    print("cache_wsdl=True  ", pc.api_version, pc.plunet_version)
    a = time.time_ns()
    print(pc.DataItem30)
    print(pc.DataOrder30)
    print(time.time_ns() - a)
    a = time.time_ns()
    print(pc.DataItem30)
    print(pc.DataOrder30)
    print(time.time_ns() - a)

    pc = PlunetAPI(base_url="https://test14.plunet.com", cache_wsdl=False)
    print(" cache_wsdl=False ", pc.api_version, pc.plunet_version)
    a = time.time_ns()
    print(pc.DataItem30)
    print(pc.DataOrder30)
    print(time.time_ns() - a)
    a = time.time_ns()
    print(pc.DataItem30)
    print(pc.DataOrder30)
    print(time.time_ns() - a)
    sqlpath = Path("zeep.db")
    chache = SqliteCache(path=str(sqlpath))
    options = {"cache": chache}
    pc = PlunetAPI(base_url="https://test14.plunet.com", cache_wsdl=False, options=options)
    print("cache_wsdl=False, options=options - cache" , pc.api_version, pc.plunet_version)
    a = time.time_ns()
    print(pc.DataItem30)
    print(pc.DataOrder30)
    print(time.time_ns() - a)
    a = time.time_ns()
    print(pc.DataItem30)
    print(pc.DataOrder30)
    print(time.time_ns() - a)
    if sqlpath.exists():
        sqlpath.unlink()

    transport = Transport(cache=InMemoryCache())
    options = {"transport": transport}
    pc = PlunetAPI(base_url="https://test14.plunet.com", cache_wsdl=False, options=options)
    print("cache_wsdl=False, options=options memory cache ", pc.api_version, pc.plunet_version)
    a = time.time_ns()
    print(pc.DataItem30)
    print(pc.DataOrder30)
    print(time.time_ns() - a)
    a = time.time_ns()
    print(pc.DataItem30)
    print(pc.DataOrder30)
    print(time.time_ns() - a)