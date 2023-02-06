from flet import *
from utils.colors import *
from utils.dimensions import *
from service.service import users

class ChatScreen(UserControl):
  def __init__(self,offset_anim,move_to_dm):
    super().__init__()
    self.offset_anim= offset_anim
    self.move_to_dm = move_to_dm

    self.msg_obj = Container(

            height=60,
            padding=padding.symmetric(horizontal=20),
            content=Container(
              
              content=Row(
                
                controls=[
                  Container(
                    height=50,
                    width=50,
                    bgcolor='purple',
                    border_radius=40,

                  ),
                  Container(
                    on_click=self.move_to_dm,
                    data='dm',
                    content=Column(
                      spacing=0,
                      alignment='center',
                      controls=[
                        Row(
                          width=220,
                          alignment='spaceBetween',
                          vertical_alignment='center',
                          controls=[
                            Text(
                              value='Jon Snow',
                              font_family='SF Pro Medium',
                              size=14,

                            ),
                            Text(
                              value='04:20',
                              font_family='SF Pro Regular',
                              size=12,

                            ),
          
                          ]
                        ),
                        Row(
                          spacing=2,
                          vertical_alignment='center',
                          controls=[
                            Container(
                              padding=padding.only(top=3),
                              content=Icon(
                                icons.DONE,
                                size=12
                              )
                            ),
                            Text(
                              value='What was the best',
                              size=12,
                              no_wrap=True,
                              width=170,
                            ),
                            
                          ]
                        ),
                      ]
                    )
                    
                  )
                ]
              )
            )


          
          )
  


    self.base = Container(
      height=base_height-130,
      bgcolor=chat_screen_base_color,
      animate_offset=self.offset_anim,
      offset=transform.Offset(0,0),
      padding=padding.only(top=35),
      # expand=True,
      content=Column(
        controls=[
          Container(
            padding=padding.only(left=20,right=20),
            content=Container(
              border_radius=8,
              height=40,
              bgcolor='white12',
            ),
          ),

          Container(
            padding=padding.only(left=20,right=20),
            content=Text(
              'RECENT UPDATES',
              font_family='SF Pro Semibold',
            ),
          ),

          

          Container(
            padding=padding.only(left=20,right=3),
            content=Row(
              scroll='auto',
              height=55,
              controls=[
                Container(
                  height=50,width=50,
                  bgcolor='red',
                  border_radius=30,
                  padding=5,
                  content=Image(
                    src='assets/images/1.jpg'
                  )
                ),
                Container(
                  height=50,width=50,
                  bgcolor='red',
                  border_radius=30,
                  padding=5,
                  content=Image(
                    src='assets/images/1.jpg'
                  )
                ),
                
                
              ]
            )
          ),

          Divider(height=0.2,thickness=0.2),

          Column(
            height=420,
            scroll='auto',
            controls=[ self.mg_obj(user.get('username'),'last_message','05:30','assets/images/1.jpg') for user in users ]
          )
        ]
      )
    )
        
  def mg_obj(self,username,last_message,last_message_time,profile_pic_url):
      return Container(
            height=60,
            padding=padding.symmetric(horizontal=20),
            content=Container(
              content=Row(
                controls=[
                  Container(
                    clip_behavior=ClipBehavior.ANTI_ALIAS,
                    height=50,
                    width=50,
                    bgcolor='purple',
                    border_radius=40,
                    content=Image(
                      src=profile_pic_url,
                      fit=ImageFit.COVER,
                      border_radius=30
                    )
                  ),
                  Container(
                    on_click=self.move_to_dm,
                    data=[
                      'dm',{
                        "username":username,
                        
                      }
                    ],
                    content=Column(
                      spacing=0,
                      alignment='center',
                      controls=[
                        Row(
                          width=220,
                          alignment='spaceBetween',
                          vertical_alignment='center',
                          controls=[
                            Text(
                              value=username,
                              font_family='SF Pro Medium',
                              size=14,

                            ),
                            Text(
                              value=last_message_time,
                              font_family='SF Pro Regular',
                              size=12,

                            ),
          
                          ]
                        ),
                        Row(
                          spacing=2,
                          vertical_alignment='center',
                          controls=[
                            Container(
                              padding=padding.only(top=3),
                              content=Icon(
                                icons.DONE,
                                size=12
                              )
                            ),
                            Text(
                              value=last_message,
                              size=12,
                              no_wrap=True,
                              width=170,
                            ),
                            
                          ]
                        ),
                      ]
                    )
                    
                  )
                ]
              )
            )
          )
          
  # def move_to_dm(self,e):
  #   print(e.control.data)

  def build(self):
    return self.base