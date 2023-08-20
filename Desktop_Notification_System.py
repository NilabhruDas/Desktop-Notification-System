from plyer import notification
import time
import pyttsx3

while True:
    try:
        interval = int(input("Enter the desired time interval (in seconds): "))
        if interval <= 0:
            print("Interval must be a positive integer.")
        else:
            break
    except ValueError:
        print("Please enter a valid integer.")

engine = pyttsx3.init()
msge = input("Enter the message: ")

if __name__ == '__main__':
    while True:
        try:
            notification.notify(
                title="Take some rest buddy",
                message=msge,
                app_icon="D:/vs code files/Python/Desktop Notification System/icon.ico",
                timeout=5
            )
            engine.say(msge)
            engine.runAndWait()
            time.sleep(interval)
        except KeyboardInterrupt:
            print("Notification loop stopped by user.")
            break
        except Exception as e:
            print(f"An error occurred: {e}")
