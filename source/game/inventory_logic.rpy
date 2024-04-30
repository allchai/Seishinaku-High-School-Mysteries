init python:
    class Item(object):
        def __init__(self, name: str, status: bool, description: str):
            self.name = name
            self.image = f"images/items/{self.name}.png"
            self.is_picked = status
            self.description = description
        
        def get_image_path(self) -> str:
            return self.image
        
        def get_name(self):
            return self.name

        def get_description(self):
            return self.description

        def get_status(self):
            return self.is_picked

    # Item list:
    Item_list = []
    Item_list.append(Item(name="test", status=True, description="Это тестовый объект, он нужен, чтобы проверить инвентарь"))
    Item_list.append(Item(name="test2", status=True, description="Это тестовый объект, он нужен, чтобы проверить инвентарь"))
    Item_list.append(Item(name="test3", status=False, description="Это тестовый объект, он нужен, чтобы проверить инвентарь"))