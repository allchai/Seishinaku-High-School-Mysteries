screen inventory(back_button=True):

    tag menu 
    use game_menu("Инвентарь", back_button=back_button):
        grid 6 3:
            style_prefix "inventory"

            xalign 0.0
            yalign 0.0

            spacing gui.inventory_spacing

            for i in range(6 * 3):

                python:
                    if i <= len(Item_list)-1:
                        item_obj = Item_list[i]
                        item_status = item_obj.get_status()
                    else:
                        item_status = False

                if item_status == True:
                    button:
                        action Confirm([item_obj.get_description()], Return())
                        add [item_obj.get_image_path()] xalign 0.0
                else:
                    button:
                        action Confirm("Тут пусто", Return())
                        

