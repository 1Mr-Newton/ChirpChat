from flet import *
from utils.colors import *
from utils.dimensions import *

class StoriesScreen(UserControl):
  def __init__(self,offset_anim):
    super().__init__()
    self.offset_anim = offset_anim
    
    self.base = Container(
      height=base_height-130,
      animate_offset=self.offset_anim,
      bgcolor=chat_screen_base_color,
      offset=transform.Offset(0,0),
      alignment=alignment.center,
      expand=True,
      content=Text('this is stories screen')
    )

  def build(self):
    return self.base