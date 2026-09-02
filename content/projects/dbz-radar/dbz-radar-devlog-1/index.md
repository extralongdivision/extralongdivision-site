---
date: '2026-08-29 02:38:17 +0000 UTC'
draft: true
title: 'Dragon Ball Radar: Devlog 1 - Frankenstein'
#
# EDIT THESE
#
author: 'Extra Long Division'
tags: ['project', 'dragon-ball-radar', 'esp32', 'circuitpython']
# description: 'I forgot to fill out the description.'
# URL is based off the filename
canonicalURL: 'https://extralongdivision.com/projects/dbz-radar/dbz-radar-devlog-1/'
# author: ["Me", "You"] # multiple authors

#
# Optional
#
showToc: true
TocOpen: false
hidemeta: false
comments: false
disableHLJS: false # to disable highlightjs
disableShare: false
hideSummary: false
searchHidden: false
ShowReadingTime: true
ShowBreadCrumbs: true
ShowPostNavLinks: true
ShowWordCount: false
ShowRssButtonInSectionTermList: false
UseHugoToc: false
cover:
   image: cover.webp # "<image path/url>" # image path/url
   alt: "Dragon Radar" # alt text
   # caption: "Dragon Ball Radar" # display caption under cover
   relative: true # when using page bundles set this to true
   hidden: false # only hide on current single page
# editPost:
#    URL: "https://github.com/<path_to_repo>/content"
#    Text: "Suggest Changes" # edit text
#    appendFilePath: true # to append file path to Edit link
---

{{< written-by-a-human >}}

## Inspiration

If you want a real life {{< tracked-anchor href="https://dragonball.fandom.com/wiki/Dragon_Radar" text="Dragon Radar" >}}, there are a small amount of toys to choose from.

{{< figure src="dbz-radar-toys.webp" alt="dragon radar shopping list" loading="lazy" >}}

None of those can really function as the radar from the anime. The maker in me wanted to change that.

There were some bumps along the way, but the first revision turned out alright. I'll disclose all those bumps, and the eventual working prototype, in this dev[^1]log.

## Prototyping

### CircutPython

A Dragon Radar requires a circular screen. In recent years, these have become more available to the hobbyist maker. There are lots on Alibaba and Aliexpress, but Adafruit has {{< tracked-anchor href="https://www.adafruit.com/product/5793" text="4\"">}} and {{< tracked-anchor href="https://www.adafruit.com/product/5793" text="2.8\"">}} varieties that are not only well documented but have a complementary dev board: the {{< tracked-anchor href="https://www.adafruit.com/product/5800" text="ESP32-S3 Qualia." >}}

This is where I began prototyping and quickly hit an impasse. Adafruit prioritizes CircuitPython and I couldn't get the `CIRCUITPY` drive to show up on my Linux machine. I bumbled around factory reset and bootloader repair documentation only for flashing to work first try after connecting the Qualia to a Windows machine. Not sure why.

Once I flashed the newest CircuitPython onto the Qualia, it showed up on my Linux machine. Maybe it's on old bug that's hence been repaired.

### Display Driver

Once CircuitPython worked, driving the display was easy using Adafruit's provided example code.

