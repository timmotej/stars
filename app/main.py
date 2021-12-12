#!/usr/bin/python3
# This is main script of application
import sys

from fastapi import FastAPI, Request
from pydantic import BaseModel
import subprocess as sp
import os
import json
from time import time, sleep
#from urllib3 import PoolManager

version = f"{sys.version_info.major}.{sys.version_info.minor}"

app = FastAPI()

#http = PoolManager()
identity = {"name": os.getenv("GIT_NAME","timmotej"), "email": os.getenv("GIT_EMAIL","timmotej@gmail.com")}
repo = {"path": "/app", "name": "stars"}
status_file = os.getenv("STATUSFILE","status")

class Stars(BaseModel):
    """
    Stars:
        names: { str name1: { "stars": int stars1, "current_award": int award_no }, ... }
        _categories: [str cat1, str cat2, ... ]
        _awards: [{str award1: int stars}, ...]
    """
    names: dict
    _categories: list
    _awards: list
    status_file: str
    def get_names(self):
        return [ name for name in self.names ]
    def set_name(self,name):
        self.names.update({name: {"stars": 0, "current_award": 0}})
        return self.names
    def get_stars(self):
        return self.names
    def set_stars(self, dict_stars):
        """
        Add/update name and number of stars
        self.set_stars({"somebody": 5})
        """
        self.names.update(dict_stars)
        return self.names
    def add_stars(self, name, stars=1):
        """
        Add number of stars to a name
        self.add_stars("somebody",3)
        """
        self.names[name]["stars"] += stars
        return self.names
    def get_categories(self):
        return self._categories
    def set_category(self, new_category):
        if new_category not in self._categories:
            self._categories += [new_category]
            return True
        return False
    def del_category(self, category):
        if category not in self._categories:
            self._categories.pop(category)
            return True
        return False
    def get_award(self, name):
        if self.names[name]["stars"] >= list(self._awards[self.names[name]["current_award"]].values())[0]:
            self.names[name]["stars"] -= list(self._awards[self.names[name]["current_award"]].values())[0]
            self.names[name]["current_award"] += 1
            return True
        else:
            return False
    def add_award(self, award, stars):
        self._awards += [{award: stars}]
        return self._awards
    def write_status(self):
        with open(f"{self.status_file}","w") as f:
            json.dump({"stars": self.stars, "categories": self._categories, "awards": self._awards}, f)
        return True
    def restore(self):
        with open(f"{self.status_file}","r") as f:
            read_dict = json.load(f)
        self._awards = read_dict["awards"]
        self._categories = read_dict["categories"]
        self.stars = read_dict["stars"]
        return read_dict
    @classmethod
    def read_json_file(cls, jsonfile):
        with open(f"{jsonfile}","r") as f:
            read_dict = json.load(f)
        return read_dict
        

class Git(BaseModel):
    identity: dict
    with open("~/.gitconfig","w") as f:
        conf = f"[user]\n\tusername = {self.identity['name']}\n\temail = {self.identity['email']}"
        f.write(conf)
    def pull_change(self):
        ret = self.exec("cd {repo['path']} && git push")
        return ret
    def push_change(self):
        ret = self.exec("cd {repo['path']} && git push")
        return ret
    def clone_repo(self):
        ret = self.exec("git clone {repo['path']}")
        return ret
    def exec(self, cmd):
        proc = sp.Popen(cmd, stdout=sp.PIPE, stderr=sp.PIPE,shell=True)
        ret = [i.decode("utf-8") for i in proc.communicate()]
        return ret
    def commit(self, message=f"Update {dt.now().strftime('%Y%m%d %H:%M:%S')}"):
        ret = self.exec(f"cd {repo['path']} && git add . --all && git commit -m '{message}'")
        return ret

g = Git(identity=identity)
g.clone_repo()

new_star = X(x=0.0)
#
@app.get("/")
async def read_root():
    message = f"Hello world! From FastAPI running on Uvicorn with Gunicorn in Alpine. Using Python {version}"
    return {"message": message}
# 
#@app.get("/start/x/{x}/v/{v}/k/{k}")
#async def start_all(x: float, v: float, k: float):
#    new_star.curl_a('sim',f'x/{x}')
#    new_star.curl_a('sim2',f'v/{v}')
#    new_star.curl_a('sim3',f'k/{k}')
#    sleep(5)
#    new_star.curl_a('sim3',f'x/{x}')
#    return {"status": stat}
#
@app.get("/check")
async def status():
    return {"status": new_star.dict()}

@app.get("/restore")
async def restore():
    new_star.restore()
    return {'restore': new_star.dict()}

#@app.get("/v/{v}")
#async def addx(v: float):
#    x = new_star.set_x(v)
#    new_star.curl_a('sim3',f'x/{x}')
#    return {'new_value': new_star.dict()}
