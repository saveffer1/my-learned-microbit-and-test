from ssd1306 import initialize, clear_oled
from ssd1306_bitmap import show_bitmap

initialize()
clear_oled()
show_bitmap("microbit_logo")