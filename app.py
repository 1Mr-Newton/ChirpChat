from flet import *
import pickle
from utils.colors import *
from utils.dimensions import *
from pages.boarding import BoardingPage
from pages.login import LoginPage
from pages.register import RegisterPage
from pages.home import HomePage
from service.service import *

class WindowDrag(UserControl):
  def __init__(self,color):
    super().__init__()
    self.color = color
  def build(self):
    return Container(content=WindowDragArea(height=10,content=Container(bgcolor=self.color)))


class App(UserControl):
  def __init__(self,pg:Page):
    super().__init__()

    pg.window_title_bar_hidden = True
    pg.window_frameless = True
    pg.window_title_bar_buttons_hidden = True
    pg.bgcolor = colors.TRANSPARENT
    pg.window_bgcolor = colors.TRANSPARENT
    pg.fonts = {
    "SF Pro Bold":"fonts/SFProText-Bold.ttf",
    "SF Pro Heavy":"fonts/SFProText-Heavy.ttf",
    "SF Pro HeavyItalic":"fonts/SFProText-HeavyItalic.ttf",
    "SF Pro Light":"fonts/SFProText-Light.ttf",
    "SF Pro Medium":"fonts/SFProText-Medium.ttf",
    "SF Pro Regular":"fonts/SFProText-Regular.ttf",
    "SF Pro Semibold":"fonts/SFProText-Semibold.ttf",
    "SF Pro SemiboldItalic":"fonts/SFProText-SemiboldItalic.ttf",
  }
    pg.window_width = 350



    self.pg  = pg
    self.delay = 0.1
    self.anim = animation.Animation(300,AnimationCurve.EASE_IN_OUT_CUBIC)


    self.login_page = LoginPage(self.switch_page,self.anim)
    self.home_page = HomePage(self.switch_page,self.anim)
    self.register_page = RegisterPage(self.switch_page,self.anim)
    self.boarding_page = BoardingPage(self.switch_page,self.anim)


    try:
      with open("token.pickle", "rb") as token_file:
        self.token = pickle.load(token_file)
    except FileNotFoundError:
      self.token = None

    self.switch_control = [
      self.login_page,
      self.register_page,
      self.boarding_page,
      self.home_page,
    ]

    self.init_helper()
  def switch_page(self,e: TapEvent):

    if e.control.data == 'get_start_clicked':
      for control in self.switch_control:
        control.base.offset.x = -1
        control.update()
      sleep(self.delay)
      self.register_page.base.offset.x = 0
      self.register_page.update()


    if e.control.data == 'login_clicked':
      user = {
        "username":self.login_page.username_field.content.content.value,
        "password":self.login_page.password_field.content.content.value
      }
      print(user)
      sleep(self.delay)
      self.home_page.base.offset.x = 0
      self.home_page.update()


    if e.control.data == 'register_clicked':
      _email = self.register_page.email_field.content.content.value
      _password = self.register_page.password_field.content.content.value
      _confirm_password = self.register_page.confirm_password_field.content.content.value
      _username = self.register_page.username_field.content.content.value

      if _password != _confirm_password or len(_password) < 8 or len(_confirm_password) < 8:
        self.register_page.password_field.content.border = border.all(color='red',width=1)
        self.register_page.confirm_password_field.content.border = border.all(color='red',width=1)
      if len(_username) < 4:
        self.register_page.username_field.content.border = border.all(color='red',width=1)

      if len(_email) < 8:
        self.register_page.email_field.content.border = border.all(color='red',width=1)

      self.register_page.update()

      if _password == _confirm_password and len(_email) > 10 and len(_password) > 7 and len(_username) > 5:
        user = {
          "username":_username,
          "email":_email,
          "password":_password,
        }


        self.pg.splash = ProgressBar()
        self.pg.update()
        u = create_user(_email,_password,_username)
        
        if u:
          expires_in = 86400
          custom_token = auth.create_custom_token(u)
          
          with open("token.pickle", "wb") as token_file:
            pickle.dump(u, token_file)
          self.pg.splash = None
          self.pg.update()
          self.register_page.base.offset.x = -1
          self.register_page.update()
          self.home_page.base.offset.x = 0
          self.home_page.update()



    if e.control.data == 'go_back_to_login':
      self.login_page.base.offset.x = 0
      self.login_page.update()



      

  def init_helper(self):
    self.notch = Container(
      bgcolor='white',
      content=Row(
      controls=[
        Text(
          value='9:19'
        ),
        Row(
          spacing=0,
          controls=[
            Image(
              src='assets/icons/network.png',
              color='black',
              scale=0.4,
            ),
            Image(
              src='assets/icons/wifi.png',
              scale=0.4,
            ),
            Image(
              src='assets/icons/battery.png',
              scale=0.4,
            ),

          ]
        )
      ]
    )
    )

    self.pg.add(
      
      Container(
        height=base_height,
        width=base_width,
        bgcolor=base_color,
        expand=True,
        clip_behavior=ClipBehavior.ANTI_ALIAS,
        border_radius=br,
        content=Column(
          spacing=0,
          expand=True,
          controls=[
            WindowDrag(chat_screen_base_color),
            Stack(
              expand=True,
              controls=[self.home_page] if self.token else [self.login_page,self.register_page,self.home_page,self.boarding_page,],
              # controls=[n for n in range(3)],
            )
          
          ]
        )
      )
    )


app(target=App,assets_dir='assets')    