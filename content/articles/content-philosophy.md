---
date: '2026-07-21T00:00:00-00:00'
lastmod: '2026-08-21T01:00:01-00:00'
draft: false
title: 'Content Philosophy'
#
# EDIT THESE
#

author: 'Extra Long Division'
tags: ['opinion', 'content-creation']
# description: 'I forgot to fill out the description.'
# URL is based off the filename
canonicalURL: 'https://extralongdivision.com/articles/content-philosophy/'

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

# cover:
# image: "<image path/url>" # image path/url
# alt: "<alt text>" # alt text
# caption: "<text>" # display caption under cover
# relative: false # when using page bundles set this to true
# hidden: true # only hide on current single page
# editPost:
# URL: "https://github.com/<path_to_repo>/content"
# Text: "Suggest Changes" # edit text
# appendFilePath: true # to append file path to Edit link
---

{{< written-by-a-human >}}

## Preface

This post ended up much longer than I'd thought it be. This document is part journal, part armchair philosophy, and part soapbox. More directly, this is a snapshot of my thinking before I start a new chapter: content creation.

Much has been written about content, but I'll condense my opinion to one phrase: content creators are the used car salesmen of the Information Age. That is, morals and ethics go out the window for the sake of money. While a used car salesmen employs dirty tactics to sell you a rundown car, content creators shamelessly publish whatever gets them views, likes, sponsorship, etc. Examples of this are endless, but Ross Creations' possum launcher is an obvious one.

Now, there are plenty of cars salesmen with integrity. Likewise, there are countless influencers monetizing ethically. I call out the bad actors so I'll never become one. In a similar sense, this plague is not unique to used car salesmen nor content creators. Alas, it is a pithy statement to get my opinion across.

## My Competitive Advantage

> In simple terms, a competitive advantage is a unique attribute or
> capability that enables a business to stand out from its competitors in
> the marketplace. - *Investopedia*

Content creation is a saturated field. My space, the maker community, is particularly saturated by people much smarter, more credentialed, and with much _much_ more resources than me. Despite the glut of people in this space, there is an area I can compete in: well documented projects.

This is beyond ironic since a working principle of the maker community is sharing and reusing others' designs. Engineers are notorious for bad documentation though, even in a professional setting. For example, as of writing this, the C unit testing framework, Unity, has virtually no documentation. Only a paid course that doesn't cover all the capabilities of the project.

This documentation contradiction is something that's frustrated me about makers. So many projects are nothing more than a sparse README, a ten second demo on YouTube, a broken link to a dead blog, etc. What will differentiate me is an obsession for detailed development logs and extensive documentation.

Moreover, very few creators document their custom PCBAs[^1]. Most rely on off-the-shelf development boards for their (very impressive) projects. Which makes sense. Hardware is hard. Staying on the content treadmill is a lot easier if someone else has already done the board design for you.

This gives me an opportunity to be a content creator not only documenting their projects well, but also documenting the hardest part about hardware.

## Documentation's Purpose

> Documentation is like sex: when it's good, it's very, very good; and when it's bad, it's still better than nothing.  *- Dick Brandon*

And when it's wrong, it's painful.

Not the best corollary, but it adds a missing aspect to this quote. Countless times I've followed a guide and realized it's wrong. It either never was right, or it isn't now and the maker didn't bother updating it.

The bad documentation problem is compounded by a recent trend: the dominant medium for knowledge is shifting from text to audio/video. For millennia, the most efficient way to preserve information was writing it down. But thanks to the attention economy, audio/video mediums are so dominant that, for example, it's standard marketing to make trailers for novels [—]({{< ref-emdash-url >}}) a written art form

Video has a place (more on that later), but video monetization has led to absurd content. I.e this 11 hour YouTube course on running an Amazon fulfillment business.

{{< youtube LegZUuOVZ9Y >}}

