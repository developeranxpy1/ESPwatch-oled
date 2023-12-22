

import network, urequests, utime, machine
from machine import RTC, SoftI2C, Pin
from ssd1306 import SSD1306_I2C
import ssd1306
import time
import framebuf
import _thread
from machine import deepsleep
import random
import machine
from oled import Write, GFX, SSD1306_I2C
from time import sleep
import esp32
from machine import Pin, SoftI2C
import machine
import oled
import math
import ubuntu_12
from oled import Write, GFX, SSD1306_I2C
from machine import Pin, PWM, I2C
from machine import Pin, PWM, I2C
from ssd1306 import SSD1306_I2C
import time
import urandom



boot = Pin(0, Pin.IN)


#speaker
ent = Pin(13, Pin.IN)
sw = Pin(12, Pin.IN)
bled = Pin(2, Pin.OUT)
flash = Pin(25, Pin.OUT)
bled.value(0)
# Vibration motor object
motor = Pin(4, Pin.OUT)

# Speaker object
speaker = PWM(Pin(14), freq=440, duty=0)

adc = machine.ADC(machine.Pin(34))

WIDTH = 128
HEIGHT = 64

oled = SSD1306_I2C(128, 64, SoftI2C(scl=Pin(22), sda=Pin(21)))

write12 = Write(oled, ubuntu_12)




ssid = "rgb"
psk = "12345678"

uptime = 0

oled.fill(0)
write12.text("Starting...", 40, 25)
bled.value(1)
oled.show()
time.sleep(0.5)
bled.value(0)
#machine.deepsleep()
showtd = 1
maths = 16
uptime = 0
backend = 0

animation_speed = 0.3
animation_phase = 0.0
animation_scale = 10.0
animation_offset = int(HEIGHT / 2)
# user data


motor.value(100)
time.sleep(0.1)
motor.value(0)
time.sleep(0.1)
motor.value(100)
time.sleep(0.1)
motor.value(0)

net = 0

flash.off()
temp = 0


while temp:
    print("pressed", sw.value())
    oled.fill(0)
    time.sleep(0.1)
    write12.text("Connect to wifi ???", 0, 25)
    write12.text("Yes", 100, 0)
    write12.text("No", 100, 50)
    oled.show()







    if sw.value() == 0:
        print("yes")
        net = 1
        temp = 0
    if ent.value() == 0:
        print("no")
        net = 0
        temp = 0

#temp end


net = 0



dino_x = 20
dino_y = 40
dino_vy = 0
cactus_x = 128
cactus_y = 45
score = 0
game_over = False
# Define the functions for drawing the game elements
def draw_dino():
    oled.fill_rect(dino_x, dino_y, 10, 15, 1)
def erase_dino():
    oled.fill_rect(dino_x, dino_y, 10, 15, 0)
def draw_cactus():
    oled.fill_rect(cactus_x, cactus_y, 10, 20, 1)
def erase_cactus():
    oled.fill_rect(cactus_x, cactus_y, 10, 20, 0)
def draw_score():
    oled.text("Score: " + str(score), 0, 0)
def draw_game_over():
    oled.fill(0)
    oled.text("Score: " + str(score), 0, 0)
    oled.text("Game Over", 30, 20)
    oled.text("Score: " + str(score), 30, 40)
    oled.show()
    motor.value(100)
    time.sleep(0.1)
    motor.value(0)
    time.sleep(0.1)
    motor.value(100)
    time.sleep(0.1)
    motor.value(0)
    while 1:
        print("waiting")
        time.sleep(0.01)
        if sw.value() == 0:
            print("ok")
            game_over = False
            backend = 1
            
def draw_animation():
    oled.fill(0)
    for x in range(WIDTH):
        y = int(math.sin((x / WIDTH) * math.pi * 2 + animation_phase) * animation_scale) + animation_offset
        oled.pixel(x, y, 1)
    oled.show()
ct = 0
backend = 1

# Helper function to play a tone
def play_tone(frequency, duration):
    speaker.duty(50)
    speaker.freq(frequency)
    time.sleep(duration)
    speaker.duty(0)

play_tone(523, 0.1)
play_tone(784, 0.1)




url = "http://worldtimeapi.org/api/timezone/Asia/Kolkata" # see http://worldtimeapi.org/timezones
web_query_delay = 60000 # interval time of web JSON query
retry_delay = 5000 # interval time of retry after a failed Web query



#with internet end

m = 0
h = 0

clocktime = 0


# Set the attenuation to 6dB to read up to 2.6V
adc.atten(machine.ADC.ATTN_6DB)

# Set the full-scale voltage to 5V
adc.width(machine.ADC.WIDTH_12BIT)

