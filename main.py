import machine, time, utime
import network
from display import TFT
from ui.interface import UI

tft = TFT()

tft.init(tft.ILI9341, width=320, height=320, miso=19, mosi=23, clk=18, cs=14, dc=27, bgr=True, backl_pin=32, rst_pin=33, backl_on=1, spihost=tft.VSPI, invrot=2)
tft.orient(2)

def init():
    tft.font(tft.FONT_Default)
    fw,fh = tft.fontSize()
    tft.clear()
    tft.text(0,0*fh, "connecting...")
    station = network.WLAN(network.STA_IF)
    station.active(True)
    station.connect("box", "pass")
    time.sleep(2)
    if station.isconnected():
        tft.text(0, 1*fh, "connected:")
        tft.text(0, 2*fh, station.ifconfig()[0])
        rtc = machine.RTC()
        rtc.ntp_sync(server="hr.pool.ntp.org")

        tmo = 100
        while not rtc.synced():
            utime.sleep_ms(100)
            tmo -= 1
            if tmo == 0:
                break

        if tmo > 0:
            tft.text(0, 3*fh, "Time set")
            utime.sleep_ms(500)
            t = rtc.now()
            a = utime.strftime("%c")
            tft.text(0, 4*fh, a)

init()

ui = UI(tft, width=320, height=240)
while True:
    ui.redraw_screen()
    utime.sleep_ms(500)
