import pgzrun
import random

WIDTH = 800
HEIGHT = 600
center_x = WIDTH/2
center_y = HEIGHT/2
center = (center_x,center_y)

current_level = 1
final_level = 6
gameover = False
gamecomplete = False
ITEMS = ["bag","battery","bottle","chips"]
items = []
animations = []

def draw():
    global items,current_level,gameover,gamecomplete
    screen.clear()
    screen.blit("bground",(0,0))
    if gameover:
        display_message("Game Over","Try again")
    elif gamecomplete:
        display_message("Congratulations!", "You beat the game!")
    else:
        for item in items:
            item.draw()

def update():
    global items,current_level
    if len(items) == 0:
        items = make_items(current_level)

def make_items(extra_items):
    items_to_create = get_option_to_create(extra_items)
    new_items = create_items(items_to_create)
    layout_items(new_items)
    animate_items(new_items)
    return new_items

def get_option_to_create(extra_items):
    items_to_create = ["paper"]
    for i in range(0,extra_items):
        random_option = random.choice(ITEMS)
        items_to_create.append(random_option)
    return items_to_create

def create_items(items_to_create):
    new_items = []
    for option in items_to_create:
        item = Actor(option + "img")
        new_items.append(item)
    return new_items

def layout_items(items_to_layout):
    number_of_gaps = len(items_to_layout) + 1
    gap_size = WIDTH/number_of_gaps
    random.shuffle(items_to_layout)
    for index,item in enumerate(items_to_layout):
        new_x_pos = (index + 1)*gap_size
        item.x = new_x_pos

def animate_items(items_to_animate):
    global animations

    






pgzrun.go()