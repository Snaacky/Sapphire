import keyboard
import mouse
import pymem
import time
from config import *

pm = pymem.Pymem("csgo.exe")


def main():
    print("Sapphire has launched. Trigger bot is enabled. Your trigger key is: {}.".format(aim_key))
    player = client_base + local_player
    crosshair_value = pm.read_int(player) + crosshair_id

    while True:
        try:
            result = pm.read_int(crosshair_value)
        except Exception as e:
            pass

        if keyboard.is_pressed(aim_key):
            if result > 0 and result <= 64:
                mouse.press()
                time.sleep(0.05)
                mouse.release()


if __name__ == '__main__':
    main()
