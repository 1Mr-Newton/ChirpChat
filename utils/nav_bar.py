from flet import *
from utils.colors import *
from utils.dimensions import *

class CustomBottomNav(UserControl):
  def __init__(self,nav_switch):
    super().__init__()
    self.nav_switch = nav_switch
    
    self.base = Row(
      alignment='center',
      controls=[
        Container(
          bgcolor=bnb_color,
          width=300,
          border_radius=30,
          padding=padding.symmetric(horizontal=30),
          margin=margin.only(bottom=12),
          content=Row(
            alignment='spaceBetween',
            height=50,
            controls=[
              Container(
                on_click=self.nav_switch,
                data = ['chats'],
                content=Column(
                    alignment='center',
                    horizontal_alignment='center',
                    spacing=2,
                  controls=[
                    Image(
                      src='assets/icons/chat.png',
                      color=nbi_select_color,
                      
                    ),
                    Text(
                      'Chat',size=bnt_size,
                      font_family='SF Pro Semibold',
                      color=nbi_select_color
                    )
                  ]
                )
              ),

              Container(
                data = ['calls'],
                on_click=self.nav_switch,
                content=Column(
                    alignment='center',
                    horizontal_alignment='center',
                    spacing=2,
                  controls=[
                    Image(
                      src='assets/icons/calls_outlined.png',
                      color=msg_time_color,
                      
                    ),
                    Text(
                      'Calls',size=bnt_size,
                      font_family='SF Pro Semibold',
                      color=msg_time_color
                    )
                  ]
                )
              ),

              Container(
                data = ['channels'],
                on_click=self.nav_switch,
                content=Column(
                    alignment='center',
                    horizontal_alignment='center',
                    spacing=2,
                  controls=[
                    Image(
                      src='assets/icons/groups_outlined.png',
                      color=msg_time_color,
                      
                    ),
                    Text(
                      'Channels',size=bnt_size,
                      font_family='SF Pro Semibold',
                      color=msg_time_color
                    )
                  ]
                )
              ),

              Container(
                data = ['stories'],
                on_click=self.nav_switch,
                content=Column(
                    alignment='center',
                    horizontal_alignment='center',
                    spacing=2,
                  controls=[
                    Image(
                      src='assets/icons/status_outlined.png',
                      color=msg_time_color,
                      
                    ),
                    Text(
                      'Stories',size=bnt_size,
                      font_family='SF Pro Semibold',
                      color=msg_time_color
                    )
                  ]
                )
              ),

              Container(
                data = ['settings'],
                on_click=self.nav_switch,
                content=Column(
                    alignment='center',
                    horizontal_alignment='center',
                    spacing=2,
                  controls=[
                    Image(
                      src='assets/icons/settings_outlined.png',
                      color=msg_time_color,
                      
                    ),
                    Text(
                      'Settings',size=bnt_size,
                      font_family='SF Pro Semibold',
                      color=msg_time_color
                    )
                  ]
                )
              ),

            ]
          )
        )
      ]
    )

  def build(self):
    return self.base