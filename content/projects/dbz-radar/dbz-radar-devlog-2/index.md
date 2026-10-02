---
date: '2026-10-02 04:43:32 +0000 UTC'
draft: false
title: 'Dragon Ball Radar: Devlog 2'
#
# EDIT THESE
#
author: 'Extra Long Division'
tags: ['dragon-ball-radar', 'esp32', 'circuitpython']
series: ['Dragon Radar']
# description: 'I forgot to fill out the description.'
# URL is based off the filename
canonicalURL: 'https://extralongdivision.com/projects/dbz-radar/dbz-radar-devlog-2/'
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
ShowPostNavLinks: false
ShowWordCount: false
ShowRssButtonInSectionTermList: true
UseHugoToc: false
cover:
   image: "images/visible-radar-in-hand.webp" # image path/url
   alt: "Held Dragon Radar held in someone's hand" # alt text
#    caption: "<text>" # display caption under cover
   relative: true # when using page bundles set this to true
#    hidden: true # only hide on current single page
# editPost:
#    URL: "https://github.com/<path_to_repo>/content"
#    Text: "Suggest Changes" # edit text
#    appendFilePath: true # to append file path to Edit link
---

{{< written-by-a-human >}}

## Previously on Dragon Ball Z!

In [the last installment of this project]({{< ref "/projects/dbz-radar/dbz-radar-devlog-1/" >}}), I proved the concept with a Frankenstein dragon radar. Keep reading to learn about the development since the last post. I've actually got something that looks like the real deal now. I'll make a separate build guide to reproduce the project.

## Electrical Design

This section will be short. I just had two action items since the last update and I only did one of them.  Originally [I wanted to make the board 0.8 mm]({{< ref "/projects/dbz-radar/dbz-radar-devlog-1/#usb-c" >}})[^1] instead of 1.6 mm. I decided to keep the PCB[^2] the same size since that'd lower the USB-C[^3] connector coming out the back of the enclosure (*ominous noises*). Also, even if the mounting pins weren't soldered into place, the SMT[^4] pads would still adhere the connector to the board.

The only electrical change I did was flip the battery connector polarity to match the ones I already have.

## Mechanical Design

Last post, I said I'd wait until new PCBs arrived before redesigning the enclosure. This cost me a couple days of messing with clearance just to mount the PCB. Ultimately I had to make the diameter of the enclosure bigger to correct this. Ironic, since that's what I was trying to avoid during the original design phase described in the last post.

The button actuator was another issue that I would've recognized sooner if I tried to assemble the radar.

{{< figure src="images/button-interference.webp" alt="a PCB button blocked by a 3D printed button" loading="lazy" >}}

The actuator interferes with the PCB's user button such that it's impossible to mount the PCB, even with the aforementioned clearance. Cutting a slot for the user button fixed the issue.

{{< figure src="images/actuator-slot.webp" alt="PCB button fitting into a 3D printed button slot" loading="lazy" >}}

Once I fit the PCB inside the enclosure, I couldn't actually press the user button because the actuator interfered with the board.

{{< figure src="images/pcb-actuator-interference.webp" alt="Highlighted image of a 3D printed button colliding with a PCB" loading="lazy" >}}

I fixed this by making the enclosure thicker and mounting the PCB in a deeper recess. But now the whole radar is too large to palm in one hand *and* press the button at the same time. I mentioned a wrist strap in the last post, but using one doesn't actually help, or at least the ones I have don't. Here's me holding the radar as best as I can with a wrist strap on.

{{< figure src="images/wrist-strap.webp" alt="Awkwardly gripping the Dragon Radar while wearing a wrist strap" loading="lazy">}}

A consequence of a thicker enclosure is the USB-C connector not being flush with the slot in the back. Said slot is larger to accomodate a more recessed connector.

{{< figure src="images/usb-slot.webp" alt="Close up of a vertical USB-C connector visible through a slot in a 3D printed part" loading="lazy" >}}

So it didn't matter if the PCB was 0.8 mm or 1.6 mm. Again, I did this mechanical work after the PCBs arrived. Lesson learned.

## Board Bring up

Everything was plug and play with the updated PCB (version 1.1). I followed the {{< tracked-anchor href="https://learn.adafruit.com/circuitpython-with-esp32-quick-start/installing-circuitpython" text="same steps to put CircuitPython on the board" >}} and my code ran with no problem. I did see some differences between PCB version 1 and version 1.1 though.

For V1, uploading new code only worked after a hard power reset. Not pressing the reset button on the board. This didn't happen with version 1.1. Also, the screen would glitch as if the signal timing was off whenever the heartbeat LED was on. Again, only for version 1 of the PCB. Not an issue for version 1.1. I haven't reproduced this on camera yet.

I'm also seeing streaks of discoloring on the display that I wasn't seeing earlier. It doesn't show up in photos well, but soft peach/orange vertical blotches overlay whatever's being shown. It's especially visible when the screen powers off. Not sure if this is a result of me driving the display incorrectly or some other problem. Either way, it's negatively affecting the authenticity of the replica.

## Cosmetics

If the cover photo didn't give it away, I didn't do any post processing on the enclosure. I don't like the aesthetics, but I'm de-prioritizing looks over other projects/potentially adding more features.

One practical cosmetic issue is screen brightness in direct sunlight. Here's a side-by-side of the radar in the shade vs the sun.

{{< figure src="images/sun-vs-shade.webp" alt="Dragon radar in sunlight and shade" caption="Left: dragon radar in shade. Right: dragon radar in direct sunlight" loading="lazy">}}

The two images accurately represent the difference between shaded and direct light to the naked eye. For the latter, the display acts more like a mirror than a screen. I believe I'm driving the backlight at 100% brightness, but it is still not the most readable in the sun. Using the project for an outdoor scavenger hunt would be very difficult. I might have to source a different screen for future iterations.

## Next Steps

I consider the first phase of this project done. The design files are available on the, still undocumented, {{< tracked-anchor href="https://codeberg.org/extralongdivision/dbz-radar" text="project's repository." >}} I promise to have a proper README there once I post the build tutorial here. Be on the lookout for some video content with the radar too.

{{< eld-byline >}}

{{< donations >}}

{{< series-itemization >}}

[Why are there footnotes?]({{< ref-jargon-url >}})

[^1]: millimeter

[^2]: printed circuit board

[^3]: universal serial bus type c

[^4]: surface mount technology