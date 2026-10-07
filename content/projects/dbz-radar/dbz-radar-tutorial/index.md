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

## Introduction

Keep reading if you want to build your own Dragon Radar from the internationally acclaimed [*Dragon Ball*] (link) franchise. If you want to learn more about how I designed it, read [the latest developer log.] (link)

Before you begin, you'll need to acquire some tools and parts. The files to manufacture the 3D[^1] printed components and PCBA[^2] are available on the [project's repository] (link).

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

[Using the binary file in the project's repository] (link), [follow the instructions provided by Adafruit to install CircuitPython on the board.] (link) Once complete, drag-and-drop the source code available on the [project's repository] (link). After firmware upload, a heartbeat LED[^3] will blink once the board recieves power.

## Assembly Procedure

1. [front enclosure and M2 set screws]
   
   - Use a soldering iron to install six (6) M2 heat set inserts in front enclosure

2. [M2 set screws installed in front enclosure]

3. [WIP front ecnslosure in next to M1 screws]
   
   - Use soldering iron to install six (6) M1 heat set inserts in front enclosure

4. [Installed M1 screws in front enclosure]

5. [uninstalled button shaft hole and button cap hole]
   
   - Use a soldering iron to install the M2 heat set inserts into the button shaft and button cap

6. [button shaft and button cap with M2 insert installed]

7. [set screw next to WIP button shaft]
   
   - Install the M2 set screw into the button shaft so it partially protrudes

8. [set screw half way into WIP button shaft]

9. [WIP shaft next to front enclosure]
   
   - Install WIP shaft into front enclosure

10. [WIP enclosure next to button cap]
    
    - Fasten button cap onto button shaft

11. [Installed button cap]

12. [WIP front enclosure next to display]
    
    - install display in front enclosure

13. [Installed display]

14. [WIP front enclosure next to PCBA]
    
    - Place PCBA in front enclosure

15. [WIP front enclosure next to M1 screws]
    
    - Use screwdriver to fasten PCBA into front enclosure

16. [Installed PCB]

17. [WIP front enclosure and double sided tape]
    
    - Apply doubled sided tape to the PCB

18. [WIP front enclosure next to lipo]
    
    - install battery connector and place it on double sided tape

19. [Speaker next to back enclosure]

20. [Speaker with adhesive cover removed]
    
    - Removed the adhesive cover and install speaker into back enclosure

21. [Speaker installed in enclosure back]

22. [WIP back WIP front enclsoure]
    
    - install speaker cable into PCBA

23. [Speaker connected]

24. [WIP back on WIP front next to M2 screws]
    
    - Using a screwdriver, fasten the enclosure back into the enclosure front with six (6) M2 screws.

25. You're done!

{{< eld-byline >}}

{{< donations >}}

{{< series-itemization >}}

[Why are there footnotes?]({{< ref-jargon-url >}})

[^1]: three dimensional

[^2]: printed circuit board assembly

[^3]: light emitting diode