```python
from displayio import release_displays
release_displays()

import displayio
import busio
import board
import dotclockframebuffer
from framebufferio import FramebufferDisplay

init_sequence_hd40015c40 = bytes((
    ...
    """obnoxiously long init code, scroll to the end for the repo containing the full code"""
    ...
))

tft_pins = dict(board.TFT_PINS)

tft_timings = {
    "frequency": 16000000,
    "width": 720,
    "height": 720,

    "hsync_pulse_width": 2,
    "hsync_back_porch": 44,
    "hsync_front_porch": 46,
    "hsync_idle_low": False,

    "vsync_pulse_width": 16,
    "vsync_back_porch": 16,
    "vsync_front_porch": 50,
    "vsync_idle_low": False,

    "pclk_active_high": True,
    "pclk_idle_high": False,
    "de_idle_high": False,
}

board.I2C().deinit()
i2c = busio.I2C(board.SCL, board.SDA)
tft_io_expander = dict(board.TFT_IO_EXPANDER)
#tft_io_expander['i2c_address'] = 0x38 # uncomment for rev B
dotclockframebuffer.ioexpander_send_init_sequence(i2c, init_sequence_hd40015c40, **tft_io_expander)
i2c.deinit()

bitmap = displayio.OnDiskBitmap("/round-display-ruler-720p.bmp") # place this file in the root of CIRCUITPY

fb = dotclockframebuffer.DotClockFramebuffer(**tft_pins, **tft_timings)
display = FramebufferDisplay(fb, auto_refresh=False)

# Create a TileGrid to hold the bitmap
tile_grid = displayio.TileGrid(bitmap, pixel_shader=bitmap.pixel_shader)

# Center the image
tile_grid.x -= (bitmap.width - display.width) // 2
tile_grid.y -= (bitmap.height - display.height) // 2

# Create a Group to hold the TileGrid
group = displayio.Group()

# Add the TileGrid to the Group
group.append(tile_grid)

# Add the Group to the Display
display.root_group = group

display.auto_refresh = True

# Loop forever so you can enjoy your image
while True:
    pass
```

I should note that I ran into an error when trying to program the board.

```
OSError: [Errno 5] Input/output error
```

This prevented me from updating the code. {{< tracked-anchor href="https://github.com/adafruit/circuitpython/issues/8449" text="Other people have had this problem too apparently." >}} I still don't know the root cause, but the work around I used on Linux was:

```
sudo cp code.py /media/<username>/CIRCUITPY/code.py
```

### Sound

This was the first hiccup. This demo of the Adafruit team playing Star Trek on the Qualia made me confident that the board could be the base for a Dragon Radar.

{{< youtube yKRatudQSsI >}}

Those familiar with the Dragon Ball series will know the radar makes this sound:

{{< audio src="radar-beep.ogg" >}}

My implementation didn't sound as good. I bought a breakout board for the same I2S[^2] chip used in the above demo, the MAX98357, and connected it to the Qualia board.

{{< figure src="sound-prototype.webp" alt="qualia and MAX98357 breakout prototype" loading="lazy" >}}

The first audio file in this section sounded like this played through my prototype hardware (put the volume down):

{{< audio src="cursed-beep.ogg" >}}

The crackling sound is not your speakers. That's actually what was coming out of my breadboard set up. I used, what I believe to be, the same speakers as the one Adafruit demoed as well as a 8 ohm variant, but that didn't change anything. Changing the gain or the stereo/L/R output of the amp didn't fix the issue either.

I doubt the code is suspect but here it is in case you can find something wrong with it.

```python
# SPDX-FileCopyrightText: 2018 Kattni Rembor for Adafruit Industries
#
# SPDX-License-Identifier: MIT

import audiocore
import board
import audiobusio

wave_file = open("beep.wav", "rb")  # must be CIRCUITPY filesystem
wave = audiocore.WaveFile(wave_file)

# For Feather M0 Express, ItsyBitsy M0 Express, Metro M0 Express
# audio = audiobusio.I2SOut(board.D1, board.D0, board.D9)
# For Feather M4 Express
# audio = audiobusio.I2SOut(board.D1, board.D10, board.D11)
# For Metro M4 Express
# audio = audiobusio.I2SOut(board.D3, board.D9, board.D8)
i2s_bit_pin = board.A1
i2s_word_pin = board.A0
i2s_data_pin = board.TX
audio = audiobusio.I2SOut(i2s_bit_pin, i2s_word_pin, i2s_data_pin)

while True:
    audio.play(wave)
    while audio.playing:
        pass
```

I don't have a lot of familiarity with I2S or sound circuits in general. Since *something* played I suspect the haphazard wiring is the culprit. Hopefully a PCB[^3] will fix the issue. So I pressed on into electrical-mechanical design.

## Enclosure Design

### Display Mounting

Given the unique shape of the Dragon Radar, I started with designing a 3D model. In the anime, the Dragon Radar took on slightly different looks.

{{< figure src="dragon-radars.webp" alt="dragon radars" loading="lazy" >}}

There are two constraints mandatory to match the anime:

