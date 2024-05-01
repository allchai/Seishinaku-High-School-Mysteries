screen game_menu(title, scroll=None, yinitial=0.0, spacing=0, back_button=True):

    zorder 100

    style_prefix "game_menu"
    if main_menu:
        add gui.main_menu_background
    else:
        add gui.game_menu_background

    frame:
        style "game_menu_outer_frame"

        hbox:

            ## Резервирует пространство для навигации.
            frame:
                style "game_menu_navigation_frame"

            frame:
                style "game_menu_content_frame"

                if scroll == "viewport":
                    pass
                    viewport:
                        yinitial yinitial
                        scrollbars "vertical"
                        mousewheel True
                        draggable True
                        pagekeys True

                        side_yfill True

                        vbox:
                            spacing spacing

                            transclude

                elif scroll == "vpgrid":

                    vpgrid:
                        cols 1
                        yinitial yinitial

                        scrollbars "vertical"
                        mousewheel True
                        draggable True
                        pagekeys True

                        side_yfill True

                        spacing spacing

                        transclude

                else:

                    transclude

    use navigation
    label title    
    if back_button:
        imagebutton auto "gui/button/back_%s.png":
            xalign gui.return_button_xalign
            yalign gui.return_button_yalign
            action ShowMenu("main_menu")

