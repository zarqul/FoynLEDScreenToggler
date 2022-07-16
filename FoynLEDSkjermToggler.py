from pythonosc import udp_client
import argparse
from datetime import datetime, date
import settings
from time import sleep
import importlib

# Setup OSC
parser = argparse.ArgumentParser()
parser.add_argument("--ip", default="10.0.1.123", help="The ip of the OSC server")
parser.add_argument("--port", type=int, default=7000, help="The port the OSC server is listening on")
args = parser.parse_args()
client = udp_client.SimpleUDPClient(args.ip, args.port)

def setScreenDim(value):
    # Setup OSC
    if value >= 0 <= 1:
        client.send_message("/composition/master", value)

# Run an infinite while loop waiting one minute between each run
def main():
    currentSetting = None
    while(True):
        importlib.reload(settings)
        # Get current timestamp
        currentTime = datetime.now()

        # Check exclusions
        if not currentTime.weekday() in settings.exclusions:
            try:
                newSetting = settings.schedule[currentTime.weekday()]
                for scheduledTime, setting in newSetting.items():
                    if scheduledTime == currentTime.strftime('%H%M'):
                        if not currentSetting == setting:
                            setScreenDim(setting / 100)
                            print("Dimming to {}%".format(setting))
                            currentSetting = setting

            except KeyError:
                print("Key does not exist")

        # Wait 60 seconds
        sleep(60)

if __name__ == '__main__':
    main()
