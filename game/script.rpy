# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define og = Character("Girl")
define g = Character("Girlfriend")
define gf = Character("Girlfriend")
define m = Character("Me")
define e = Character("Me")
define w = Character("My wife")
define s = Character("Scott")
define p = Character("Phone")
define d = Character("Dr. Manhattan")
image eileen movie = Movie(size=(1280, 720), channel="me", play="images/girl2.mkv")
label main_menu:
     if not persistent.set_afm_time:
         $ persistent.set_afm_time = True
         $ _preferences.afm_time = 5

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
    play music "restaurant.ogg" fadein 5.0
    "When I first started drinking, it had a lot to do with being one of the crowd."

    "I'm not relaxed until I have a drink."

    "Alcohol takes away the shyness, paralysing self-consciousness."

    "I always want to feel how all those other people look."

    scene birthday bar at truecenter with dissolve

    "Today is Scott's twenty-first birthday. "

    "As his best friend, of course I have to take him out to celebrate. "

    "Scott is lucky though."

    "He's funny and outgoing even when he doesn't drink."

    scene drink-glass-dark at truecenter with dissolve
    play sound "ice.mp3" fadein 2.0
    "Scott offers me another drink."
    s "This one's on me buddy!"
    stop sound fadeout 2.0

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

    og "Hey. How come your cup is empty?"
    og "What do you say I buy the booze and you show me how to shake it."
    play sound "laugh.ogg" fadein 2.0 fadeout 3.0
    "Scott laughs and pats my shoulder."

    e " I guess one more drink can't hurt."
    hide eileen

    scene bored_at_bar  at truecenter with dissolve

    "Soon enough, Scott gets bored at the bar."
    s "Hey, let's go somewhere more interesting. I wanna dance tonight."
    s "Let's get out of here."

    scene walking to club


    "We walk along the street, stumbling around as we go into the first club we see."
    scene walking to club  at truecenter with hpunch
    scene walking to club  at truecenter with hpunch
    play sound "ring.mp3" fadein 2.0
    "Ring Ring Ring. My phone is going off."
    scene walking to club  at truecenter with hpunch
    scene walking to club  at truecenter with hpunch

    "I see 4 missed calls. They're all from my girlfriend."

    menu call_menu:
        "Scott is already walking ahead, telling me to hurry up."

        "I pick up the phone.":
            stop sound
            jump gfriend_calls

        "I ignore the call.":
            stop sound
            jump ignore_gfriend_calls

label gfriend_calls:
    gf "I've been trying to call you forever. Where are you??"
    gf "I thought you were suppose to pick me up from class tonight."

    m "Shit I totally forgot about that."


    gf "You know what. Nevermind. I'm already on the bus home. Let's talk about this later."
    jump club

label ignore_gfriend_calls:

    "It's fine. I'll just talk to her tomorrow anyway."
    jump club



label club:
    "I'm feeling a slight headache. My heart is beating fast."
    "The club is just around the corner though, and Scott leads me in."

    play music "club.ogg" fadein 3.0
    scene club at truecenter with dissolve

    "Scott and I get more drinks."
    "We mix in some pills Scott brought too."
    " I'm feeling like nothing can go wrong tonight."

    "I can do anything."

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
    scene black  at truecenter with dissolve
    scene club2 at truecenter with dissolve

    "The lights are looking so bright."
    scene club1 at truecenter with Dissolve(.25)
    scene club2 at truecenter with Dissolve(.25)
    scene club at truecenter with Dissolve(.25)
    scene club1 at truecenter with Dissolve(.25)
    scene club2 at truecenter with Dissolve(.25)
    "I'm feeling so lightheaded."
    scene black with fade
    stop music fadeout 5.0
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

    $push_scott_on_side = False
    menu wake_scott2:
        "I push him on his side.":
            $push_scott_on_side = True
            "At least now, he won't choke on his vomit."
            jump cant_wake_scott2

        "I continue trying to shake him till he wakes.":
            jump cant_wake_scott2

label cant_wake_scott2:
    "Scott still doesn't wake up."

    play sound "<from 0 to 5>police.mp3" fadein 2.0
    "Suddenly I can hear the siren of police cars."
    scene tracks_red at truecenter with Dissolve(0.25)
    scene tracks_blue at truecenter with Dissolve(0.25)
    scene tracks_red at truecenter with Dissolve(0.5)
    scene tracks at truecenter with Dissolve(0.5)

    stop sound fadeout 4.0

    "Shit. I've still got drugs in my system. If the police get here, they'll find out I'm underage."

    menu wake_scott3:
        "I should make a run for it. If the cops see Scott, they'll be able to help him better than me.":
            "I'll call him a taxi too. Just in case."
            jump run_away

        "I stay with Scott. It's too dangerous to leave him alone.":
            if (push_scott_on_side == False):
                jump stay_with_scott
            else:
                jump scott_alcohol_poisoning

