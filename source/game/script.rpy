define e = Character('Эйлин', color="#ffffff")

label start:
    show screen Frame
    scene bg room
    show sisi with lineDisolver:
        xpos 0.5
    
    

    e "Диалог"

    menu:
        "Выбор 1":
            pass
        "Выбор 2":
            pass
    
    e "Ещё какая-то фраза."

    return
