#!/usr/bin/python

import time
import smbus
import socket
def get_host_ip():
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect(('8.8.8.8', 80))
        ip = s.getsockname()[0]
    finally:
        s.close()

    return ip

BUS = smbus.SMBus(1)
#LCD_ADDR = 0x27
LCD_ADDR = 0x3F # sudo i2cdetect -y -a 0

def send_command(comm):
        # Send bit7-4 firstly
        buf = comm & 0xF0
        buf |= 0x04               # RS = 0, RW = 0, EN = 1
        BUS.write_byte(LCD_ADDR ,buf)
        time.sleep(0.002)
        buf &= 0xFB               # Make EN = 0
        BUS.write_byte(LCD_ADDR ,buf)
        
        # Send bit3-0 secondly
        buf = (comm & 0x0F) << 4
        buf |= 0x04               # RS = 0, RW = 0, EN = 1
        BUS.write_byte(LCD_ADDR ,buf)
        time.sleep(0.002)
        buf &= 0xFB               # Make EN = 0
        BUS.write_byte(LCD_ADDR ,buf)

def send_data(data):
        # Send bit7-4 firstly
        buf = data & 0xF0
        buf |= 0x05               # RS = 1, RW = 0, EN = 1
        BUS.write_byte(LCD_ADDR ,buf)
        time.sleep(0.002)
        buf &= 0xFB               # Make EN = 0
        BUS.write_byte(LCD_ADDR ,buf)
        
        # Send bit3-0 secondly
        buf = (data & 0x0F) << 4
        buf |= 0x05               # RS = 1, RW = 0, EN = 1
        BUS.write_byte(LCD_ADDR ,buf)
        time.sleep(0.002)
        buf &= 0xFB               # Make EN = 0
        BUS.write_byte(LCD_ADDR ,buf)
	BUS.write_byte(LCD_ADDR,~0x00) # blacklight on
def init_lcd():
        try:
                send_command(0x33) # Must initialize to 8-line mode at first
                time.sleep(0.005)
                send_command(0x32) # Then initialize to 4-line mode
                time.sleep(0.005)
                send_command(0x28) # 2 Lines & 5*7 dots
                time.sleep(0.005)
                send_command(0x0C) # Enable display without cursor
                time.sleep(0.005)
                send_command(0x01) # Clear Screen
        except:
                return False
        else:
                return True

def clear_lcd():
        send_command(0x01) # Clear Screen

def print_lcd(x, y, str):
        if x < 0:
                x = 0
        if x > 15:
                x = 15
        if y <0:
                y = 0
        if y > 1:
                y = 1

        # Move cursor
        addr = 0x80 + 0x40 * y + x
        send_command(addr)
        
        for chr in str:
                send_data(ord(chr))

if __name__ == '__main__':
        init_lcd()
        localIP=get_host_ip()
	while True:
        	print_lcd(0, 0,localIP )
		file = open("/sys/class/thermal/thermal_zone0/temp")  
		temp = float(file.read()) / 1000 
		file.close()
		wd="CPU temp : %.1f" %temp 
        	print_lcd(0, 1, wd)
		time.sleep(3)
