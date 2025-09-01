# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define mc = Character("You")
default name = "???"
define j = Character("[name]")


# The game starts here.

label start:

    scene black
    play music bg

    "It’s strange…"
    "I came all this way to the hospital, but I really, really…"
    "Don’t want to open this door."
    "Something inside me is screaming at me to not open it, no matter what."
    "Paradoxically, I feel a kind of tenderness thinking about what’s behind the door as well."
    "But both of these voices seem to agree on one simple fact:"
    stop music
    play sound "sting.mp3"
    "{cps=7}DON’T LET HIM LEAVE\nDON'T LET HIM KNOW{/cps}"

    play music bg
    play sound "creak.mp3"
    scene long
    with fade

    j "So it's you."
    mc "... Jude."
    $ name = "Jude"
    j "Long time no see! I’m surprised you still remember my name."

    "I am too. The name had slipped from my lips as if it had always been there."
    "Looking at the person sitting in front of me, I feel a kind of sadness."
    "He looks thin and fragile, like the shadow of a person rather than an actual living being."
    "His eyes, sunken-in as they are, reflect no light."
    "And of course, those wings…"

    j "Don't be shy, Yasha. C’mon, sit down."
    "So that’s my name. I guess I’ll sit."


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
