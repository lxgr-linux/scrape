# Scrape
By lxgr <lxgr@protonmail.com> 

![Demo](pics/demo.gif)

## Installation
For linux just do this:
```Shell
$ git clone https://github.com/lxgr-linux/scrap_engine.git
$ git clone https://github.com/lxgr-linux/scrape.git
$ cp ./scrap_engine/scrap_engine.py ./scrape
$ ./scrape/scrape.py
```
For windows first install pynput and then do a windows equivalent to the above.

## What the game is about
Scrape is basically a clone of the snake game, but with some additional modes. The Main goal of the player is to eat as many apples while not dying.

## Modes
Until now there are 5 modes:
- normal: In this mode you have regularly spawning apples and berries, the apples make the snake longer but the berries shorter and faster. Colliding with the walls or the snake it self kills it.
- single: The only difference to the normal mode is that apples and berries just respawn when one berry/apple is eaten.
- easy: In this mode just apples exist and colliding with wall does not kill the snake.
- hard: This is the hard mode, here the amount of apples and berries spawning is the same, but also blocks are spawned, that will kill the snake at colliding.
- multi: This in the multiplayer mode, in this mode two snakes are present which can be controlled separately. The goal of each player is to kill the other player.
- really_fucking_easy: This is the REALLY FUCKING EASY mode, and it's really fucking easy. Therefore the snake does not die on crash with itself.

## How to play
General buttons: "e" -- to end the game, "m" -- to pause it

Control buttons: snake1: w,a,s,d; snake2: i,j,k,l

## Resizing
In scrape resizing the game window is supported. Maximizing works flawlessly, minimizing can be tricky, because the snake(s) have to be in the left top corner, when minimizing, else, when the snake(s) are outside of the newly created widows size, they will die.

## Scores
The scores for each mode are saved to ```~/.cache/scrape/scrape ```.

## Hacking
You can hack the game by, for example, adding modes, which can be very simply done.
The first thing to do is to add two functions: level_$modename and level_$modename_init, and adding $modename to the modes array in circa line 436. The the mode will be available in the menu.

The level_$modename_init function will be executed one time per game, at it's start and the level_$modename function will be executed every frame. It handles for example berry/apple genration.
The level_$modename_init function has to contain the definition of the Start class which is the class of all objects in the snake. For most modes it is Start=Start_master.
