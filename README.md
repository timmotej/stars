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
**Comet weather forecast/Simulation of simple non-linear system**

## Literature

  * [arXiv - Computational physics](https://arxiv.org/list/physics.comp-ph/recent)
  * [arXiv - Chaotic Dynamics](https://arxiv.org/list/nlin.CD/recent)
  * [py 3D Shape class - pi3d module](https://pi3d.github.io/html/pi3d.html#pi3d.Shape.Shape)

***Other interesting links***
  1. [Visible and near-infrared observations of interstellar comet 2I/Borisov](https://arxiv.org/abs/2005.00786)
  2. [Outburst and Splitting of Interstellar Comet 2I/Borisov](https://arxiv.org/abs/2006.01242)
  3. [The dust-to-gas ratio, size distribution, and dust fall-back fraction of comet 67P/Churyumov-Gerasimenko](https://arxiv.org/abs/2005.13700)
  4. [Evidence that 1I/2017 U1 Oumuamua was composed of molecular hydrogen ice](https://arxiv.org/abs/2005.12932)
  5. [Activity of (6478) Gault during January 13 - March 28, 2019](https://arxiv.org/abs/2005.12030)
  6. [Continuum mechanics](https://en.m.wikipedia.org/wiki/Continuum_mechanics)
  7. [3D python programming pages](https://sites.google.com/site/3dprogramminginpython/)

## Structure of simulation

Simulation is very simple done in the form of interacting nodes, whose represent parts of system, e.g. grains of materials in the comet body, Sun/star wind. There is one node responsible for logging the events and state of subsystem and will make a presentation of the revolution of system.

The goal is to simulate the changes in system, included:

  * changes of temperature of different parts (like a vector field), 
  * changes of states of matter, 
  * the atmosphere around the comet, 
  * the solar radiation, 
  * albedo of parts, 
  * energy flows, 
  * possible ***greenhouse effect***, 
  * gravitational interraction of comet parts, 
  * creation of bubbles of liquid/gas inside of comet, its abrupt bursts outside, 
  * creation of other instances (when there is change, which create the new part of the comet),
  * the solar wind, 
  * the gravitation of the star, 
  * rotation, 
  * rotation changes, 
  * day/night changes. 

The goal ***doesn't include***: 
  * gravitational interractions of other planets, 
  * asteroids.

TODO:
  * pick the right 3D model for the comet structure,
    which will include surfaces, mass, can define 
    a vector fields inside

## Branches

### 0-basic

  1. Add logging positions of system
  2. Think and make the simple and effective way how to start process
  3. Visualization: time/animation and graphs

### 1-pendulum

  1. add curl call for other containers