# Read the voltage
voltage = adc.read() * 5 / 4095
rawv = "Voltage: {:.2f}V".format(voltage)
    
# Extract the voltage value from the rawv string and convert it to a float
voltage_float = float(rawv.split(": ")[1].split("V")[0])
    
print("Voltage (float):", voltage_float)



def core_1():
    
    
    

    
    global adc
    global h
    global m
    global clocktime
    #runs in different core
    while 1:
        
        
        
        
        # Set the attenuation to 6dB to read up to 2.6V
        adc.atten(machine.ADC.ATTN_6DB)

        # Set the full-scale voltage to 5V
        adc.width(machine.ADC.WIDTH_12BIT)

        # Read the voltage
        voltage = adc.read() * 5 / 4095
        rawv = "Voltage: {:.2f}V".format(voltage)
    
        # Extract the voltage value from the rawv string and convert it to a float
        voltage_float = float(rawv.split(": ")[1].split("V")[0])
    
        print("Voltage (float):", voltage_float)

        clocktime += 1

        if clocktime >= 59:
            clocktime = 0
            m += 1
        if m >= 59:
            m = 0
            h += 1
        if h == 24:
            m = 0
            h = 0
            motor.value(100)
            time.sleep(0.1)
            motor.value(0)
            time.sleep(0.1)
            motor.value(100)
            time.sleep(0.1)
            motor.value(0)

        time.sleep(1)
        print("time", h, ":", m, ":", clocktime)
_thread.start_new_thread(core_1, ())

        
date_str = ""
xtime_str = ""


