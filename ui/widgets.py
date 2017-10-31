from .base import Widget

class Text(Widget):
    def __init__(self, tft, x, y, background=0x000000,
                 color=0xFFFFFF, font=None, transparent=True,
                 fixedwidth=False, rotate=False,
                 text=""):
        super().__init__(tft, x, y, background=background)
        self.text = text
        self.color = color
        self.font = font
        if self.font is None:
            self.font = tft.FONT_Default
        self.transparent = transparent
        self.fixedwidth = fixedwidth
        self.rotate = rotate

        self._set_font()
        self._compute_size()

    def draw(self):
        self._setwin()
        self._set_font()
        self._clear()
        self.tft.text(0, 0, self.text, self.color)

    def _set_font(self):
        self.tft.font(self.font, rotate=self.rotate,
                      transparent=self.transparent,
                      fixedwidth=self.fixedwidth,
                      color=self.color)

    def _compute_size(self):
        self._fw, self._fh = self.tft.fontSize()
        self.width = self.tft.textWidth(self.text)
        self.height = self._fh

    def set_text(self, text):
        self.text = text
        self._compute_size()

    def set_font(self, font):
        self.font = font
        self._compute_size()

class Image(Widget):
    def __init__(self, tft, x, y, width, height, filename, image_type):
        super().__init__(tft, x, y)
        self.width = width
        self.height = height
        self.filename = filename
        self.image_type = image_type

    def draw(self):
        self._setwin()
        self._clear()
        self.tft.image(0, 0,
                       self.filename, type=self.image_type)
