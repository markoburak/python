import pyautogui as pg
from time import sleep
# pg.move(1,500,0.5)

# pg.moveTo(1,1,1)

# pg.drag(-500,20,0.5,button='left')
# pg.moveTo(105,272)

# pos = pg.position()


# pg.doubleClick(105,272)

# pg.typewrite('hello world')

# pg.click(769,101)

# pg.hotkey("winleft")
def get_3():
    pg.moveTo(152,1052,0.2)
    pg.click()
    pg.typewrite("chrome\n", 0.5)
    pg.typewrite(" youtube.com\n", 0.2)
    pg.hotkey("ctrl","t")
    pg.typewrite(" soccerway.com\n", 0.2)
    pg.hotkey("ctrl","t")
    pg.typewrite("https://rozetka.com.ua/ua/\n", 0.1)

# pg.alert("Info some","Title",button="Button")
# age = pg.prompt("AGE","Your age")
# print(age)

get_3()
sleep(10)
pg.screenshot("picture.png")