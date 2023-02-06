from flet import *
from utils.colors import *
from utils.dimensions import *

class RegisterPage(UserControl):
  def __init__(self,switch_page:object,anim):
    super().__init__()
    self.anim = anim
    self.switch_page=switch_page
    
    self.username_field = Container(
            padding=padding.symmetric(horizontal=30),
            content=Container(
              height=50,
              border=border.all(color=input_outline_color,width=1),
              bgcolor=input_fill_color,
              border_radius=10,
              padding=padding.symmetric(horizontal=20),
              content=TextField(
                hint_text='Username',
                hint_style=TextStyle(
                  color=input_outline_color,
                  
                ),
                border=InputBorder.NONE
              )
            ),
          )

    self.email_field = Container(
            padding=padding.symmetric(horizontal=30),
            content=Container(
              height=50,
              border=border.all(color=input_outline_color,width=1),
              bgcolor=input_fill_color,
              border_radius=10,
              padding=padding.symmetric(horizontal=20),
              content=TextField(
                hint_text='Email',
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

    self.confirm_password_field = Container(
            padding=padding.symmetric(horizontal=30),
            content=Container(
              height=50,
              border=border.all(color=input_outline_color,width=1),
              bgcolor=input_fill_color,
              border_radius=10,
              padding=padding.symmetric(horizontal=20),
              content=TextField(
                hint_text='Confirm Password',
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
        # horizontal_alignment='center',
        controls=[
          Container(
            Image(
              src='assets/icons/login_illustration.png',
              # scale=0.7
            ),
            alignment=alignment.center,
            # bgcolor='white'
          ), 
          Container(
            height=20,
          ),
          
          Container(
            padding=padding.symmetric(horizontal=35),
            content=Text(
              value='We are glad to have you',
              text_align='center',
              font_family='SF Pro semibold',
              size=20,
              color="white",
            ),
          ),
          Container(
            
            padding=padding.symmetric(horizontal=35),
            content=Text(
              value="Please register below",
              font_family='SF Pro Regular',
              size=16,
              color=input_outline_color,
            ),
          ),
          
          self.username_field,
          
          self.email_field,
          

          self.password_field,
          
          self.confirm_password_field,

          Container(height=20),
          
          Container(
            padding=padding.symmetric(horizontal=30),
            content=Container(
              content=Row(
                spacing=2,
                alignment='center',
                controls=[
                  Text(
                  value="Already have an account?",
                  font_family='SF Pro Regular',
                  size=12,
                  color=input_outline_color,
                ),
                Container(
                  data='go_back_to_login',
                  on_click=self.switch_page,
                  content = Text(
                    value="Login",
                    font_family='SF Pro Regular',
                    size=12,
                    color='#ffffff',
                  ),
                )
              ]
            ),
            ),
          ),


          # Container(height=2),
          
          Container(
            on_click=self.switch_page,
            data = 'register_clicked',
            padding=padding.symmetric(horizontal=30),
            content=Container(
              height=55,
              bgcolor=button_fill_color,
              border_radius=10,
              alignment=alignment.center,
              content=Text(
                value='Register',
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