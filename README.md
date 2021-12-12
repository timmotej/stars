# How to start and try the current branch

__It's very easy, give it a try!__ : :rocket:

`python3 test_start_project.py`

will start Docker container, reachable on: 

`http://localhost:8081`
1. Go to `http://localhost:8081/x/${original value}`, where `${original value}` can be any float value (integer will be converted)\
This value represents starting value of system part

2. Go to `http://localhost:8081/v/${velocity value}`, where `${velocity value}` is any value, represents speed of change `x / time [s]`\
The result is new value of x, change by `delta x = v * delta t`

* ___Prerequisities:___
  * installed:
    * `docker`
    * `python3` _(for script starting the container, otherwise not necessary, container can be started manualy with `docker` commands)_
    * some __browser__ (or __curl__ or __whatever sh\*t__ which can make ___url requests___)

# About the project

## Topic
