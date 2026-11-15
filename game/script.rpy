# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

#TODO - add colours to character names
define u = Character("You", color="#ff80d9") #aka Lilico
define m = Character("Mary-Anne", color="#fa9d32")
define j = Character("Jessica", color="#9d2ef2")
define pa = Character("Prarie", color="#53c95e")
define ca = Character("Carrie", color="#8a9ad4")
define que = Character("???", color="#000000") #use when player doesn't know the name of the character yet


# The game starts here.

label start:
    play music "1knova-nostalgic-piano-114892.mp3" loop

    #first scene - in the city
    scene bg crossing

    #start narration
    "28th January. The first day of Gakuen High School."
    "The cicadas chirped cheerfully, the sunlight shone gently, gazing down at the line of black-clad office workers bustling like ants." 
    "For a moment, everything was perfectly orderly."
    "All around, monochromatic shoes marched mechanically through the cracked pavement. Tired office workers and depressed adults trudged about, groans spilling out of their lips."
    "{i}So this was what being an adult is like, huh?{/i}"
    "—Breaking the monotony of the endless march, a pair of fiery red runners flickered in and out of existence." 
    "Amidst the sea of pale leather loafers, black boots and sleek khaki heels, the vibrant runners stood out like a sore thumb."
    "...Well...like a sore...{i}toe{/i}."
    show lilico embarassed with hpunch
    u "{i}(Ugh, I'm sooo late! This is sooooo embarassing!){/i}"

    scene bg black screen
    #ADD AUDIO - Rushed footsteps and opening of door.
    "The sound of rushed footsteps pierced the silent hallways as you sprint through the school corridors, your heart pounding in your chest." 
    "You skid to a halt in front of the classroom door, your hand trembling as you reach for the handle."
    "The classroom door creaked open."

    scene bg openSeat
    u "{i}An open seat! Quick, it's mine!{/i}"
    "You quickly slid into the empty seat, your face flushed with embarrassment as you try to catch your breath."


    scene bg classroom
    "The other students in the classroom glanced up from their desks, some with curiosity, others with mild annoyance at the disruption."
    show maryanne normal
    que "{i}(Who is this??? I don't recognise her...A new student?? Joining this late in the year??){/i}"
    
    scene bg red sneakers
    que "{i}(Really??? Red sneakers with school uniform?? Wow, how could she be so stupid??){/i}"
    que "{i}(Well, whatever...){/i}" 
    que "{i}(...Maybe she knows how to play {b}basketball{/b}?){/i}"

    scene bg classroom
    show maryanne normal
    que "{i}(I really don't want to talk to her but, if we can't maintain 5 players minimum, we might be disbanded!){/i}"
    show maryanne stressed
    que "{i}(That {b}cannot{/b} happen...not after all we have done to keep it!){/i}"
    
    hide maryanne normal
    show lilico normal
    show maryanne normal at right with easeinright
    que "{i}(I guess I'll have to talk to her...){/i}"
    hide lilico normal

    show maryanne normal at center with easeinright
    m "Hey, are you new? What's your name? I'm Mary-Anne."
    hide maryanne normal
    show lilico awkward
    u "Oh! Um hey...yeah, I'm Lilico! It's nice to meet you, I can't tell you how nervous I was coming here today, I overslept and now well, I'm late hahaha...*awkward laugh*"
    show maryanne normal at right with easeinright
    show lilico normal at left with easeinleft
    m "Oh...well I mean its okay. I run a basketball club here, you'll probably be asked to join a club anyway."
    m "We really need a 5th player...after *sigh* she quit..."
    show lilico awkward
    u "Oookay?"
    m "Great, we're practicing at the gym during recess today."
    show maryanne normal flipped at right
    "Mary-Anne quickly turned around to leave"
    m "I'll see you there, Lilico."
    hide maryanne normal flipped with easeoutright
    show lilico normal at left
    show lilico awkward at center with vpunch
    u "{i}(...Huh!?!?! What the heck just happened!?!?){/i}"
    u "W-w-ait!! Mary-Anne!! I don't even know where the gym is!!!"
    
    scene bg gym door
    #audio - basketball court ambience
    "*At recess*"
    show lilico normal at left with easeinleft
    u "{i}(Phew...I finally found the gym!! I made it!!!){/i}"
    hide lilico normal
    "The gym was filled with the sound of bouncing basketballs and the squeak of sneakers on the polished wooden floor." 
    "The smell of sweat and rubber hung in the air, a testament to the hours of practice that had taken place here."
    show prairie normal at center with vpunch
    que "HEY!!! Are you the new member of the team, Lilico?"
    hide prairie normal
    show lilico embarassed at center
    u "H...hi? Yeah thats me!?"
    scene bg gym door
    show lilico embarassed at left
    show prairie normal at right
    que "Oh my gosh, I can't believe it! Someone {i}finally{/i} joined!"
    que "Everyone has been wayyy too focused on their exams, ugh!!! Study club is suuuuuuper popular right now, but its sooooo boring. Like seriously, nobody even wants to play basketball anymore!"
    que "—Anyways, come join in!"

    scene bg gym
    "It was a large gymnasium, with high ceilings and bright lights that illuminated the court. The bleachers were empty, but the echoes of past games and practices seemed to linger in the air."
    show prairie normal
    pa "Ooooookay, Let's introduce ourselves guys! Don't be shy...I'm Prairie, this is Lilico..."
    hide prairie normal
    show lilico normal
    u "Hi I'm Lilico, nice to meet you all!"
    hide lilico normal
    show carrie normal
    ca "I'm Carrie."
    hide carrie normal
    show jessica normal
    j "H-h-hi I'm Jessica..."
    hide jessica normal
    show maryanne normal
    m "...We've met before. I'm Mary-Anne, team captain." 
    m "I'm surprised you actually showed up, I thought you were going to chicken out."
    scene bg basketballCourt
    "Everyone looked apprehensively at Mary-Anne, and then at Prairie"
    show prairie scary at right
    show maryanne normal at left
    "Prairie glares at Mary-Anne, eyes burning holes into Mary-Anne's head."
    pa "Seriously? Why would you say that?{b} Do you want her to leave too{/b}?"
    show maryanne stressed at left with vpunch
    m "!!!"
    show lilico awkward
    u "{i}(Ooook...this is tense...){/i}"
    show maryanne normal
    show prairie normal
    m "Whatever, we dont have time for this right now."
    m "show us what you got, Lilico."
    
    scene bg gym
    "The team played a round of basketball that recess, the ball {b}bouncing back{/b} and forth between the players as they ran across the court with black sneakers squeaking against the polished wooden gym floor."
    "Suddenly, a pair of red sneakers darted across the court, catching everyone's attention. The ball was passed to Lilico, who skillfully dribbled it down the court, her movements fluid and precise."
    "The other players watched in awe as Lilico made a perfect shot, the ball swishing through the net with ease. The sound of the ball bouncing off the court echoed through the gymnasium, and the players erupted into cheers and applause."
    "All" "{i}Wow! That was amazing, Lilico! Good job! Damn, you're good! Holy cow, you're a natural! You're awesome!{/i}"
    show maryanne normal
    m "Wow Lilico, you're actually really good at this!"
    hide maryanne normal
    show maryanne embarrassed
    m "Well...it's not like I thought you weren't or anything"
    hide maryanne embarrassed
    show maryanne normal
    m "Anyways...I see you have a lot of potential. I think you'll fit in well. Welcome to the team."
    hide maryanne normal
    show lilico happy
    u "Yayyyy!!! Thank you guys so much!!! I'm sosososo happy to be here!!! I cant wait to play more games with you all!!!"

    scene bg cafeteria
    "*Later that day*"
    "You want to get to know your teammates, who cares about your classmates anyways."

    #menu 1 - who to get to know first? 2 options
    $ bring = []
    menu bringMenu1: #yes a menu can be a label 
        set bring 
        "Who do you want to get to know?"
        "Mary-Anne":
        #write dialogue for Mary-Anne here
            scene bg school hallway
            "As you're carrying a heavy stack of handouts and cradling your pencil case, you bump into Mary-Anne." 
            "The papers in your hands explode upward and scatter all across the floor! Welp, you were about to seek Mary-Anne in the locker room anyway! Perhaps this is the perfect chance?"
            scene bg scattered papers
            show maryanne embarrassed
            m "Hey! Watch where you're going!"
            hide maryanne
            "You scramble to collect the papers to your left, Mary-Anne helps you collect the ones that fell to your right before stacking them on top of your pile of hastily gathered papers."
            show lilico awkward
            u "Oh! Thanks..."
            show maryanne embarrassed
            m "I mean...It's not like I wanted to help you anyway...hmph..."
            scene bg school hallway
            "Despite her provocative tone, Mary-Anne accompanies you as you walk to your desk. Along the way, you make small talk with one another."
            show lilico awkward at right with easeinright
            show maryanne embarrassed at left with easeinleft
            u "So...How did you come to be the club president anyway?"
            m "Well...I mean I grew up watching my sister play...she really inspired me...but it's not like I'll ever tell her...or anything..."
            show maryanne normal at left
            show lilico normal at right
            m "..."
            m "You know, Lilico, I'm so glad you joined our club...It's honestly been hard the past term. I was really worried that we wouldn't be able to keep the club..."
            m "To be fair, Carrie has been carrying the promotion of the club. Everyone in the district knows about her skill."
            m "She's seriously insane. She earned herself the nickname 'the basketball star of district 5' for a reason."
            u "Hey, I'm glad I could help! You seem really stressed about it, no wonder why that's the first thing you said to me when we first met."
            m "Well...I didn't think you would agree to join the club in the first place...People tend to avoid me as I can be pretty cold sometimes."
            u " It was a little weird at first, but I don't think you're cold or anything...I'm glad you spoke to me first. I was super worried I wouldn't be able to make friends..."
            show maryanne embarrassed at left
            m "I MEAN- I was just asking! It's not like I wanted to know what you think about me...or anything..."
            u "I-"
            show maryanne stressed at left
            "Oh my gosh! Would you look at the time, I have to go! My sister's probably furious with how long I'm taking...see you tomorrow!"
            scene bg black screen
            "You feel like you know Mary-Anne a little better now."
            scene bg cafeteria
            #end of dialogue for Mary-Anne
            pass 
            jump bringMenu1 
        "Jessica": 
            #write dialogue for Jessica here
            scene bg jessica talk
            "You pull Jessica aside in an attempt to get to know her better. Although she is the quietest member of the team, you had a good feeling you'd warm up to her soon enough..."
            show lilico normal at left
            show jessica normal at right
            u "Jessica! Hi! I've been meaning to talk to you!"
            u "I'm kinda doing this thing where I'm trying to get to know everyone...Is that weird? I hope not..."
            j "N-n-no...Umm...It's okay...I hope we hit it off t-t-too..."
            scene bg jessica talk
            show lilico awkward
            u "({i}It seems Jessica doesn't feel fully comfortable talking to me one on one...I wonder why that is...){/i}"
            scene bg black screen
            "You hope Jessica can become more comfortable with you soon."
            scene bg cafeteria
            pass 
            jump bringMenu1
    jump bringMenu2
    #menu 2 - who to get to know next? 2 options
    
    scene bg cafeteria
    $ bring = []
    menu bringMenu2: #yes a menu can be a label 
        set bring 
        "The following day, you want to get to know the rest of the team members. Who do you want to get to know next?"
        "Carrie":
        #write dialogue for Carrie here
            scene bg gym door
            "It's practice day once again. As you walk to the gym, Carrie joins you."
            "You were just thinking about getting to know her more! Something about her demeanour intrigues you greatly..."
            show lilico normal
            u "Hey Carrie!"
            show carrie normal
            "Carrie nods nonchalantly"
            show lilico normal at left with easeinleft
            show carrie normal at right with easeinright
            u "You know, yesterday, I bumped into Mary-Anne and she mentioned how famous you are in the district."
            u "What did she say again? 'The basketball star of district 5' – if I remembered correctly!"
            u "I knew you were good but I didn't know you were thaaaat amazing! You are seriously cool."
            ca "Thanks. I won a few competitions here and there."
            show lilico awkward at left
            u "Haha yeah, must have been pretty hard, right?"
            "Carrie shrugs, head tilting toward the gym entrance as she pockets her hands into her hoodie."
            u "{i}(That was awkward...On that note, how did I even understand her?{/i}"
            u "{i}(It seems like she was speaking with vague gestures, almost as if she is talking telepathically somehow, although not really?){/i}"
            scene bg black screen with dissolve
            show lilico awkward at left
            show carrie normal at right
            "You and Carrie walk together into the gym for practice. The air around them seems thick with awkwardness..."
            "Or perhaps only you feel that way...Carrie seems just like her usual self."
            scene bg gym
            show lilico awkward at left
            show carrie normal at right
            u "{i}(I don't know what to say, how on earth can I break the ice with Carrie...? She's just too...icy){/i}"
            u "{i}(Maybe I'll ask her about her interests? Okay...I'll start with what she did on the weekend...{/i}"
            u "Carrie! What did you do on the weekend?"
            ca "I went to a convention..."
            u "Wait, you mean that cosplay expo? I went too! I begged my mum to take me there, she almost said no because school was about to start for me..."
            hide lilico normal
            show carrie excited at center with vpunch
            ca "No way...you like cosplay too!?"
            scene bg black screen
            "You and Carrie talk about cosplaying and she excitedly tells you about her hand-made cosplays. You are glad that Carrie has opened up to you"
            scene bg cafeteria
            #end of dialogue for Carrie
            pass 
            jump bringMenu2
        "Prairie":
            #write dialogue for prairie here
            scene bg locker room
            "After training, you return to your locker to grab your belongings."
            "As you finish folding your towel and placing it into your bag, you hear soft footsteps approaching the locker room. Who could it be?"
            "You turn around to see Prairie awkwardly hiding behind the walkway into the locker room."
            "Earlier, you wished that you could've continued talking before group practice began...It looked like your wish was about to be fulfilled!"
            show prairie normal
            pa "Hey Lilico...Can I talk to you about something?"
            u "Yeah sure...What's up?"
            show prarie awkward
            pa "W-w-w-ell, I can't..."
            scene bg locker room
            "Prairie turns away and averts her eyes, she's never shared this with anyone."
            show prarie awkward at right
            show lilico normal at left
            pa "Well...you know, I'm actually quite hard on myself when I play..."
            pa "I always feel like I'm lacking compared to others...even {b}her{/b}..."
            pa "Anyway...do you sometimes feel like that too? I had a good feeling about you, so I feel like I can open up about this..."
            pa "It's been weighing me for the longest time..."
            u "Yeah, I mean, it's normal to feel like that sometimes..."
            u "I'm sure you're just overthinking it. I saw you during practice earlier and honestly, you were amazing!"
            show prairie normal at left
            pa "Thank you so much Lilico. I knew I could trust you with this..."
            pa "{b}Don't tell anyone about our conversation today, okay?{/b}"
            scene bg cafeteria
            #end of dialogue for prairie
            pass 
            jump bringMenu2
    jump after
    label after:
        scene bg cafeteria
        "After getting to know your teammates, you could confidently say you feel much closer to all...most all of them."
        "That lunch, when the entire club gathers together, you ask about the upcoming competition."
        "At that moment, the members froze. A heavy silence hung around the room."
        "Shortly after, Mary-Anne whispers dejectedly."
        scene bg black screen with dissolve
        m "We've been on a losing streak..."
        m "If we don't win this competition...It's over for us"
        m "...And ever since our 5th member left, the club has been on the verge of disbandment..."
        m "This is our final chance."
        menu finalchoice:
            "What will you do?"
            "Comfort the members":
                #write dialogue for comfort ending here
                scene bg gym
                "...and with that, the rest of the team members immerse themselves into daily practice. They {b}bounced back{/b} and forth, dribbled left and right, and practised shooting day and night."
                "As the season approaches, the team of rag-tag basketballers transform into an united family, ready to tackle any opponents and balls thrown in their way"
                "{i}Metaphorically, of course, tackling your opponents is illegal in basketball...{/i}"
                "..."
                scene bg black screen
                "Finally, the timer ends and the results are announced..."
                "..."
                "The winners are.."
                scene bg trophy with hpunch
                "GAKUEN HIGH SCHOOL'S BASKETBALL TEAM!"
                show lilico happy
                u "AAAHHH— WE DID IT!!!! WE WON!!!!"
                scene black screen
                "We...did it..?!"
                "We....won....!"
                "..."
                "Carrie nods cooly, a barely noticeable corner of her mouth curving slightly upward. Next to her Pairie mutters under her breath."
                "Wow...we really won...even after all that effort?"
                "Overwhelmed with joy, the team celebrates the win with a tight group hug."
                "Little did they know, from the back of the audience stand, a resentful individual glared at them silently, eyes burning with hatred."
                que "You got lucky this time, Pairie..."
                #end of dialogue for comfort ending
                pass
            "Stay silent":
                #write dialogue for silent ending here
                scene bg black screen
                "You stay silent, joining the rest of the team in their moment of uncomfortable stillness."
                scene bg gym
                show jessica angry
                j " ...T-this was just like back then..."
                j "..."
                j "when she was still here..."
                u "{i}(She){/i}"
                show pairie angry
                pa "DON'T—"
                show prairie awkward
                pa "I- I mean. Don't think about her. She's already gone."
                j "...hah..."
                "Jessica sighs."
                "If you were just standing a little further away, you wouldn't have noticed it."
                scene bg black
                "The door slams open."
                "Prairie comes into the room, looking unlike her usual cheerful self."
                scene bg hallway
                "Later..."
                show prairie scary
                pa "Jessica, follow me."
                scene bg black screen
                "You silently trail the two as they shuffle down the hallway, their conversation drifting into your ears in jagged snippets."
                "At that moment, Prairie shoves Jessica into the wall."
                scene bg hallway
                show jessica angry
                j "Stop taking it out on me Pairie..."
                j "We all know why you're acting this way, you just need someone to take your anger out on right?"
                j "You did this to her too...right?" 
                j "Don't look shocked, I-i know what happened to HER."
                scene bg black screen
                "You hear Prairie's footsteps, she's running away...does that mean...it's true?"
                #end of dialogue for silent ending
                pass
        jump end


    label end:
        "The End"
        "Credits: Made by: Musarrat Mahbub - Lead coder,game formatting, and story editor Norah Shan - Lead story writer and coder, Flora Luu - Lead Artist and story writer"
        "And lastly..."
        "Thank you so much for playing! Hope you enjoyed our game :D"

    # This ends the game.
    return
