#!/usr/bin/python3

"""
This is main script of logs analyst
"""

import sys
from re import sub,subn

from fastapi import FastAPI, Request
from pydantic import BaseModel
from time import time, sleep
from urllib3 import PoolManager
from os import getenv

version = f"{sys.version_info.major}.{sys.version_info.minor}"
log_file = getenv("LOG_FILE","/data/log")

app = FastAPI()

http = PoolManager()

class X(BaseModel):
    x: float
    t: float
    log_file: str

    def get_values(self):
        ln = 1
        data = []
        with open(self.log_file,"r") as f:
            for line in f:
                l_data = line.replace("\n","")
                dt, val = subn(r".*\[([0-9-]+)\]:\s*([0-9:]+).*",r"\1 \2",l_data), subn(r".*/[A-z]*/([0-9-]+\.[0-9e%B]*)\s.*",r"\1",l_data)
                if ln % 1000 == 1 and val[1] > 0 and dt[1] > 0:
                    data += [[ln, dt[0], val[0]]]
                ln += 1
        return {"lines": data}

    def curl_a(self, con, uri, timeout=0.1):
        url = f'http://{con}:8085/{uri}'
        try:
            req = http.request('GET',url,timeout=timeout)
        except:
            pass


new_f = X(x=0.0, t=time(), log_file=log_file)

@app.get("/")
async def read_root():
    message = f"Hello world! From FastAPI running on Uvicorn with Gunicorn in Alpine. Using Python {version}"
    return {"message": message}
 

@app.get("/print")
async def print_lines():
    lines = new_f.get_values()
    return lines
 

