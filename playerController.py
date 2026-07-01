class PlayerController:

    def __init__(self, keyboard):
        self.keyboard = keyboard

    def get_direction(self, snake):

        if self.keyboard.key_pressed("RIGHT") and snake.direction != (-1,0):
            return (1,0)

        if self.keyboard.key_pressed("LEFT") and snake.direction != (1,0):
            return (-1,0)

        if self.keyboard.key_pressed("UP") and snake.direction != (0,1):
            return (0,-1)

        if self.keyboard.key_pressed("DOWN") and snake.direction != (0,-1):
            return (0,1)

        return None