label run_away:
    scene tracks_red at truecenter with Dissolve(0.25)
    scene tracks_blue at truecenter with Dissolve(0.25)
    scene tracks_red at truecenter with Dissolve(0.5)
    scene tracks at truecenter with Dissolve(0.5)

    "As I run into the nearest alleyway, I see the police stop in front of Scott."
    "I don't stay and look for long."
    "It's time for me to go home."
    "I'm sorry Scott."
    jump bus_stop



label scott_alcohol_poisoning:
    scene tracks_red  at truecenter with Dissolve(0.5)
    scene tracks_blue  at truecenter with Dissolve(0.5)
    scene tracks_red at truecenter  with Dissolve(0.5)
    scene tracks  at truecenter with Dissolve(0.5)

    "The sirens fade in and then out."
    "Looks like they made a turn before this street."

    "I have no idea what to do with Scott."

    "Suddenly Scott starts shaking in his sleep."
    scene tracks at truecenter  with hpunch
    scene tracks at truecenter  with hpunch
    "Oh my god he's having a seizure."
    "I pick up my phone and call for an ambulance. Scott needs to go to the hospital before this gets too bad."

    scene tracks_red at truecenter  with Dissolve(0.5)
    scene tracks_blue at truecenter  with Dissolve(0.5)
    scene tracks_red at truecenter  with Dissolve(0.5)
    scene tracks  at truecenter with Dissolve(0.5)
    "When the paramedics arrive, I step out their way."
    "I should really go home now. It's almost sunrise. Scott will hopefully be fine after some rest."
    jump bus_stop


label stay_with_scott:
    play sound "police.mp3" fadein 2.0
    scene tracks_red  at truecenter with Dissolve(0.5)
    scene tracks_blue  at truecenter with Dissolve(0.5)
    scene tracks_red  at truecenter with Dissolve(0.5)
    scene tracks  at truecenter with Dissolve(0.5)
    stop sound fadeout 3.0

    "The sirens fade in and then out."
    "Looks like they made a turn before this street."

    "I have no idea what to do with Scott."

    "Suddenly, Scott chokes in his sleep. He's vomited all over himself. His face looks blue."
    "Shit, I should have turned him over."

    "I pick up my phone and call for an ambulance. Scott needs to go to the hospital before this gets too bad."

    scene tracks_red  at truecenter with Dissolve(0.5)
    scene tracks_blue  at truecenter with Dissolve(0.5)
    scene tracks_red  at truecenter with Dissolve(0.5)
    scene tracks  at truecenter with Dissolve(0.5)


    "When the paramedics arrive, I step out their way."
    "I should really go home now. It's almost sunrise. Scott will hopefully be fine after some rest."
label bus_stop:
    scene busstop at truecenter with dissolve

    "It's been a long day."

    "I'll figure everything out tomorrow."
    scene black with dissolve


