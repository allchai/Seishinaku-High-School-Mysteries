screen about():

    tag menu

    ## Этот оператор включает игровое меню внутрь этого экрана. Дочерний vbox
    ## включён в порт просмотра внутри экрана игрового меню.
    use game_menu(_("Об игре"), scroll="viewport"):

        style_prefix "about"

        vbox:

            label "[config.name!t]"
            text _("Game jame версия.")

            ## gui.about обычно установлено в options.rpy.
            if gui.about:
                text "[gui.about!t]\n"

            text _('Сделано командой Approuch Games в рамках "Hybrid Visual Novel Jam".')
            text _("{a=https://vk.com/gospodin_balakhnin}Даня Балахнин{/a} - Сценарист, лидер")
            text _("{a=https://vk.com/kannye_west}Леонид Каня{/a} - Сценарист")
            text _("{a=https://vk.com/problems_are_cool}Дарья Toboos{/a} - Художница")
            text _("{a=https://vk.com/dim_enfilade}Майк Pilatus{/a} - Музыкант")
            text _("{a=https://vk.com/fifteen_art}Артём Фифтин{/a} - Музыкант")
            text _("{a=https://vk.com/allchai}Кирилл Алыча{/a} - Программист")