if net == 0:
    #no internet mode
    
    oled.fill(0)
    l = 0

    main = 1
    
    
    cx = 0
    while main:
        
        
        
        try:
            #try to connect
            rtc = RTC()
            # wifi connection
            wifi = network.WLAN(network.STA_IF) # station mode
            wifi.active(True)
            wifi.connect(ssid, psk)
            connectx = 1
        except:
            connectx = 0
            print("tried but failed")


        if maths == 32 and ent.value() == 0:
            motor.value(100)
            time.sleep(0.1)
            motor.value(0)
            
            cx += 1
            play_tone(523, 0.1)
            play_tone(784, 0.1)

            if (cx % 2) == 0:
                flash.off()
                print("flash off")
            
            if (cx % 2) != 0:
                flash.on()
                print("flash on")

        oled.contrast(255)
        oled.fill(0)
        
        mstr = str(m)
        hstr = str(h)
        sec = str(clocktime)


      
        

        showtd = 1
        ct += 1
        if ct > 150:
            ct = 0
        print("core-0 running ", ct)
        time.sleep(0.001)
        print(maths)

        write12.text("___________________________", 0, 3, showtd)
        write12.text(hstr+":"+mstr+":"+sec, 50, 0, showtd)



        #draw home
        write12.text("[____________________]", 0, maths+2, showtd)
        write12.text("Sleep", 10, 16, showtd)
        write12.text("Flash", 10, 32, showtd)
        write12.text("Game !!!", 10, 48, showtd)

        oled.show()

        if maths > 50:
            maths = 16
        if not sw.value() == 1:
            ct = 0
            play_tone(523, 0.1)
            maths += 16
            #time.sleep(0.001)



        screen = 1




        if maths == 16 and ent.value() == 0 or ct > 100:
            motor.value(100)
            time.sleep(0.1)
            motor.value(0)
            ct = 0
            
            bled.value(1)
            play_tone(523, 0.1)
            play_tone(784, 0.1)
            bled.value(0)
            #sleep logic
            nxp = 1
            backend = 0


            oled.fill(0)
            oled.show()
            time.sleep(0.2)

            print("joke")
            oled.fill(0)
            bled.value(1)

            bled.value(0)
            nxp = 1
            backend = 0

            oled.show()


            
            while nxp:
                vstr = str(voltage_float)
                ct += 1
                
                hstr = str(h)
                mstr = str(m)
                sec = str(clocktime)
                
                oled.contrast(1)
                
                
               


                oled.fill(0)
                # write12.text("___________________________", 0, 36, 1)
                
                write12.text(hstr+":"+mstr+":"+sec, 50, 30, 1)
                write12.text(date_str, 35, 20, 1)
                write12.text(xtime_str, 40, 40, 1)
                
                #write12.text("V "+vstr, 50, 50, 1)


                    

                oled.show()
                if ent.value() == 0 or sw.value() == 0:
                    backend = 1
                    nxp = 0
                    joke = ""
                if connectx == 1:
                    try:

                        if sw.value() == 0 or ent.value() == 0:
                            ct = 0
                            nxp = 0
                            backend = 1
                        oled.contrast(1)
                        update_time = utime.ticks_ms() - web_query_delay
                        if utime.ticks_ms() - update_time >= web_query_delay:
                        
                            # HTTP GET data
                            response = urequests.get(url)
                            if response.status_code == 200: # query success

                                print("JSON response:\n", response.text)
                                # parse JSON
                                parsed = response.json()
                                datetime_str = str(parsed["datetime"])
                                year = int(datetime_str[0:4])
                                month = int(datetime_str[5:7])
                                day = int(datetime_str[8:10])
                                hour = int(datetime_str[11:13])
                                minute = int(datetime_str[14:16])
                                second = int(datetime_str[17:19])
                                subsecond = int(round(int(datetime_str[20:26]) / 10000))
                                # update internal RTC
                                rtc.datetime((year, month, day, 0, hour, minute, second, subsecond))
                                update_time = utime.ticks_ms()
                                print("RTC updated\n")
                            else: # query failed, retry retry_delay ms later
                                update_time = utime.ticks_ms() - web_query_delay + retry_delay
                        # generate formated date/time strings from internal RTC
                        date_str = " {2:02d}.{1:02d}.{0:4d}".format(*rtc.datetime())
                        time_str = " {4:02d}:{5:02d}:{6:02d}".format(*rtc.datetime())
                        # update SSD1306 OLED display
                        from machine import RTC

                        rtc = RTC()
                        time_tuple = rtc.datetime()

                        hour = time_tuple[4] if time_tuple[4] <= 12 else time_tuple[4] - 12
                        am_pm = 'AM' if time_tuple[4] < 12 else 'PM'

                        xtime_str = " {0:02d}:{1:02d} {2}".format(hour, time_tuple[5], am_pm)



                        ix = 30

                        #write12.text("Loading new content...", 0, 0)

                        response = urequests.get("https://official-joke-api.appspot.com/jokes/programming/random")
                        joke = response.json()[0]["setup"] + " " + response.json()[0]["punchline"]

                        for i in range(len(joke)):
                            print(i)
                            print(joke)


                            ix -= 5

                            oled.fill(0)
                            write12.text("___________________________", 0, 36, 1)
                            write12.text(date_str, 35, 25, 1)
                            write12.text(xtime_str, 40, 10, 1)

                            write12.text(joke, ix, 50)

                            oled.show()
                            if ent.value() == 0 or sw.value() == 0:
                                backend = 1
                                nxp = 0
                                joke = ""
                    except:
                        print("tried but no success")
                    
                    




        print("maths-", maths)

        if maths == 48 and ent.value() == 0:
            motor.value(100)
            time.sleep(0.1)
            motor.value(0)
            ct = 0
            #game logic
            bled.value(1)
            play_tone(523, 0.1)
            play_tone(784, 0.1)
            bled.value(0)


            # Define the main game loop
            
            oled.fill(0)
            backend = 0
            while not game_over:
                # Move the cactus
                erase_cactus()
                cactus_x -= 2
                if cactus_x < -10:
                    cactus_x = 128
                    cactus_y = urandom.getrandbits(2) + 30
                    score += 1
                draw_cactus()

                # Move the dino
                erase_dino()
                if sw.value() == 0 and dino_y == 40:
                    dino_vy = -6
                    play_tone(523, 0.1)
                dino_vy += 0.3
                dino_y += int(dino_vy)
                if dino_y > 40:
                    dino_y = 40
                    dino_vy = 0
                draw_dino()

                # Draw the score

                #draw_score()


                # Check for collision
                if cactus_x < dino_x + 10 and cactus_x + 10 > dino_x and cactus_y < dino_y + 15 and cactus_y + 20 > dino_y:
                    game_over = True

                # Update the OLED display
                oled.show()
                #time.sleep(0.001)

            # Draw the game over screen
            #draw_game_over()
            oled.fill(0)
            oled.text("Game Over", 30, 20)
            oled.text("Score: " + str(score), 30, 40)
            oled.show()
            motor.value(100)
            time.sleep(0.1)
            motor.value(0)
            time.sleep(0.1)
            motor.value(100)
            time.sleep(0.1)
            motor.value(0)
            lx = 1
            while lx:
                print("waiting")
                time.sleep(0.01)
                if sw.value() == 0 or ent.value() == 0:
                    lx = 0
                    print("ok")
                    game_over = False
                    backend = 1
                    dino_x = 20
                    dino_y = 40
                    dino_vy = 0
                    cactus_x = 128
                    cactus_y = 45
                    score = 0
                    game_over = False






        















































































































                



































