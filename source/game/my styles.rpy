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

style game_menu_navigation_frame:
    xsize 137
    yfill True

style history_label_text:
    xalign 0.0

style inventory_button:
    background "gui/button/inventoryCell_idle.png"
    hover_background "gui/button/inventoryCell_hover.png"
    padding (8, 8, 8, 8)
    xsize 100
    ysize 100

define gui.inventory_spacing = 17
