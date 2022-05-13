from .env import WALL_IMG_PATH_DICT
from .Props import Props


class Obstacle(Props):
    def __init__(self, _id: int, x: int, y: int, width: int, height: int):
        super().__init__(x, y, width, height)
        self._id = _id
        self.lives = 5
        self.img_path_list = WALL_IMG_PATH_DICT

    def update(self, *args, **kwargs) -> None:
        if self.lives <= 0:
            self.kill()

    def collide_with_bullets(self):
        if self.lives > 0:
            self.lives -= 1

    def get_xy_pos(self):
        return self.rect.x, self.rect.y

    def get_info(self):
        info = {"id": f"wall_{self._id}.{self.lives}", "x": self.rect.x, "y": self.rect.y, "lives": self.lives}
        return info

    def get_image_data(self):
        if self.lives > 0:
            super().get_image_data()
            self.image_data["id"] = f"wall_{self._id}.{self.lives}"
            return self.image_data
