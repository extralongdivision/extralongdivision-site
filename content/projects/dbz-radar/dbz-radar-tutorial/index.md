---
date: '2026-10-06 06:09:05 +0000 UTC'
draft: true
title: 'How To Make a Dragon Ball Radar'
#
# EDIT THESE
#
author: 'Extra Long Division'
tags: ['dragon-ball-radar', 'esp32', 'circuitpython']
series: ['Dragon Radar']
# description: 'I forgot to fill out the description.'
# URL is based off the filename
canonicalURL: 'https://extralongdivision.com/projects/dbz-radar/dbz-radar-tutorial/'
# author: ["Me", "You"] # multiple authors

#
# Optional
#
showToc: true
TocOpen: true
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
   image: "images/dbz-radar-xray.webp" # image path/url
   alt: "An image split diagnally, the to left is a Dragon Ball Radar in someone's hand and the bottom right is a PCB inside a 3D printed enclosure"
#    caption: "<text>" # display caption under cover
   relative: true # when using page bundles set this to true
#    hidden: true # only hide on current single page
# editPost:
#    URL: "https://github.com/<path_to_repo>/content"
#    Text: "Suggest Changes" # edit text
#    appendFilePath: true # to append file path to Edit link
---

{{< written-by-a-human >}}

## Introduction

Keep reading if you want to build your own Dragon Radar from the internationally acclaimed *{{< tracked-anchor href="https://www.viz.com/shonenjump/chapters/dragon-ball" text="Dragon Ball" >}}* franchise. If you want to learn more about how I designed it, read [the latest developer log.]({{< ref "/projects/dbz-radar/dbz-radar-devlog-2/" >}})

Before you begin, you'll need to acquire some tools and parts. The files to manufacture the 3D[^1] printed components and PCBA[^2] are available on the {{< tracked-anchor href="https://codeberg.org/extralongdivision/dbz-radar/" text="project's repository." >}}

If you don't have the means to produce the PCBA and 3D printed parts yourself, you can use a contract manufacturer that services your region. Exact providers will vary based on where you live.

### Parts

1. Enclosure front (3D printed)

2. Enclosure Back (3D printed)

3. Button shaft (3D printed)

4. Button top (3D printed)

5. M2x0.4mm threaded insert (x7)

6. M2x8mm set screw

7. M2x4 fastener (x6)

8. HD40015C40 4" round display

9. Dragon Radar V1.1 PCBA 

10. M1x0.25mm threaded insert (x6)

11. M1x4mm screw (x6)

12. Double-sided tape

13. Lithium polymer battery

14. Mini oval speaker

### Tools

At minimum you'll need:

1. A screwdriver for the fasteners

2. A heat stake or soldering iron

3. Scissors

Not required, but useful tools:

- Tweezers

- Needle nose pliers

## Program board

{{< tracked-anchor href="https://codeberg.org/extralongdivision/dbz-radar/src/branch/main/bin/" text="Using the binary file in the project's repository" >}}, {{< tracked-anchor href="https://learn.adafruit.com/circuitpython-with-esp32-quick-start/installing-circuitpython/" text="follow the instructions provided by Adafruit to install CircuitPython on the board." >}} Once complete, drag-and-drop the source code available on the {{< tracked-anchor href="https://codeberg.org/extralongdivision/dbz-radar/" text="project's repository." >}} After firmware upload, a heartbeat LED[^3] will blink once the board recieves power.

## Assembly Procedure

