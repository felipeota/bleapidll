from ctypes import *

bleapi = cdll.LoadLibrary("./BLEApi.dll")
bleapi.init()
bleapi.start_device_watcher()

while True:
    g = input("type exit to exit: ")
    if g == "exit":
        break
bleapi.stop_device_watcher()