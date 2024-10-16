from hitbox import Hitbox

hb1 = Hitbox(x=0, y=100, width=100, height=100)
hb2 = Hitbox(x=150, y=80, width=100, height=100)


print(f'Верхняя граница hb1:{hb1.top}'
      f'Верхняя граница hb2:{hb2.top}')
print(f'Нижняя граница hb1:{hb1.bottom}'
      f'Нижняя граница hb2:{hb2.bottom}')
print(f'Левая граница hb1:{hb1.left}'
      f'Левая граница hb2:{hb2.left}')
print(f'Правая граница hb1:{hb1.right}'
      f'Правая граница hb2:{hb2.right}')

intersection = hb1.intersects(hb2)
print(intersection)