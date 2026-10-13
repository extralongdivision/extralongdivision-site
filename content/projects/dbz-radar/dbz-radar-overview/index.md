---
date: '2026-10-12 17:30:00 +0000 UTC'
draft: false
title: 'Dragon Ball Radar Project Overview'
#
# EDIT THESE
#
author: 'Extra Long Division'
tags: ['dragon-ball-radar', 'esp32', 'circuitpython', 'kicad']
series: ['Dragon Radar']
# description: 'I forgot to fill out the description.'
# URL is based off the filename
canonicalURL: 'https://extralongdivision.com/projects/dbz-radar/dbz-radar-overview/'
# author: ["Me", "You"] # multiple authors

#
# Optional
#
showToc: false
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
cover:
   image: "images/radar-in-nature.webp" # image path/url
   alt: "Dragon ball radar in front of fall foliage" # alt text
#    caption: "<text>" # display caption under cover
#    relative: false # when using page bundles set this to true
#    hidden: true # only hide on current single page
# editPost:
#    URL: "https://github.com/<path_to_repo>/content"
#    Text: "Suggest Changes" # edit text
#    appendFilePath: true # to append file path to Edit link
---

{{< written-by-a-human >}}

Over the past couple of months, I've been making a replica Dragon Radar from {{< tracked-anchor href="https://en.wikipedia.org/wiki/Dragon_Ball" text="Akira Toriyama's Dragon Ball series." >}} The project now looks pretty close to its anime inspiration. This post will condense all the design decisions made into one place. For nitty-gritty details, read the [previous series of developer logs.]({{< ref "projects/dbz-radar/dbz-radar-devlog-2/" >}})

## Capabilities

Before I get into how I made the project, let's go over what it can actually do. It's pretty simple: press the button and the radar starts beeping and shows a graphic indicating nearby dragon balls.

{{< figure src="images/screen-load.webp" alt="Dragon ball radar screen loading it's screen." loading="lazy" width="700" >}}

In the future, it'd be cool to make replica dragon balls that the radar can detect. Ideally, beeping faster depending on how close the ball is while also indicating the ball's proximity on screen. Perhaps in a future version.

## Electrical Design

The circuitry contains a handful of components:

- A microcontroller
  
- An audio amplifier
  
- A display
  
- Battery charger
  
- Battery monitor
  

The schematic is a combination of {{< tracked-anchor href="https://www.adafruit.com/product/5800" text="Adafruit's Qualia" >}} and {{< tracked-anchor href="https://www.adafruit.com/product/5477" text="Adafruit's ESP32-S3 Feather" >}}. Instead of explaining the schematic, you can study or modify it yourself. I've released the {{< tracked-anchor href="https://codeberg.org/extralongdivision/dbz-radar/src/branch/main/ecad/dbz-radar" text="KiCAD project" >}} as Solderpad Hardware License 2.1.

{{< figure src="images/schematic.webp" alt="schematic" loading="lazy" >}}

## Mechanical Design

The Dragon Radar's enclosure is designed for 3D printing. There's only four components.

1. The enclosure front
  
  - {{< figure src="images/enclosure-front-all-inserts.webp" alt="3D printed enclosure front" loading="lazy"
   >}}

2. The enclosure back
  
  - {{< figure src="images/enclosure-back.webp" alt="3D printed enclosured back" loading="lazy" >}}

3. The button shaft
  
  - {{< figure src="images/button-shaft.webp" alt="3D printed button shaft" loading="lazy" >}}

4. The button cap
  
  - {{< figure src="images/button-cap.webp" alt="3D printed button cap" loading="lazy" >}}

Heat-set inserts need to be installed into the 3D-printed parts for everything to assemble together. Using a FDM[^1], printer, all the parts took ~17 hours to print. The enclosure front and back were the biggest time sinks.

Again, print the radar for yourself from {{< tracked-anchor href="https://codeberg.org/extralongdivision/dbz-radar/src/branch/main/mcad" text="the files available on the project's repository" >}}. For step-by-step instructions on how to build the radar, [follow this tutorial.]({{< ref "projects/dbz-radar/dbz-radar-tutorial/" >}})

## Software

All the code is written in CircuitPython. The microcontroller is a ESP32-S3 and the board is programmed via a USB-C connector, so you could use just about any toolchain you want to modify the firmware.

Honestly, the code is messy. It also doesn't implement all the hardware. I.e the battery monitor doesn't do anything nor is the backlight brightness programmable. And it probably should be a finite state machine instead of a bunch of if else statements. {{< tracked-anchor href="https://codeberg.org/extralongdivision/dbz-radar#license" text="The code is permissively released under Apache-2.0" >}}, so please improve it.

## Next Steps

As said earlier, [a tutorial is already out]({{< ref "projects/dbz-radar/dbz-radar-tutorial/" >}}). I've finally documented the {{< tracked-anchor href="https://codeberg.org/extralongdivision/dbz-radar/" text="project's repository" >}} as well. Development for this phase is over. If you'd like to see more updates, shoot me an [email]({{< email >}}) or message me on [social media.]({{< links >}}) I'll be posting some video content of the radar and start working on my next project.

{{< eld-byline >}}

{{< donations >}}

{{< series-itemization >}}

[Why are there footnotes?]({{< ref-jargon-url >}})

[^1]: fused deposition modeling