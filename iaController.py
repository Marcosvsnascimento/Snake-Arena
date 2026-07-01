class IAController:

    def __init__(self):
        self.enemy = None
        self.point = None

    def set_game(self, enemy, point):
        self.enemy = enemy
        self.point = point

    def get_direction(self, snake):

        enemy = self.enemy
        point = self.point

        candidates = []

        dx = point.grid_x - snake.grid_x
        dy = point.grid_y - snake.grid_y

        if dx > 0:
            candidates.append((1,0))
        elif dx < 0:
            candidates.append((-1,0))

        if dy > 0:
            candidates.append((0,1))
        elif dy < 0:
            candidates.append((0,-1))

        for d in [(1,0),(-1,0),(0,1),(0,-1)]:
            if d not in candidates:
                candidates.append(d)


        opposite = (-snake.direction[0], -snake.direction[1])

        for d in candidates:

            if d == opposite:
                continue

            if self.safe(snake, enemy, d):
                return d

        return snake.direction

    def safe(self, snake, enemy, direction):

        nx = snake.grid_x + direction[0]
        ny = snake.grid_y + direction[1]

        if nx < 0 or nx >= 40:
            return False

        if ny < 0 or ny >= 27:
            return False

        if (nx, ny) in snake.positions[:-1]:
            return False

        if (nx, ny) in enemy.positions:
            return False

        return True