Below are step-by-step instructions to build the project. Cross-reference the numbered list in the [Parts](#parts) section to identify components.

1. Gather M1 heat-set inserts and the enclosure front.

   - {{< figure src="images/enclosure-front-m1-inserts-annotated.webp" alt="3D printed part next to a bag of M1 threaded inserts" loading="lazy" >}}
   
   - Use a soldering iron to install six (6) M1 heat set inserts in the enclosure front.

1. The enclosure front should look something like this.

   - {{< figure src="images/enclosure-front-m1-inserts-highlight.webp" >}}

1. Gather M2 heat-set inserts and the enclosure front.

   - {{< figure src="images/enclosure-front-m2-inserts-annotated.webp" alt="3D printed part next to a bag of M2 threaded inserts" loading="lazy" >}}
   
   - Use a soldering iron to install six (6) M2 heat set inserts in the enclosure front.

1. The enclosure front should look something like this.

   - {{< figure src="images/enclosure-front-all-inserts-highlight.webp" alt="Enclosure front with all inserts installed" loading="lazy" >}}

1. Gather the button shaft, button cap, and M2 heat set inserts.

   - {{< figure src="images/button-shaft-cap-m2-inserts-annotated.webp" alt="Button parts next to M2 inserts" loading="lazy" >}}
   
   - Use a soldering iron to install the M2 heat set inserts into the button shaft and button cap

1. The parts should now look something like this.

   - {{< figure src="images/button-inserts-highlight.webp" alt="M2 inserts installed in 3D printed button cap and button shaft." loading="lazy" >}}

1. Install the button shaft sub-assembly into the enclosure front.

   - {{< figure src="images/enclosure-front-button-shaft-highlight.webp" alt="3D printed button shaft in the enclosure front's slot." loading="lazy" >}}

1. Gather an M2 set screw.

   - {{< figure src="images/enclosure-front-set-screw-annottated.webp" alt="M2 set screw next to the enclosure front." loading="lazy" >}}
   
   - Install the M2 set screw into the button shaft so it partially protrudes.

1. The sub-assembly should look something like this now.

   - {{< figure src="images/m2-set-screw-highlight.webp" alt="M2 set screw installed into the button shaft." loading="lazy" >}}

   - Install the button cap onto the partially extruded M2 set screw

1. The enclosure front should look somthing like this now

   - {{< figure src="images/button-cap-highlight.webp" alt="Button cap fastened onto the button shaft." loading="lazy" >}}

1. Gather a HD40015C40 round display.

   - {{< figure src="images/display-enclosure-front-annotated.webp" alt="Round display next to enclosure front." loading="lazy" >}}
    
   - install the display in the enclosure front.

1. The sub-assembly should look something like this now

   - {{< figure src="images/display-enclosure-front-installed.webp" alt="Round display installed in enclosure front." loading="lazy" >}}

1. Gather a PCBA.

   - {{< figure src="images/pcba-enclosure-front-annotated.webp" alt="PCBA next to the enclosure front sub-assembly." loading="lazy" >}}
    
   - Place the PCBA in the enclosure front.

1. Attach the display ribbon cable to the PCBA connector.

   - {{< figure src="images/display-ribbon-highlight.webp" alt="PCBA in enclosure front without the display ribbon connected." loading="lazy" >}}

1. The sub-assembly should look something like this now

   - {{< figure src="images/display-ribbon-installed-highlight.webp" text="PCBA in enclosure front with display ribbon connected." loading="lazy" >}}

1. Gather M1 screws.

   - {{< figure src="images/enclosure-front-m1-screws-annotated.webp" alt="M1 screws next to the enclosure sub-assembly" loading="lazy" >}}

   - Use the M1 screws to fasten the PCBA into the enclosure front.

1. It's hard to see but the sub-assembly should look something like this now.

   - {{< figure src="images/m1-screws-highlight.webp" alt="PCBA fastened into the enclosure front." loading="lazy" >}}
    
1. Gather a battery and double-sided-tape

    - {{< figure src="images/enclosure-front-lipo-tape-annotated.webp" alt="Enclosure front sub-assembly next to a battery and double sided tape." loading="lazy" >}}
    
    - Insert the battery connector into the PCBA and secure it with double sided tape.

1. The enclosure sub-assembly should look like this now.

   - {{< figure src="images/installed-lipo.webp" alt="Battery installed into sub-assembly." loading="lazy" >}}

1. Gather the enclosure back and a speaker

   - {{< figure src="images/enclosure-back-speaker-annotated.webp" alt="Enclosure back next to a mini oval speaker" loading="lazy" >}}

1. Depending on your part tolerance, the speaker can friction fit into into the enclosure back. If not, expose the adhesive tape on the speaker.

    - {{< figure src="images/enclosure-back-speaker-tape-highlight.webp" alt="Mini oval speaker with adhesive partially exposed." loading="lazy" >}}
    
    - Now, install the speaker into the enclosure back.

1. The sub-assembly should look something like this now.

    - {{< figure src="images/enclosure-back-subassembly.webp" alt="Mini oval speaker installed into the enclosure back." loading="lazy" >}}

1. Gather the enclosure front and back sub-assemblies.

    - {{< figure src="images/wip-enclosures.webp" alt="Front and back enclosure sub-assemblies next to each other." loading="lazy" >}}
    
    - Insert the speaker cable into the PCBA connector.

1. The assembly should look something like this now.

    - {{< figure src="images/speaker-installed-highlight.webp" alt="Speaker cable connected to the PCBA." loading="lazy" >}}

1. Gather M2 screws and the radar sub-assembly.

    {{< figure src="images/enclosure-m2-screws-annotated.webp" alt="M2 screws next to the Dragon Radar sub-assembly." loading="lazy" >}}
    
    - Using a screwdriver, fasten the enclosure back into the enclosure front with six (6) M2 screws.

1. The back of the Dragon Radar should look like this.

    - {{< figure src="images/m2-screws-installed-highlight.webp" alt="Back of completed Dragon Radar." loading="lazy" >}}

You're done!

{{< figure src="images/visible-radar-in-hand.webp" alt="Someone holding a fully built Dragon Radar." loading="lazy" >}}

{{< eld-byline >}}

{{< donations >}}

{{< series-itemization >}}

[Why are there footnotes?]({{< ref-jargon-url >}})

[^1]: three dimensional

[^2]: printed circuit board assembly

[^3]: light emitting diode