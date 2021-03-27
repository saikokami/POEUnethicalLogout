import win32api
import keyboard
import time
import pyautogui
from pyautogui import *
import os

# Get pixel colour func
# pyautogui.displayMousePosition() for console


# Source: https://rosettacode.org/wiki/Color_of_a_screen_pixel#Python 
def get_pixel_colour(i_x, i_y):
	import win32gui
	i_desktop_window_id = win32gui.GetDesktopWindow()
	i_desktop_window_dc = win32gui.GetWindowDC(i_desktop_window_id)
	long_colour = win32gui.GetPixel(i_desktop_window_dc, i_x, i_y)
	i_colour = int(long_colour)
	win32gui.ReleaseDC(i_desktop_window_id, i_desktop_window_dc)
	return (i_colour & 0xff), ((i_colour >> 8) & 0xff), ((i_colour >> 16) & 0xff)


# Specify the logout pixel
print("Don't press windows key or hover other applications over the healthbar or u will get logged out!")
print("Hover your mouse over the health ball and press space to confirm the point to logout!  ")


keyboard.wait('space')
x, y = win32api.GetCursorPos()
r, g, b = get_pixel_colour(x, y)
print("Logout point set!")
print("Now press ESC to fetch pixel colour if u pressed esc")
keyboard.wait('esc')
r_esc, g_esc, b_esc = get_pixel_colour(x, y)
while r_esc == r and g_esc == g and b_esc == b:
	r_esc, g_esc, b_esc = get_pixel_colour(x, y)
print("Esc pixel fetched!")
print("Script is now ready to logout!")

while True:
	# non escape= (23, 27, 30), escape = (9, 12, 14)
	time.sleep(0.3)
	if(pyautogui.pixel(1916, 922) == (23, 27, 30) or pyautogui.pixel(1916, 922) == (9, 12, 14)):
		r_c, g_c, b_c = get_pixel_colour(x, y)
		if((r_c, g_c, b_c) != (r, g, b) and (r_c, g_c, b_c) != (r_esc, g_esc, b_esc)):
			os.system("cports /RunAsAdmin /close * * * * PathOfExile_x64Steam.exe")
			time.sleep(5)
