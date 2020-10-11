ezrassor_sim_gazebo
---------------------
![Build Badge](https://github.com/FlaSpaceInst/ezrassor_sim_gazebo/workflows/Build/badge.svg) 
![Style Badge](https://img.shields.io/badge/Code%20Style-black-000000.svg)

The `ezrassor_sim_gazebo` package contains the worlds and models that the EZRASSOR can interact with when running in Gazebo 11.

usage
-----
```
command:
  ros2 launch ezrassor_sim_gazebo gazebo_launch.py [argument:=value]

optional arguments:
  world  *.world file name (default base.world)
```

example
--------
Launch the Gazebo client with the Moon world:
```
ros2 launch ezrassor_sim_gazebo gazebo_launch.py world:=moon.world
```   
![Moon World](moon-world.jpg)
