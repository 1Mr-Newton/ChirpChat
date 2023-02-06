from flet import *
from utils.colors import *
from utils.dimensions import *

class CallScreen(UserControl):
  def __init__(self,offset_anim):
    super().__init__()
    self.offset_anim = offset_anim
    
    self.base = Container(
      height=base_height-130,
      padding=padding.only(top=20,right=20,left=20),
      offset=transform.Offset(0,0),
      animate_offset=self.offset_anim,
      bgcolor=chat_screen_base_color,
      alignment=alignment.center,
      expand=True,
      content=Column(
        controls=[
          Row(
            alignment='spaceBetween',
            controls=[
              Container(
                content=Text(
                  'Edit',
                  size=14,
                  color=button_fill_color,
                  font_family='SF Pro Semibold,'
                ),
              ),

              Container(
                content=Icon(
                  icons.CALL_RECEIVED_OUTLINED,
                  size=14,
                  color=button_fill_color,
                )
              )

            ]
          ),
          
          Row(
            controls=[
              Text(
                value='Calls',
                size=24,
                font_family='SF Pro Semibold'


              ),
            ]
          ),
          
          Container(
            height=30,bgcolor=search_field_bgcolor,
            padding=padding.only(left=10),#,top=5,bottom=5,right=10),
            alignment=alignment.center,
            border_radius=8,
            content=Row(
              controls=[
                Container(
                  content=Icon(
                    icons.SEARCH_OUTLINED,
                    color='white',
                    size=12,
                  ),
                ),
                TextField(
                  expand=True,
                  hint_text='Search your calls',
                  hint_style=TextStyle(
                    color=msg_time_color,
                    font_family='SF Pro Regular'
                  ),
                  border=InputBorder.NONE,
                  # content_padding=0,
                  color=msg_time_color,
                  # font_family='SF Pro Regular'
                ),
              ]
            )
          ),


          Divider(height=0.2,thickness=0.2),
          
          Container(
            content=Row(
              controls=[
                Column(
                  controls=[
                    Container(
                      Row(
                        width=280,
                        alignment='spaceBetween',
                        controls=[
                          Row(
                            controls=[
                              Container(
                                height=40,
                                width=40,
                                border_radius=25,
                                bgcolor='white',
                                content=Image(
                                  src="assets/images/"
                                )
                              ),
                              Column(
                                alignment='spaceAround',
                                controls=[
                                  Text(
                                    value="Name",
                                    size=14,
                                    color=name_color,
                                    font_family='SF Pro Medium',
                                  ),
                                  Row(
                                    spacing=1,
                                    controls=[
                                      Image(
                                        src='assets/icons/calls.png',
                                        color=msg_time_color,
                                        scale=0.4,
                                      ),
                                      Text(
                                        value="incoming",
                                        size=10,
                                        color=msg_time_color,
                                        font_family='SF Pro Medium',
                                      ),
                                    ]
                                  )

                                ]
                              ),
                          
                            ]
                          ),
                          
                          Container(
                            content=Text(
                              value="6:30",
                              size=12,
                              color=msg_time_color,
                              font_family='SF Pro Medium',
                            ),
                          )
                        ]
                      ),
                    ),

                  ]
                )
              ]
            )
          )
        ]
      )
    )

  def build(self):
    return self.base