label day2:

    scene morning at truecenter
    with dissolve

    "I wake up in the morning with a headache and I'm so thirsty.. I might have had too many drinks last night."
    "I should probably check up on my friend Scott and make sure that he is alright. Oh and I need to call my girlfriend too."

    menu hospital_or_girlfriend:
        "Check up on Scott":
            $ the_choice = 'scott'
            jump hospital

        "Call girlfriend":
            $ the_choice = 'girlfriend'
            m "Hey girlfriend, I was out with Scott last night."
            g "Yeah I heard about Scott, how is he doing now?"
            m "I was thinking of checking up on him later."
            g "Can you come over? I want to talk to you about you drinking every night."
            m "Okay I'm on my way."
            jump girlfriend_house

    label hospital:
        scene driving at truecenter
        with dissolve
        play sound "traffic.mp3" fadein 1.0
        "I drive down to the hospital to visit Scott"
        stop sound fadeout 1.5
        play music "ecg.ogg" fadein 5.0
        scene hospital at truecenter
        with dissolve
        m "Hey Scott are you feeling better now?"
        s "Hey man.. not really that was a pretty rough night."
        scene doctor at truecenter

        "The doctor enters the room."
        d "Hi Scott, I'm Dr. Manhattan. You had alcohol poisoning and we had to pump your stomach. You'll need to stay in the hospital for a few days while we monitor your condition."
        d "I'll put you on an intravenous drop to manage hydration, blood glucose, and vitamin levels"
        d "You are lucky that your friend called the amubulance, Scott. Binge drinking is dangerous, if alcohol poison goes untreated it and can lead to brain and liver damage, stroke, heart problems and your breating might stop completely"
        d "I'll leave you to your friend now. Take care."
        scene hospital at truecenter

        m "Oh shit dude did you hear that? You could have died and I totally saved your ass. You owe me now"
        stop music fadeout 6.0

        if the_choice == 'scott':
            play sound "<from 0 to 2.3>ring.mp3" fadein 1.5
            "I'm getting a call from my girlfriend"
            stop sound fadeout 2.0
            g "Where have you been? Why have I not heard from you since last night? We need to talk. Can you come over now?"

        if the_choice == 'girlfriend':
            "That was a really long day for me"
            jump day2_end

    label girlfriend_house:
        scene driving at truecenter
        with dissolve
        play sound "traffic.mp3" fadein 3.0
        if the_choice == 'girlfriend':
            "I hurry over to my girlfriends house"
        else:
            "I drive down to my girlfriends house"
        stop sound fadeout 4.0

        scene house at truecenter
        with dissolve
        "I hope she's not angry at me"
        scene arguing at truecenter
        g "You don’t spend enough time with me - you’re always out at bars!"
        m "I work so hard every day. I need to let off some steam after work!"
        g "Just take one day off. You don’t need to go to the pub every night. We never spend any time together anymore!"
        m "Come with me then, you don’t have to sit indoors all the time!"

        menu:
            "Storm out in rage.":
                $ arg_choice = 'rage'
                play sound "slamdoor.ogg" fadein 1.0
                jump end_gf

            "Try to talk it out.":
                $ arg_choice = 'talk'
                jump end_gf

        label end_gf:
            if the_choice == 'girlfriend':
                "I almost forgot about Scott in the heat of the argument. I better go check on him."
                jump hospital
            else:
                "That was a really long day for me"

        label day2_end:
            if arg_choice == 'talk':
                jump talk
            else:
                jump rage

        label rage:
            play music "crickets.ogg" fadein 5.0
            scene night  at truecenter
            with fade

            "You managed to get out of the argument with your girlfriend, but your she deems your behavior \
            unreasonable and breaks up with you. As a result, you spiral further and \
            further into depression and alcoholism."

            jump end2

        label talk:
            play music "crickets.ogg" fadein 5.0
            scene night at truecenter
            with fade

            "You and your girlfriend manage to work something out for now, but the\
            distance between you grows, and you begin to turn increasingly to alcohol \
            for comfort."
label end2:
    scene black with fade

    ""
    stop music fadeout 4.0
    scene arguing at truecenter with dissolve

    g "Are you drinking again?"
    g "I thought I told you that you need to quit already."
    m "I know but-"
    g "I'm really serious here. You and I both know that this is destroying you."
    g "Just the other day you got in trouble again at work because you were drinking again."
    g "What are you going to do?"
    m "I couldn't help myself. I was- I was just shaking so hard, my heart was going crazy and I couldn't take it anymore-"
    m "..."
    m "...I'm sorry."

    scene girlfriend_crying at truecenter with fade

    "She sighs and turns away."
    g "You don't have to be."
    g "I'm sorry too, I think I'm just tired."
    g "I'm going to go rest for a bit."
    "Before I could get another word in, she leaves and shuts the door behind her."

    scene morning at truecenter with dissolve
    "Now not only are my own friends avoiding me because of all my drinking lately, but my own girlfriend has been really exhausted from putting up with me all the time."
    "I can see where she's coming from - I know I’m drinking first thing in the morning every morning just to face the day."
    "I know she's right, but the pressure is overwhelming."
    "I have to go to work now, but I’m sweating and shaking. My head is spinning and I can’t focus."
    "I need to stop drinking, but every time I stop, this happens."
    "There’s no way I could get through today like this – I have to drink now if I want to make it through the day at work."

    menu:
        "What should I do?"

        "Take a drink.":
            jump drinkyes

        "Don't take a drink.":
            jump drinkno

label drinkyes:

    scene warehouse at truecenter
    with fade

    "I stopped shaking after I took a drink."
    "I felt so much better already. Like I could take on the world."
    "But while I was at work, I fumbled and caused a huge problem at work."
    "My boss yelled at me for being drunk and I got fired. I don’t know how I’m going to pay rent like this."
    "I drank so much that night I blacked out for who knows how long."

    jump final


