from flet import *
from utils.colors import *
from utils.dimensions import *

class DmScreen(UserControl):
  def __init__(self,offset_anim,back_to_chat_screen,dm_data):
    super().__init__()
    self.offset_anim = offset_anim
    self.back_to_chat_screen = back_to_chat_screen
    self.dm_data = dm_data
    self.display_name = Text(
      value=self.dm_data[1].get('username'),
      size=14,
      no_wrap=True,
      font_family='SF Pro Medium',
      width=100
    )


    self.received_msg_template = Row(
      alignment='start',
      spacing=5,
      controls=[
        Container(
          # width=200,
          # height=60,
          padding=10,
          border_radius=border_radius.BorderRadius(
            topLeft=12,topRight=12,
            bottomLeft=0,bottomRight=12),
          bgcolor=received_msg_bgcolor,
          content=Text(
            value='Hey bruh\nHow\'s it going?',
            size=14,
            font_family='SF Pro Regular',
            width=200,
            # max_lines=2
          )
        )
      ]
    )

    self.sent_msg_template = Row(
      alignment='end',
      spacing=5,
      controls=[
        Container(
          # width=200,
          # height=60,
          padding=10,
          border_radius=border_radius.BorderRadius(
            topLeft=12,topRight=12,
            bottomLeft=12,bottomRight=0),

          bgcolor=nbi_select_color,
          content=Text(
            value='Man I\'m alright. Just trynna finish some works. What is up ?',
            size=14,
            font_family='SF Pro Regular',
            width=200,
            # max_lines=2
          )
        )
      ]
    )
    
    
    self.msg_with_media =  Container(
          border_radius=border_radius.BorderRadius(
            topLeft=15,topRight=15,
            bottomLeft=0,bottomRight=15),
          bgcolor=received_msg_bgcolor,
            padding=15,
          content=Column(
          spacing=10,
            controls=[
              Container(
                clip_behavior=ClipBehavior.ANTI_ALIAS,
                height=190,
                width=190,
                content=Image(
                  src='assets/images/2.jpg',
                  fit=ImageFit.COVER,
                  # height=230 ,
                  semantics_label= "Yes",
                  border_radius=10
                  # width=200,
                )
              ),
              Text(
                value='Some random caption for a photo, testing my app\nTesting app 1 2 🤣🤣🤣',
                width=200,
              )
            ]
          )
        )
        

    self.chat_area = Column(
      height=520,
      scroll='auto',
      controls=[
        
      ]

    )


    self.base = Container(
      height=0,
      padding=padding.symmetric(horizontal=20),
      animate_offset=self.offset_anim,
      bgcolor=chat_screen_base_color,
      offset=transform.Offset(0,0),
      alignment=alignment.center,
      # expand=True,
      content=Column(
        controls=[
          Container(
            padding=padding.only(top=20),
            content=Row(
              alignment='spaceBetween',
              controls=[
                Container(
                  on_click=self.back_to_chat_screen,
                  data = ['chats'],
                  content=Icon(
                    icons.ARROW_BACK_IOS_OUTLINED,
                    size=14,
                  ),
                ),
                Row(
                  controls=[
                    Container(
                      height=40,
                      width=40,
                      bgcolor='white',
                      border_radius=30,
                      clip_behavior=ClipBehavior.ANTI_ALIAS,
                      content=Image(
                        fit=ImageFit.COVER,
                        border_radius=30,
                        src='assets/images/2.jpg',
                        
                      )
                    ),
                    Column(
                      spacing=2,
                      controls=[
                        self.display_name,
                        Text(
                          value='Last seen: 06:20 PM',
                          size=10,
                          font_family='SF Pro Medium',
                          color=last_seen_color
                        ),
                      ]
                    ),
                  ]
                ),
                Row(
                  controls=[
                    Image(
                      src="assets/icons/video_call.png",
                      color='white',
                      scale=0.7
                    ),
                    Image(
                      src="assets/icons/calls_outlined.png",
                      color='white',
                      scale=0.8
                    ),
                  ]
                )
              ]
            )
          ),

          Divider(height=0.2,thickness=0.2),
          self.chat_area ,
          Container(
            height=55,
            bgcolor=search_field_bgcolor,
            border_radius=30,
            content=Row(
              alignment='spaceBetween',
              controls=[
                Container(
                  padding=padding.only(top=10,bottom=10,right=8,left=20),
                  content=Row(
                    width=200,
                    controls=[
                      Container(
                        width=20,
                        content=Icon(
                          icons.EMOJI_EMOTIONS_OUTLINED,
                          size=14,
                        )
                      ),
                      TextField(
                        expand=True,
                        hint_text='Send a message',
                        hint_style=TextStyle(
                          size=12
                        ),
                        # border=InputBorder.NONE,
                        border=InputBorder.OUTLINE,
                        border_color=search_field_bgcolor,
                        content_padding=0,
                        multiline=True,
                        text_style=TextStyle(
                          size=14,

                        )
                      )
                    ]
                  ),
                ),
                Container(
                  height=45,
                  width=45,
                  bgcolor=nbi_select_color,
                  border_radius=25,
                  margin=5,
                  alignment=alignment.center,
                  clip_behavior=ClipBehavior.ANTI_ALIAS,
                  padding=10,
                  content=Image(
                    src='assets/icons/send.png',
                    color='white',
                    scale=0.8
                    
                  )
                )
              ]
            )
          )

        ]
      )
    )
  def ms_obj(self,msg):
    return Row(
      alignment='start',
      spacing=5,
      controls=[
        Container(
          # width=200,
          # height=60,
          padding=10,
          border_radius=border_radius.BorderRadius(
            topLeft=12,topRight=12,
            bottomLeft=0,bottomRight=12),
          bgcolor=received_msg_bgcolor,
          content=Text(
            value=msg,
            size=14,
            font_family='SF Pro Regular',
            width=200,
            # max_lines=2
          )
        )
      ]
    )  

  def build(self):
    return self.base