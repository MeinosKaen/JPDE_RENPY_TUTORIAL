# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define e = Character("Eileen")
define p = Character("Penny")

# The game starts here.

label start:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene vale_day

    show Penny happy:
        zoom 0.5 xalign 0.5 yalign 1.0

    p "Salutations! My name is Penny, and this is the JPDE Ren'py Tutorial series!"

    scene vale_night

    show Penny blush

    p "We're going to learn how to make games! Once you add a story, pictures, and music, you can release it to the world!"

    # This ends the game.

    return
