#!/usr/bin/python3
# This is main script of application
import sys

from fastapi import FastAPI, Request
from pydantic import BaseModel
import subprocess as sp
#from time import time, sleep
#from urllib3 import PoolManager

version = f"{sys.version_info.major}.{sys.version_info.minor}"

app = FastAPI()

#http = PoolManager()

class Stars(BaseModel):
    names: dict
    def get_names(self):
        return [ name for name in self.names ]
    def set_name(self,name):
        self.names.update(name)
        return self.names

class Git(BaseModel):
    identity: dict
    def push_change(self):
        ret = self.exec("git push")
        return ret
    def clone_repo(self):
        ret = self.exec("git clone")
        return ret
    def exec(self,cmd):
        proc = sp.Popen(cmd, stdout=sp.PIPE, stderr=sp.PIPE,shell=True)
        ret = [i.decode("utf-8") for i in proc.communicate()]
        return ret

#new_f = X(x=0.0)
#
@app.get("/")
async def read_root():
    message = f"Hello world! From FastAPI running on Uvicorn with Gunicorn in Alpine. Using Python {version}"
    return {"message": message}
# 
#@app.get("/start/x/{x}/v/{v}/k/{k}")
#async def start_all(x: float, v: float, k: float):
#    new_f.curl_a('sim',f'x/{x}')
#    new_f.curl_a('sim2',f'v/{v}')
#    new_f.curl_a('sim3',f'k/{k}')
#    sleep(5)
#    new_f.curl_a('sim3',f'x/{x}')
#    return {"status": stat}
#
#@app.get("/check")
#async def status():
#    stat = new_f.get_x()
#    return {"status": stat}
#
#@app.get("/x/{x}")
#async def setx(x: float):
#    new_f.null_all(x)
#    return {'new_value': new_f.dict()}
#
#@app.get("/v/{v}")
#async def addx(v: float):
#    x = new_f.set_x(v)
#    new_f.curl_a('sim3',f'x/{x}')
#    return {'new_value': new_f.dict()}
