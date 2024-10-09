
define j = Character("Jenny")
define c = Character("Clarence")
define a = Character("Alice")
define dn="music/dn.mp3"
define wavesound="music/ocean.mp3"
define sd="music/sd.mp3"
define dz="music/dz.mp3"
define bs="music/bs.mp3"

define x = 0
label start:
    play sound dn
    scene imager
    with fade

    show greengirl at left
    with dissolve
    show redgirl
    show redboy at right
    menu:
        "Choose your character:"
        "{alpha=0.5}Choice 1: Jenny":
            $ x = 1
        "{alpha=0.5}Choice 2: Alice":
            $ x = 2
        "{alpha=0.5}Choice 3: Clarence":
            $ x = 3
    hide greengirl
    hide redgirl
    hide redboy

    "Hi!"
    if x==1:
        show greengirl
        with dissolve
        "{size=45}{b}You chose Jenny."
        j "I am Jenny, I am expeled from China.."
        j "Where can I go..."
        menu:
            "Choose the place you want to go first:{a=jump:skip}if you want to skip the story, click this"
            "Taiwan":
                $ y=1
            "Chenla":
                $ y=2
            "Champa":
                $ y=3
        if y==1:
            scene taiwan
            with fade
            j "Welcome to Taiwan."
            scene birds
            with fade
            j "The scenery here seems pleasant, lots of birds assembled together! I love to have contacts with animals!"
            menu:
                "Do you want to stay in Taiwan island?"
                "Yes":
                    $ z=1
                "No":
                    $ z=2
            if z==1:
                scene taiwan
                with fade
                hide greengirl
                with dissolve
                show crabs1
                with dissolve
                j "Also, there are crabs moving on the island..."
                hide crabs1
                with dissolve
                show crabs
                with dissolve
                "Wait, what is that, crabs cooked throughly!?"
                hide crabs
                with dissolve
                show greengirl
                with dissolve
                j "That's magic, I got crabs for my lunch!"
                "A big wave came from behind."
                stop sound
                play sound wavesound
                hide greengirl
                with dissolve
                show mermaid
                with dissolve
                "mermaid""Hi, girl. I want you to be my servant, follow me."
                hide mermaid
                with dissolve
                stop sound
                j "She wants to catch me! Run!"
                play sound sd
                show greengirl
                with dissolve
                "I am going to leave this place, it's too dangerous!"
            else:
                ""
        elif y==2:
            scene zhenla
            with fade
            hide greengirl
            with dissolve
            j "Welcome to Chenla."
            scene zhenla1
            with fade
            j "The scenery here seems pleasant, there are lots of ancient architectures and culture relics!"
            j "I would like to live here! "
            menu:
                "Do you want to stay in Chenla?"
                "Yes":
                    $ z=1
                "No":
                    $ z=2
            if z==1:
                scene maigua
                with fade
                hide greengirl
                with dissolve
                j "I am hungry... wanna get some food for lunch."
                j "Oh! There.. someone is setting up a stall!"
                "I want to exchange some daily supplies and solid foods with them."
                menu:
                    "Should I go?"
                    "You decided to trade with them.":
                        $n=1
                    "No, they don't look like good people, I want to leave Chenla.":
                        $n=2
                if n==1:
                    "The man who put the stall""You looks like..."
                    "The man who put the stall""Guys, catch her! She's the one disobeyed the China's law!"
                    show greengirl
                    with dissolve
                    stop sound
                    play sound sd
                    j "I should leave here! Run!"
                else:
                    ""

            else:
                ""

        else:
            scene chanpa
            with fade
            hide greengirl
            with dissolve
            j "Welcome to Chanpa."
            j "It seems wonderful here, with splendid architecture and clear sky!"
            menu:
                "Do you want to stay here?"
                "Yes, this place matched my imagination of Holy Land!":
                    $g=1
                "No.":
                    $g=2
            if g==1:
                j "I traveled for a long time..."
                j "My stomach is so empty, I am hungry. Where can I get something for lunch?"
                "Lots of people are doing something there, lets go and ask them if there's any food!"
                scene zongjiaohuodong
                with fade
                "What is that?!"
                "Are they sacrificing people?"
                show greengirl
                with dissolve
                stop sound
                play sound sd
                "The man stand on the sacrificial altar""I am the king!"
                "The man stand on the sacrificial altar""If you want to stay here, you have to listen to me, or you will be killed."
                j "I must go, it's too scary."
                ""
            else:
                ""
    elif x==2:
            show redgirl
            with dissolve
            "{size=45}{b}You chose Alice."
            a "I am Alice, I am expeled from China.."
            a "Where can I go..."
            menu:
                "Choose the place you want to go first:{a=jump:skip}if you want to skip the story, click this"
                "Taiwan":
                    $ y=1
                "Chenla":
                    $ y=2
                "Champa":
                    $ y=3
            if y==1:
                scene taiwan
                with fade
                a "Welcome to Taiwan."
                scene birds
                with fade
                a "The scenery here seems pleasant, lots of birds assembled together! I love to have contacts with animals!"
                menu:
                    "Do you want to stay in Taiwan island?"
                    "Yes":
                        $ z=1
                    "No":
                        $ z=2
                if z==1:
                    scene taiwan
                    with fade
                    hide redgirl
                    with dissolve
                    show crabs1
                    with dissolve
                    a "Also, there are crabs moving on the island..."
                    hide crabs1
                    with dissolve
                    show crabs
                    with dissolve
                    "Wait, what is that, crabs cooked throughly!?"
                    hide crabs
                    with dissolve
                    show redgirl
                    with dissolve
                    a "That's magic, I got crabs for my lunch!"
                    "A big wave came from behind."
                    hide redgirl
                    with dissolve
                    show mermaid
                    with dissolve
                    "mermaid""Hi, girl. I want you to be my servant, follow me."
                    hide mermaid
                    with dissolve
                    stop sound
                    a "She wants to catch me! Run!"
                    play sound sd
                    show redgirl
                    with dissolve
                    "I am going to leave this place, it's too dangerous!"
                else:
                    ""
            elif y==2:
                scene zhenla
                with fade
                hide redgirl
                with dissolve
                a "Welcome to Chenla."
                scene zhenla1
                with fade
                a "The scenery here seems pleasant, there are lots of ancient architectures and culture relics!"
                a "I would like to live here! "
                menu:
                    "Do you want to stay in Chenla?"
                    "Yes":
                        $ z=1
                    "No":
                        $ z=2
                if z==1:
                    scene maigua
                    with fade
                    hide redgirl
                    with dissolve
                    a "I am hungry... wanna get some food for lunch."
                    a "Oh! There.. someone is setting up a stall!"
                    "I want to exchange some daily supplies and solid foods with them."
                    menu:
                        "Should I go?"
                        "You decided to trade with them.":
                            $n=1
                        "No, they don't look like good people, I want to leave Chenla.":
                            $n=2
                    if n==1:
                        "The man who put the stall""You looks like..."
                        "The man who put the stall""Guys, catch her! She's the one disobeyed the China's law!"
                        show redgirl
                        with dissolve
                        stop sound
                        play sound sd
                        a "I should leave here! Run!"
                    else:
                        ""

                else:
                    ""

            else:
                scene chanpa
                with fade
                hide redgirl
                with dissolve
                a "Welcome to Chanpa."
                a "It seems wonderful here, with splendid architecture and clear sky!"
                menu:
                    "Do you want to stay here?"
                    "Yes, this place matched my imagination of Holy Land!":
                        $g=1
                    "No.":
                        $g=2
                if g==1:
                    a "I traveled for a long time..."
                    a "My stomach is so empty, I am hungry. Where can I get something for lunch?"
                    "Lots of people are doing something there, lets go and ask them if there's any food!"
                    scene zongjiaohuodong
                    with fade
                    "What is that?!"
                    "Are they sacrificing people?"
                    show redgirl
                    with dissolve
                    stop sound
                    play sound sd
                    "The man stand on the sacrificial altar""I am the king!"
                    "The man stand on the sacrificial altar""If you want to stay here, you have to listen to me, or you will be killed."
                    a "I must go, it's too scary."
                    ""
                else:
                    ""

    else:
                show redboy
                with dissolve
                "{size=45}{b}You chose Clarence."
                c "I am Clarence, I am expeled from China.."
                c "Where can I go..."
                menu:
                    "Choose the place you want to go first:{a=jump:skip}if you want to skip the story, click this"
                    "Taiwan":
                        $ y=1
                    "Chenla":
                        $ y=2
                    "Champa":
                        $ y=3
                if y==1:
                    scene taiwan
                    with fade
                    c "Welcome to Taiwan."
                    scene birds
                    with fade
                    c "The scenery here seems pleasant, lots of birds assembled together! I love to have contacts with animals!"
                    menu:
                        "Do you want to stay in Taiwan island?"
                        "Yes":
                            $ z=1
                        "No":
                            $ z=2
                    if z==1:
                        scene taiwan
                        with fade
                        hide redboy
                        with dissolve
                        show crabs1
                        with dissolve
                        c "Also, there are crabs moving on the island..."
                        hide crabs1
                        with dissolve
                        show crabs
                        with dissolve
                        "Wait, what is that, crabs cooked throughly!?"
                        hide crabs
                        with dissolve
                        show redboy
                        with dissolve
                        c "That's magic, I got crabs for my lunch!"
                        "A big wave came from behind."
                        stop sound
                        play sound wavesound
                        hide redboy
                        with dissolve
                        show mermaid
                        with dissolve
                        "mermaid""Hi, boy. I want you to be my servant, follow me."
                        hide mermaid
                        with dissolve
                        stop sound
                        c "She wants to catch me! Run!"
                        play sound sd
                        show redboy
                        with dissolve
                        "I am going to leave this place, it's too dangerous!"
                    else:
                        ""
                elif y==2:
                    scene zhenla
                    with fade
                    hide redboy
                    with dissolve
                    c "Welcome to Chenla."
                    scene zhenla1
                    with fade
                    c "The scenery here seems pleasant, there are lots of ancient architectures and culture relics!"
                    c "I would like to live here! "
                    menu:
                        "Do you want to stay in Chenla?"
                        "Yes":
                            $ z=1
                        "No":
                            $ z=2
                    if z==1:
                        scene maigua
                        with fade
                        hide redboy
                        with dissolve
                        c "I am hungry... wanna get some food for lunch."
                        c "Oh! There.. someone is setting up a stall!"
                        "I want to exchange some daily supplies and solid foods with them."
                        menu:
                            "Should I go?"
                            "You decided to trade with them.":
                                $n=1
                            "No, they don't look like good people, I want to leave Chenla.":
                                $n=2
                        if n==1:
                            "The man who put the stall""You looks like..."
                            "The man who put the stall""Guys, catch him! He's the one disobeyed the China's law!"
                            show redboy
                            with dissolve
                            stop sound
                            play sound sd
                            c "I should leave here! Run!"
                        else:
                            ""

                    else:
                        ""

                else:
                    scene chanpa
                    with fade
                    hide redboy
                    with dissolve
                    c "Welcome to Chanpa."
                    c "It seems wonderful here, with splendid architecture and clear sky!"
                    menu:
                        "Do you want to stay here?"
                        "Yes, this place matched my imagination of Holy Land!":
                            $g=1
                        "No.":
                            $g=2
                    if g==1:
                        c "I traveled for a long time..."
                        c "My stomach is so empty, I am hungry. Where can I get something for lunch?"
                        "Lots of people are doing something there, lets go and ask them if there's any food!"
                        scene zongjiaohuodong
                        with fade
                        "What is that?!"
                        "Are they sacrificing people?
                        w"
                        show redboy
                        with dissolve
                        stop sound
                        play sound sd
                        "The man stand on the sacrificial altar""I am the king!"
                        "The man stand on the sacrificial altar""If you want to stay here, you have to listen to me, or you will be killed."
                        c "I must go, it's too scary."
                        ""
                    else:
                        ""
    label skip:
        menu:
            "{color=#00BFFF}{alpha=0.5}Choose the next place you want to go:"
            "{color=#00BFFF}{size=60}Byzantium":
                $o=1
            "{color=#00BFFF}{alpha=0.5}Go back to China.":
                $o=2
        if o==1:
            scene baizhanting
            with fade
            show greengirl
            with dissolve
            show redgirl at left
            with dissolve
            show redboy at right
            with dissolve
            a "{alpha=0.5}{color=#F0F8FF}This is a good place to settle!"
            c "{alpha=0.5}{color=#F0F8FF}The soil is fertile, and sea is surrounded, also some natives still live here."
            j "{alpha=0.5}{color=#F0F8FF}Let's try to talk with them!"
            menu:
                "Do you want to talk with the armys standing beside the river?"
                "Yes, of course!":
                    $ p=1
                "No.":
                    $ p=2
            if p==1:
                hide greengirl
                with dissolve
                hide redgirl
                with dissolve
                hide redboy
                with dissolve
                "{i}The army""Who are you?"
                c "If you want to live peacefully, then be our army."
                j "Or we're gonna have a fight."
                "The army""...?"
                "The army""How dare you look down upon us!"
                stop sound
                play sound dz
                "The army""My brothers, go and give them some color to see!"
                scene dazhang
                with fade
                show greengirl at right
                with dissolve
                j "That's it?"
                hide greengirl
                with dissolve
                show redboy at left
                with dissolve
                c "Let me use my strength to defeat them!"
                show redgirl at right
                with dissolve
                a "And me!"
                hide redboy
                with dissolve
                hide redgirl
                with dissolve
                stop sound
                play sound dn
                scene hyed
                "At last, the army belongs to us, and we settled in Byzantium happily ever after..."
                "Maybe there are some quarrels and political disputes."
                "But we are going to overcome them together."
                "{size=60}{b}HAPPY ENDING"
            else:
                "The army saw you."
                "They came infront of you."
                hide greengirl
                with dissolve
                hide redgirl
                with dissolve
                hide redboy
                with dissolve
                "{i}The army""Who are you?"
                c "If you want to live peacefully, then be our army."
                j "Or we're gonna have a fight."
                "The army""...?"
                "The army""How dare you look down upon us!"
                stop sound
                play sound dz
                "The army""My brothers, go and give them some color to see!"
                scene dazhang
                with fade
                show greengirl at right
                with dissolve
                j "That's it?"
                hide greengirl
                with dissolve
                show redboy at left
                with dissolve
                c "Let me use my strength to defeat them!"
                show redgirl at right
                with dissolve
                a "And me!"
                hide redboy
                with dissolve
                hide redgirl
                with dissolve
                stop sound
                play sound dn
                scene hyed
                "At last, the army belongs to us, and we settled in Byzantium happy ever after..."
                "Maybe there are some quarrels and political disputes."
                "But we are going to overcome them together."
                "{size=60}{b}HAPPY ENDING"

        else:
            scene china
            with fade
            stop sound
            play sound bs
            "Because you disobeyed the law, you went back and get caught into the jail."
            "{size=60}{b}BAD ENDING"
    return
