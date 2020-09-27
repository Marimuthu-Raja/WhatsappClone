from kivymd.app import MDApp
from kivy.lang import Builder
from kivymd.uix.floatlayout import FloatLayout
from kivymd.uix.tab import MDTabsBase


kv = """
ScreenManager:
    Screen:
        name:"home"
        MDBoxLayout:
            orientation:"vertical"
            MDToolbar:
                title:"Whatsapp"
                right_action_items:[["magnify",lambda x:print("Hello")],["dots-vertical", lambda x:print("Hello")]]
            MDTabs:
                Tab:
                    text:"Chat"
                    ScrollView:
                        MDList:
                            TwoLineAvatarIconListItem:
                                text : 'Group Name'
                                secondary_text : 'Some text'
                                IconLeftWidget:
                                    icon : "account-group-outline"
                            TwoLineAvatarIconListItem:
                                text :'Name'
                                secondary_text : 'Some text'
                                IconLeftWidget:
                                    icon : 'emoticon-cool-outline'
                            TwoLineAvatarIconListItem:
                                text : 'Name'
                                secondary_text : 'Some text'
                                IconLeftWidget:
                                    icon : 'emoticon-excited-outline'
                            TwoLineAvatarIconListItem:
                                text : 'Name'
                                secondary_text : 'Some text'
                                IconLeftWidget:
                                    icon : 'emoticon-neutral-outline'
                            TwoLineAvatarIconListItem:
                                text : 'Name'
                                secondary_text : 'Some text'
                                IconLeftWidget:
                                    icon : 'emoticon-happy-outline'
                            TwoLineAvatarIconListItem:
                                text : 'Name'
                                secondary_text : 'Some text'
                                IconLeftWidget:
                                    icon : 'emoticon-neutral-outline'
                            TwoLineAvatarIconListItem:
                                text : 'Name'
                                secondary_text : 'Some text'
                                IconLeftWidget:
                                    icon : 'emoticon-excited-outline'
                            TwoLineAvatarIconListItem:
                                text : 'Name'
                                secondary_text : 'Some text'
                                IconLeftWidget:
                                    icon : 'emoticon-happy-outline'
                    MDFloatingActionButton:
                        icon:'message-reply-text'
                        text_color:(1,1,1,1)
                        pos_hint:{'center_x':0.9, 'center_y':0.1}
                        md_bg_color:app.theme_cls.primary_color    
                Tab:
                    text:"Status"
                    ScrollView:
                        MDList:
                            TwoLineAvatarIconListItem:
                                text : 'Name'
                                secondary_text : 'Just now'
                                IconLeftWidget:
                                    icon : 'emoticon-excited-outline'
                            TwoLineAvatarIconListItem:
                                text : 'Name'
                                secondary_text : 'Today, 10:10 am'
                                IconLeftWidget:
                                    icon : 'emoticon-happy-outline'
                            TwoLineAvatarIconListItem:
                                text : 'Name'
                                secondary_text : 'Today, 11:30 am'
                                IconLeftWidget:
                                    icon : 'emoticon-cool-outline'
                            TwoLineAvatarIconListItem:
                                text : 'Name'
                                secondary_text : 'Today, 12:00 pm'
                                IconLeftWidget:
                                    icon : 'emoticon-excited-outline'
                            TwoLineAvatarIconListItem:
                                text : 'Name'
                                secondary_text : 'Yesterday, 11:55 pm'
                                IconLeftWidget:
                                    icon : 'emoticon-cool-outline'
                            TwoLineAvatarIconListItem:
                                text : 'Name'
                                secondary_text : 'Yesterday, 7:00 pm'
                                IconLeftWidget:
                                    icon : 'emoticon-happy-outline'
                            TwoLineAvatarIconListItem:
                                text : 'Name'
                                secondary_text : 'Some text'
                                IconLeftWidget:
                                    icon : 'emoticon-excited-outline'
                    MDFloatingActionButton:
                        icon:'camera'
                        text_color:(1,1,1,1)
                        pos_hint:{'center_x':0.9, 'center_y':0.1}
                        md_bg_color:app.theme_cls.primary_color
                    MDFloatingActionButton:
                        icon:'pen'
                        text_color:(1,1,1,1)
                        pos_hint:{'center_x':0.9, 'center_y':0.25}
                        md_bg_color:app.theme_cls.primary_color
                Tab:
                    text:"Calls"
                    ScrollView:
                        MDList:
                            TwoLineAvatarIconListItem:
                                text : 'Name'
                                secondary_text : '22 Sept, 10:10 am'
                                IconLeftWidget:
                                    icon : 'emoticon-cool-outline'
                                IconRightWidget:
                                    icon : 'phone'
                                    theme_text_color:"Custom"
                                    text_color: (18/255, 140/255, 126/255, 1)
                            TwoLineAvatarIconListItem:
                                text : 'Name'
                                secondary_text : '15 Sept, 7:30 pm'
                                IconLeftWidget:
                                    icon : 'emoticon-happy-outline'
                                IconRightWidget:
                                    icon : 'phone'
                                    theme_text_color:"Custom"
                                    text_color: (18/255, 140/255, 126/255, 1)
                            TwoLineAvatarIconListItem:
                                text : 'Name'
                                secondary_text : '14 Sept, 6:40 pm'
                                IconLeftWidget:
                                    icon : 'emoticon-neutral-outline'
                                IconRightWidget:
                                    icon : 'phone'
                                    theme_text_color:"Custom"
                                    text_color: (18/255, 140/255, 126/255, 1)
                            TwoLineAvatarIconListItem:
                                text : 'Name'
                                secondary_text : '6 Sept, 5:50 pm'
                                IconLeftWidget:
                                    icon : 'emoticon-happy-outline'
                                IconRightWidget:
                                    icon : 'phone'
                                    theme_text_color:"Custom"
                                    text_color: (18/255, 140/255, 126/255, 1)
                            TwoLineAvatarIconListItem:
                                text : 'Name'
                                secondary_text : '24 Aug, 9:30 am'
                                IconLeftWidget:
                                    icon : 'emoticon-cool-outline'
                                IconRightWidget:
                                    icon : 'phone'
                                    theme_text_color:"Custom"
                                    text_color: (18/255, 140/255, 126/255, 1)
                            TwoLineAvatarIconListItem:
                                text : 'Name'
                                secondary_text : '15 Aug, 7:30 am'
                                IconLeftWidget:
                                    icon : 'emoticon-neutral-outline'
                                IconRightWidget:
                                    icon : 'phone'
                                    theme_text_color:"Custom"
                                    text_color: (18/255, 140/255, 126/255, 1)
                            TwoLineAvatarIconListItem:
                                text : 'Name'
                                secondary_text : '14 Aug, 8:00 am'
                                IconLeftWidget:
                                    icon : 'emoticon-happy-outline'
                                IconRightWidget:
                                    icon : 'phone'
                                    theme_text_color:"Custom"
                                    text_color: (18/255, 140/255, 126/255, 1)
                    
                    
<Tab>:
    
"""


class Tab(FloatLayout, MDTabsBase):
    pass


class WhatsappClone(MDApp):
    def build(self):
        self.theme_cls.primary_palette = "Teal"
        self.theme_cls.primary_hue = '800'
        return Builder.load_string(kv)


WhatsappClone().run()
