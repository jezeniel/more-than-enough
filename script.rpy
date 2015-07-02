# You can place the script of your game in this file.

# Declare images below this line, using the image statement.
# eg. image eileen happy = "eileen_happy.png"

# Declare characters used by this game.
define narrator = Character(None, kind=nvl, what_style="centered_text")
image white = "#fff"
image bg boke = "assets/boke.jpg"

label splashscreen:
    scene white
    with fade
    return

# The game starts here.
label start:
    play music "assets/madoka_wind.mp3" fadein 1.0
    scene bg boke
    with dissolve

    nvl show dissolve

    "I love you my dearest."
    "More than enough."
    "I may not be the perfect man."
    "And you can still consider me a {i}boy{/i}."

    nvl clear
    
    "But I am pretty damn sure."
    "That my feelings for you are true."
    "I am sorry for the promises I broke, "
    "For all the shortcomings I made."
    "And the disappointments I've done."

    nvl clear

    "Still, {w=1.0}you're here with me."
    "Being enveloped by your radiant love."
    "Giving me the warmest hug,"
    "And infinite happiness."

    nvl clear

    "I can still vividly remember."
    "The day we {cps=5}kissed.{/cps}"
    "The way we held hands."
    "As you look at my eyes and say..." 

    nvl clear

    '{vspace=150}"{i}I love you.{/i}"'

    nvl clear

    "That moment,{w=1.5} I felt and knew."
    "That I will be with {i}you{/i}."
    "That I will always love {i}you{/i}."
    "That I will always be besides {i}you{/i}."
    

    scene black 
    with dissolve

    centered "Until the day I die."

    stop music fadeout 0.5
    scene white
    with fade

    return
