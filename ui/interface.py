from .base import Widget, Screen


class Controls(Widget):
    def __init__(self, tft, height, screen_width, screen_height):
        self.height = height
        self.width = screen_width
        self.zone_width = int(self.width / 3)
        self.is_dirty = True
        super().__init__(tft, 0, screen_height-self.height,
                         background=tft.BLACK)

    def draw(self):
        self._setwin()
        # self._clear() # not using it for now... needed ?
        self.tft.line(0, 0, self.width, 0, 0x444444)  # horizontal bar
        self.tft.line(self.zone_width-1, 0, self.zone_width-1, self.height-1,
                      0x444444)
        self.tft.line(self.width-self.zone_width+1, 0,
                      self.width-self.zone_width+1, self.height-1, 0x444444)

        self.tft.image(self.tft.CENTER, self.tft.CENTER,
                       'icons/ic_menu_white_24dp.jpg', type=self.tft.JPG)
        self.tft.image(int(self.zone_width/2-(24/2)), self.tft.CENTER,
                       'icons/ic_arrow_upward_white_24dp.jpg', type=self.tft.JPG)
        self.tft.image(int(self.width-(self.zone_width/2+(24/2))), self.tft.CENTER,
                       'icons/ic_arrow_downward_white_24dp.jpg', type=self.tft.JPG)


class UI:
    def __init__(self, tft, width=320, height=240):
        self.tft = tft
        self.width = width
        self.height = height
        self._current_screen = None
        self._controls = Controls(self.tft, 30, width, height)

    @property
    def screen_dimensions(self):
        """ Returns the x, y, width and height of the screen zone.
        """
        return (0, 0, self.width, self.height-self._controls.height)

    def set_screen(self, screen):
        self._current_screen = screen

    def draw_controls(self):
        self._controls.draw()

    def redraw_screen(self):
        if self._controls is not None:
            if self._controls.is_dirty:
                self._controls.draw()

        if self._current_screen is not None:
            self._current_screen.draw()