It's not a series of videos, it's an 11 hour block. The ability to jump to sections is irrelevant to my gripe. A blog post could be searched for by keyword, updated as certain sections go out-of-date, added to as new information is discovered, etc. But since this is a video, the whole thing has to be remade regularly. Which is the point. This particular creator makes a new video every year because it's part of their content cycle. Education is a secondary goal. The primary goal is to consistently publish new content.

But documentation's primary goal is to inform. Docs are a reference. Imagine if you had to read your car's manual from start to finish in order to change your tire. Instead, you go to the relevant section and read the portion you're interested in whenever you have an inquiry. Skipping through a video or podcast is not the solution!

In the digital age, the best medium for technical documentation is rich text. Not video. Not audio. Text and photo. Nothing is better. It's trivial to update text, but videos require shooting a whole new one. It's trivial to search text for the content you want. With video, you're lucky if AI[^6] vomited out a poorly converted transcript. For documentation, rich text >> audio/video. Period.

## Video's Purpose (For Makers)

What video can do much better than text is quickly showcase the capabilities of a project. Trying to explain what a yo-yo does via text is much less effective than a short clip.

But if you combine engineers' tendency to ignore documentation with how easy video content goes out-of-date, the result is a graveyard of promising project demos with absolutely zero follow up. "OP[^2] never delivers" is painfully true for makers. Demo videos paired with good documentation solve this problem.

For me, polished demos/video updates on social media platforms will be ads for my competitive advantage [—]({{< ref-emdash-url >}}) well-documented projects. There will be other content creators making cooler, more impressive projects than me. Hopefully, consistent "ads" will grow an audience entertained by my taste, but also interested in reproducing and re-mixing the projects I share.

## A Digression on Freedom of Information

> Everyone has the right to ... seek, receive and impart information and ideas through any media and regardless of frontiers *- Article 19, Universal Declaration of Human Rights*

The United Nations wrote this document as a guiding principle for nation states, not individuals. It is still relevant, though. As said earlier, a cornerstone of the maker community is the ability to share and learn from others' projects. What's beautiful about makers is our community thrives in an environment where creator share of profits consistently shrink.

Now, a common-business model is stashing articles, design files, behind-the-scenes content, etc. behind a pay wall. Do not mistake this remark as an argument against makers earning money. I believe the opposite. You deserve compensation for your work. But if every maker puts the details of their project behind a paywall, we reduce our ability to learn from each other.

A shining counterexample is {{< tracked-anchor href="http://incompetech.com/" text="Kevin Macleod" >}}. You've probably heard his music without knowing it. Kevin has thousands of royalty-free music available on his website. All he asks for is credit. Because of that, not in-spite of, he has credits in award-winning films and TV shows.

I'll likely never reach the acclaim of Kevin Macleod. I'll follow the path he pioneered, though: generously licensing the work I publish while kindly asking for donations. This will almost certainly be less lucrative in the short-term, potentially long-term as well. But to quote Sir Issac Newton:

> If I have seen further than others, it is by standing upon the shoulders of giants.

I would not be the engineer I am today without studying, and receiving mentorship from, extremely talented makers. It is only right to contribute back to the community that I benefited so greatly from.

## "Community Building"

Many people in the content creation space use the term "community" when they really mean fans. They build a "community", by asking their "community" questions, replying to comments, and answering DMs[^3]. This is not community building. It's growing a following. The former sounds more authentic so that's the preferred language.

But if someone follows you because they like you, they're a fan. Remove the creator and the ~~community~~ following dissolves. A community interacts because they like each other, not just a specific person. Remove one creator and the community persists.

So I will not be building a community. I will be joining one (more on that later). My content will try to convince them to let me in. Hopefully they do.

### Goals

My community-joining goals are simply:

1. Connect with fellow makers

2. Discover other like-minded communities

The difference between these goals is subtle but important. As said earlier, a core principle in the maker community is reproducing and re-mixing peoples' ideas. Other makers need to know my projects exist to do that. I need to know that they exist too. There is also a group of people who are not makers, but use or celebrate what makers create, often from a perspective that someone busy making does not have. I need to connect with these people too. Not just for the sake of improved projects, but because they are good vibes.

