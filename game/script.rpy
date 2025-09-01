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
    "But both of these sides seem to agree on one simple fact:"
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
    
    hide default
    show speak2
    j "So, what brings you to here to visit?"

    hide speak2
    show default

    menu reason:
        "... Why am I here?"

        "I missed you":
            hide default
            show blush_open
            j "Aw, how sweet!"
            hide blush_open
            show speak_sinis
            j "But you haven't visited me for at least a month before this."
            j "Did you miss me then? Or did you only start missing me now?"
            mc "..."
            hide speak_sinis
            show speak2
            j "I'm just pulling your leg, Yasha. Sorry. I know this is hard for you too."
            jump after_reason

        "I was worried about you":
            hide default
            show stare_dark
            j "..."
            hide stare_dark
            show melan
            j "Don't feel guilty about me, Yasha. I'll be fine."
            hide melan
            show speak3
            j "I may have these things growing out of my back, but I'm feeling better by the day!"
            j "Who knows, maybe I'll be the first person to actually get some use out of these \"wings\" of mine."
            menu illness:
                "How will you use them?":
                    hide speak3
                    show speak2
                    j "Maybe I'd cruise around the city. We've never been there before, right, Yasha?"
                    j "I thought after I got sick, they'd think me important enough to move me to an inner-city hospital."
                    hide speak2
                    show melan
                    j "But I got stuck here instead, yeah?"
                    hide melan
                    show anger
                    j "..."
                    hide anger
                    show default
                    j "You better visit me more!"
                    jump illness

                "I want to hear more about your illness":
                    hide speak3
                    show stare
                    j "Really?"
                    hide stare
                    show melan
                    j "Don't you already know all about it? You were always the smart one."
                    mc "... But the teachers always liked you best..."
                    hide melan
                    show blush_close
                    j "Wow, still remember that? You jealous?"
                    "It seems that when I prod at him enough, I start to remember things..."
                    mc "No, just reminiscing."
                    hide blush_close
                    show default
                    j "I get it. I do it all the time."
                    jump illness

                "Guilty?":
                    stop music
                    play sound "sting.mp3"
                    "{cps=7}DON'T LET HIM KNOW{/cps}"
                    play music bg
                    jump illness

                "Let's not talk about this anymore":
                    hide speak3
                    show sad
                    j "... I agree."
                    hide sad
                    show default
                    jump after_reason
        
        "I don't want you to leave or know":
            "Something stirs within you..."
            "That something says: ARE YOU TRYING TO GET US FOUND OUT??"
            jump reason
    
    label after_reason:
        hide default
        show melan
        j "..."
        j "To be honest, I don't really care why you're here. I'm glad you visited."
        j "But..."
        hide melan
        show stare_dark
        stop music
        j "{cps=9}Why are you acting like a different person?{/cps}"

        scene black
        hide stare_dark
        "TO BE CONTINUED"


    # This ends the game.

    return
