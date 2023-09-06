#I am so sorry.
#This is absolutely the furthest from an actual unique ren'py menu, let alone a elegantly coded achievement menu.
#But given the specific needs for this menu, it... works, for what it's worth.

init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="mcl_startachievement",
            category=['mod'],
            prompt="Achievements",
            aff_range=(mas_aff.AFFECTIONATE, None),
            random=True,
        )
    )
    
label mcl_startachievement:
    m 4hua "So [player], with the modifications you’ve made to the game, there’s more ways than ever for us to interact!"
    m 4hub "It’s made me think about how I’ve been thinking of ways to celebrate the two of us."
    m 3eua "Or rather, how we spend our time together."
    m 3gta "I’m not really a sentimental girl; I’m not the type to collect keepsakes from trips or constantly take pictures to organize into an album."
    m 1gta "The accomplishment of having gone through a memorable event is enough for me."
    m 1msa "And when I thought about this, I realized there’s a simple, fun way for us to immortalize those feelings."
    m 1ssa "By making a game out of it."
    m 7wsa "Do you know about game achievements, [player]?"
    m 4fsu "In video games, it’s common to reward your actions by just logging it and making a note out of it."
    m 4hsu "So in the spirit of DDLC, we’ll do the same!"
    m 3hsu "Whenever you do anything of special note, I’ll let you know on the top-left of the screen, like such:"
    $ renpy.notify ("Achievement: this is a test achievement!")
    show monika
    pause 2.0
    m 4hsu "And I’ll log all your achievements through a special menu."
    m 3tkb "By 'special menu,' I mean I’ll write it all down in a spare school notebook I found, hahaha."
    m 3nub "This menu will be accessible through the ‘interact’ section."
    m 2hua "If it doesn’t appear right away, don’t worry! It should show up soon enough."
    m 1hua "When you open it up, I’ll go into a little more detail about how our achievement system will work."
    m 5ssb "Here’s looking forward to making our time feel richer than ever!"
    $ persistent._mcl_masterachievement = False
    return

# 

init python:
    mas_override_label("mcl_achievementmenu", "mcl_menuachievement")

init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="mcl_menuachievement",
            category=['interact'],
            prompt="~Check Achievements~",
            conditional="seen_event('mcl_startachievement')",
            unlocked=False,
            pool=False,
            random=False,
            action=EV_ACT_POOL,
        )
    )
