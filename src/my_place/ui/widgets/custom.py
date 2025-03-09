from kivy.uix.widget import Widget
from kivy.graphics import Color, Rectangle, Line
from kivy.properties import ColorProperty

class CustomBorder(Widget):
    border_size : int = 2
    border_color : ColorProperty = ColorProperty((0, 0, 0, 1))
    
    def __init__(self, **kw):
        super().__init__(**kw)
        with self.canvas:
            Color(rgba=self.border_color)
            self.line = Line(
                width=self.border_size,
                rectangle=self._calc_border_rect(self.pos, self.size),
            )
            
        self.bind(size=self._update_line, pos=self._update_line)
        
        self.padding = [x + self.border_size for x in self.padding]
        
    def _calc_border_rect(self, pos, size):
        return (pos[0], pos[1], size[0]-self.border_size, size[1]-self.border_size)
            
    def _update_line(self, instance, value):
        self.line.rectangle = self._calc_border_rect(instance.pos, instance.size)

class CustomBackgroundColor(Widget):
    background_color : ColorProperty = ColorProperty((1, 1, 1, 1))
    
    def __init__(self, **kw):
        super().__init__(**kw)
        with self.canvas.before:
            Color(rgba=self.background_color)
            self.rect = Rectangle(
                pos=self.pos,
                size=self.size
            )
            
        self.bind(size=self._update_rect, pos=self._update_rect)
            
    def _update_rect(self, instance, value):
        self.rect.pos = instance.pos
        self.rect.size = instance.size