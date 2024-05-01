screen navigation():
    zorder 100

    if main_menu:


        vbox:
            xalign 0.241
            yalign 0.87
            spacing 5

            imagebutton auto "gui/button/start_%s.png" action Start()
            imagebutton auto "gui/button/load_%s.png" action ShowMenu("load")
        
        vbox:
            xalign 0.757
            yalign 0.869
            spacing 3


            imagebutton auto "gui/button/about_%s.png" action ShowMenu('about')
            imagebutton auto "gui/button/settings_%s.png" action ShowMenu('preferences')
            imagebutton auto "gui/button/exit_%s.png" action Quit(confirm=not main_menu)

    else:


        vbox:
            xalign 0.5
            yalign 0.865
            spacing 5 

            imagebutton auto "gui/button/back_game_%s.png" action Return()
            imagebutton auto "gui/button/mainMenu_%s.png" action MainMenu()


    if _in_replay:

        textbutton _("Завершить повтор") action EndReplay(confirm=True)

    elif not main_menu:
        
        


        if renpy.variant("pc") or (renpy.variant("web") and not renpy.variant("mobile")):

            ## Помощь не необходима и не относится к мобильным устройствам.
            textbutton _("Помощь") action ShowMenu("help")

        if renpy.variant("pc"):

            ## Кнопка выхода блокирована в iOS и не нужна на Android и в веб-
            ## версии.
            textbutton _("Выход") action Quit(confirm=not main_menu)