label drinkno:

    scene warehouse at truecenter
    with fade

    "I beat back my need to drink. I know I'm stronger than this."
    "This is just what I would have to do to start combating my addiction."
    "Despite the heart palpitations and blurry vision, I mustered up my strength and went into work."
    "But while I was at work, I was shaking so that I fumbled and caused a huge problem."
    "This was the third time this happened this week."
    "My boss yelled at me and I got fired. I don’t know how I’m going to pay rent like this."
    "I drank so much that night I blacked out for who knows how long."

    jump final

label final:

    scene morning at truecenter
    with fade

    "Another dreary morning."
    "Without work, I don't even know what to do anymore with my life."
    m "I’m so miserable I just want to end it all."
    m "I don’t care how, I just want it to stop."
    "With nothing better to do, I spend the entire day drinking."

    scene morning at truecenter
    with fade
    play sound "heartbeat.ogg" fadein 3.0

    "My heart palpitations are stronger than ever this morning..."
    scene morning at truecenter with hpunch
    stop sound fadeout 3.0
    "Shivering furiously, I climb out of bed and dig through my refrigerator for something to eat."
    "Sitting on my bed, I spend the entire day drinking again."

    scene morning at truecenter
    with fade

    "I have a horrible hangover this morning."
    scene morning at truecenter with hpunch
    "Despite all that, I'm shivering so hard I can't focus on anything at all."
    "I spend the entire day drinking once again."

    scene phonecall at truecenter
    with fade

label final_call:
    play sound "<from 0 to 2.3>ring.mp3" fadein 2.0
    "Ring! Riiing!"
    stop sound fadeout 2.0
    "A phone call? In the middle of the night?"
    "I'm tempted to ignore it, but I immediately notice the name on the screen - it's the doctor. I saved the number from the last time Scott was hospitalized."
    m "Doctor? Is everything alright?"
    d "Apologies for calling so late at night. It's about your friend - Scott."
    "I immediately feel a cold rush through my veins. What's happened?"
    d "I'm so sorry, but he's been in a terrible car accident. Both he and the other driver were drunk."
    d "We don't have contact information for any of his relatives, only you."
    d "We thought you would like to know. we think you should see him."
    "Before he could even finish talking, I immediately jump out of bed and get in my car to rush to the hospital."

    play sound "traffic.mp3" fadein 3.0
    scene waitingroom at truecenter
    with fade
    stop sound fadeout 3.0

    "I wait outside for several hours while they perform the necessary surgery on him."
    "I had never felt so worried in my life."
    "After a while, the doctors come out and inform me of his status."
    "I'm relieved that he only suffered a broken leg and a minor head injury. I know it could have been much worse."

    play music "ecg.ogg" fadein 4.0
    scene hospital at truecenter
    with fade
    "I go in to see him. He greets me with a crooked smile."
    s "Sorry you had to come in and see me like this again."
    s "I'm feeling much better now though. I'm so glad I'm still alive."
    s "Guess I really should do something about that drinking problem, huh?"
    m "I'm glad too, bro. And I think we both need some help in that department."
    "He nodded."
    "We both knew what we needed to do. We needed help."
    stop music fadeout 4.0


    scene hands at truecenter
    with fade

    "When Scott got out of the hospital, we both started looking into getting help together."
    "My girlfriend and family were incredibly supportive. They started looking into all sorts of resources for our sake."
    "The two of us eventually got help at our local Drug and Alcohol Team unit."
    "They understood exactly what I was going through."
    "The doctor helped talk Scott through methods for avoiding binge drinking."
    "As for me, they had me spend 10 days in the hospital to detox me."
    "During that time, I struggled each day to make it through the day with all the heart palpitations and shivering that come with withdrawal."
    "The doctor explained that I was simply one of those people that was “allergic” to alcohol, that for me, alcohol is poison, and that I will never be able to control alcohol as long as I live."
    "I understand now that I was fighting a losing battle this entire time."
    "I was just not like most people when it comes to alcohol, and as long as I understood and worked with that, there was hope that I could move on."
    "When I went home again, it was tough, but I started putting the doctor's advice to work to combat my addiction."
    "Day by day, I could feel myself getting a little stronger. I was more like my old self."
    "I think Scott, my girlfriend, and my family could all see that as well."
    "From here on out, I have the support I need to start rebuilding my life."

    # This ends the game.

    scene theend at truecenter
    with fade

    ""
    pause 10


    return