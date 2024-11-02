from tank import Tank
from tkinter import*



KEY_W = 87
KEY_S = 83
KEY_A = 65
KEY_D = 68

FPS = 60

def update():
    player.update()
    enemy.update()
    check_collision()
    w.after(1000//FPS, update)


def check_collision():
    player.inersects(enemy)
    enemy.inersects(player)
    if enemy.inersects(player):  # 4 Вызвать обертку
        print('Танки столкнулись')
        enemy.undo_move()

def key_press(event):
    if event.keycode == KEY_W:
        player.forward()
    elif event.keycode == KEY_S:
        player.backward()
    elif event.keycode == KEY_A:
        player.left()
    elif event.keycode == KEY_D:
        player.right()
    check_collision()           # 5 вызвать проверку столкновений при событиях нажатия на клавиши
                                   # смоделировать ситуацию столкновения
w = Tk()
w.title('Танки на минималках 2.0')
canv = Canvas(w, width = 800, height = 600, bg = 'alice blue')
canv.pack()
player = Tank(canvas = canv, x = 100, y = 50, ammo = 100, speed=2, bot = False)
enemy = Tank(canvas = canv, x = 500, y = 150, ammo = 100, speed=2, bot = True)
enemy.set_target(player)
w.bind('<KeyPress>', key_press)
update()
w.mainloop()