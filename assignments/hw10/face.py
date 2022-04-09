from graphics import Circle, Line, Polygon


class Face:
    def __init__(self, window, center, size):
        eye_size = 0.15 * size
        eye_off = size / 3.0
        mouth_size = 0.8 * size
        mouth_off = size / 2.0

        mouth_size_circle = 0.15 * size

        self.window = window
        self.head = Circle(center, size)
        self.head.draw(window)
        self.left_eye = Circle(center, eye_size)
        self.left_eye.move(-eye_off, -eye_off)
        self.right_eye = Circle(center, eye_size)
        self.right_eye.move(eye_off, -eye_off)
        self.left_eye.draw(window)
        self.right_eye.draw(window)

        point_1 = center.clone()
        point_1.move(-mouth_size / 2, mouth_off)
        point_2 = center.clone()
        point_2.move(mouth_size / 2, mouth_off)

        point_3 = center.clone()
        point_3.move(center, mouth_off + 5)

        self.mouth = Line(point_1, point_2)
        self.mouth.draw(window)

        self.mouth_tri = Polygon(point_1, point_2, point_3)
        self.mouth_tri.move(0, mouth_off)

        self.mouth_circle = Circle(center, mouth_size_circle)
        self.mouth_circle.move(0, mouth_off)

        self.left_eye_blink = Line(point_1, point_2)
        self.left_eye_blink.move(-eye_off, -eye_off)

    def smile(self):
        self.mouth.undraw()
        self.mouth_tri.draw(self.window)

    def shock(self):
        self.mouth.undraw()
        self.mouth_circle.draw(self.window)

    def wink(self):
        self.mouth.undraw()
        self.mouth_tri.draw(self.window)

        self.left_eye.undraw()
        self.left_eye_blink.draw(self.window)


