from hitbox import Hitbox

hb1 = Hitbox(x=0, y=100, width=100, height=100)
hb2 = Hitbox(x=50, y=50, width=100, height=100)
hb3 = Hitbox(x=100, y=100, width=100, height=100)


print(f'Верхняя граница hb1:{hb1.top}'
      f'Верхняя граница hb2:{hb2.top}'
      f'Верхняя граница hb3:{hb3.top}')
print(f'Нижняя граница hb1:{hb1.bottom}'
      f'Нижняя граница hb2:{hb2.bottom}'
      f'Нижняя граница hb3:{hb3.bottom}')
print(f'Левая граница hb1:{hb1.left}'
      f'Левая граница hb2:{hb2.left}'
      f'Левая граница hb3:{hb3.left}')
print(f'Правая граница hb1:{hb1.right}'
      f'Правая граница hb2:{hb2.right}'
      f'Правая граница hb3:{hb3.right}')

intersection = hb1.intersects(hb2)
print(intersection)