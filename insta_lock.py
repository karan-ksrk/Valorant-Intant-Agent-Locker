#! E:\Valorant\venv\Scripts\python.exe
from infi.systray import SysTrayIcon
from pynput.mouse import Button, Controller
import time
import keyboard
import screeninfo
screen_info = screeninfo.get_monitors()[0]

screen_width = screen_info.width
screen_height = screen_info.height

mouse = Controller()

width_ratio = screen_width / 1600
height_ratio = screen_height / 900

agents = {
    'Astra': (453 * width_ratio, 773 * height_ratio),
    'Breach': (522 * width_ratio, 773 * height_ratio),
    'Brimstone': (589 * width_ratio, 773 * height_ratio),
    'Chamber': (663 * width_ratio, 773 * height_ratio),
    'Cypher': (723 * width_ratio, 773 * height_ratio),
    "Fade": (803 * width_ratio, 773 * height_ratio),
    'Gekko': (870 * width_ratio, 773 * height_ratio),
    'Harbour': (938 * width_ratio, 773 * height_ratio),
    'Jett': (1012 * width_ratio, 773 * height_ratio),
    'KAY/O': (1081 * width_ratio, 773 * height_ratio),
    'Killjoy': (1149 * width_ratio, 773 * height_ratio),
    'Neon': (453 * width_ratio, 836 * height_ratio),
    'Omen': (522 * width_ratio, 836 * height_ratio),
    'Phoenix': (589 * width_ratio, 836 * height_ratio),
    'Raze': (663 * width_ratio, 836 * height_ratio),
    'Reyna': (723 * width_ratio, 836 * height_ratio),
    'Sage': (803 * width_ratio, 836 * height_ratio),
    'Skye': (870 * width_ratio, 836 * height_ratio),
    'Sova': (938 * width_ratio, 836 * height_ratio),
    'Viper': (1012 * width_ratio, 836 * height_ratio),
    'Yoru': (1081 * width_ratio, 836 * height_ratio)
}

lock_in_pos_x, lock_in_pos_y = (797, 674)

# Specify the target position
target_x = 500
target_y = 300


def lock_agent(agent):
    agent_x, agent_y = agents[agent]
    for i in range(50):
        mouse.position = (agent_x, agent_y)
        mouse.click(Button.left)
        mouse.position = (lock_in_pos_x, lock_in_pos_y)
        time.sleep(0.1)
        mouse.click(Button.left)
        time.sleep(0.5)
        if keyboard.is_pressed('q'):
            break

hover_text = "SysTrayIcon Demo"

menu_options = (
    ('Duelists', 'roles/duelist.ico', (
                ('Phoenix', "agents/pheonix.ico", lambda  _: lock_agent('Phoenix')),
                ('Jett', "agents/jett.ico", lambda _: lock_agent('Jett')),
                ('Reyna', "agents/reyna.ico", lambda _: lock_agent('Reyna')),
                ('Raze', "agents/raze.ico", lambda _: lock_agent('Raze')),
                ('Yoru', "agents/yoru.ico", lambda _: lock_agent('Yoru')),
                ('Gekko', "agents/gekko.ico", lambda _: lock_agent('Gekko')),
                )),
    ('Controllers', 'roles/controller.ico', (
                ('Brimstone', "agents/brimstone.ico", lambda _: lock_agent('Brimstone')),
                ('Viper', "agents/viper.ico", lambda _: lock_agent('Viper')),
                ('Omen', "agents/omen.ico", lambda _: lock_agent('Omen')),
                ('Astra', "agents/astra.ico", lambda _: lock_agent('Astra')),
                ('Harbour', "agents/harbour.ico", lambda _: lock_agent('Harbour')),
                )),
    ('Initiators', 'roles/initiator.ico', (
                ('Sova', "agents/sova.ico", lambda _: lock_agent('Sova')),
                ('Breach', "agents/breach.ico", lambda _: lock_agent('Breach')),
                ('Skye', "agents/skye.ico", lambda _: lock_agent('Skye')),
                ('KAY/O', "agents/kayo.ico", lambda _: lock_agent('KAY/O')),
                ('Fade', "agents/fade.ico", lambda _: lock_agent('Fade')),
                )),
    ('Sentinels', 'roles/sentinel.ico', (
                ('Killjoy', "agents/killjoy.ico", lambda _: lock_agent('Killjoy')),
                ('Cypher', "agents/cypher.ico", lambda _: lock_agent('Cypher')),
                ('Sage', "agents/sage.ico", lambda _: lock_agent('Sage')),
                ('Chamber', "agents/chamber.ico", lambda _: lock_agent('Chamber')),
                ))
    )
sysTrayIcon = SysTrayIcon("icon.ico", hover_text, menu_options, on_quit=(), default_menu_index=1)
sysTrayIcon.start()
