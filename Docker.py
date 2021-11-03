#!/bin/env python3

import os
import sys


class Docker:
    """'Docker' object 
    - new Containers = Docker( list names, str network=None, dict options=None, dict commands=None, str dockerfile_suffix=None)
        - names: e.g. ["mysql",...] -> there has to be Dockerfile with the same name or the image in Docker repo
        - network: e.g. "some_net"
        - options: e.g. { "container1":f" -i -e MYSQL_DATABASE=somedb --net={network} -p 9000:3306", "container2": ...}
        - commands: e.g. { "container1":f"ls -las /home" }
        - dockerfile_suffix: added string to Dockerfile from which to start, e.g. if you want to start from {name}-debug.Dockerfile then set to "-debug"
        - no_containers: e.g. { "container1":3, "container2":5 ...}
    """

    def __init__(
        self,
        names,
        network=None,
        options=None,
        commands=None,
        dockerfile_suffix=None,
        no_containers=None,
    ):
        self.names = names
        self.options = (
            {name: "" for name in self.names}
            if (options is None or not isinstance(options, dict))
            else options
        )
        self.network = network
        self.commands = (
            {name: "" for name in self.names}
            if (commands is None or not isinstance(commands, dict))
            else {
                name: commands[name] if name in list(commands.keys()) else ""
                for name in self.names
            }
        )
        self.no_containers = (
            {name: 1 for name in self.names}
            if (no_containers is None or not isinstance(no_containers, dict))
            else {
                name: no_containers[name] if name in list(no_containers.keys()) else 1
                for name in self.names
            }
        )
        self.dockerfile_suffix = dockerfile_suffix if dockerfile_suffix else ""

    def debug(self):
        [
            print(var)
            for var in [
                self.names,
                self.options,
                self.network,
                self.commands,
                self.dockerfile_suffix,
                self.no_containers,
            ]
        ]

    def rm_network(self):
        comms = [f"docker network rm {self.network}"]
        return [
            os.system(comm) if self.network is not None else False for comm in comms
        ]

    def create_network(self):
        comms = [f"docker network create {self.network}"]
        return [
            os.system(comm) if self.network is not None else False for comm in comms
        ]

    def stop_containers(self):
        comms = [
            f"docker stop {name}{str(no_container+1) if (self.no_containers[name] > 1) else ''}"
            for name in self.names
            for no_container in range(self.no_containers[name])
        ]
        return [os.system(comm) for comm in comms]

    def rm_containers(self):
        comms = [
            f"docker rm {name}{str(no_container+1) if (self.no_containers[name] > 1) else ''}"
            for name in self.names
            for no_container in range(self.no_containers[name])
        ]
        return [os.system(comm) for comm in comms]

    def rm_images(self):
        comms = [f"docker rmi {name}" for name in self.names]
        return [os.system(comm) for comm in comms]

    def build_images(self):
        # check if the dockerfile is there, otherwise it will pull from repo
        comms = [
            f"docker build -t {name}:latest -f  {name}{self.dockerfile_suffix}.Dockerfile ."
            if os.path.isfile(f"{name}{self.dockerfile_suffix}.Dockerfile")
            else f"echo \"'{name}{self.dockerfile_suffix}.Dockerfile' doesn't exist, the '{name}:latest' will be downloaded from Docker repo in the docker run step"
            for name in self.names
        ]
        return [os.system(comm) for comm in comms]

    def start_containers(self):
        comms = [f"docker start {name}" for name in self.names]
        return [os.system(comm) for comm in comms]

    def run_containers(self):
        comms = [
            # if there are more containers needed to deploy, there will be run with numbers name{1,...,n}
            f"docker run -d --name {name}{str(no_container+1) if (self.no_containers[name] > 1) else ''} {self.options[name]}  {name} {self.commands[name]}"
            for name in self.names
            for no_container in range(self.no_containers[name])
        ]
        [print(comm) for comm in comms]
        return [os.system(comm) for comm in comms]

    def copy_file(self, dict_comm):
        comms = [
            f"docker cp {dict_comm[name][0]} {dict_comm[name][1]}"
            for name in self.names
        ]
        [print(comm) for comm in comms]
        return [os.system(comm) for comm in comms]

    def run_command(self, dict_comm):
        comms = [
            f'docker exec -it {name} sh -c " {dict_comm[name]} "'
            for name in dict_comm.keys()
        ]
        [print(comm) for comm in comms]
        return [os.system(comm) for comm in comms]

    def restart_containers(self):
        self.stop_containers()
        self.rm_containers()
        self.run_containers()

    def rebuild_containers(self):
        self.stop_containers()
        self.rm_containers()
        self.rm_network()
        self.rm_images()
        self.build_images()
        self.create_network()
        self.run_containers()