### Communities >> Followers

Notice how gaining a large following is not my goal. In fact, I think a large following is a trap.

The standard business model for tech services in general, not just social media, is capture the attention of as many people as possible, often by used-car-salesmen-y means, then sell their attention to advertisers. This actually gives the user, not tech companies, more power.

An user can pick and choose who to give their attention to on a whim. In the copycat world of tech, there are plenty of options to choose from. This is why platforms {{< tracked-anchor href="https://www.merriam-webster.com/slang/enshittification" text="ensh*ttify" >}}. They hold their users' attention hostage to ensure their real customers, advertisers, get their money's worth. Eventually, the platform hits a critical mass of ensh*ttification and users migrate somewhere else. It happened to LiveJournal, Digg, Facebook, Vine. The list is endless.

The same happens to content creators. No matter how they spin it, their following is a customer base. Content creators falling off is akin to users migrating from social media platforms. Your following can revolt in multiple ways. Perhaps you don't post as much as they want. Perhaps you're posting different content than what they originally followed you for. Perhaps you're not reciprocating the para-social relationship they've formed with you. Either way, if your following leaves, your career is over.

But communities are different.

Communities are about the collective, not the creator. Communities are resilient. Even more so in the digital age. Ostracized communities still congregate in chat rooms and forums despite mainstream channels deplatforming them.

It does not matter what big tech platform rises or falls [—]({{< ref-emdash-url >}}) people will still make things. If I'm a welcome member, I can follow makers wherever they decide to hangout.

Large followings restrict creator freedom too. Remember, it is the follower, not content creator, that has the power. Robert Rich, a trailblazer in the ambient, trance music scene with albums dating back to the 80s, described this exact phenomenon in 2008; before Instagram or the Facebook like existed.

> If we play to the same 1000 people, and keep doing the same basic thing, eventually the Fans become sated and don’t feel a need to purchase this year’s model, when it’s almost identical to last year’s but in a slightly different shade of black. Yet when the Fans’ Favorite Artist starts pushing past the comfort zone of what made them True Fans to begin with, they are just as likely to move their attention onwards within the box that makes them comfortable. Damned if you do or don’t...When an artist relies on such intense personal commitmen[sic] from such a small population, it’s like an animal that relies solely upon the fruit of one tree to survive. This is a recipe for extinction.

This is a massive problem if the goal is growing a following. Many creators, like iDubbbz and Natalie Tran, felt obligated to continue making content similar to what gained them fame. The very following they worked so hard to build prevented them from experimenting in new areas.

Joining a community doesn't have this problem. Communities have expectations, but cultures naturally evolve, grow, and redefine themselves as time goes on. Makers can jump from project to project without being criticized for it. It doesn't matter if you're reusing or remixing something; the community will welcome the contribution.

### Communities: Joining vs Building

#### Moderation

Growing a following is not a new concept, nor are its problems. As far back as 2004, Austin Whitney encouraged musicians to build a small group of die hard fans.

> I think a new definition of success will be the artist who has 5000
> passionate fans worldwide who spend 20-30 dollars a year on your
> creative output.

Some people like Pat Flynn and Kevin Kelly advocate for growing a group of 1,000 dedicated fans. They admit that you'll need several casual fans for every super fan gained. This is similar to amassing the large following described in the last section. It also has the same pitfalls.

One not mentioned in the previous section is the burden on the creator. Kevin Kelly admits as much.

> Not every artist is cut out, or willing, to be a nurturer of fans.

If I join a community, they have already self-selected. Sub-communities have formed and splinter groups have branched off. I don't have to do any moderation.

If I build a community, the onus is on me to shepherd those people. I'd rather make things.

#### Communities are Easier to Make Content For Than Followings

