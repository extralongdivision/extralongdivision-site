---
date: '2026-08-18T22:56:32-07:00'
draft: false
title: 'Analytics Statement'


canonicalURL: 'https://extralongdivision.com/analytics-statement/'

showToc: true
TocOpen: true
UseHugoToc: false
---

{{< written-by-a-human >}}

## This is More Than a Privacy Policy

While a privacy policy is a legal document meant to conform to governing law, this declaration states my ethos with regards to your privacy. I'll also allow you to peek behind the curtain to see exactly what data I track and care about.

But first, it's important to say:

- I do not sell your personal data.

- I have no plans to sell your personal data in the near or distant future.

## Why I Have Trackers

Respectfully, I don't even care *who* you are.

I do care, though, about *what* you do on this site. You plural. Not you singular. Knowing what articles and projects get the most traffic, have the lowest bounce rate, highest visit duration, etc, help me know what subjects and content people find interesting.

Similarly, I'm interested in what channels work the best in bringing people here. Since [I syndicate quite liberally across different sites]({{< ref "articles/content-philosophy/#content-channels" >}}), this data is good feedback to optimize that practice.

While my ethos won't change, the minutiae of analytics may. The following sections may be updated to reflect that.

## What I Collect and How I do it

I use {{< tracked-anchor href="https://umami.is/" text="Umami">}} for analytics. It's FLOSS[^1], GDPR[^2] compliant, and most importantly, doesn't follow you around the internet. Notice the lack of cookie consent banners on this site. Umami doesn't use them as a feature.

You could search the Umami docs to see the data it collects, but below is the peak behind the curtain I promised.

{{< figure src="dashboard.webp" alt="Umami dashboard" >}}

This is my gold. The pages people visit and the amount of time they spend on them is invaluable information. Umami is probably overkill for this site, but it was easy to setup, so I use it.

The links to my [RSS]({{< ref "/rss" >}}) feeds are Umami redirects too. Similarly there is a 1-by-1 tracking pixel within the RSS file itself. These let me know when someone uses an RSS reader to access this site's content without ever visiting from a browser. There is also a tracking pixel on the site. 

Finally, l also track when users leave via external links. The link to Umami in this section is one of them. This outbound traffic can help me answer questions like, " do people prefer viewing my Codeberg repo or GitHub?"

## How to Circumvent Tracking

Not something most sites will show you how to do. I'll be honest: it's pretty easy. Most add blockers disable, from what I can tell, all the tracking mentioned above. Even the 1-by-1 pixel and outbound event tracking. Using a lightly hardened browser like Brave made users invisible from my testing.

[Why are there footnotes?]({{< relref-jargon-url >}})

[^1]: free (as in beer) libre open source software

[^2]: General Data Protection Regulation
