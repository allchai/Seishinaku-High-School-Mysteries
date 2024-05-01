screen quick_menu():

    ## Гарантирует, что оно появляется поверх других экранов.
    zorder 100

    if quick_menu:

        hbox:
            style_prefix "quick"

            xalign 0.5
            yalign 0.934
            spacing 15.4


            imagebutton auto "gui/button/Qhistory_%s.png" action ShowMenu('history', back_button=False)
            imagebutton auto "gui/button/Qscip_%s.png" action Skip() alternate Skip(fast=True, confirm=True)
            imagebutton auto "gui/button/Qauto_%s.png" action Preference("auto-forward", "toggle")
            imagebutton auto "gui/button/Qsave_%s.png" action ShowMenu('save', back_button=False)
            imagebutton auto "gui/button/Qload_%s.png" action ShowMenu('load', back_button=False)
            imagebutton auto "gui/button/Qsettings_%s.png" action ShowMenu('preferences', back_button=False)
        
        imagebutton auto "gui/button/inventory_%s.png" action ShowMenu('inventory', back_button=False):
            xalign 0.9766
            yalign 0.856