1. The display has to be at the center of the enclosure
2. The activation button must be at the top of the enclosure, aligned with the vertical symmetrical axis

These two constraints seem simple, but forced my hand during mechanical design.

I decided to use the 4" display, HD40015C40, since I figured a display that was too big was better than one that was too small. I didn't have the display in hand yet when designing the enclosure so I had to go off its datasheet.

{{< figure src="HD40015C40-drawing.webp" alt="display mechanical drawing" loading="lazy" >}}

It was in chinglish and honestly frustrating to interpret, but the visible pixels on the screen are not centered in the display assembly. In fact, the center of the bounding box of the display assembly and the center of the active pixel area is offset by 2.44 mm.

{{< figure src="aa-offset.webp" alt="render of screen and display assembly" loading="lazy" >}}

I was able to reduce the offset to 1.5 mm in the opposite direction with the activiation button's placement. I used a THT[^4] switch for mechanical strength, but this forced the PCB to be bigger than the display so the switch's leads didn't interfere with the display.

{{< figure src="aa-pcb-offset.webp" alt="render of display on PCBA" loading="lazy" >}}

To keep the screen centered in the end product, I had to put a sizable bevel around the enclosure's edges.

{{< figure src="bevel-length.webp" alt="render of enclosure over display assembly" loading="lazy" >}}

This is close enough to the anime. Finishing the mechanical design for the user input changed things though.

### Activation Button

The button to turn the device on and off is actually an assembly of a shaft and cap. There's heat-set inserts in each part and they're assembled together with a set screw.

{{< figure src="actuator-xray.webp" alt="transparent view of actuator button" loading="lazy" >}}

This is where the beveled edges on the enclosure became a problem. Bear with me because this depedancy tree is a little convoluted. Because the switch is on the same PCB as the display, and switches are only available at certain hieghts, and the activation button must be on the same axis as the switch's actuator, the shaft for the activation button can't sit on the top of the enclosure like in the anime.

{{< figure src="switch-actuator.webp" alt="switch and actuator side view" loading="lazy" >}}

{{< figure src="render-vs-anime.webp" alt="modeled activation button vs anime's activation button" loading="lazy" >}}

This is fine for this first revision. I'll probably 3D print a non-functional version that looks more like the anime then decide which is better.

### Power Cable Routing

For practical reasons, I wanted the radar to run off a rechargeable battery. The slot for the charger would be easiest to put into the enclosure's back, which would thus require a vertical connector. USB-C is the default nowadays, so I went with the USB440 series from GCT. This ultimately resulted in some problems, but more on that in the bring up phase.

I'm doing a little time bending here because I placed the USB-C connector in the PCB layout before defining the charging port's location in the mechanical design. I did this because electrical constraints defined the connector's position more than mechanical ones.

Also, at this point I knew there was a lot of empty space on the board, so I didn't leave a special mounting place for the battery. I'll attach it to the board with some double sided tape.

### Mounting Points

Snap-fits are the premiere way to assemble parts together. But I'm too lazy to iterate through a bunch of tolerances before everything assembles well. Instead, I used heat-set inserts to mount the PCB and assemble the enclosure together. To preserve {{< tracked-anchor href="https://en.wikipedia.org/wiki/Poka-yoke" text="poka-yoke" >}}, I used different threads for the PCB mounting and fastening the enclosure front and back together.

{{< figure src="mounting-holes.webp" alt="render with PCB and enclosure mounting holes" loading="lazy" >}}

One of the sizes was M1 which were surprisingly expensive to source from the usually suspects. I ultimately found some on Amazon.

### Speaker

The speakers I'm using thankfully ship with adhesive foam. I cut a small nest about ~0.25 mm bigger than the speaker in the enclosure's back as a mounting location. Hopefully the adhesive is enough to keep it into place. Add some holes so the sound escapes and mechanical design is done!

{{< figure src="speaker-nest.webp" alt="render of enclosure back" loading="lazy" >}}

## Electronics Design

### Schematic Capture

