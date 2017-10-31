class Widget:
    def __init__(self, tft, x, y, background=0x000000):
        self.tft = tft
        self.x = x
        self.y = y
        self.background = background

    def _setwin(self):
        self.tft.setwin(self.x, self.y,
                        self.x+self.width-1, self.y+self.height-1)

    def _clear(self):
        self.tft.clearwin(self.background)

    def draw(self):
        print("not implemented")


class Screen(Widget):
    def __init__(self, ui, background=0x000000):
        tft = ui.tft
        x, y, self.width, self.height = ui.screen_dimensions
        super().__init__(tft, x, y, background=background)
        self._widgets = []

    def add_widget(self, widget):
        self._widgets.append(widget)  # no handling of z index for now.
        # should we handle sizing and position here ?

    def draw(self):
        for widget in self._widgets:
            widget._setwin()
            widget.draw()

    def clear(self):
        self._setwin()
        self._clear()

    def _get_actions(self):
        return ['up', 'menu', 'down']

    def _on_btn(self, btn):
        print('btn %r pressed' % btn)