While previous sections might sound dismissive of content creators growing their own following, the communities that I, and likely you, know and love are probably the product of a small group of passionate people nurturing a fandom. This is very hard. Way harder than joining an existing community.

I mentioned Robert Rich earlier and quoted his response to Kevin Kelly's concept of 1000 True Fans. {{< tracked-anchor href="https://kk.org/thetechnium/the-reality-of/" text="I highly encourage you to read it in full." >}}

There is much to ponder in Robert's commentary, but especially relevant to makers is the isolation.

> The sort of artist who survives at the long tail is the sort who would
> be happy doing nothing else, who willingly sacrifices security and
> comfort for the chance to communicate something meaningful, hoping to
> catch the attention of those few in the world who seek what they also
> find meaningful. It’s a somewhat solitary existence, a bit like a
> lighthouse keeper throwing a beam out into the darkness, in faith that
> this action might help someone unseen.

To survive being a maker, you must enjoy making. We spend most of our time designing, troubleshooting, and iterating on a project that only exists in our head. It takes months or years of work before anyone else sees it.

Content creators must enjoy the process. If having a following is your goal, you will not last. I have friends who are effectively lifestyle content creators, but they only share to their close friends on Instagram, inner circle on Snapchat, etc. They make content because they enjoy the process, not because they're amassing a following.

To expand on Robert's lighthouse analogy, if you join a community, they're already other lighthouse keepers. If you add a lighthouse to their collection, the other keepers will come by. Check out how yours is running. Tell you how they run theirs. But if you're building a community, you are alone in the lighthouse. If you don't enjoy maintaining it, you'll abandon it completely.

### Work Life Balance

A curious thing is happening in content creation. Creators used to gain an audience from a niche. Perhaps it was stop motion video, health and fitness tips, editing their mouth onto an orange, etc. Their content was their expertise. Now a days, for the majority of creators, their *life* is their content. As of writing this, IRL[^7] streaming is the dominant category on all major platforms.

Reality TV pioneered this; ordinary people living their life in a non-narrative manner. But even a reality TV star got a break when the cameras turned off. A lifestyle content creator is always working.

I need to be able to clock out from work. Otherwise, I'll burn out. My content will be my niche: electronic projects and topics interesting to makers.

Once again, Robert Rich prophesied the content treadmill in 2008.

> In reality the life of a “microcelebrity” resembles more the fate of
> Sisyphus, whose boulder rolls back down the mountain every time he
> reaches the summit. After every tour I feel exhausted but empowered by
> the thought that a few people really care a lot about this music. Yet, a
>  few months later all is quiet again and CD/downoad[sic] sales slow down
> again. If I take the time to concentrate for a year on what I hope to be
>  a breakthrough album, that time of silence widens out into a gaping
> hole and interest seems to fade. When I finally do release something
> that I feel to be a bold new direction, I manage only to sell it to the
> same 1,000 True Fans. The boulder sits back at the bottom of the
> mountain and it’s time to start rolling it up again.

If you are making content for a community you built, you are Sisyphus. Creating the content is pushing the boulder to the summit. But unlike a CD[^8], content is ephemeral. It's seen for a day and then becomes obscure instantly. Your boulder tumbles down to the valley and you must start again.

But you are not alone if you join an existing community. Multiple people have pushed a boulder up the mountain before you. People will help you push your boulder. You may help someone else push their boulder. Someone might even take your boulder and push it to places you never imagined.

An existing community does not need you. This is good. You can go on hiatus or take your time making content without the community imploding. If you're building the community yourself, it can collapse with a single misstep.

### Monetization

An existing community and a fledgling following have very different expectations when it comes to ads. The latter expect creators to sell their audience's attention to advertisers. Communities expect you to be an entrepreneur. They expect you to solve their problem or serve them better than others have. This doesn't completely remove normal monetization strategies; just mandates more discretion.

