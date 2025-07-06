# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define e = Character("Eileen")
define p = Character("Penny")
define b = Character("Blake")

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

    p "Thank you for joining me, friend Blake! I hope everyone learns a lot from this video!"

    # This ends the game.

    return
