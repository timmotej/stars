#!/bin/env python3

from Docker import Docker, os

dict_options = {
    "sim": "",
    # "ftpd2": f"--mount type=bind,src=/home/ftptest,dst=/home/ftp --mount type=bind,src=/home/timo/git/ftp-server/logs,dst=/var/log --net={network} -p 20-21:20-21 -p 21100-21110:21100-21110  " ,
}

first_container = list(dict_options.keys())[0]
network = os.system(
    f'docker inspect {first_container} -f "{{{{json .NetworkSettings.Networks}}}}" | cut -f1 -d: | cut -f2 -d\'"\''
)

dict_commands = {
    "sftp": "'foo::1001:100:upload'",
}

container = Docker(list(dict_options.keys()), network, dict_options, dict_commands)
container.stop_containers()
container.rm_containers()
container.rm_images()
container.rm_network()
# container.debug()
# container.restart_containers()
# container.stop_containers()
# container.rm_containers()
# container.run_containers()
#
# container.rebuild_containers()

# [print("docker logs " + name) for name in dict_options.keys()]
# [(print(f"\n\ndocker logs {name}\n\n"),os.system("docker logs " + name)) for name in dict_options.keys()]

print("\n\nStatus of docker containers:\n\n")
os.system("docker ps -a")