I'm not above accepting sponsorship. Before creating content, PCB[^4] manufacturers would offer me free services in exchange for their company's logo on my project pages.  Makers are OK with this because they need PCB services as well. I'm not above running (relevant) mid-roll ads in content either.

This monetization scheme has consequences though. The more content you publish the more surface area you can run ads on. Money comes from more content not better content. Regardless of how fast I'd burn out from spewing as many projects as possible, I'd rather post a few builds I'm proud off, than several that generate more passive ad income. The maker community would too.

I considered the podcast model: providing a free RSS[^5] feed and putting (tasteful) ads in it. I also considered publishing first to a newsletter with space reserved for sponsored content. These strategies incentivize increasing ad surface area instead of improving content quality, though.

Instead, I'll plaster donation links to PayPal, Buy Me A Coffee, Ko-fi, and Liberapay accounts everywhere I have a digital footprint. I'll also have cheap subscriptions tiers on Patreon. All content there will be free though. More on that later. I considered making an OnlyFans, but I'm cautious of associating with the content typical for that site.

### Ownership

The people at the {{< tracked-anchor href="https://indieweb.org/why" text="Indie Web Movement" >}} better summarize my opinion about owning your work. That said, the best place to advertise my projects is social media. Posting, though, will likely give the platform a commercial license to do whatever they want with my content. Worse, no one has solved content moderation at scale. So my accounts could be banned with no warning or explanation.

For that reason, I will be platform agnostic. I'll prioritize posting my content in the {{< tracked-anchor href="https://jointhefediverse.net/learn" text="fediverse" >}}, but will also cross-post on closed-platforms.

## Content Channels

Once again, other people have better defined my strategy: {{< tracked-anchor href="https://indieweb.org/POSSE" text="POSSE" >}} or *P*ublish *O*n your own *S*ite, *S*yndicate *E*lsewhere. Sometimes that's not possible or hard to do, especially on photo/video platforms. Instead I'll {{< tracked-anchor href="https://indieweb.org/PESOS" text="PESOS" >}}, or *P*ublish *E*lsewhere, and *S*yndicate on my *O*wn *S*ite.

This has many benefits. One of them is actually reaching people interested in your content. Ironically, having millions of followers doesn't mean they'll see anything you post. Robert Rich once again prophetically predicted this back in 2008.

> The internet can also give us tools more narrowly to target specific
> demographics and to strengthen those assumptions that prevent acceptance
>  of new ideas, nudging people towards algorithmically determined tastes
> or styles. Companies can use demographic models and track people’s
> search patterns to pander to their initial tastes and to strengthen
> those tastes, rather than broaden their horizons. This problem doesn’t
> lie within the technology of the internet, but within the realities of
> capitalism and human psychology.

Publishing content on a platform you don't control is a recipe for disaster. Owning distribution is a requirement. Otherwise, an algorithm change can make it impossible for you to reach your audience.

The rest of this section will detail where I'll post and what content will go on each platform. I'll start where the project documentation will go and progressively move to where the "ads", as described earlier, will be posted.

It's important to note that different social media platforms have different personalities. The same content on TikTok gets very different comments on Instagram. Also, new platforms are constantly popping up and dying. I've organized my content by category, not platform. While I intend to cross-post, some platforms I understand more than others. This is all new to me, so I'll continuously learn as the journey goes.

### Repositories

Codeberg will host the projects themselves and GitHub will be the mirror. Codeberg is a newer, open-source focused, git repository. Not only do I want to try it myself, I suspect makers will like a creator who uses it. GitHub, however, is the most popular git platform by far. Mirroring projects there is a form of project advertising.

Though those sites are for code, I'll host 3D models there too. GrabCAD and Thingiverse are the normal spots for these, so I'll cross-post any of mine there and ensure they point to my repositories.

There are also closed-ecosystems like Bambu Lab's MakerWorld and Dassault Systemes' 3D Content Central, but they likely won't fit my content strategy.

### Detailed Developer Logs

