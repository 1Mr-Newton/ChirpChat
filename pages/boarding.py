from flet import *
from utils.colors import *
from utils.dimensions import *

class BoardingPage(UserControl):
  def __init__(self,switch_page:object,anim):
    super().__init__()
    self.switch_page=switch_page
    self.anim = anim
    self.base = Container(
      offset=transform.Offset(0,0),
      animate_offset=self.anim,
      # on_click=self.switch_page,
      expand=True,
      bgcolor=base_color,
      alignment=alignment.center,
      content=Column(
        horizontal_alignment='center',
        controls=[
          Container(
            Image(
              src='assets/icons/multi_icons.png',
              # scale=0.7
            ),
            # bgcolor='white'
          ),
          Container(
            height=20,
          ),
          Container(
            content=Image(
            src='assets/icons/logo.png',
          ),
          ),
          Container(
            padding=padding.symmetric(horizontal=35),
            content=Text(
              value='Sign in to your account to see your messages and media from friends',
              text_align='center',
              font_family='SF Pro Medium',
              size=13,
              color=input_outline_color,
            ),
          ),
          Container(height=2),
          Container(
            on_click=self.switch_page,
            data='get_start_clicked',
            padding=padding.symmetric(horizontal=30),
            content=Container(
              height=55,
              bgcolor=button_fill_color,
              border_radius=10,
              alignment=alignment.center,
              content=Text(
                value='Get Started',
                font_family='SF Pro Semibold',
                size=16,
              ),
            ),
          ),
        ]
      )
    )

  def build(self):
    return self.base