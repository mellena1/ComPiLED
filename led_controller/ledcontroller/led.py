from neopixel import ws, Color, Adafruit_NeoPixel
import json
import os

# LED strip configuration:
LED_PIN = 18  # GPIO pin connected to the pixels (18 uses PWM!).
LED_FREQ_HZ = 800000  # LED signal frequency in hertz (usually 800khz)
LED_DMA = 10  # DMA channel to use for generating signal (try 10)
LED_INVERT = False  # True: invert signal (using NPN transistor level shift)
LED_CHANNEL = 0  # set to '1' for GPIOs 13, 19, 41, 45 or 53
LED_STRIP = ws.SK6812_STRIP_GRBW

# Current LED Config
CURRENT_CONFIG = '/current_config/config.json'


class LEDStrip:
    def __init__(self, led_count):
        """
        Create a LEDStrip

        Initializes the strip and calls read_current_config to get the config
        """
        # Bind animation methods to JSON strings
        self.animations = {
            "Static": self.static
        }

        self.led_count = led_count
        self.brightness = 0
        # Create NeoPixel object with appropriate configuration
        self.strip = Adafruit_NeoPixel(self.led_count, LED_PIN, LED_FREQ_HZ,
                                       LED_DMA, LED_INVERT, self.brightness,
                                       LED_CHANNEL, LED_STRIP)
        # Intialize the library
        self.strip.begin()
        self.read_current_config()

    def update(self):
        """
        Update the strip with the current config values
        """
        leds = {}
        for ledconfig in self.config['LEDs']:
            new_leds = self.animations[ledconfig['Animation']](ledconfig)
            leds.update(new_leds)
        changed = False
        for index, color in leds.items():
            if self.strip.getPixelColor(index) != color:
                changed = True
                self.strip.setPixelColor(index, color)
        if changed:
            self.strip.show()

    def read_current_config(self):
        """
        Reads in CURRENT_CONFIG and creates the config dict

        Check example-config.json in the root of ComPiLED for an example
        config.
        """
        config = {}
        if os.path.exists(CURRENT_CONFIG):
            with open(CURRENT_CONFIG) as f:
                config = json.loads(f.read())
            self.set_brightness(config['Brightness'])
            # Change all of the 'r,g,b' strings to neopixel.Color values
            for led in config['LEDs']:
                for pixel_range, color in led['Colors'].items():
                    rgb = [int(n) for n in color.split(',')]
                    if rgb == [255, 255, 255]:
                        color = Color(0, 0, 0, 255)
                    else:
                        color = Color(rgb[0], rgb[1], rgb[2])
                    led['Colors'][pixel_range] = color
        else:  # No config
            config = {'Name': None, 'Brightness': 0, 'LEDs': []}
        self.config = config

    def set_brightness(self, brightness):
        """
        Set the brightness of the strip

        Must be between 0 and 255
        """
        if brightness < 0:
            brightness = 0
        elif brightness > 255:
            brightness = 255
        self.brightness = brightness
        self.strip.setBrightness(self.brightness)

    def static(self, config_block):
        """
        Configure the static section

        :config_block dict: The config block for one LED area from self.config
        :returns dict{led_index:Color}: The colors for each led
        """
        leds = {}
        for _range, color in config_block['Colors'].items():
            _range = [int(n) for n in _range.split('-')]
            first = _range[0]
            last = _range[1]
            for i in range(first, last + 1):
                leds[i] = color
        return leds