Source files belong in git, but higher level documentation (design intent, design decisions, experiment results, etc.) should be in a developer blog. GitHub and Codeberg provide services for that as well. I'll start off there, but might move to a federated platform like WriteFreely.

The main destinations for developer blogs are Medium, Substack, Instructables, Hackaday, and Hackster. Medium by far is the biggest mainstream blogging platform for every topic under the sun. Substack is equally huge, but focuses on subscriber-only content. I'll make all my content their public. Instructables focuses on DIY projects, not just those in the maker community. Hackaday has a more grass roots, hacker slant. Hackster, however, has more corporate sponsorship. From a usability point of view, Medium, Instructables, and Hackster focus on the "reproducing" aspect of makers instead of the remixing. It's not easy to continuously post project updates on those platforms. It is on Hackaday, on the other hand.

I have no idea how Substack works, so I'll figure it out as I go. I might use Patreon updates as a syndication point for developer logs too. We'll see.

Adafruit Playground is an honorable mention. I'll experiment posting there as well.

The Codeberg/GitHub pages will be the source-of-truth for detailed project updates, then I'll cross-post to the sites mentioned above.

I would be remiss not to mention DEV.to. This blogging platform is specifically for programming. The only relevant content I could post would be for firmware and embedded software. I'll probably won't have anything of merit to share there.

### Quick Project Updates/Networking

Before Elon's take over, Twitter was *the* centralized place for the maker community to talk to each other. Makers shared photos and clips of their projects, asked other makers questions, and generally nerded out on whatever topics they felt like. I plan on doing the same on Twitter/X, Bluesky, Mastodon, and Threads.

Substack has a micro-blogging feature that seems to be available to non-subscribers. I'll try it out. I'm not sure if the platform suits itself to nerd talk though.

This is where I'd list live-streaming platforms if I planned on using them. Twitch, Kick, and YouTube are the main ones. There are categories for makers, but entertaining a chat while working would dramatically slow me down. Pass.

### Video Hub

While I'll be platform agnostic, all video content will go on a PeerTube instance first, then circulated on the other appropriate platforms. I can't be banned on a self-hosted service, but I don't expect to go viral on PeerTube. I'll use it as an archive and nothing more.

### Polished Demos/Project Updates

This is the first category of "ads" mentioned earlier. They'll showcase the project's capabilities in a compelling way to people interested in the build's cosmetic or technical aspects. Platforms appropriate for this content are Instagram, Facebook, TikTok, YouTube, Reddit, Lemmy, and Hacker News.

I might also cross-post to Substack and Patreon. We'll see. Odysee is another alternative, but I have environmental concerns for its block-chain based infrastructure.

### Project Trailers

The most "used-car salesmen"-y content I'll make. Quick, hooky, and by no means technical. These will likely be scripted unlike a demo or project update. Maybe focused on the narrative behind the projects inspiration. Either way, the goal for these is to attract as many people as possible the same way video trailers do for novels. Project trailers will go on Instagram, Facebook, TikTok, and YouTube.

Again, I'll experiment with posting this content on Substack and Patreon. Who knows if anyone will bite on those platforms.

## Conclusion/TL;DR

I suspect my content philosophy will change over time. Maybe I'll write a follow up to this. For now, I'll use this document to keep future me grounded.

If this was too long for you to read: my content will focus on hobbyist electronic projects. What will differentiate me from other makers is ensuring my projects are well documented. My goal is to join the maker community and like-minded off shoots. A large following is an anti-goal. I'll be platform agnostic; focusing on publishing on a domain controlled by me and then syndicating that content to other appropriate channels.

{{< eld-byline >}}

{{< donations >}}

[Why are there footnotes?]({{< ref-jargon-url >}})

[^1]: printed circuit board assembly

[^2]: original poster

[^3]: direct message

[^4]: printed circuit board

[^5]: really simply syndication; this is what you're actually interfacing with when you subscribe to a podcast

[^6]: artificial intelligence

[^7]: in real life

[^8]: compact disc,
