import pgzrun
import random



WIDTH = 720
HEIGHT = 480

target1 = Actor("target_red1")
target1.x = WIDTH/2
target1.y = HEIGHT/2

target2 = Actor("duck_target_brown")
target2.x = WIDTH/2
target2.bottom = HEIGHT

target3 = Actor("duck_target_white")
target3.x = random.randint(0,WIDTH)
target3.y = random.randint(0,HEIGHT)

target4 = Actor("target_red1")
target4.x = WIDTH/2
target4.y = random.randint(0,HEIGHT)

cursor = Actor("crosshair_blue_small")
rifle = Actor("rifle")

score = 0

def update():
    # target1.x = target1.x-1
    target1.x += random.randint(1,5)
    # move the target1 back to the right side if it reaches the left edge
    # target2.y = target.x-1
    target2.y += random.randint(1,5)
    target3.x += random.randint(1,5)
    target4.y += random.randint(1,5)

    if target1.left  >= WIDTH:
        target1.left = 0
    if target2.top  >= HEIGHT:
        target2. top = 0
    if target3.right >= WIDTH:
        target3.right = 0
    if target4.top >= HEIGHT:
        target4.top = 0 

def on_mouse_move(pos):
    # print(pos)
    cursor.pos = pos
    rifle.left =  pos[0]
    rifle.top = pos[1]

def on_mouse_down(pos):
    global Score
    # print ("mouse clicked") 
    if cursor.colliderect(target1):
        target1.right = 0
        target1.y = random.randint(0,HEIGHT)    
    elif cursor.colliderect(target2):
        target2.top = 0
        target2.x = random.randint(0,HEIGHT) 
    elif cursor.colliderect(target3):
        target3.right = 0
        target3.y = random.randint(0,HEIGHT)
    elif cursor.colliderect(target4):
        target4.top = 0
        target4.x = random.randint(0,HEIGHT)

    

# draw the actors
def draw():
    screen.clear()
    target1.draw()
    target2.draw()
    target3.draw()
    target4.draw()
    rifle.draw()
    cursor.draw()
    screen.draw.text(str(score),(10,10), fontsize=60, color='blue')

# to start
pgzrun.go()



