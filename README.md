# turtlesim-challenge
Python and javascripts turtlesim examples.

Before testing the scripts
* Run `roscore`
* Run `rosrun turtlesim turtelsim_node`

Test the python script just execute it from the terminal.
* Run `python2.7 turtlesim.py`

Test the javascript by also launching rosbridge besides roscore and the turtlesim node.
* Run `roslaunch rosbridge_server rosbridge_websocket.launch`
* Open turtle-sim.html and press the draw pentagram button.

The python script draws two stars, one after the other with 4 seconds between them.
The javascript one draws a pentagram when you execute it.

## Known bugs
The javascript star drawer sometimes fails for no apparent reason.

## TODO
 * Improve javascript acurracy.
 * Picture interpreter.
