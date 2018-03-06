# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define g = Character("Girl")
define gf = Character("Girlfriend")
define m = Character("")
define e = Character("Me")
define w = Character("My wife")
define s = Character("Scott")
define p = Character("Phone")
image eileen movie = Movie(size=(1280, 720), channel="me", play="images/girl2.mkv")


# The game starts here.

    #return


label start:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene bar night at truecenter

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    # show eileen happy

    # These display lines of dialogue.

    m "When I first started drinking, it had a lot to do with being one of the crowd."

    m "I'm not relaxed until I have a drink."

    m "Alcohol takes away the shyness, paralysing self-consciousness."

    m "I always want to feel how all those other people look."

    scene birthday bar at truecenter with dissolve

    m "Today is Scott's twenty-first birthday. "

    m "As his best friend, of course I have to take him out to celebrate. "

    m "Scott is lucky though."

    m "He's funny and outgoing even when he doesn't drink."

    scene drink-glass-dark at truecenter with dissolve
    "Scott offers me another drink."
    s "This one's on me buddy!"

    scene onelater at truecenter with fade

    menu drink_menu:
            "I take the drink, chugging it down.":
                "It gives me a warm and happy feeling."
                jump girl

            "Sorry Scott, maybe I'll get another drink later.":
                jump girl


label girl:
    scene black with dissolve
    "Suddenly, A girl slides up to us. She looks directly at me and smiles."
    show eileen movie at truecenter with dissolve

    g "Hey. How come your cup is empty?"
    g "What do you say I buy the booze and you show me how to shake it."
    "Scott laughs and pats my shoulder."

    e " I guess one more drink can't hurt."
    hide eileen

    scene black with dissolve

    "Soon enough, Scott gets bored at the bar."
    s "Hey, let's go somewhere more interesting. I wanna dance tonight."
    s "Let's get out of here."

    scene walking to club


    m "We walk along the street, stumbling around as we go into the first club we see."
    scene walking to club with hpunch
    scene walking to club with hpunch
    "Ring Ring Ring. My phone is going off."
    scene walking to club with hpunch
    scene walking to club with hpunch

    "I see 4 missed calls. They're all from my girlfriend."

    menu call_menu:
        "Scott is already walking ahead, telling me to hurry up."

        "I pick up the phone.":
            jump gfriend_calls

        "I ignore the call.":
            jump ignore_gfriend_calls

label gfriend_calls:
    gf "I've been trying to call you forever. Where are you??"
    gf "I thought you were suppose to pick me up from class tonight."

    e "Shit I totally forgot about that."


    gf "You know what. Nevermind. I'm already on the bus home. Let's talk about this later."
    jump club

label ignore_gfriend_calls:

    "It's fine. I'll just talk to her tomorrow anyway."
    jump club



label club:
    "I'm feeling a slight headache. My heart is beating fast."
    "The club is just around the corner though, and Scott leads me in."

    scene club at truecenter with dissolve


    "Scott and I get more drinks."
    "We mix in some pills Scott brought too."
    " I'm feeling like nothing can go wrong tonight."

    m "I can do anything."

    menu wat_do:
        "I dance like no one's watching.":
            "I'm lighting up the dancefloor."
            jump after_wat_do

        "I take a couple more shots.":
            "It's really a wild night."
            jump after_wat_do

        "I kiss the girl next to me.":
            "She rolls her eyes at me as she dodges out the way."
            jump after_wat_do

label after_wat_do:

    "I dance the night away."
    scene club2 at truecenter with hpunch
    scene black with dissolve
    scene club2 at truecenter with dissolve

    "The lights are looking so bright."
    scene club1 at truecenter with Dissolve(1.)
    scene club2 at truecenter with Dissolve(1.)
    scene club at truecenter with Dissolve(1.)
    scene club1 at truecenter with Dissolve(1.)
    scene club2 at truecenter with Dissolve(1.)
    "I'm feeling so lightheaded."
    scene black with fade
    pause 3

    scene tracks at truecenter with fade

    "It's cold."

    "Have I been sleeping here all night?"

    "Scott is laying beside me. He's unconscious, face down on the concrete."

    menu wake_scott:
        "I try to push him awake.":
            jump cant_wake_scott

        "I yell at him till he wakes.":
            jump cant_wake_scott

label cant_wake_scott:
    "Scott doesn't move. His breathing is slow. When I touch his arm, his skin feels ice cold."

    menu wake_scott2:
        "I push him on his side.":
            "At least now, he won't choke on his vomit."
            jump cant_wake_scott2

        "I continue trying to shake him till he wakes.":
            jump cant_wake_scott2

label cant_wake_scott2:
    "Scott still doesn't wake up."

    "Suddenly I can hear the siren of police cars."
    scene tracks_red with Dissolve(0.5)
    scene tracks_blue with Dissolve(0.5)
    scene tracks_red with Dissolve(0.5)
    scene tracks with Dissolve(0.5)

    "Shit. I've still got drugs in my system. If the police get here, they'll find out I'm underage."

    menu wake_scott3:
        "I should make a run for it. If the cops see Scott, they'll be able to help him better than me.":
            "I'll call him a taxi too. Just in case."
            jump run_away

        "I stay with Scott. It's too dangerous to leave him alone.":
            jump stay_with_scott

label run_away:
    scene tracks_red with Dissolve(0.5)
    scene tracks_blue with Dissolve(0.5)
    scene tracks_red with Dissolve(0.5)
    scene tracks with Dissolve(0.5)

    "As I run into the nearest alleyway, I see the police stop in front of Scott."
    "I don't stay and look for long."
    "It's time for me to go home."
    "I'm sorry Scott."
    jump bus_stop

label stay_with_scott:
    scene tracks_red with Dissolve(0.5)
    scene tracks_blue with Dissolve(0.5)
    scene tracks_red with Dissolve(0.5)
    scene tracks with Dissolve(0.5)

    "The sirens fade in and then out."
    "Looks like they made a turn before this street."

    "I have no idea what to do with Scott."

    "Suddenly, Scott chokes in his sleep. He's vomited all over himself. His face looks blue."

    "I pick up my phone and call for an ambulance. Scott needs to go to the hospital before this gets too bad."

    scene tracks_red with Dissolve(0.5)
    scene tracks_blue with Dissolve(0.5)
    scene tracks_red with Dissolve(0.5)
    scene tracks with Dissolve(0.5)


    "When the paramedics arrive, I step out their way."
    "I should really go home now. It's almost sunrise. Scott will hopefully be fine after some rest."
label bus_stop:
    scene busstop at truecenter with dissolve

    "It's been a long day."

    "I'll figure everything out tomorrow."
    scene black with dissolve


    return
