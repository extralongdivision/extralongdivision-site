---
date: '2026-08-06T07:04:04-07:00'
draft: false
title: "My Ensh*ttified Experience at FIFA's World Cup"
#
# EDIT THESE
#
author: 'Extra Long Division'
tags: ['fifa', 'enshittification', 'enpoopification', 'world-cup']
# description: 'I forgot to fill out the description.'
# URL is based off the filename
canonicalURL: 'https://extralongdivision.com/articles/my-enpoopified-experience-at-fifas-world-cup/'
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

## An Ode to the Ticket Stub

On March 2, 1962, Wilt Chamberlain scored 100 points in a single game [—]({{< relref-emdash-url >}}) an NBA[^1] record to this day. Why discuss basketball on a World Cup post? [Because 100,000 people say they attended that game, but the venue sat less than 5,000](https://shibevintagesports.com/blogs/news/the-night-wilt-scored-100-as-told-by-harvey-pollack). So how do you differentiate the eyewitnesses from the liars? Easy: ticket stubs.

They prove a fan's story and also serve as a life-long keepsake. But the ticket stub is dying a digital death. Do not confuse this post as an old man shaking his first at technology. Digital tickets are convenient. Can't be lost. Often, they update instantly if scheduling or seating changes.

Ticket stubs still have value in 2026, though. Most events shift the burden, and cost, of printing a ticket to the customer. Some organizations are so adamant about removing  physical ticket overhead, that they lie about their ability to print them. Exhibit A: [Errol Segal, a season ticket holder of 50 years, missed the opening day game because the Los Angeles Dodgers refused to print him physical tickets](https://www.cbsnews.com/losangeles/news/50-year-dodgers-season-ticket-holder-misses-opening-day-after-team-refuses-to-print-tickets-for-2026-season/). The Dodgers did the sensible thing only after Errol's story went viral.

But even this I would not call ensh*ttification. Simply bad customer service.

I had the misfortune to experience FIFA's ensh*ttification firsthand. Of which, I will ~~rant about~~ recant in the rest of this post. 

## The Week Of

I received email reminders to download my ticket the week leading up to the match. [The tickets were only available through FIFA's official app](https://www.fifa.com/en/tournaments/mens/worldcup/canadamexicousa2026/articles/ticket-delivery-information).

{{< figure src="ticket-policy.webp" alt="ticket policy" >}}

As a privacy conscious netizen, I checked how invasive the app was. It had 6 trackers and requested 28 permissions when I first looked. As of writing this, [it has 3 trackers and 16 permissions](https://reports.exodus-privacy.eu.org/en/reports/755617/).

{{< figure src="ticket-app-trackers.webp" alt="ticket app trackers" >}}

Spyware disguised as an app does not surprise me anymore. Perhaps I should be more upset. I decided to be productive and searched for an alternative to FIFA uniquely fingerprinting my phone. They instruct fans to contact them if they have trouble accessing their ticket through the app. I assumed this was the only way to get a ticket emailed to me.

{{< figure src="fifa-contact-instructions.webp" alt="FIFA contact instructions" >}}

The link to the contact form is https://gpcustomersupportfwc2026.tickets.fifa.com/hc/en-gb/requests/new. I couldn't find a way to navigate to it through FIFA's main website. Someone not on FIFA's email list would have to Google for it.

I filled out the contact form and got an automated email that regurgitated the same information about using the ticketing app. Nowhere in the email did it state or imply that a human read my inquiry nor would a living person actually get back to me. It provided no follow up method either. I submitted multiple inquires through the form but couldn't get a response from a human being that wasn't information I'd already received from FIFA.

I don't know what I, or anyone else, would've done if my phone was truly incompatible with the ticketing app. People did recieve physical tickets though. I'll explain how I know that later. Given how difficult it was to even reach a human being, I wouldn't be surprised if FIFA has their own version of Errol Segal who could not attend a game because of technical difficulties.

This, though, I still would not call ensh*ttification. Simply bad customer service. Frustrating, but not surprising. Unfortunately, it's nothing we're all not used to.

## Match Day

The game I'd waited two years to attend finally had arrived. I'd prepared my outfit days in advance. I should've adorned my country's colors with joy, but one thing weighed me down. I still did not have my ticket.

FIFA was still sending me reminders to download it. They warned that cell and WiFi service at the venue could be spotty. FIFA support was still no help. Forced between my privacy and entertainment: I caved. I downloaded the app. Perhaps that is the strategy. Wearing a customer down is a common sales tactic and I rewarded FIFA for this privacy-neglecting pattern. I can't say I'm proud of it.

But then the ensh*ttification began.

The app's ratings were an early sign. As of writing this, about 230 of 306 ratings are 1 star.

{{< figure src="app-ratings.webp" alt="FWC2026 Mobile ticket app ratings" >}}

As soon as I opened the app, it asked for access to my photo gallery. I declined. It also asked for access to my contacts. Declined. None of this is unusual even if it is invasive. After declining permissions, the app sent me to a browser login page. Not an uncommon design pattern, but one I do not like given how error prone it is. Which is exactly what I ran into. After filling in my credentials, I went back to the app... which promptly sent me back to the browser login. I lathered, rinsed, and repeated with no progress.

This excited me honestly. Without logging in, FIFA still hadn't associated all my personal data with my phone's unique fingerprint. And this blip was an opportunity on two fronts. Now I had evidence to claim I could not access my ticket. I returned to the their contact page upset that I hadn't tried to use the app earlier. If it was a few weeks out, they could've emailed my ticket or, * gasp *, even have a beloved physical ticket shipped.

I tried to screenshot the problem... but couldn't. The app wouldn't let me for "security reasons." I used a second device to send a video of the login loop to FIFA and hoped there was a same day solution.

The second opportunity was the login URL[^2]. Perhaps I could sleuth around and access my ticket through this web portal.

The login URL is `https://auth.fifa.com/as/authorize?response_type=code&client_id=<hash>&redirect_uri=tixngo%3A%2F%2Fauth&code_challenge=<hash>&code_challenge_type_method=S256&state=<my-browser-id>&scope=openid+email+profile+tixngo+tixngo8hTTL&campaign=TicketingMobile&lang=en`.

For comparison, trying to login through the FIFA website sends me to this URL: `https://auth.fifa.com/as/authorize?response_type=code&response_mode=form_post&client_id=<hash>&scope=openid+profile+marketing+email+address+phone+p1%3Aupdate%3Auser%3Asafe-only+p1%3Areset%3AuserPassword&lang=en&redirect_uri=https%3A%2F%2Fwww.fifa.com%2Fauth&state=%2Fen&campaign=Fifacom-Web`

The URL parameters hint at the information the ticketing app needs that the normal FIFA site does not. Namely, the `code_challenge`, `code_challenge_type`, `and campaign` parameters and the `tixngo` value in the `state` parameter.

TIXNGO is apparently [an app](https://auth.fifa.com/as/authorize?response_type=code&response_mode=form_post&client_id=35072598-fc20-4142-a469-1b940db47e6f&scope=openid+profile+marketing+email+address+phone+p1%3Aupdate%3Auser%3Asafe-only+p1%3Areset%3AuserPassword&lang=en&redirect_uri=https%3A%2F%2Fwww.fifa.com%2Fauth&state=%2Fen&campaign=Fifacom-Web) and [a service provided by SECUTIX](https://p5backoffice.tixngo.io/login). Their app has no reviews as of writing this. I wouldn't be surprised if the official FIFA app is SECUTIX's with a different skin. That's probably SECUTIX's entire business model.

I tried to mix and match key-value pairs in the URL to access my ticket through the web portal. Specifically, modifying the `redirect_uri` and the `campaign` parameters while removing everything to do with TIXNGO.

After submitting my credentials, the browser sent me back to the app, but this time... I logged in successfully. Oops. Instead of finding a work around, I bypassed the authentication bug. I couldn't tell you what URL made it work.

Since it was match day, I was more happy that I had a ticket than upset by the privacy I had to give up to do so.

While this is ensh*ttification, it's not the reason why I wrote this post.

## Inside the Venue

The mobile ticket worked as expected, thankfully. I bought a hospitality package, so I received a special wristband to grant me access to a reserved area.

I will keep that wristband for the rest of my life.

Why? Printed on it was the match number, date, and countries playing.

{{< figure src="freed-wristband.webp" alt="commemorative wristband" >}}

Finally. It wasn't the keepsake I wanted but it served as proof of my attendance and a lifelong memory. I had one, but the other attendees I met who didn't purchase a hospitality package lacked any match-specific memorabilia.

More frustrating was the gift I received after the game. Because of my ticket package, FIFA gifted me a free laptop case.

{{< figure src="laptop-case.webp" alt="commemorative laptop" >}}

Now this gift in itself is fine. I'll probably use this case. The card was almost certainly intended to be thrown away but I'm going to frame it.

Despite the quality of the gifts, they irked me. An international soccer organization should give gifts geared towards, you know, soccer. Maybe something like a commemorative ticket.

You might call me an entitled fan. You might also say this is an innocent choice made by out-of-touch executives. There's evidence, though, that this choice was an intentional business decision.

## FIFA Created the Problem and Sold the Solution

Let's time jump to a few hours before the match to the moment that compelled me to  document my experience.

Even though I didn't have a physical ticket, I still wanted some type of keepsake as a memory for this specific game. At this point I did not have the match-specific wristband  or the hospitality package gift. Luckily, FIFA had a popup store at a fan festival near the stadium.

I must say, this festival was great. Mostly because of the fellow soccer fans. One of which was on the same quest as me. I never got his name, but he noticed a scarf I'd purchased from the FIFA web store and thought it was specific to the day's match. I regretfully informed him it was country-specific, not match-specific. We commiserated on the lack of merchandise to commemorate the day and parted ways.

Despite the popup not having anything match-specific, I did want to buy a chain of the USA mascot.

{{< figure src="necklace.webp" alt="USA laptop necklace" >}}

Notice how this is a photo of mine and not a screenshot of the web store. If the necklace is available online, I can't find it.

But I did find the reason why I wrote this post. While price checking items in the popup store, I found the following:

{{< figure src="replica-ticket.webp" alt="replica ticket screenshot" >}}

My precious physical ticket. Finally within grasp.

Finding it didn't bring me joy, though. Ten years ago, a physical ticket was the expectation, not a novelty. Even if it wouldn't be usable as event entry, why didn't FIFA gift it to everyone with a hospitality package? Why didn't FIFA include one with all ticket purchases??? The opposite is commonplace. Buying a Blu-ray disc default comes with a free digital download.

I debated not writing this post because how it must seem to an outside observer. "Fan well-off enough to afford World Cup VIP lounge complains about a 19 dollar keepsake." It's the principal that bothers me and should bother you too.

FIFA only sells things people want to buy. An obvious statement that leads to anomalies like some qualifying nations' jerseys being unavailable in the FIFA online store.

{{< figure src="jerseys.webp" alt="Jersey webstore screenshot" >}}

Notice, on the left-hand side, how countries like Jamaica, who did not make the tournament, have jerseys available, but the Scottish cannot buy their country's jersey even though they were a qualifying team.

The fact that replica tickets are available means FIFA *knows* people want physical tickets. Instead of including them with all purchases, they're sold separately. The reason is obvious: profit. Moving to mobile-only tickets reduces overhead, gathers sellable personal data, and increases merchandise sales.

60,000 people packed the venue at the match I attended. If only attendees could buy physical tickets, FIFA grosses 1.1 M. If everyone with an internet connection can buy a replica ticket, the profits will be through the roof.

With this information, let's time skip to a disgruntled me at the venue with the match-specific wristband. Like most event wristbands, it's designed to be destroyed.

{{< figure src="attached-wristband.webp" alt="wristband around my arm" >}}

The black cylinder stopped me from being able to take the wristband off. Pulling, twisting, or a Chinese-finger-trap approach did not work. It makes sense. Otherwise I could give the wristband to someone else who didn't have access to the hospitality area. At this point though, it was the only keepsake FIFA gave me and I be damned if I destroyed it.

I wore that wristband for much longer than I'm willing to admit to strangers on the internet. I was able to cut the black cylinder with heavy duty wire cutters. Inside are spokes that allow fabric to slide in but not out.

{{< figure src="wristband-lock.webp" alt="broken wristband lock" >}}

The internal teeth are akin to tiger spikes that allow you to leave a parking garage but pop your tires if you reverse. Again, this makes sense for the wristband's intended purpose. But I shouldn't have to jump through some many ~~spikes~~ hoops to get a match keepsake.

## Post-Match

Two weeks after the final match, FIFA invited me to fill out a survey.

{{< figure src="survey-email.webp" alt="survey invite screenshot" >}}

Well, since they asked. The email said the survey would take 15 minutes. I intended to share every question they asked me, but after ~45 minutes and 250+ questions, I stopped counting. I wouldn't be surprised if most people didn't finish the survey. I, however, was hell bent on complaining.

From the questions, it's clear FIFA's goal was to quantify sponsorship impact and assess the popularity of new changes to the game like hydration breaks and referee body cams. The most dystopian of the questioning was picking who was and was not a tournament sponsor.

Of the 250+ questions, only 6 asked about the mobile ticketing experience. I submitted the lowest rating for each question of course. One thing did catch my eye though.

{{< figure src="physical-ticket-proof.webp" alt="mobile ticket survey question screenshoot" >}}

The last option proved what, at this point, I thought impossible. The mythical physical ticket does exist! So there were Errol Segal's out there who could not use the mobile app and received physical tickets. How though?  If you're one of the few people who got a physical ticket [please contact me to let me know](mailto:helloworld@extralongdivision.com)!

I complained about many other things in the survey. How difficult it was to contact someone at FIFA, about the non-soccer orientated commemorative gift, and much more I will not bore you with. I even agreed to be recontacted within 3 months so I could complain some more.

The survey culminated with a open-ended text box. Here's what I wrote:

> As mentioned earlier, the mobile ticket app was terrible. FIFA has grown the greatest sports tournament in history but its mobile ticketing app nearly ruined the entire experience for me. As of writing this, 80% of the app store reviews are 1 star. I am not the only one who hated how the mobile tickets we're handled. FIFA created amazing experiences the entire tournament from the fan festivals to the VIP lounge I had the privilege to experience. However, your entire brand will crumble to the ground if the fans who love the tournament you worked so hard to put on cannot even get in! When I downloaded the app I was stuck in a login loop for ages! When I tried to contact FIFA I was given a generic auto-reply that directed me to the same horrendous mobile app that 80% of attendees hated. I am lucky that someone [a white lie; that someone is me] had a device to access my ticket for me. If not I would've been denied access to the great match FIFA put on. Worse, I could not get a reply from a single human being at FIFA. I was only directed to contact forms and automatic email replies. I would love to attend the 2030 Word Cup but I don't want to risk not being able to access the very match I paid to see! Please for the love of the beautiful game, fix ticket delivery and please please please make it easier for paying customers to reach a living, breathing human being if they have trouble accessing their ticket!

I tried to craft my response to pander to FIFA's true intent: maximizing profit. I intentionally made it sound as if FIFA was a great brand that I would happily spend more money on if its ticket delivery was better. Let's see if it works.

## Despite the Ensh*ttification, I'd Do It All Over Again

I've done a lot of grumbling, but truly, the World Cup was an amazing experience. A decade from now, I will not remember the login loop. I will not remember fighting with an inch of black plastic to preserve a piece of clothe with ink on it. I'll remember singing my country's chants on the train to the stadium. Dancing with my countrymen after the match. Taking pictures with strangers from all over the globe because they liked my patriotic outfit.

This is where I must admit, despite all the effort I went to salvage my wristband [—]({{< relref-emdash-url >}}) I still bought a replica ticket. Hypocritical for all the mud I just slang at FIFA. But when 2030 rolls around, that ticket will bring back memories even if it's a fake.

My money is the strongest weapon I have against ensh\*ttification, but I made FIFA's coffers heavier despite the hurdles they made me go through. Perhaps that's the balance companies must make now to maximize profit. Like slowly boiling a frog, FIFA added just enough ensh\*ttification to make me still want to attend their events. Instead of jumping out of the simmering pot, I will gladly save the date for the next tournament. Hopefully, I don't burn.

{{< eld-byline >}}

{{< donations >}}

[Why are there footnotes?]({{< relref-jargon-url >}})

[^1]: national basketball association

[^2]: uniform resource locator, website addresses are a version of these