Created for the 2013 7DRL contest.

Version 2
Changes:
    Fixed typo in user interface ('mana_use' instead of 'mana')
    Readme now tells windows users to run 'Flee.exe' instead of 'windowsFlee.exe'

Written by Spferical (Spferical [at] gmail [dot] com)

Uses libtcod 1.5.1 © Jice & Mingos
http://doryen.eptalys.net/libtcod

TO RUN:
    Windows users can run Flee.exe
    Linux users should have python installed, and can run main.py
    (unfortunately, the game does not run in WINE for me - but you can try...)
    OSX users can install Python and run main.py or run BootCamp or whatever

MENUS:
    Arrow keys - navigate
    Enter - select

HOW TO PLAY:

Movement is done with the number pad or with vi style keys.
(If you want to suffer a great tactical disadvantage,
you can also use the arrow keys)
7 8 9    y k u
 \|/      \|/
4-5-6    h-.-l
 /|\      /|\
1 2 3    b j n

Keys:
    z/x/c - use your items / abilities
    alt + enter - enter fullscreen
    escape - enter escape menu (where you can exit the game)

Targeting:
    movement keys to move cursor, enter to confirm
    mouse to target, left click to select


ABOUT:
I wanted to create a game where you are thrust into a
large conflict and need to use your wits to survive and move onward.
"Ooooorrrcs!" by Jakub Debski was definitely an inspiration.
http://www.alamak0ta.republika.pl/orcs.html
There are two armies:
    the dwarves, spawning on the top of the screen
    various baddies, spawning on the bottom of the screen
You are a stinking human thief who managed to get into a fortress
of the dwarves and steal some valuable artifacts in the middle of an
invasion. You now need to get out in the middle of an invasion,
with your escape route blocked by a raging battle. The exit is, oh,
200 squares away. Fortunately, you have items on you that you stole
from the dwarves! You will have to use mana to utilize those items,
though. Mana recharges by 1 unit per turn. Good luck!

THE ITEMS:
Crossbow - a basic ranged weapon. You can fire it in any of 8
    directions. It deals 5 damage, using 5 mana.
Heal - heals you completely, using 30 mana.
Regeneration Amulet - heals you by one hit point every 4 turns.
Fireball - Explodes in a location of your choosing (that you can see),
    dealing 10 damage in a 2-tile radius of the spot that you chose.
    Note that the 'circle' of effect is a square.
Scroll of Confusion - confuses an enemy for 10 turns using 40 mana.
    Confused enemies will move in random directions, possibly
    damaging teammates, and possibly damaging themselves!
Self-destruct package - a fun item. It explodes, dealing 10 damage to
    everyone in a 10-tile radius (square), INCLUDING you. Make sure
    you have at least 10 health when you use this! Unless you just
    want to go out with a bang.


Have fun!
