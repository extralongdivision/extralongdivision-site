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
# canonicalURL: 'https://extralongdivision.com/projects/dbz-radar-devlog-1/'
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
ShowRssButtonInSectionTermList: true
UseHugoToc: false
# cover:
#    image: "<image path/url>" # image path/url
#    alt: "<alt text>" # alt text
#    caption: "<text>" # display caption under cover
#    relative: false # when using page bundles set this to true
#    hidden: true # only hide on current single page
# editPost:
#    URL: "https://github.com/<path_to_repo>/content"
#    Text: "Suggest Changes" # edit text
#    appendFilePath: true # to append file path to Edit link
---

{{< written-by-a-human >}}

## Inspiration

If you want a real life [Dragon Radar](!https://dragonball.fandom.com/wiki/Dragon_Radar#Other_Z_Fighter_Radars)(track this), there are small amount of toys to choose from.

[photo]

None of those can really function as the radar from the anime. The maker in me wanted to change that.

There were some bumps along the way, but the first revision turned out alright. I'll disclose all those bumps, and the eventual working prototype, in this dev[^1]log.

## Prototyping

### CircutPython

A Dragon Radar requires a circular screen. In recent years, these have become more available to the hobbyist maker. There are lots on Alibaba and Aliexpress, but Adafruit has [4"](https://www.adafruit.com/product/5793) and [2.8"](https://www.adafruit.com/product/5793) varieties that are not only well documented but have a complementary dev board: the [ESP32-S3 Qualia.](https://www.adafruit.com/product/5800)

This is where I began prototyping and quickly hit an impasse. Adafruit prioritizes CircuitPython and I couldn't get the CIRCUITPY drive to show up on my Linux machine. I bumbled around factory reset and bootloader repair documentation only for flashing to work first try after connecting the Qualia to a Windows machine. Not sure why.

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

This prevented me from updating the code. [Other people have had this problem too apparently](https://github.com/adafruit/circuitpython/issues/8449) I still don't know the root cause, but the work around I used on  Linux was:

```
sudo cp code.py /media/<username>/CIRCUITPY/code.py
```

### Sound

This was the first hiccup. Those familiar with the Dragon Ball series will know the radar makes this sound:

[sound]

This demo of the Adafruit team playing Star Trek on the Qualia made me confident that the board could be the base for a Dragon Radar.

[https://www.youtube.com/watch?v=yKRatudQSsI] (embeded)

My implementation didn't sound as good.

I bought a breakout board for the same I2S[^2] chip used in the above demo, the MAX98357, and connected it to the Qualia board.

[photo of breadboard setup]

The first audio file in this section sounded like this played through my prototype hardware:

[sound]

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

[anime dragon ball radar]

There are two constraints mandatory to match the anime:

1. The display has to be at the center of the enclosure
2. The activation button must be at the top of the enclosure, aligned with the vertical symmetrical axis

These two constraints seem simple, but forced my hand during mechanical design.

I decided to use the 4" display, HD40015C40, since I figured a display that was too big was better than one that was too small. I didn't have the display in hand yet when designing the enclosure so I had to go off its datasheet.

[photo of display datasheet]

It was in chinglish and honestly frustrating to interpret, but the visible pixels on the screen are not centered in the display assembly. In fact, the center of the bounding box of the display assembly and the center of the active pixel area is offset by [x] mm.

[screenshot]

To hide this in the end product, I'd have to put a bevel around the enclosure's edges. Add a THT[^4] tactile switch (not SMT [^12] for mechanical strength reasons) for the activation button and the offset between the active pixel area and PCB center increases to [Y] mm.

[screenshot]

Adding a bevel to the edges of the display allowed the screen to be the center of the enclosue.

[screenshot]

This close enough to the anime. Finishing the mechanical design for the user input changed things though.

### Activation Button

The button to turn the device on and off is actually an assembly of a shaft and cap. There's heat-set inserts in each part and they're assembled together with a set screw.

[photo]

This is where the beveled edges on the enclosure became a problem. Having the button on the top of the radar would make it much thicker. I could make the button shaft visible from the front when looking at the display, but it doesn't look as true to the anime.

[photo]

I'll probably print both options and decide which one I like more once they're in my hand

### Power Cable Routing

For practical reasons, I wanted the radar to run off a rechargeable battery. The slot for the charger would be easiest to put into the enclosure's back, which would thus require a vertical connector. USB-C is the default nowadays, so I went with the USB440 series from GCT.

[screenshot of rendered back]

This ultimately resulted in some problems, but more on that in the bring up phase.

I'm doing a little time bending here because I placed the USB-C connector in the PCB layout before defining the charging port's location in the mechanical design. I did this because electrical constraints defined the connector's position more than mechanical ones.

Also, at this point I knew there was a lot of empty space on the board, so I didn't leave a special mounting place for the battery. I'll attach it to the board with some double sided tape.

### Mounting Points

Snap-fits are the premiere way to assemble parts together, but I'm too lazy to iterate through a bunch of tolerances before everything assembles well. Instead, I used heat-set inserts to mount the PCB and assemble the enclosure together. To preserve [poka-yoke](https://en.wikipedia.org/wiki/Poka-yoke)(track this), I used different threads for the PCB mounting and enclosure

[photo]

M1 screws were surprisingly expensive to source from the usually suspects. I ultimately found some on Amazon.

### Speaker

The speakers I'm using thankfully ship with adhesive foam. I cut a small nest about ~0.25 mm bigger than the speaker in the enclosure's back as a mounting location. Hopefully the adhesive is enough to keep it into place. Add some holes so the sound escapes and mechanical design is done!

[photo]

## Electronics Design

### Schematic Capture

Adafruit did most of the work. "My" design is a mashup up of the Qualia board, MAX98357 breakout, and the charging circuit from the [Adafruit Feather ESP32-S3](https://learn.adafruit.com/assets/110822).

["my" schematic]

The few modifications I made were:

- Remove the `DN` and `UP` buttons and replaced them with the button chosen in the mechanical enclosure section
- Remove the STEMMA QT/Qwiic connector
- Replace the JST connector with 2.54" spaced THTs[^4] and connected all unused IO[^4.5] to it
- Add a heartbeat LED[^5]
- Replaced jumpers with 0 ohm resistors, depopulating the ones I don't want
- Various quality of life changes like adding more test points and egregious amount of 0 ohm resistors in series with interesting traces

### PCB Layout

#### Placement

The mechanical design dictated the position of the mounting holes, activation button, and the FFC[^6] connector (*technically I could physically rotate the display and rotate the image in software but I opted just to put the connector and activation button at the vertical symmetrical axis of the device*).

This choice forced me to rotate the ESP32 package 45 degrees to avoid a THT inside a keep-out zone. I put the ESP32 on the top right of the board to give the most amount of space to place other components.

[pic of placement]

I'm actually still violating the layout rules provided by Espressif. They recommend the antenna hang off the board ideally or, if not possible, the end of the antenna be at least 15 mm away from the board edge and that the feed point be max 2 mm from a board edge.

[picture]

If I hung the antenna off the board it'd collide with the enclosure and I didn't want to make the enclosure any larger.

[screenshot]

To make rework and hand-soldering easier, I used 0805 sized components wherever I could. This would make my life easier once the boards came back.

#### Stack-up

I decided to do a 4 layer stack-up of `signal+ground/ground/ground/signal+ground`. 

[stackup]

The RGB565[^7] parallel signals were my greatest concern. The two inner ground layers would shield signals on layer 4 from the RGB.

Layer 1 would have the USB[^8] 2.0 traces which technically should be fabricated to 90 ohm, but in practice I've never had problems omitting a controlled impedance. I still routed the signals differential though.

The four layer stack-up also made it much easier to route 3.3 V power rail on layer 4.

#### Routing

The most interesting part to route was the USB-C connector. It has a keep-out zone near the pads that make it almost impossible to connect the USB D+/D- pins and VBUS[^9] pins together.

[screenshot of datasheet keep out]

I interpreted the keep-out zone as only for components and not for all copper. I'm justifying this conclusion with the metal flaps on the side of the connector (These will rear their ugly head once the board is made).

[photo of metal flaps]

Everything else was fairly straight forward to route. I did have to rotate most things 45 degrees so the traces we're neater. Here's the final layout.

[screenshot of layout]

### Ordering

While ordering the board, I realized that I assigned a 100 *uF* decoupling capacitor for the ESP32 instead of a 100 *nF* cap. If you hadn't caught on to the trend, I am lazy. I didn't want to regenerate the gerbers so I just DNP[^10]'d the cap.

The USB-C connector was also out-of-stock. I already designed the mechanical enclosure around that connectors height and (re: lazy) DNP'd that part thinking I could hand solder it on once the boards arrive. That was not a safe assumption.

## Board Bring-Up

### Physical Inspection

Once the boards came back, I realized just how large they are.

[Photo in my hand]

The PCBA[^11] are about as large as they can comfortably fit in my hand and that's before they're put in a larger assembly. I'll certainly have to use a wrist strap for the final build.

### Smoke test

I plugged in a battery into the board and... smoke. Quickly, I realized my mistake. I swapped the battery connector polarity. The Adafruit design I based it on used pin 1 as ground and pin 2 as the positive battery terminal. My schematic matched that, but the footprint mismatched the manufacturer's drawing.

[manufacturing pin 1 location vs KiCad]

I should've caught this, but the root-cause is KiCad's built-in libraries having the wrong pin assignment.

Thankfully Q1 and D7 act as reverse polarity protection for the rest of the circuitry.

[screenshot of Q1 & D7]

### USB-C

Now comes the most egregious mistake I made in the design that I so un-elegantly foreshadowed earlier. I couldn't connect a battery so next step was to solder on the USB-C connector.

While earlier I mentioned how surprisingly large the board was. The USB-C pads were surprisingly *small*.

[Photo of pads]

I figured I had my work cutout for me, but then I placed the USB-C connector in on the board and spotted another grievous error. The mounting pins for the connector were 1.2 mm long, but the board is 1.6 mm thick.

[screenshot of datasheet]

Even if it was in stock, no fabricator on the planet could assemble the connector onto the board. The next revision will have to be 0.8 mm thick.

But the mistakes didn't end there. With the connector on the board, the SMT[^12] pads are inaccessible thanks to those aforementioned side flaps.

[Photo of connector placed into board]

Thankfully, the connector I chose was USB 2.0, not 3.0. With some bodge wires and a spare USB-A plug, I made a haphazard USB cable... which created a short across VBUS and ground. My second attempt worked though. I was able to flash the ESP32 with CircuitPython and upload code to it 😎.

[photo of bodged]

Notice how the D+/D- wires are on the side of ESD[^13] diode closest to the connector. This ensures that an ESD event doesn't damage the ESP32.

Also, the process to get CircuitPython on my board was slightly different than the Qualia. This is the tutorial I followed to do it: https://learn.adafruit.com/circuitpython-with-esp32-quick-start/installing-circuitpython.

### Battery Charging/Monitoring

I had some faith the battery charger, MCP73831, was still functioned because it's status LED blinked when the board was on with no battery connected. In the absence of a battery emulator, I connected a lipo[^12.5] to the board with some hook-to-DuPont connectors, a 2-pin JST-PH pigtail cable, and the enduring will of the human spirit.

[photo of contraption]

According to the datasheet, the status LED should be on during charging and off otherwise

[screenshot of datasheet]

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

I plugged in a known good 4" display into my PCBA and programmed the board with  example code and... nothing.

[photo]

The display's back-light turned on which tells me that the pin-out for the connector was correct and that I2C[^14] works (only partially true, keep reading) since the I2C expander controls the LED driver. I began to search TTL[^15] RGB routing guidelines to see if I violated any rules, but I didn't find anything specific. What ultimately led me to the error was comparing the waveforms on my board vs the Qualia. All the RGB565 signals looked fine, but the I2C expander, the PCA9554, sent no SPI[^16] signals to the display. The ESP32 produced the expected I2C signals, but the PCA9554 didn't respond. I realized the problem after doing a port scan.

The example code from Adafruit assumed the I2C address was `0x63`while my board configures it to `0x27`. I actually left a note about this confusion on my schematic.

[screenshot]

Setting the proper I2C address made the display work properly.

### Sound

When plugged in a speaker and loaded up example code... nothing. Not even the crackling sound I heard during the prototyping phase. I probed the pins of the I2S chip, the MAX98357, and quickly realized the pin assignment for the PCB and the breadboard prototype were different.

For easier routing, I made the following changes from prototype to PCB:

| MAX98357 Pin     | Prototype Pin Assignment | Custom Board Asignment |
| ---------------- | ------------------------ | ---------------------- |
| Bit Clock        | board.A1                 | board.A0               |
| Left/Right Clock | board.A0                 | board.RX               |
| Data In          | board.TX                 | board.A1               |

While I'm 99% sure this was the only problem, before I discovered the pin mismatch I replaced the pull up resistor on the `SD_MODE` pin with an 1M ohm one to match Adafruit's breakout board. I would swap back to the original 5.1k resistor, but I consider the board verified at this point.

## Next Steps

- I have to swap the polarity of the battery connector. 

- I have to make the board thinner.

That's it. Not bad for a first revision. The repository for this project, though completely undocumented as of writing this, is available at [https://codeberg.org/extralongdivision/dbz-radar](track this). I'll post another write up here when it's ready. [Subscribe to my RSS feed](projects link) to get the update as soon as it drops.

{{< eld-byline >}}

{{< donations >}}

[Why are there footnotes?]({{< relref-jargon-url >}})

[^1]: developer

[^2]: inter-integrated circuit sound

[^3]: printed circuit board

[^4]: through hole technology

[^4.5]: input/output

[^5]: light emitting diode

[^6]: flat flex cable

[^7]: red, blue, green 5 bit, 6 bit, 5 bit

[^8]: Universal serial bus

[^9]: voltage bus

[^10]: do not populate

[^11]: printed circuit board assembly

[^12]: surface mount technology

[^12.5]: lithium polymer battery

[^13]: electrostatic discharge or "static shock"

[^14]: inter-integrated circuit

[^15]: transistor-transistor logic

[^16]: serial peripheral interface