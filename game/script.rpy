# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define g = Character("Girl")
define m = Character("You")
define e = Character("Me")
define w = Character("My wife")
define s = Character("Scott")
define d = Character("Dr. Manhattan")
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

    m "I'm not relaxed until I had a drink."
    
    m "Alcohol takes  away the shyness, paralysing self-consciousness"
    
    
    scene drink glass dark at truecenter with dissolve
    
    m "I want to feel how all those other people look"
    
    scene onelater at truecenter with fade
    
    menu drink_menu:
        "I take another drink":
            " It gives me a warm and happy new feeling."
            jump club
            
        "Maybe I'll get another drink later":
            jump girl
            
    
    label girl:
    scene black with dissolve
    "A girl slides up to me"
    show eileen movie at truecenter with dissolve

    g "Hey. How come you're not drinking?"
    g "What do you say I buy the booze and you show me how to shake it."
    hide eileen
    
    label club:
        
    scene club at truecenter with dissolve
    
    m "I feel like I can do anything."
    
    m "There's nothing holding me back anymore."
    
    menu wat_do:
        "I dance like no one's watching":
            jump after_wat_do
        
        "I yell down the streets":
            jump after_wat_do
        
        "I kiss the girl next to me":
            jump after_wat_do
            
    label after_wat_do:
    
    scene tracks at truecenter with fade

    "It's cold"
    
    "Have I been sleeping here all night?"
    
    "Ring ring ring. My phone is ringing."
    
    "I see 4 missed calls. They're all from my girlfriend."
    
    menu call_menu:
        "I'm tired and groggy"
        
        "I pick up the phone":
            jump calls
        
        "I ignore the calls":
            jump ignore
    
    label calls:
    "Hey, why are you calling me so early? I'm tired. You don't need to call me every second of the day."
    "I hear a snort in the phone"
    "*she hangs up*"
    "Why is she always like this?"
    
    jump day2
    
    label ignore:
    scene busstop at truecenter with dissolve
    
    "I should probably head home now"
    
    "Oh, Julie's party is tonight"
    
    "She's celebrating her 21st today"
    
    "I'll just grab drinks on my way there"
    
    # This ends the game.
    
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
        "I drive down to the hospital to visit Scott"
        
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
        
        if the_choice == 'scott':
            "I'm getting a call from my girlfriend"
            g "Where have you been? Why have I not heard from you since last night? We need to talk. Can you come over now?"
        
        if the_choice == 'girlfriend':
            "That was a really long day for me"
            jump day2_end
        
    label girlfriend_house:
        scene driving at truecenter
        with dissolve
        if the_choice == 'girlfriend':
            "I hurry over to my girlfriends house"
        else:
            "I drive down to my girlfriends house"
            
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
            scene night  at truecenter
            with fade

            "You managed to get out of the argument with your girlfriend, but your she deems your behavior \
            unreasonable and breaks up with you. As a result, you spiral further and \
            further into depression and alcoholism."

            jump end2

        label talk: 
            scene night at truecenter
            with fade

            "You and your girlfriend manage to work something out for now, but the\
            distance between you grows, and you begin to turn increasingly to alcohol \
            for comfort."
label end2:
    scene black with fade
    
    ""

   # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene morning at truecenter with dissolve

    "Another morning."
    "I can’t bring myself to get out of bed and meet a friend before heading to work."
    "It’s subtle, but by now, many of my friends have started avoiding me. Giving excuses for why we can’t meet up, or even suggesting that I should stop drinking."
    "I can see where they’re coming from - I know I’m drinking first thing in the morning every morning just to face the day."
    "I know they're right, but the pressure is overwhelming."
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
    "However, I fumbled and caused a huge problem at work."
    "My boss yelled at me for being drunk and I got fired. I don’t know how I’m going to pay rent like this."
    "I drank so much that night I blacked out for who knows how long."
    
    jump final
    
    
label drinkno:
    
    scene warehouse at truecenter
    with fade
    
    "I beat back my need to drink, but I was shaking so hard at work that I fumbled and caused a huge problem."
    "This was the third time this happened this week."
    "My boss yelled at me and I got fired. I don’t know how I’m going to pay rent like this."
    "I drank so much that night I blacked out for who knows how long."
    
    jump final
    
label final:
    
    scene homeless at truecenter
    with fade
    
    "I haven’t been able to find another job, and lost my apartment."
    "Without my wife or a place to live, I’m desperate to do something."
    "I’m so miserable I just want to end it all."
    "I don’t care how, I just want it to stop."
    
    scene hands at truecenter
    with fade
    
    "I forced myself to ask for help at my local Drug and Alcohol Team unit."
    
    "They were incredibly supportive and understood exactly what I was going through."
    "They had me spend 10 days in the hospital to detox me."
    "The doctor explained that I was simply one of those people that was “allergic” to alcohol, that for me, alcohol is poison, and that I will never be able to control alcohol as long as I live."
    "I understand now that I was fighting a losing battle this entire time."
    "I was just not like most people when it comes to alcohol, and as long as I understood and worked with that, there was hope that I could move on."
    "From here on out, I have the support I need to start rebuilding my life."

    # This ends the game.
    
    scene theend at truecenter
    with fade
    
    ""
    pause 10


    return
