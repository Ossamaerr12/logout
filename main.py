from flet import * 

def main(page:Page):

    page.title = "oussama"
    page.window.width = 390
    page.window.height = 740
    page.window.top = 10 
    page.window.left = 900
    page.vertical_alignment="center"
    page.horizontal_alignment="center"

    page.appbar =AppBar(
        bgcolor=colors.RED,
        title=Text("login system"),
        center_title=True,
        leading=Icon(icons.HOME),
        leading_width=40,
        actions=[ 
            IconButton(icons.NOTIFICATIONS),
            PopupMenuButton(
                items=[
                    PopupMenuItem(text='Profile'),
                    PopupMenuItem(text='Settings App'),
                    PopupMenuItem(text='How me'),
                    PopupMenuItem(),
                    PopupMenuItem(text='Close'),
                    
                ]
            )
        ]
    )
###########################################

    def show(e):
        v1 = en1.value
        v2 = en2.value
        if v1 == 'oussama' and v2 == '123456789':
            alert1 = AlertDialog(
                title=Text('Welcome admin', size=18, color='green')
            )
            page.overlay.append(alert1)
            alert1.open = True
            page.update()
        else:
            alert1 = AlertDialog(
                title=Text('Data error', size=18, color='red')
            )
        page.overlay.append(alert1)
        alert1.open = True
        page.update()

    img =Image(src="img/logo.png",width=170)
    text = Text("Login system",color='white',size=25)
    en1 =TextField(label='Email', icon=icons.EMAIL)
    en2 =TextField(label='Password',icon=icons.PASSWORD , password=True , can_reveal_password=True)
    btn =ElevatedButton('login now' , on_click=show,bgcolor='RED' , color='white',width=200)
###########################################
    page.add(
        img,
        text,
        en1,
        en2,
        btn
    )
    ###############################
    page.navigation_bar = CupertinoNavigationBar(
        bgcolor=colors.RED,
        inactive_color=colors.BLUE,
        destinations=[
            NavigationBarDestination(icon=icons.CALL,label='call'),
            NavigationBarDestination(icon=icons.CAMERA,label='camera'),
            NavigationBarDestination(icon=icons.CONTACT_PHONE,label='contact'),
        ]
    )
    ###############################
    page.update()
app(main)
