from plyer import notification
import time

if __name__ == '__main__':
        while True:
            notification.notify(
                title = "Take some rest buddy",
                message = "It is very important of your health",
                app_icon = "D:/vs code files/Python/Desktop Notification System/icon.ico",
            timeout = 5 )
            time.sleep(3600)