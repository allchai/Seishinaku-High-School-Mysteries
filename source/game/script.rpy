define ai = Character('Ай', color="#ffffff")
define kadum = Character('Кадум', color = "#ffffff")
define whisper = Character('Девичий шёпот', color="#ffffff") 

init python:
    WasOnFirstFloor = False
    WasOnThirdFloor = False
    HeardMistiphan = False
    WasInGym = False 
    WasAtExit = False
    WasAtBuphet = False
    ThinkYasuka = False
    ThinkKadum = False
    ThinkAruya = False
    WasInGymSecondTime = False
    WasInGymThirdTime = False
    Flashback = False
    WasEnterClass = False
    MirrorChoice = False
    SecondExploreSecondFloor = False
    ThinkShizasaki = False
    ThinkHoruchi = False

label start:
    show screen Frame
    scene bg room
    show sisi:
        xpos 0.5


    ai "Слухи разжигают любопытство в людях"
    kadum "\"Призрак возмездия\"? Дай угадаю - это ещё один мистический детектив?"
    "Поменял ковычки, потому что в этом шрифте их нет"

    label .choice:
        menu:
            "Начать поиск издалека":
                ai "П-погоди!"
                jump .choice
            "Проверить соседний класс":
                pass
    ai "Тише. Мне кажется, я что-то слышу за той дверью."
    label SecondFloorChoise:  
        menu:
            "Пойти на третий этаж":
                "Мы проверили все незапертые комнаты на этаже, но загадочной девушки нигде не было."
                jump ThirdFloor
            "Пойти на первый этаж":
                jump FirstFloor
            "Пойти в класс":      
                kadum "Хочешь вернуться к Ясуке и Хорючи?"
                jump SecondFloorChoise
                
    label ThirdFloor:    
        if not WasOnFirstFloor:
            ai "Стоит проведать комнаты в нижней части школы."
            $ WasOnThirdFloor = True
        else:
            ai "Но мы всё осмотрели. Её там не было."
        kadum "Но перед тем, как мы пойдём..."
        if not WasOnFirstFloor:
            kadum "У нас есть около тридцати минут до полуночи."
        else:
            kadum "До полуночи остались считанные минуты. Нам стоит поторопиться."
        kadum "Да, а что?"
        ai "Нам нужно поторопиться и найти остальных."
        label ThirdFloorChoice:
            menu:
                "Пойти на первый этаж":
                    jump FirstFloor
                "Пойти на второй этаж":
                    jump SecondFloorChoise
                "Оглядеть третий этаж":
                    "Здесь есть как запертые, так и незапертые помещения."
                    "В любом случае сейчас они не представляют интереса."
                    jump ThirdFloorChoice

    label FirstFloor:
        if not WasOnFirstFloor:
            "Вестибюль встретил нас оглушительной тишиной."
            kadum "Стоит заглянуть во все открытые двери."
        label FirstFloorChoice:
            menu:
                "Зайти в спортзал":
                    if not WasInGym:
                        kadum "A?"
                        kadum "Кажется, дверь открыта."
                        kadum "Рискнём?"
                    menu:
                        "Войти":
                            if WasInGym:
                                kadum "Если есть ещё ученики, то они должны находиться в других местах."
                                jump FirstFloorChoice
                            whisper "Тихо. Кто-то вошёл."
                            ai "У неё, должно быть, очень сложный характер, раз она ни с кем не сходится."
                            $ WasInGym = True
                            if WasInGym and WasAtBuphet and WasAtExit:
                                jump FirstFloorChoiceTwo 
                            jump FirstFloorChoice
                        "Не входить":
                            jump FirstFloorChoice
                "Зайти в столовую":
                    if WasAtBuphet:
                        kadum "Лучше не возвращаться сейчас к Аруе."
                        jump FirstFloorChoice
                    ai "Столовая не заперта..."
                    kadum "Не знаю... Может, Аруя отжала их у какого-то работника столовой, чтобы проникнуть в школу ночью."
                    if WasAtExit:
                        ai "Иначе говоря... она может открыть чёрный вход, чтобы мы не ждали до утра, когда откроются двери школы?"
                        kadum "Не думаю, что она сделает это для кого-либо."
                    else:
                        "Значит, не все ученики спрятались в школе..."
                    ai "Если честно, я всё ещё не могу понять, что Аруя здесь делает, если не верит в призраков."
                    kadum "У меня предчувствие, будто мы скоро узнаем."
                    $ WasAtBuphet = True
                    if WasInGym and WasAtBuphet and WasAtExit:
                        jump FirstFloorChoiceTwo 
                    jump FirstFloorChoice
                "Пойти к выходу из школы":
                    $ WasAtExit = True
                    kadum "Хочешь выйти?"
                    if WasOnThirdFloor:
                        ai "Да... Мне немного не по себе от течения времени в этом месте."
                        kadum "Согласен, меня это тоже напрягает. Тогда уйдём?"
                    "Вы хотите выйти?"
                    menu:
                        "Выйти":
                            pass
                        "Не уходить":
                            pass
                    kadum "Мы всё равно не сможем это сделать. Двери школы закрываются на ночь."
                    kadum "Да ладно, ты струсила, Мистифан?"
                    if not HeardMistiphan:
                        ai "Как-как ты меня назвал?"
                        kadum 'Ну, "Мистический фанат".'
                        $ HeardMistiphan = True
                    if WasInGym and WasAtBuphet and WasAtExit:
                        jump FirstFloorChoiceTwo
                    jump FirstFloorChoice
        
        label FirstFloorChoiceTwo:
            ai "Мы обошли все доступные места на первом этаже, но нигде не видели ту странную девушку."
            kadum "Должно быть, она убежала наверх."
            menu:
                "Пойти на второй этаж":
                    ai "Если подумать, она могла вернуться на второй этаж."
                    kadum "Проверить всё равно стоило."
                    if not WasOnThirdFloor:
                        ai "Пора подняться на этаж выше."
                        jump ThirdFloor
                    else:
                        ai "Пора спуститься на этаж ниже."
                        if WasInGym and WasAtBuphet and WasAtExit and WasOnThirdFloor:
                            pass
                "Пойти на третий этаж":
                    jump ThirdFloor
                        
    "Вдруг в конце первого этажа мы увидели знакомую фигуру."
    label ForFlashback:
        "Что-то про Хорючи, говорящего, что сука боится призраков"
        if Flashback:
            jump AfterSecondFlashback
    label FirstFloorChoiceThree:
        menu:
            "Пойти на второй этаж":
                menu:
                    "Думать о Кадуме":
                        if not ThinkKadum:
                            "Мог ли Кадум пригласить меня по той же причине, что и Ясука взяла с собой Хорючи?"
                            "Страшно было бы ему ходить по ночной школе в одиночку?"
                            $ ThinkKadum = True
                            jump FirstFloorChoiceThree        
                        else:
                            "Спрошу его потом, когда эта ночь закончится."
                            jump FirstFloorChoiceThree
                    "Зайти в класс":
                        pass

            "Думать о Ясуке":
                if not ThinkYasuka:
                    "Получается, Ясука отказывается верить в призраков, потому что боится их?"
                    "Но если ей страшно... зачем она вообще пришла?"
                    $ ThinkYasuka = True 
                    jump FirstFloorChoiceThree
                else:
                    "Интересно, заметит ли Ясука когда-нибудь заботу Хорючи?"
                    "Несмотря на внешность, у этого парня доброе сердце."
                    "И, если это любовь, я надеюсь, что у них всё будет хорошо."
                    jump FirstFloorChoiceThree

    "Собравшись с духом, я коснулась двери."
    "Очень много текст!"
    kadum "Ах да, верно... Время проверить загадочную связку."
    menu:
        "Думать об Аруе":
            if not ThinkAruya:
                "Держись, Аруя. Хоть ты и, вроде, плохой человек... но без страха первая бросилась на того монстра."
                "Это случилось из-за нашего бездействия. Мы должны быть признательны тебе за храбрость. Спасибо."
                $ ThinkAruya = True
            else:
                "Лишиться кисти – это... ужасно. Надеюсь, у Аруи найдутся силы, чтобы пережить потерю."                        
        "Пойти в вестибюль":
            pass
    kadum "Сейчас проверим..."
    "Много текст!"
    label ThirdFlashback:
        "Что-то про Хорючи, у которого трясутся ноги"
        if Flashback:
            jump AfterThirdFlashback

    label Flashback:
        "Что-то про Хорючи, кидающего стул"
        if Flashback:
            jump AfterFlashback
    kadum "Резонно. Давай найдём её."
    label FirstFloorChoiceFour:
        menu:
            "Пойти в спортзал":
                if not WasInGymSecondTime:
                    kadum "Ясука упоминала, что ей нужны были ключи для запертой комнаты. Это не может быть спортзал."
                    kadum "Ага, теперь мы знаем, что там никого нет."
                    $ WasInGymSecondTime = True
                    jump FirstFloorChoiceFour
                elif WasInGymSecondTime:
                    kadum "Что такое? Ты что-то там забыла?"
                    kadum "Это была самая бессмысленная трата времени. Даже не думай снова меня звать туда."
                    $ WasInGymThirdTime = True
                    jump FirstFloorChoiceFour
                elif WasInGymThirdTime:
                    ai "Стой! Мы кое-что упустили там!"
                    kadum "Ты о куче упущенного времени? Я больше не пойду туда."
                    jump FirstFloorChoiceFour
            "Осмотреть первый этаж":
                pass
    ai "Давай проверим все двери в коридоре?"
    kadum "Спросим, когда встретим. Пойдём, поищем где-нибудь ещё."
    label ExploringFirstFloor:
        menu:
            "Пойти в спортзал":
                if not WasInGymSecondTime:
                        kadum "Ясука упоминала, что ей нужны были ключи для запертой комнаты. Это не может быть спортзал."
                        kadum "Ага, теперь мы знаем, что там никого нет."
                        $ WasInGymSecondTime = True
                        jump ExploringFirstFloor
                elif WasInGymSecondTime:
                    kadum "Что такое? Ты что-то там забыла?"
                    kadum "Это была самая бессмысленная трата времени. Даже не думай снова меня звать туда."
                    $ WasInGymThirdTime = True
                    jump ExploringFirstFloor
                elif WasInGymThirdTime:
                    ai "Стой! Мы кое-что упустили там!"
                    kadum "Ты о куче упущенного времени? Я больше не пойду туда."
                    jump ExploringFirstFloor
            "Осмотреть первый этаж":
                "Помимо всех помещений, здесь расположена комната охраны"
                "Но я не хочу туда заходить. Если охранник доложит о нас, то мы можем быть исключены из школы."
                jump ExploringFirstFloor
            "Подняться на второй этаж":
                pass
    "Мы снова ступаем на этаж, на котором творился кошмар."
    ai "Мне любопытно заглянуть в тот класс ещё раз..."
    label ClassChoice:
        menu:
            "Войти в класс":
                if not WasEnterClass:
                    "Но когда я вошла туда..."
                    "А ты не помнишь?"
                    $ Flashback = True 
                    jump Flashback
                    label AfterFlashback:
                        ai "Это... часть стула?"
                    ai "Нет, меня напрягает не только это в его поведении."
                    jump ForFlashback
                    label AfterSecondFlashback:
                        jump ThirdFlashback
                    label AfterThirdFlashback:
                        ai "Всё это время Хорючи вёл себя и говорил так, словно знал, что произойдёт."
                    $ WasEnterClass = True
                    if SecondExploreSecondFloor:
                        jump FloorChoice
                    else:
                        jump ClassChoice  
                else:
                    ai "Преступник всегда возвращается на место преступления!"
                    kadum "Мы только что были там. Пойдём, мы спешим."
                    ai "Но... но... эх"  
                    jump ClassChoice           
            "Осмотреть второй этаж":
                if not ItemChoice:
                    pass
                else:
                    ai "Осталось одно место, куда мы ещё не заходили."
                    kadum "Но оно же открытое?"
                    ai "..."
                    $ SecondExploreSecondFloor = True
                    if WasEnterClass:
                        jump FloorChoice
                    else:
                        jump ClassChoice

    "Мы прошлись по коридору, проверяя, не открылись ли новые комнаты."
    label ItemChoice:
        menu:
            "Часы":
                ai "Ты о часах?"
                kadum "Нет, они есть везде и показывают одно и то же время."
                ai "Время остановилось?"
                kadum "..."
                jump ItemChoice
            "Что-то на учительском столе":
                "Кажется, на нём появилось кое-что новое."
                ai "Хм? Что это?"
                kadum "По-моему, то же самое, что и раньше. Ничего особенного."
                ai "Ах... ты прав..."
                jump ItemChoice
            "Зеркало":
                ai "Зеркало?"
                if WasEnterClass:
                    ai "Ты думаешь... с Ясукой что-то произошло?"
                    kadum "Нам нужно поторопиться."
                else:
                    ai "Как-то странно всё это..."
                $ MirrorChoice = True
                jump ClassChoice
                
    label FloorChoice:
        ai "Что?!"
        "Я задолбался"

    label ToiletChoice:
        menu:
            "Думать о Шизасаки":
                if not ThinkShizasaki:
                    "Мне сложно понять, что у этой девушки на уме."
                    "Однако слова Шизасаки мне казались искренними…"
                    $ ThinkShizasaki = True
                    jump ToiletChoice
                else:
                    "Как и сказал Кадум, не всё то, во что по-настоящему верит человек, может оказаться правдой."
                    "Этот случай достаточно сложный..."
                    jump ToiletChoice
            "Выйти из туалета":
                ai "Итак, остался последний этаж. Ясука должна быть где-то здесь."

    kadum "Смотри, кажется, библиотека открыта."
    label LibraryChoice:
        menu:
            "Думать о Хорючи":
                if not ThinkHoruchi:
                    "Если я права, *он* будет внутри."
                    "Я должна быть готова раскрыть правду о нём."
                    $ ThinkHoruchi = True
                    jump LibraryChoice
                else:
                    "Так, я готова. Вперёд!"
            "Идти в библиотеку":
                pass
    "Дверь тихонько скрипит, когда я открываю её."
    return
