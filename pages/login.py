from flet import *
from utils.colors import *
from utils.dimensions import *

class LoginPage(UserControl):
  def __init__(self,switch_page:object,anim):
    super().__init__()
    self.switch_page=switch_page
    self.anim = anim

    self.username_field = Container(
            padding=padding.symmetric(horizontal=30),
            content=Container(
              height=50,
              border=border.all(color=input_outline_color,width=1),
              bgcolor=input_fill_color,
              border_radius=10,
              padding=padding.symmetric(horizontal=20),
              content=TextField(
                hint_text='Email / Username / Phone',
                hint_style=TextStyle(
                  color=input_outline_color,
                  
                ),
                border=InputBorder.NONE
              )
            ),
          )

    self.password_field = Container(
            padding=padding.symmetric(horizontal=30),
            content=Container(
              height=50,
              border=border.all(color=input_outline_color,width=1),
              bgcolor=input_fill_color,
              border_radius=10,
              padding=padding.symmetric(horizontal=20),
              content=TextField(
                hint_text='Password',
                hint_style=TextStyle(
                  color=input_outline_color,
                  
                ),
                border=InputBorder.NONE
              )
            ),
          )

    self.base = Container(
      offset=transform.Offset(0,0),
      animate_offset=self.anim,
      bgcolor=base_color,
      expand=True,
      alignment=alignment.center,
      content=Column(
        expand=True,
        controls=[
          Container(
            Image(
              src='assets/icons/login_illustration.png',
              # scale=0.7
            ),
            alignment=alignment.center,
            # bgcolor='white'
          ), 
          
          Container(height=20,),
          
          Container(
            padding=padding.symmetric(horizontal=35),
            content=Text(
              value='Let\'s sign you in',
              text_align='center',
              font_family='SF Pro semibold',
              size=20,
              color="white",
            ),
          ),
          Container(
            padding=padding.symmetric(horizontal=35),
            content=Text(
              value="Welcome back,\nYou've been missed!",
              font_family='SF Pro Regular',
              size=16,
              color=input_outline_color,
            ),
          ),
    
          Container(height=10),

          self.username_field,
          
          Container(height=5),

          self.password_field,

          Container(
            padding=padding.symmetric(horizontal=30),
            content=Container(
              content=Row(
                alignment='end',
                controls=[
                  Text(
                  value="Forgot password",
                  font_family='SF Pro Regular',
                  size=12,
                  color='#ccffffff',
                ),
              ]
            ),
            ),
          ),
          
          Container(height=20),

          Container(
            padding=padding.symmetric(horizontal=30),
            content=Container(
              content=Row(
                spacing=2,
                alignment='center',
                controls=[
                  Text(
                  value="Don't have an account?",
                  font_family='SF Pro Regular',
                  size=12,
                  color=input_outline_color,
                ),
                  Container(
                    on_click=self.switch_page,
                    data='get_start_clicked',
                    content=  Text(
                      value="Register",
                      font_family='SF Pro Regular',
                      size=12,
                      color='white',
                    ),
                  )
              ]
            ),
            ),
          ),

          Container(height=10),

          Container(
            on_click=self.switch_page,
            data='login_clicked',
            padding=padding.symmetric(horizontal=30),
            content=Container(
              height=55,
              bgcolor=button_fill_color,
              border_radius=10,
              alignment=alignment.center,
              content=Text(
                value='Login',
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