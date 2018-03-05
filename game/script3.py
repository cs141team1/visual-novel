

label scene3start:
    scene black with fade
    
    ""

   # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene girlfriend crying at truecenter with dissolve

    w "Are you drinking again?"
    w "I thought I told you that you need to quit already."
    m "I know but-"
    w "I'm really serious here. You and I both know that this is destroying you."
    w "Just the other day you got in trouble again at work because you were drinking again."
    w "What are you going to do?"
    m "I couldn't help myself. I was- I was just shaking so hard, my heart was going crazy and I couldn't take it anymore-"
    m "..."
    m "...I'm sorry."
    "She sighs and turns away."
    w "You don't have to be."
    w "I'm sorry too, I think I'm just tired."
    w "I'm going to go rest for a bit."
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

    "My heart palpitations are stronger than ever this morning..."
    "Shivering furiously, I climb out of bed and dig through my refrigerator for something to eat."
    "Sitting on my bed, I spend the entire day drinking once again."

    scene morning at truecenter
    with fade

    "I have a horrible hangover this morning"

    scene morning at truecenter
    with fade

    "Ring! Riiing!"
    "I'm woken up in the middle of the night by a phone call."

    
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
