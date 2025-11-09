# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define e = Character("Eileen")
define p = Character("Penny",what_prefix="\"",what_suffix="\"")
define b = Character("Blake",what_prefix="\"",what_suffix="\"")

init python:
    renpy.music.register_channel("LoNoise","bgs")
    renpy.music.register_channel("sound2","sfx",loop=False)

# The game starts here.

label start:
    pause 2.0
    scene vale_day with dissolve
    pause 0.5
    show Penny happy:
        zoom 0.5 xalign 0.33 yalign 1.0
    show Blake neutral:
        zoom 0.5 yalign 1.0 xalign 0.66
    with pixellate
    pause 0.5
    b "Hello, my name is Blake and... I guess welcome to this tutorial?"

    show Penny:
        easein 3.0 xalign 0.66
    show Blake:
        easeout 3.0 xalign 0.33
    
    pause 0.5
    play music bgm_whimsy
    p "\"Thank you for joining me, friend Blake! {b}I hope everyone learns a lot from this video{/b}!\""

    b "\"I mean... What is there to learn? It's a Visual Novel engine. {i}Those things are easy-mode, {size=12}as they say.{/size}{/i}\""

    pause 0.5
    play LoNoise bgs_wind
    show Penny surprise

    pause 1.0

    show Penny angry:
        easein 0.3 xalign 0.5
    pause 0.2
    play sound sfx_punch
    pause 0.1
    play sound2 sfx_shock
    show Blake surprise:
        easein 0.05 xalign 0.73
    
    p "Friend Blake, I am afraid you underestimate the effort and talent that goes into making Visual Novels!"
    stop music
    b "DID YOU JUST SMACK ME ON THE HEAD?!"
    call pondering
    pause 1.0
    jump kitty_choice

label violence:
    pause 1.0
    show Blake angry with dissolve
    b "You asked for it!"
    play sound2 sfx_punch
    pause 0.2
    scene black
    pause 1.0

    # This ends the game.

    return

label knowledge:
    pause 1.0
    show Blake surprise
    b "Okay, maybe I don't know enough about Visual Novels... Would you care to teach me, Penny?"
    pause 1.0
    show Penny happy with dissolve
    pause 1.0
    scene black
    pause 1.0

    return

menu kitty_choice:

    "You realize this means war.":
        jump violence
    
    "Maybe I was too hasty.":
        jump knowledge