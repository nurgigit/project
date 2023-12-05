
def setup(): 
    size(800,600)  # Устанавливаем размер окна 
 
 
def draw(): 
    background(255)  # Задаем белый фон 
    background(229,229,53)
    fill(38,152,52)
    ellipse(468,200,30,30)
    fill(38,152,52)
    ellipse(468,400,30,30)
    ellipse(270,200,30,30)
    ellipse(270,400,30,30)
    ellipse(370,150,50,50)
    fill(206,178,78)
    ellipse(370,300,250,250)
    stroke(2)    
    fill(46,134,209)
    # Настройки цвета и формы волны 
    fill(46,134,209)  # Черный цвет 
      # Черный цвет 
      # Толщина линии 
 
    # Параметры волны 
    amplitude = 50  # Амплитуда (высота) волны 
    frequency = 0.02  # Частота (количество волн) 
 
    # Рисуем волну 
    for x in range(width): 
        y = height / 2 + sin(x * frequency) * amplitude 
        point(x, y)  # Рисуем точку 
 
    # Увеличиваем частоту волны с течением времени 
    frequency += 0.01
