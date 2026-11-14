# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define u = Character("You")
define l = Character("Lilico")
define m = Character("Mary-Anne")
define j = Character("Jessica")
define pa = Character("Prarie")
define ca = Character("Carrie")
define que = Character("???")


# The game starts here.

label start:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    #first scene - in the city
    scene bg cityPath

    #start narration
    "28th January. The first day of Gakuen High School."
    "The cicadas chirped cheerfully, the sunlight shone gently, gazing down at the line of black-clad office workers bustling like ants." 
    "For a moment, everything was perfectly orderly."
    "All around, monochromatic shoes marched mechanically through the cracked pavement. Tired office workers and depressed adults trudged about, groans spilling out of their lips."
    "{i}So this was what being an adult was like, huh?{/i}"
    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.
    show lilico run with hpunch
    "—Breaking the monotony of the endless march, a pair of fiery red runners flickered in and out of existence." 
    "Amidst the sea of pale leather loafers, black boots and sleek khaki heels, the vibrant runners stood out like a sore thumb."
    "...Well...like a sore...{i}toe{/i}."

    #next scene - in the homeroom
    scene bg hallway

    #start dialogue
    show lilico blush with hpunch
    u "{i}Ugh, I\’m sooo late! This is sooooo embarassing!{/i}"

    scene bg blackScreen
    #ADD AUDIO - Rushed footsteps and opening of door.
    "The sound of rushed footsteps pierced the silent hallways as you sprinted through the school corridors, your heart pounding in your chest." 
    "You skidded to a halt in front of the classroom door, your hand trembling as you reached for the handle."
    "The classroom door creaked open."

    scene bg openSeat
    u "{i}An open seat! Quick, it's mine!{/i}"
    "You quickly slid into the empty seat, your face flushed with embarrassment as you tried to catch your breath."


    scene bg Classroom
    "The other students in the classroom glanced up from their desks, some with curiosity, others with mild annoyance at the disruption."
    scene bg Classroom
    show maryanne normal
    que "{i}Who is this??? I don\’t recognise her… A new student?? Joining this late in the year?? {/i}"
    
    scene bg redSneakers
    que "{i}Really??? Red sneakers with school uniform?? Wow, how could she be so stupid??{/i}"
    que "{i}Well, whatever...{/i}" 
    que "{i}...Maybe she knows how to play {b}basketball{/b}?{/i}"

    scene bg Classroom
    show maryanne awkward
    que "{i}I really don\’t want to talk to her but, if we can\’t maintain 6 players minimum, we might be disbanded!{/i}"
    show maryanne normal
    que "{i}That {b}cannot{/b} happen… not after all we have done to keep it!{/i}"
    
    hide maryanne normal
    show lilico normal
    show maryanne awkward at left with easeinleft
    que "{i}I guess I\’ll have to talk to her…{/i}"
    hide lilico normal

    show maryanne normal at center with easeinleft
    m "Hey, are you new? What\’s your name? I\’m Marry-Anne."
    hide maryanne normal
    show lilico awkward
    u "Hey… yeah, I\’m Lilico! It's nice to meet you, I can\’t tell you how nervous I was coming here today, I overslept and now well, I\’m late hahaha...*awkward laugh*"
    show maryanne normal at left with easeinleft
    show lilico awkward at right with easeinright
    m "Oh… well I mean its okay. I run a basketball club here, you\’ll probably be asked to join a club anyway."
    m "We really need a 6th player… after *sigh* she quit…"
    u "Oookay?"
    m "Great, we're practicing at the gym during recess today."
    show maryanne normal flipped at left
    "Mary-Anne quickly turned around to leave"
    m "I\’ll see you there, Lilico."
    hide maryanne normal flipped with easeoutleft
    u "{i}...Huh!?!?! what the helly just happened!?!?{/i}"
    u "W-w-ait!! Mary-Anne!! I don\’t even know where the gym is!!!"
    
    scene bg gymEntrance
    #audio - basketball court ambience
    "*At recess*"
    show lilico normal at right with easeinright
    u "{i}Phew...I finally found the gym!! I made it!!!{/i}"
    hide lilico normal
    "The gym was filled with the sound of bouncing basketballs and the squeak of sneakers on the polished wooden floor." 
    "The smell of sweat and rubber hung in the air, a testament to the hours of practice that had taken place here."
    show prarie normal at center with vpunch
    que "HEY!!! Are you the new member of the team, Lilico?"
    show lilico blush at center
    u "H...hi? Yeah thats me!?"
    show lilico blush at right with easeinright
    show prarie normal at left with easeinleft
    que "Oh my gosh, I can\’t believe it! Someone {i}finally{/i} joined!"
    show prarie angry at left
    que "Everyone has been wayyy too focused on their exams, ugh!!! Study club is suuuuuuper popular right now, but its sooooo boring. Like seriously, nobody even wants to play basketball anymore!"
    show prarie normal at left
    show lilico normal at right
    que "—Anyways, come join in!"

    scene bg basketballCourt
    "It was a large gymnasium, with high ceilings and bright lights that illuminated the court. The bleachers were empty, but the echoes of past games and practices seemed to linger in the air."
    show prarie normal
    pa "Ooooookay, Let's introduce ourselves guys! Don\’t be shy...I\’m Prairie, this is Lilico…"
    show lilico normal
    u "Hi I\’m Lilico, nice to meet you all!"
    show carrie normal
    ca "I'm Carrie."
    show jessica normal
    j "H-h-hi I’m Jessica..."
    show maryanne normal
    m "...We've met before. I'm Mary-Anne, team captain." 
    m "I\'m surprised you actually showed up, I thought you were going to chicken out."
    scene bg basketballCourt
    "Everyone looked apprehensively at Mary-Anne, and then at Prairie"
    show prairie angry
    "Prairie glares at Mary-Anne, eyes burning holes into Mary-Anne's head."
    pa "Seriously? Why would you say that?{b} Do you want her to leave too{/b}?"
    show maryanne angry with vpunch
    m "!!!"
    show lilico awkward
    u "{i}Ooook...this is tense...{/i}"
    show maryanne normal
    m "Whatever, we dont have time for this right now."
    m "Show us what you got, Lilico."
    
    scene bg basketballCourt
    "The team played a round of basketball that recess, the ball {b}bouncing back{/b} and forth between the players as they ran across the court with black sneakers squeaking against the polished wooden gym floor."
    "Suddenly, a pair of red sneakers darted across the court, catching everyone's attention. The ball was passed to Lilico, who skillfully dribbled it down the court, her movements fluid and precise."
    "The other players watched in awe as Lilico made a perfect shot, the ball swishing through the net with ease. The sound of the ball bouncing off the court echoed through the gymnasium, and the players erupted into cheers and applause."
    "All" "{i}Wow! That was amazing, Lilico! Goog job! Damn, you\’re good! Holy cow, you\’re a natural! You\’re awesome!{/i}"
    show maryanne normal
    m "Great job, Lilico. I see you have a lot of potential. I think you\’ll fit in well. Welcome to the team."
    show lilico joyful
    u "YAYYYY!!! Thank you guys so much!!! I'm sosososo happy to be here!!! I cant wait to play more games with you all!!!"

    scene bg cafeteria
    "*Later that day*"
    "You want to get to know your teammates, who cares about your classmates anyways."

    #menu 1 - who to get to know first? 2 options
    $ bring = []
    menu bringMenu1: #yes a menu can be a label 
        set bring 
        "Who do you want to get to know first?"
        "Mary-Anne":
            #write dialogue for Mary-Anne here
            "dialogue" 
            #end of dialogue for Mary-Anne
            pass 
            jump bringMenu1 
        "Jessica": 
            #write dialogue for Jessica here
            "dialogue"
            #end of dialogue for Jessica
            pass 
            jump bringMenu1 
    jump bringMenu2
    #menu 2 - who to get to know next? 2 options
    $ bring = []
    menu bringMenu2: #yes a menu can be a label 
        set bring 
        "Who do you want to get to know next?"
        "Carrie":
            #write dialogue for Carrie here
            "dialogue" 
            #end of dialogue for Carrie
            pass 
            jump bringMenu2
        "Prairie": 
            #write dialogue for Prairie here
            "dialogue"
            #end of dialogue for Prairie
            pass 
            jump bringMenu2
    jump after
    
    label after:
        scene bg cafeteria
        "after getting to know your teammates bla bla bla"
        scene bg blackScreen with dissolve
        "mary anne stressy wessy :("
        menu finalchoice:
            "What will you do?"
            "Comfort the members":
                #write dialogue for comfort ending here
                "dialogue"
                #end of dialogue for comfort ending
                pass
            "Stay silent":
                #write dialogue for silent ending here
                "dialogue"
                #end of dialogue for silent ending
                pass
        jump end
    label end:
        "The End"
        "Credits: Thank you to (insert names and jobs)"
        "And lastly..."
        "Thank you so much for playing!"

    # This ends the game.
    return