Adafruit did most of the work. "My" design is a mashup up of the Qualia board, MAX98357 breakout, and the charging circuit from the [Adafruit Feather ESP32-S3](https://learn.adafruit.com/assets/110822).

{{< figure src="schematic.webp" alt="schematic" loading="lazy" >}}

The few modifications I made were:

- Remove the `DN` and `UP` buttons and replaced them with the button chosen in the mechanical enclosure section
- Remove the STEMMA QT/Qwiic connector
- Replace the JST connector with 2.54" spaced THTs and connected all unused IO[^5] to it
- Add a heartbeat LED[^6]
- Replaced jumpers with 0 ohm resistors, depopulating the ones I don't want
- Various quality of life changes like adding more test points and egregious amount of 0 ohm resistors in series with interesting traces

### PCB Layout

#### Placement

The mechanical design dictated the position of the mounting holes, activation button, and the FFC[^7] connector (*technically I could physically rotate the display and rotate the image in software but I opted just to put the connector and activation button at the vertical symmetrical axis of the device*).

This choice forced me to rotate the ESP32 package 45 degrees to avoid a THT inside a keep-out zone. I put the ESP32 on the top right of the board to give the most amount of space to place other components.

{{< figure src="pcb-render.webp" alt="render of PCBA" loading="lazy" >}}

I'm actually still violating the layout rules provided by Espressif. They recommend the antenna hang off the board ideally or, if not possible, the end of the antenna be at least 15 mm away from the board edge and that the feed point be max 2 mm from a board edge.

{{< figure src="https://docs.espressif.com/projects/esp-hardware-design-guidelines/en/latest/esp32s3/_images/esp32s3-module-place-on-base-board-right.png" alt="hanging ESP32-WROOM guidelines" loading="lazy" >}}

{{< figure src="https://docs.espressif.com/projects/esp-hardware-design-guidelines/en/latest/esp32s3/_images/esp32s3-module-clearance.png" alt="ESP32 module 15mm from board cutout and 1mm from board edge" loading="lazy" >}}

If I hung the antenna off the board it'd collide with the enclosure and I didn't want to make the enclosure any larger.

{{< figure src="esp32-placement-render.webp" alt="render of ESP32 module in assembly" loading="lazy" >}}

To make rework and hand-soldering easier, I used 0805 sized components wherever I could. This would make my life easier once the boards came back.

#### Stack-up

I decided to do a 1.6 mm thick (foreshadowing), 4 layer stack-up of `signal+ground/ground/ground/signal+ground`. The RGB565[^8] parallel signals were my greatest concern. The two inner ground layers would shield signals on layer 4 from the RGB. Layer 1 would have the USB[^9] 2.0 traces which technically should be fabricated to 90 ohm, but in practice I've never had problems omitting a controlled impedance. I still routed the signals differential though. The four layer stack-up also made it much easier to route 3.3 V power rail on layer 4.

#### Routing

The most interesting part to route was the USB-C connector. It has a keep-out zone near the pads that make it almost impossible to connect the USB D+/D- pins and VBUS[^10] pins together.

{{< figure src="usbc-drawing.webp" alt="USB-C connector keepout zone" loading="lazy" >}}

I interpreted the keep-out zone as only for components and not for all copper. I'm justifying this conclusion with the metal flaps on the side of the connector (these will rear their ugly head once the board is made).

{{< figure src="usb-flap.webp" alt="metal slaps of USB-C connector" loading="lazy" >}}

Everything else was fairly straight forward to route.

### Ordering

While ordering the board, I realized that I assigned a 100 *uF* decoupling capacitor for the ESP32 instead of a 100 *nF* cap. If you hadn't caught on to the trend, I am lazy. I didn't want to regenerate the gerbers so I just DNP[^11]'d the cap.

The USB-C connector was also out-of-stock. I already designed the mechanical enclosure around that connectors height and (re: lazy) DNP'd that part thinking I could hand solder it on once the boards arrive. That was not a safe assumption.

## Board Bring-Up

### Physical Inspection

Once the boards came back, I realized just how large they are.

{{< figure src="board-in-hand.webp" alt="PCBA in my hand" loading="lazy" >}}

The PCBA[^12] are about as large as they can comfortably fit in my hand and that's before they're put in a larger assembly. I'll certainly have to use a wrist strap for the final build.

### Smoke test

I plugged in a battery into the board and... smoke. Quickly, I realized my mistake. I swapped the battery connector polarity. The Adafruit designed I based it on used a horizontal connector, while mine is vertical. This shouldn't matter, but the manufacturere flipped the location of pin 1 on the datasheet.

{{< figure src="jst-ph-footprint.webp" alt="battery connector footprint" loading="lazy" >}}

I should've caught this, but I will remind JST that pin 1 should be in the top left of a footprint to comply with an IPC[^13] {{< tracked-anchor href="https://www.protoexpress.com/blog/features-of-ipc-7351-standards-to-design-pcb-component-footprint/#zero-component-orientation" text="7351" >}}. Thankfully Q1 and D7 act as reverse polarity protection for the rest of the circuitry.

{{< figure src="q1-d7.webp" alt="reverse polarity circuit" loading="lazy" >}}

### USB-C

Now comes the most egregious mistake I made in the design that I so un-elegantly foreshadowed earlier. I couldn't connect a battery so next step was to solder on the USB-C connector.

While earlier I mentioned how surprisingly large the board was. The USB-C pads were surprisingly *small*.

{{< figure src="usbc-pads.webp" alt="unpopulated USB-C connector" loading="lazy" >}}

I figured I had my work cutout for me, but then I placed the USB-C connector in on the board and spotted another grievous error. The mounting pins for the connector were 1.2 mm long, but the board is 1.6 mm thick.

{{< figure src="usbc-tht-length.webp" alt="usb connecotr mounting pin drawing" loading="lazy" >}}

Even if it was in stock, no company on the planet could assemble the connector onto the board. The next revision will have to use a thinner PCB. If you scroll up to the [PCB Routing section](#routing) you'll notice the footprint has a 1.2 mm PCB thickness recommendation.

But the mistakes didn't end there. With the connector on the board, the SMT[^14] pads are inaccessible thanks to those aforementioned side flaps.

{{< figure src="usb-connector-on-board.webp" alt="USB connector on PCB" loading="lazy" >}}

Thankfully, the connector I chose was USB 2.0, not 3.0. With some bodge wires and a spare USB-A plug, I made a haphazard USB cable... which created a short across VBUS and ground. My second attempt worked though. I was able to flash the ESP32 with CircuitPython and upload code to it 😎.

{{< figure src="bodge-cable.webp" alt="bodged on USB 2.0 cable" loading="lazy" >}}

Notice how the D+/D- wires are on the side of ESD[^15] diode closest to the connector. This ensures that an ESD event doesn't damage the ESP32.

Also, the process to get CircuitPython on my board was slightly different than the Qualia. This is the tutorial I followed to do it: https://learn.adafruit.com/circuitpython-with-esp32-quick-start/installing-circuitpython.

### Battery Charging/Monitoring

I had some faith the battery charger, MCP73831, still functioned because it's status LED blinked when the board was on with no battery connected. In the absence of a battery emulator, I connected a lipo[^16] to the board with some hook-to-DuPont connectors, a 2-pin JST-PH pigtail cable, and the enduring will of the human spirit.

{{< figure src="battery-bodge.webp" alt="battery questionably attached to the board" loading="lazy" >}}

According to the datasheet, the status LED should be on during charging and off otherwise.

{{< figure src="charge-stat-table.webp" alt="MCP73831 STAT pin truth table" loading="lazy" >}}

This is exactly what happened. I found a some CircuitPython test code for the battery monitor and easily read the battery voltage.

```python
# SPDX-FileCopyrightText: Copyright (c) 2022 ladyada for Adafruit Industries
#
# SPDX-License-Identifier: Unlicense

import time
import board
import adafruit_max1704x

i2c = board.I2C()  # uses board.SCL and board.SDA
# i2c = board.STEMMA_I2C()  # For using the built-in STEMMA QT connector on a microcontroller
max17 = adafruit_max1704x.MAX17048(i2c)

print(
    "Found MAX1704x with chip version",
    hex(max17.chip_version),
    "and id",
    hex(max17.chip_id),
)

# Quick starting allows an instant 'auto-calibration' of the battery. However, its a bad idea
# to do this right when the battery is first plugged in or if there's a lot of load on the battery
# so uncomment only if you're sure you want to 'reset' the chips charge calculator.
# print("Quick starting")
# max17.quick_start = True

while True:
    print(f"Battery voltage: {max17.cell_voltage:.2f} Volts")
    print(f"Battery state  : {max17.cell_percent:.1f} %")
    print("")
    time.sleep(1)
```

I didn't bother testing how accurate the monitor was as the battery discharged since it'd be hard to track with the USB cable disconnected.

### Display

I plugged in a known good 4" display into my PCBA and programmed the board with example code and... nothing. The display's back-light turned on which tells me that the pin-out for the connector was correct and that I2C[^17] works (only partially true, keep reading) since the I2C expander controls the LED driver.

I began to search TTL[^18] RGB routing guidelines to see if I violated any rules, but I didn't find anything specific. What ultimately led me to the error was comparing the waveforms on my board vs the Qualia. All the RGB565 signals looked fine, but the I2C expander, the PCA9554, sent SPI[^19] signals to the display at start on the Qualia. There were no SPI signals on my board. The ESP32 produced the expected I2C signals, but the PCA9554 didn't respond. I realized the problem after doing a port scan.

The example code from Adafruit assumed the I2C address was `0x63`while my board configures it to `0x27`. I actually left a note about this confusion on my schematic.

{{< figure src="io-expander-schematic.webp" alt="schematic of IO expander" loading="lazy" >}}

Setting the proper I2C address made the display work properly.

### Sound

When plugged in a speaker and loaded up example code... nothing. Not even the crackling sound I heard during the prototyping phase. I probed the pins of the I2S chip, the MAX98357, and quickly realized the pin assignment for the PCB and the breadboard prototype were different.

For easier routing, I made the following changes from prototype to PCB:

| MAX98357 Pin     | Qualia Pin Assignment  | Custom Board Asignment |
| ---------------- | ---------------------- | ---------------------- |
| Bit Clock        | board.A1               | board.A0               |
| Left/Right Clock | board.A0               | board.RX               |
| Data In          | board.TX               | board.A1               |

The sound output was clean too. This makes me confident that the horrendous sound coming out of the prototyp was due to bad wiring.

While I'm 99% sure the mismapped pinout was the only problem, before I discovered it, I replaced the pull up resistor on the `SD_MODE` pin with an 1M ohm one to match Adafruit's breakout board. I would swap back to the original 5.1k resistor, but I consider the board verified at this point.

## Next Steps

- I have to swap the polarity of the battery connector. 

- I have to make the board thinner.

That's it. Not bad for a first revision. At this point, I could try to assemble the display and PCB into the enclosure, but it'd be inconvienent to have to dissemble the entire project just to charge the battery. I'll sort out mechanical assembly once the new PCB comes in.

The repository for this project, though completely undocumented as of writing this, is hosted on {{< tracked-anchor href="https://codeberg.org/extralongdivision/dbz-radar" text="Codeberg." >}}. I'll post another write up here when it's ready. [Subscribe to my RSS feed]({{< ref-projects-rss-feed >}}) to get the update as soon as it drops.

{{< eld-byline >}}

{{< donations >}}

[Why are there footnotes?]({{< ref-jargon-url >}})

[^1]: developer

[^2]: inter-integrated circuit sound

[^3]: printed circuit board

[^4]: through hole technology

[^5]: input/output

[^6]: light emitting diode

[^7]: flat flex cable

[^8]: red, blue, green 5 bit, 6 bit, 5 bit

[^9]: Universal serial bus

[^10]: voltage bus

[^11]: do not populate

[^12]: printed circuit board assembly

[^13]: previously known as Institute of Printed Circuits, but known known as Global Electronics Association

[^14]: surface mount technology

[^15]: electrostatic discharge or "static shock"

[^16]: lithium polymer battery

[^17]: inter-integrated circuit

[^18]: transistor-transistor logic

[^19]: serial peripheral interface