screen Frame:
    zorder 2
    add "Frame.png"

style window:
    xalign 0.5
    xfill True
    yalign 0.88
    ysize gui.textbox_height


style say_dialogue:
    properties gui.text_properties("dialogue")

    xpos 0.17
    xsize gui.dialogue_width
    ypos gui.dialogue_ypos

    adjust_spacing False

screen quick_menu():
    variant "touch"

    zorder 100

    if quick_menu:

        hbox:
            style_prefix "quick"

            xalign 0.5
            yalign 1.0

            textbutton _("Назад") action Rollback()
            textbutton _("Пропуск") action Skip() alternate Skip(fast=True, confirm=True)
            textbutton _("Авто") action Preference("auto-forward", "toggle")
            textbutton _("Меню") action ShowMenu()

style namebox:
    xpos 0.165
    xanchor gui.name_xalign
    xsize gui.namebox_width
    ypos 0.02
    ysize gui.namebox_height

    background Frame("gui/namebox.png", gui.namebox_borders, tile=gui.namebox_tile, xalign=gui.name_xalign)
    padding gui.namebox_borders.padding

style choice_vbox:
    xalign 0.5
    ypos 580
    yanchor 0.5

    spacing gui.choice_spacing

define pixelDisolver = ImageDissolve(image="pixelDissolver.png", remplen=8, time=2, reverse=True, mipmap=None)
define lineDisolver = ImageDissolve(image="lineDissolver.png", remplen=8, time=2, reverse=True, mipmap=None)
image sisi = "a_girl_with_tits.png"