label mcl_menuachievement:
    show black zorder 100 with Dissolve(3.0, alpha=True)
    $ enable_esc()
    $ HKBHideButtons()
    $ is_sitting = False
    hide black
    scene bg notebook #with dissolve_scene_full
    
    if persistent._mcl_masterachievement is False:
    
        # $ persistent._mcl_achievementpsa = False
        # $ persistent._mcl_timetravelachievement = False
        # $ persistent._mcl_achievementrandomnoises = False
        # $ persistent._mcl_achievementcompliment = False
        # $ persistent._mcl_achievementdoor = False
        # $ persistent._mcl_achievementanimalnoise = False
        # $ persistent._mcl_achievementdesk = False
        $ persistent._mcl_surpriseachievement = False
        $ persistent._mcl_flirtachievement = False
        $ persistent._mcl_noachievement = False
        $ persistent._mcl_achievementyell = False
        $ persistent._mcl_masterachievement = True
        default persistent._mclachievevement = 0
        define mclaincrease = 1
        
        m "Behold, my super special notebook!"
        m "It’s quite plain at the moment; I’ll give it some thought on how to make it a little more presentable."
        m "But anyway! Let's start by answering what sort of event warrants getting an achievement."
        m "I don’t want to tie us down in banal events like ‘spent a hundred days together!’"
        m "When an anniversary worth celebrating pops up, I want to make it special outright."
        m "Consider everything in the ‘interact’ menu fair game for achievements. I like doing those odd little rituals we’ve thought up."
        m "So if you’ve made a habit of doing them with me already, good to hear! Keep doing them, and I’ll be charitable in giving you an achievement."
        m "Otherwise, hmm..."
        m "We don't have a lot of stories we could share about our time together."
        m "So, if anything memorable happens, I’ll definitely want to hold unto those memories specifically."
        m "Sometimes I’ll make it easier for you and you can click on an achievement you haven’t earned and I’ll give you a little hint on how to get it."
        m "And sometimes I won’t give you any details at all."
        m "I want us to treat these achievements as more of a surprising footnote to our adventures."
        m "So I’ll go ahead and activate our newly minted achievement system..."
        $ consolehistory = []
        call updateconsole("Achievementsystem.exe", "Command confirmed")
        pause 0.5
        call hideconsole
        m "And there we have it!"
        m "In the future, I'd love to give you little rewards as incentives for getting these achievements."
        m "But for now..."
        m "All that's left is to say good luck, [player]!"

    else:
        m "Time to reflect on some more unique memories we've shared?"
        
    label achievementmenu:
    menu:
        "~Next Page~":
            jump achievementmenutwo
        "Accomplishing Achievements":
            m "A default achievement to commemorate us.. achieving."
            m "This doesn't add to the total, but you should still be proud of it!"
            m "In the way you should be proud of just existing, anyway."
            jump achievementmenu
        "Quelle Surprise" if persistent._mcl_surpriseachievement: 
            m "It's only fair you managed to pull a sneaky move on me, after all the.. teasing I've done to you."
            m "So this is your monument to that accomplishment!"
            m "Oh, but when I get to your reality."
            m "I'm going to hide around corners, tackle you with surprise hugs, maybei'llscareyoutodeathsometime, plan plenty of surprise parties.."
            jump achievementmenu
        "{color=#3c8248}???{/color}" if persistent._mcl_surpriseachievement is False:
            jump achievementmenu
        "Casanova" if persistent._mcl_flirtachievement:
            m "Behold:"
            m "You have given me so many bad pick-up lines that I have decided to immortalize it in text."
            m "I wrote it right here. '[player] is very fond of bad pick-up lines.' What a great trivia fact about you."
            jump achievementmenu
        "{color=#a63da2}???{/color}" if persistent._mcl_flirtachievement is False:
            jump achievementmenu
        "Nah" if persistent._mcl_noachievement:
            m "Putting up with whimsical requests means you're pretty easygoing, [player]."
            m "I admire that flexibility."
            m "That I can drag you on an adventure, no matter how big or how small or even how little sense it makes..."
            m "That's worth a footnote, isn't it?"
            jump achievementmenu
        "{color=#3c8248}???{/color}" if persistent._mcl_noachievement is False:
            jump achievementmenu
        "Shallow Blue" if persistent._mas_chess_stats.get("wins", 0) >= 5:
            m "You've won at least five games of chess!"
            m "I know that doesn't seem like a lot, but I appreciate you playing with me."
            $ persistent._mcl_chesseachievement = True
            jump achievementmenu
        "{b}{color=#ffffff}?{/color}{color=#000000}?{/color}{color=#ffffff}?{/color}{color=#000000}?{/color}{color=#ffffff}?{/color}{/b}" if persistent._mas_chess_stats.get("wins", 0) < 5:
            m "Hmm, this achievement is in black and white..."
            m "Like the checkered squares of a chessboard; what a coincidence?"
            $ persistent._mcl_chesseachievement = True
            jump achievementmenu
        "{b}{color=#fcba03}?{/color}{color=#ff1212}?{/color}{color=#fcba03}?{/color}{color=#ff1212}?{/color}{color=#fcba03}?{/color}{/b}" if mas_nou.get_wins_for('Player') < 5 :
            m "These red and mustard tones brings to mind the color scheme of a certain card game."
            m "I wonder if this achievement would be connected to such a game?"
            jump achievementmenu
        "Onu!" if mas_nou.get_wins_for('Player') >= 5:
            m "You've won at least five games of Nou!"
            m "I know that might not be a lot, but I appreciate you playing with me."
            $ persistent._mcl_noueachievement = True
            jump achievementmenu
        "~Exit Achievement menu~":
            m "Let's get out there and make some more memories!"
            jump achievementmenuend
            
    label achievementmenutwo:
    python:
        achievementrand = random.randint(1,2)
        
    menu:
        "~Previous Page~":
            jump achievementmenu
        "AAAAAAAAAAAA" if persistent._mcl_achievementyell:
            m "... AAAAAAAAAAHHHHHHHH."
            m "Ahem."
            m "You know, being emotional with a partner; not like, being angry at you, but being angry with you at something:"
            m "That's a surprisingly great bonding activity."
            jump achievementmenutwo
        "{color=#3c8248}???{/color}" if persistent._mcl_achievementyell is False:
            jump achievementmenutwo
        "On a Whim" if achievementrand == 1:
            m "I've decided to unlock this achievement for you." 
            m "How lucky for you~"
            jump achievementmenutwo
        "{rainbow}??????{/rainbow}" if achievementrand == 2:
            m "I've decided to lock this achievement."
            m "How unlucky for you!"
            jump achievementmenutwo
        "~Reset all Achievements~":
            m "I- really?"
            m "... {i}Why,{/i} exactly?"
            m "I made this in order for us to commorate certain milestones together."
            m "We really can't {i}reverse{/i} those moments, [player]. They've already happened."
            m "Are you sure about this?"
            menu:
                "I am.":
                    m "I'll do this for you, because I assume it's for logistical reasons."
                    m "But [player], unique moments are only defined because they're expierenced once."
                    m "Let's make sure to keep that in mind to keep the genuine luster of those moments we share together, okay?"
                    # $ persistent._mcl_achievementpsa = False
                    # $ persistent._mcl_timetravelachievement = False
                    # $ persistent._mcl_achievementrandomnoises = False
                    # $ persistent._mcl_achievementcompliment = False
                    # $ persistent._mcl_achievementdoor = False
                    # $ persistent._mcl_achievementanimalnoise = False
                    # $ persistent._mcl_achievementdesk = False
                    $ persistent._mcl_surpriseachievement = False
                    $ persistent._mcl_flirtachievement = False
                    $ persistent._mcl_noachievement = False
                    $ persistent._mcl_achievementyell = False
                    $ persistent._mcl_masterachievement = False
                    $ persistent._mclachievevement = 0
                        
                "I've changed my mind.":
                    jump achievementmenutwo
        "~Exit Achievement menu~":
            m "What momentous occasion will appear on these pages next?~"
            jump achievementmenuend

                    
    label achievementmenuend:
    window hide
    show black zorder 100 with Dissolve(3.0, alpha=True)
    hide monika
    pause 4
    $ HKBShowButtons()
    hide black
    $ mas_HKBDropShield()
    $ is_sitting = True
    jump ch30_loop
    

