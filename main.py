from src.bean_conqueror.parser import BeanConquerorParser
from src.bean2obsidian import Bean2Obsidian


if __name__ == '__main__':
    json_file = "Beanconqueror/Beanconqueror-1.json"
    obsidian = Bean2Obsidian(json_file, "/Users/jiaboshi/OneDrive/004-Notes/003-CoffeeGround")
    obsidian.save()