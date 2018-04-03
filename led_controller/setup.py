from setuptools import setup


setup(
    name='ledcontroller',
    version='0.0.1',
    description='Runs the LEDS',
    long_description=('Runs the LED controller and listens through a REST API'
                      ' for info from led_api'),
    url='https://github.com/mellena1/ComPiLED',
    author='Andrew Mellen',
    author_email='andrew_mellen@icloud.com',
    packages=['ledcontroller'],
    entry_points={
        'console_scripts': ['ledcontroller = ledcontroller.__main__:main']
    }
)
