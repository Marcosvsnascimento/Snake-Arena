from PPlay.sprite import Sprite

class Snake:

    def __init__(self, x, y, controller, spritePath):

        self.controller = controller
        self.spritePath = spritePath

        self.sprite = Sprite(self.spritePath, 14)
        self.sprite.set_curr_frame(3)

        self.cell_size = 22

        self.grid_x = x // self.cell_size
        self.grid_y = y // self.cell_size

        self.direction = (1, 0)
        self.next_direction = (1, 0)

        self.body = []

        initial_size = 1

        for i in range(initial_size):
            segment = Sprite(self.spritePath, 14)

            segment.set_position(
                (self.grid_x - (i + 1)) * self.cell_size,
                self.grid_y * self.cell_size
            )

            self.body.append(segment)

        self.positions = [
            (self.grid_x - i, self.grid_y)
            for i in range(len(self.body) + 1)
        ]

        self.move_delay = 0.1
        self.timer = self.move_delay

        self.sprite.set_position(
            self.grid_x * self.cell_size,
            self.grid_y * self.cell_size
        )

        

    def update(self, delta_time):

        new_direction = self.controller.get_direction(self)

        if new_direction is not None:
            self.next_direction = new_direction

        self.timer += delta_time

        if self.timer >= self.move_delay:

            self.timer = 0

            self.direction = self.next_direction

            self.grid_x += self.direction[0]
            self.grid_y += self.direction[1]

            self.positions.insert(0, (self.grid_x, self.grid_y))

            if len(self.positions) > len(self.body) + 1:
                self.positions.pop()

            for i, segment in enumerate(self.body):

                if i + 1 >= len(self.positions):
                    continue

                curr = self.positions[i + 1]

                segment.x = curr[0] * self.cell_size
                segment.y = curr[1] * self.cell_size

                if i + 2 < len(self.positions):

                    prev = self.positions[i]
                    next_pos = self.positions[i + 2]

                    frame = self.get_curve_frame(prev, curr, next_pos)
                    segment.set_curr_frame(frame)

                else:

                    prev = self.positions[i]
                    curr = self.positions[i + 1]

                    dx = curr[0] - prev[0]
                    dy = curr[1] - prev[1]

                    if dx == 1:
                        segment.set_curr_frame(13)

                    elif dx == -1:
                        segment.set_curr_frame(12)

                    elif dy == 1:
                        segment.set_curr_frame(10)

                    elif dy == -1:
                        segment.set_curr_frame(11)

        self.update_head_sprite()

        self.sprite.x = self.grid_x * self.cell_size
        self.sprite.y = self.grid_y * self.cell_size

    def update_head_sprite(self):

        if self.direction == (0, -1):
            self.sprite.set_curr_frame(0)

        elif self.direction == (0, 1):
            self.sprite.set_curr_frame(1)

        elif self.direction == (-1, 0):
            self.sprite.set_curr_frame(2)

        elif self.direction == (1, 0):
            self.sprite.set_curr_frame(3)

    def get_curve_frame(self, prev, curr, next_pos):

        dx1 = curr[0] - prev[0]
        dy1 = curr[1] - prev[1]

        dx2 = next_pos[0] - curr[0]
        dy2 = next_pos[1] - curr[1]

        if dy1 == 0 and dy2 == 0:
            return 4

        if dx1 == 0 and dx2 == 0:
            return 5

        if (dx1, dy1) == (1, 0) and (dx2, dy2) == (0, 1):
            return 7

        if (dx1, dy1) == (0, 1) and (dx2, dy2) == (1, 0):
            return 8

        if (dx1, dy1) == (-1, 0) and (dx2, dy2) == (0, 1):
            return 6

        if (dx1, dy1) == (0, 1) and (dx2, dy2) == (-1, 0):
            return 9

        if (dx1, dy1) == (1, 0) and (dx2, dy2) == (0, -1):
            return 9

        if (dx1, dy1) == (0, -1) and (dx2, dy2) == (1, 0):
            return 6

        if (dx1, dy1) == (-1, 0) and (dx2, dy2) == (0, -1):
            return 8

        if (dx1, dy1) == (0, -1) and (dx2, dy2) == (-1, 0):
            return 7

        return 4

    def grow(self):

        segment = Sprite(self.spritePath, 14)
        segment.set_curr_frame(13)
        last = self.positions[-1]

        segment.set_position(
            last[0] * self.cell_size,
            last[1] * self.cell_size
        )

        self.body.append(segment)

    def draw(self):

        for segment in self.body:
            segment.draw()

        self.sprite.draw()

    def reset(self, x, y):
        self.grid_x = x // self.cell_size
        self.grid_y = y // self.cell_size
        self.direction = (1,0)
        self.next_direction = (1,0)

        self.body.clear()

        initial_size = 1

        for i in range(initial_size):
            segment = Sprite(self.spritePath, 14)

            segment.set_position((self.grid_x-(i+1))*self.cell_size, self.grid_y*self.cell_size)
            self.body.append(segment)

        self.positions = [(self.grid_x-i, self.grid_y) for i in range(len(self.body)+1)]