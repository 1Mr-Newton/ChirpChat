from flet import *
from utils.colors import *
from utils.dimensions import *
from utils.nav_bar import CustomBottomNav
from utils.chat_screen import ChatScreen
from utils.calls_screen import CallScreen
from utils.stories import StoriesScreen
from utils.channels import ChannelScreen
from utils.settings import SettingScreen
from utils.dm_screen import DmScreen
from service.service import *

class HomePage(UserControl):
  def __init__(self,switch_page:object,anim):
    super().__init__()
    self.anim = anim
    self.switch_page=switch_page
    self.dm_data = ['dm',{"username":""}]
    self.bottom_nav_bar = CustomBottomNav(self.nav_switch)
    self.chat_screen = ChatScreen(self.anim,self.nav_switch)
    self.calls_screen = CallScreen(self.anim)
    self.stories_screen = StoriesScreen(self.anim)
    self.channels_screen = ChannelScreen(self.anim)
    self.settings_screen = SettingScreen(self.anim)
    self.dm_screen = DmScreen(self.anim,self.nav_switch,self.dm_data)
    self.base = Container(
      bgcolor=chat_screen_base_color,
      offset=transform.Offset(0,0),
      animate_offset=self.anim,
      expand=True,
      alignment=alignment.center,
      content=Column(
        alignment='spaceBetween',
        controls=[
          Stack(
            controls=[
              self.calls_screen,
              self.settings_screen,
              self.stories_screen,
              self.channels_screen,
              self.dm_screen,
              self.chat_screen,
            ]
          ),
          self.bottom_nav_bar,
        ]
      )
    )


    self.screen_control = {
      "chats":self.chat_screen,
      "calls":self.calls_screen,
      "settings":self.settings_screen,
      "stories":self.stories_screen,
      "channels":self.channels_screen,
      "dm":self.dm_screen,
    }
        
  def nav_switch(self,e:TapEvent):
    for page in self.screen_control:
      self.screen_control[page].base.offset.x=-1
      self.screen_control[page].base.update()
    if e.control.data[0] == 'dm':
      self.dm_screen.display_name.value = e.control.data[1].get('username')
      messages = fetch_messages('')
      print(messages)
      if messages:
        for message in messages['messages']:

          print(messages['messages'][message]['text'])
          self.dm_screen.chat_area.controls.append(
            self.dm_screen.ms_obj(messages['messages'][message]['text']),
          )


      self.screen_control[e.control.data[0]].base.height = base_height
      sleep(.05)
      self.screen_control[e.control.data[0]].base.offset.x =0
      self.screen_control[e.control.data[0]].base.update()
    else:
      self.dm_screen.base.height = 0
      self.dm_screen.base.update()
      sleep(.1)
      self.screen_control[e.control.data[0]].base.offset.x =0
      self.screen_control[e.control.data[0]].base.update()

  def fetch_messages(self):
    pass

  def build(self):
    return self.base


