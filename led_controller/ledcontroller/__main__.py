from .led import LEDStrip
from . import api
import time
from threading import Thread


def flaskThread():
    api.serve(debug=False, port=20002, use_reloader=False, host='0.0.0.0')


def main():
    """
    Run everything
    """
    Thread(target=flaskThread).start()
    strip = LEDStrip(59)
    while True:
        if api.new_config:
            strip.read_current_config()
            api.new_config = False
        strip.update()
        time.sleep(0.01)