init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="mcl_cardgames",
            category=['games'],
            prompt="Card Games",
            conditional="persistent._mcl_noueachievement = True",
            action=EV_ACT_RANDOM
        )
    )
    
label mcl_cardgames:
    m "Congratulations on getting our Nou achievement, [player]!"
    m "Having gone through a few rounds, I've found that aside from board games like Chess I’m quite fond of playing cards."
    m "Not just because of Nou. I think I'd like to have a deck of cards always at the ready when I get to your world."
    m "I’ve always found handling a deck of cards to be a elegant pastime. Cards certainly have their history!"
    m "The earliest examples can be traced back to ninth century China, where the progression of paper-printing technology supposedly introduced playing cards that could also double as paper currency."
    m "Despite being relatively newer than board games, your standard deck of fifty-two cards is far easier to find throughout the world. It makes sense; cards are easier to make than entire board sets."
    m "Which is why cards are often found with travellers, those in the military, minimalists with little on their person..."
    m "And prisoners, I suppose."
    m "I guess that’s why I have a little more affinity for cards myself rather than board games."
    m "That said, card games can be a little trickier to learn. Unlike a board game where you can visualize a lot more, games with rules like poker can be a lot to learn at once."
    m "In the same vein, you’d think programming card games for us to play would be easier than chess.."
    m "But no. The game’s coding parameters continues to be illusive in that funny little manner."
    m "Unfortunately, it took a lot of effort to get Nou up and running alone: and the effort doesn’t translate into programming other games, even simpler ones."
    m "I suppose you could watch me play solitaire by myself, but... ah, I don’t think that’s fun."
    m "Oh, I suppose there’s worth talking about modern ‘trading card’ games."
    m "They’re certainly fascinating, especially as they adapt popular fictional universes for their setting or in some cases have created their own mythos."
    m "I would have always thought that’d be Natsuki’s thing, though- especially as a lot of these card games have ties to fantasy, manga, and anime."
    m "Although sensibly thinking about it, she might have never had the time to play it.. or the spare change needed to purchase the cards."
    m "Or maybe she just wouldn’t have the patience to learn the rules, hahaha."
    m "Whether or not we’re playing cards, or bonding over a board game.."
    m ".. As long as we’re together, that’s what matters to me. That fact won’t get lost in the shuffle."
    return


