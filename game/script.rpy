# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define g = Character("Girl")
define m = Character("")
define e = Character("Me")
define w = Character("My wife")
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
    
    jump end
    
    label ignore:
    scene busstop at truecenter with dissolve
    
    "I should probably head home now"
    
    "Oh, Julie's party is tonight"
    
    "She's celebrating her 21st today"
    
    "I'll just grab drinks on my way there"
    
    # This ends the game.
    
    label end:
        
    show 2years with fade
    
    ""
    
    
    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene arguing  at truecenter
    with dissolve

    # These display lines of dialogue.

    e "Hey I’m going to the pub."
    w "You don’t spend enough time with me - you’re always out at bars!"
    e "My work depends on this! I need to go out to meet with potential customers."
    w "Just take one day off. You don’t need to go to the pub every night. We never spend any time together anymore!"
    e "Come with me then, you don’t have to sit indoors all the time!"

menu: 
    "Storm out in rage.":
        jump rage

    "Try to talk it out.":
        jump talk

label rage: 
    scene alcoholism_scene3  at truecenter
    with fade

    "You manage to run away for the night, but your wife deems your behavior \
    unreasonable and files for divorce. As a result, you spiral further and \
    further into depression and alcoholism."

    jump drunk_driving

label talk: 
    scene talking at truecenter
    with fade

    "You and your wife manage to work something out for the night, but the\
    distance between you grows, and you begin to turn increasingly to alcohol \
    for comfort."    

label drunk_driving: 
    scene drunk_driving at truecenter
    with fade

    "After a late night of drinking, I make some stupid decisions and get pulled\
    over for drunk driving."

menu: 
    "Tell the cop a sob story about your failing marriage in the hope that he lets\
    you off the hook.":
        jump off_hook

    "Accept the consequences and check yourself into rehab.":
        jump rehab

label off_hook:
    scene cry_in_car at truecenter
    with fade

    "Your sob story worked! The officer let you off the hook, but now your behavior \
    is more reckless than ever. "

    jump end2

label rehab: 
    scene court  at truecenter
    with fade

    "Rehab helped for a while, but you, like 90 percent of alcoholics, relapse. \
    This time, you’re not sure if you’ll ever be able to stop drinking. "

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
