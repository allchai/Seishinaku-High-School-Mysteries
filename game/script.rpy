# Вы можете расположить сценарий своей игры в этом файле.

# Определение персонажей игры.
define e = Character('Эйлин', color="#ffffff")

# Вместо использования оператора image можете просто
# складывать все ваши файлы изображений в папку images.
# Например, сцену bg room можно вызвать файлом "bg room.png",
# а eileen happy — "eileen happy.webp", и тогда они появятся в игре.

# Игра начинается здесь:
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
