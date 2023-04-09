from micropython import const
from  microbit import *
from time import sleep_us, sleep_ms
TM1637_CMD1 = const(64)  # 0x40 data command
TM1637_CMD2 = const(192) # 0xC0 address command
TM1637_CMD3 = const(128) # 0x80 display control command
TM1637_DSP_ON = const(8) # 0x08 display on
TM1637_DELAY = const(10) # 10us delay between clk/dio pulses
TM1637_MSB = const(128)  # msb is the decimal point or the colon depending on your display
_SEGMENTS = bytearray(b'\x3F\x06\x5B\x4F\x66\x6D\x7D\x07\x7F\x6F\x63')
class TM1637(object):
    def __init__(self, clk, dio, brightness=7):
        self.clk = clk.write_digital
        self.dio = dio.write_digital
        if not 0 <= brightness <= 7:
            raise ValueError("Brightness out of range")
        self._brightness = brightness
        self.clk(0)
        self.dio(0)
        sleep_us(TM1637_DELAY)
        self._write_data_cmd()
        self._write_dsp_ctrl()
    def _start(self):
        self.dio(0)
        sleep_us(TM1637_DELAY)
        self.clk(0)
        sleep_us(TM1637_DELAY)
    def _stop(self):
        self.dio(0)
        sleep_us(TM1637_DELAY)
        self.clk(1)
        sleep_us(TM1637_DELAY)
        self.dio(1)
    def _write_data_cmd(self):
        self._start()
        self._write_byte(TM1637_CMD1)
        self._stop()
    def _write_dsp_ctrl(self):
        self._start()
        self._write_byte(TM1637_CMD3 | TM1637_DSP_ON | self._brightness)
        self._stop()
    def _write_byte(self, b):
        for i in range(8):
            self.dio((b >> i) & 1)
            sleep_us(TM1637_DELAY)
            self.clk(1)
            sleep_us(TM1637_DELAY)
            self.clk(0)
            sleep_us(TM1637_DELAY)
        self.clk(0)
        sleep_us(TM1637_DELAY)
        self.clk(1)
        sleep_us(TM1637_DELAY)
        self.clk(0)
        sleep_us(TM1637_DELAY)
    def brightness(self, val=None):
        if val is None:
            return self._brightness
        if not 0 <= val <= 7:
            raise ValueError("Brightness out of range")
        self._brightness = val
        self._write_data_cmd()
        self._write_dsp_ctrl()
    def write(self, segments, pos=0):
        if not 0 <= pos <= 5:
            raise ValueError("Position out of range")
        self._write_data_cmd()
        self._start()
        self._write_byte(TM1637_CMD2 | pos)
        for seg in segments:
            self._write_byte(seg)
        self._stop()
        self._write_dsp_ctrl()
    def encode_digit(self, digit):
        return _SEGMENTS[digit & 0x0f]
    def encode_string(self, string):
        segments = bytearray(len(string))
        for i in range(len(string)):
            segments[i] = self.encode_char(string[i])
        return segments
    def encode_char(self, char):
        o = ord(char)
        if o == 32:
            return _SEGMENTS[36] # space
        if o >= 48 and o <= 57:
            return _SEGMENTS[o-48] # 0-9
        raise ValueError("Character out of range: {:d} '{:s}'".format(o, chr(o)))
    def hex(self, val):
        string = '{:04x}'.format(val & 0xffff)
        self.write(self.encode_string(string))
    def numbers(self, num1, num2, colon=True):
        num1 = max(-9, min(num1, 99))
        num2 = max(-9, min(num2, 99))
        segments = self.encode_string('{0:0>2d}{1:0>2d}'.format(num1, num2))
        if colon:
            segments[1] |= 0x80 # colon on
        self.write(segments)
    def show(self, string, colon=False):
        str1=string
        ind=0
        try:
            ind=str1.index(".")
            string=string.replace(".", "")
        except:
            pass
        segments = self.encode_string(string)
        #if len(segments) > 1 and colon:
        #    segments[1] |= 128
        if len(segments) > 1 and ind > 0:
            segments[ind-1] |= 128
        self.write(segments[:4])
    def number(self, num):
        # limit to range -999 to 9999
        num = max(-999, min(num, 9999))
        #string = '{0: >4d}'.format(num)
        #self.write(self.encode_string(string))
        self.show(str(num))