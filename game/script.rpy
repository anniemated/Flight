# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define mc = Character("You")
define j = Character("Jude")


# The game starts here.

label start:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene black

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    # These display lines of dialogue.

    "I open the door."

    scene long

    j "So it's you. Long time no see! Wanna sit?"
    mc "..."
    j "Don't be shy, Yasha."

    scene close
    show speak3

    j "That's a lot better, isn't it?"

    # This ends the game.

    return
