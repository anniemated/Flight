# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define mc = Character("You")
define j = Character("Jude")


# The game starts here.

label start:

    scene black
    play music menu

    "I open the door."

    play sound "creak.mp3"
    scene long
    with fade

    j "So it's you. Long time no see! Wanna sit?"
    mc "..."
    j "Don't be shy, Yasha."

    play sound "<from 0 to 2.5>steps.mp3"
    scene close
    show speak3
    with fade

    j "That's a lot better, isn't it?"
    
    hide speak3
    show default

    mc "It is."

    # This ends the game.

    return
