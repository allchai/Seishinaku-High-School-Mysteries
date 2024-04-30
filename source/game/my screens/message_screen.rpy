screen message_screen(message):

    ## Гарантирует, что другие экраны будут недоступны, пока показан этот экран.
    modal True

    zorder 200

    style_prefix "confirm"

    add "gui/overlay/confirm.png"

    frame:

        vbox:
            xalign .5
            yalign .5
            spacing 23

            label _(message):
                style "confirm_prompt"
                xalign 0.5

            hbox:
                xalign 0.5
                spacing 75

                textbutton _("ok") action Hide("message_screen")
                #textbutton _("Нет") action no_action

    ## Правый клик и esc, как ответ "Нет".
    key "game_menu" action Hide("message_screen")