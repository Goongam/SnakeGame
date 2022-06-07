def setDefaultSetting():
    global snake_color
    snake_color = 'blue'
    global food_color
    food_color = 'green'
    global background_color
    background_color = 'aqua'
    global snake_shape
    snake_shape = 'triangle'

def changeSnakeColor(color):
    global snake_color
    snake_color = color

def changeFoodColor(color):
    global food_color
    food_color = color

def changeBackgroundColor(color):
    global background_color
    background_color = color

def changeSnake_shape(shape):
    global snake_shape
    snake_shape = shape