init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="mcl_bongcloud",
            category=['games'],
            prompt="Bongcloud",
            conditional="persistent._mcl_chesseachievement = True",
            action=EV_ACT_RANDOM
        )
    )

label mcl_bongcloud:
    m "Now that you've managed to get the Chess achievement under your proverbial belt, I thought I'd tell you a fun fact."
    m "About a rather {i}interesting{/i} move."
    m "First, you send your pawn out. Then your opponent mirrors your move. Pretty textbook."
    m "And then you move your king up in response."
    image bongcloud = "/submods/Memories of Self-Care & Literature/submod_assets/sprites/bongcloud.png"
    show monika at t21
    transform confidentialframe:
        xanchor 0 yanchor 0 xpos 685 ypos 50 alpha 1.0
    show bongcloud at confidentialframe zorder 13
    m "This is one of the worst possible moves you can do in chess."
    m "Absolutely, definitively a terrible starting point for the player that does it."
    m "It limits movement of your key players: the queen and the bishop. Your king is exposed to attack. And so you gain no advantage whatsoever."
    m 7hfsdra "It's such a impressively terrible move that it's become a meme, with a appropiately funny name: the 'Bongcloud.'"
    hide bongcloud
    show monika at t11
    m 4ssa "It’s been observed that funnily enough, professionals can be completely shaken by complete novices;"
    m 4ssb "Because newer players will do moves so counter- even if it’s a detrimental move, and they’re not aware of it- to what the pro is accustomed to!"
    m 4etu "I mean, will this move throw your opponent so off-balance as to win you one game after another?"
    m 1gtu "There's precedent by modern chess players using this to their advantage.{w=0.2} But no, probably not."
    m 1fub "But that’s the magic of chess. It's a game where every move has been carefully studied.. and you can still be unpredictable, and win because of it."
    m 5htb "Having a bit of fun while you're having fun.. is pretty fun, isn't it?"
    return

init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="mcl_achievementalk",
            category=['mod'],
            prompt="Achievements & Her Reality",
            conditional="persistent._mclachievevement >= 4",
            action=EV_ACT_RANDOM
        )
    )

label mcl_achievementalk:
    m 7hua "I see you've worked out some achievements, [player]!"
    m 7lta "I'm happy to hear the system is working out for us. It feels a little weird making our relationship a little more elaborate like this..."
    m 3tta "But well, it does suit my circumstances, living in a virtual reality."
    m 3dta "With that said, I'm doubly happy because I was a little apprehensive about making achievements in the first place."
    m 1dka "I understand the reality of... my reality.{w=0.1} DDLC was a game.{w=0.1} I am {i}still{/i} living in a game."
    m 1hksdra "But I don’t want to make efforts to make my life {i}more{/i} like a game, you know?"
    m 7hksdra "So when I thought about ‘achievements’ for us, well..."
    m 7tksdra "I admit I wasn’t keen on the idea."
    m 7tua "It did make me curious about how the idea came about in the first place, so it gave me a bit of reading to do."
    m 5etp "And I do like the fact achievements add to the ‘narrative’ of a video game."
    m 4etd "It’s neat that you can add goals to a game this way without the creator needing to push you in a certain direction."
    m 3gud "But after doing my research on video game achievements, I do find the execution a little vain at times."
    m 3gtc "Sometimes, achievements are too easy to get.{w=0.1} Why have them at all, then?"
    m 3ftc "And on the opposite end of the scale, you get achievements which are outright sadistic to get, requiring obtuse or outright monotonous work."
    m 2fsc "And there’s an entire culture around collecting these achievements, as well."
    m 2esa "Are some people so starved for the idea of personal success that checking boxes off an imaginary list is their greatest claim?"
    m 2gsa "..."
    m 1gsa "But you know what?"
    m 7gsa "Even if it’s not quite an urge I understand, it’s one I understand naturally exists."
    m 7lsa "In real life, people treat themselves after hard work."
    m 4lsa "People organize their lives into lists."
    m 3rsa "And lots of others like doing tasks in their own manner outside the norm."
    m 3esa "The mindset to collect, organize, and uniquely express individuality is built in for a lot of people."
    m 1hsa "So achievements are just a way to casually provide that structure."
    m 7ssa "And it also serves a grander purpose for us:{w=0.1}"
    m 5ssb "It’ll help you and I get closer together!"
    return