#!/bin/env python3

from Docker import Docker, os

net = input("Give here network name, e.g. empty -> produces 'empty_net':\n")
network = f"{net}_net"

dict_options = {
    "sim": f" -it -p 8081:8085 --net={network} ",
    "sim2": f" -it -p 8082:8085 --net={network} ",
    "sim3": f" -it -p 8083:8085 --net={network} ",
}

commands = {
    "sim": f"",
    "sim2": f"",
    "sim3": f"",
}

no_containers = {
    "sim": 1,
    "sim2": 1,
    "sim3": 1,
}

dockerfile = "-debug"

container = Docker(
    list(dict_options.keys()),
    network,
    dict_options,
    commands,
    dockerfile,
    no_containers,
)

container.rebuild_containers()

[print("docker logs " + name) for name in dict_options.keys()]
[
    (print(f"\n\ndocker logs {name}\n\n"), os.system("docker logs " + name))
    for name in dict_options.keys()
]

print("\n\nStatus of docker containers:\n\n")
os.system("docker ps -a")
[print(f"docker IP address {name}:") for name in dict_options.keys()]
[
    (
        print(f"\ndocker inspect {name} | grep -v '\"\"' | grep 'IPAddress\"'\n"),
        os.system(f"docker inspect {name} | grep -v '\"\"' | grep 'IPAddress\"'"),
    )
    for name in dict_options.keys()
]
