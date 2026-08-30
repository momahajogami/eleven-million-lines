# The Web Before the Phone

*A narrative for Unit 10*

---

## Before the Web, There Was Everything Else

The internet existed before the web. This is worth saying clearly, because the web won so completely that it is difficult now to remember what came before it — or that anything came before it at all.

In the 1980s, if you had a computer with a modem, you could connect to a **bulletin board system** — a BBS. You dialed a phone number. Your modem made the sound. You connected to someone else's computer, usually running in a basement or a spare bedroom, and you entered a world.

BBSs were not the internet, technically speaking. They were point-to-point telephone connections to a single machine. But they had message boards, file archives, games, chat rooms, and — crucially — a culture. People built identities there. They argued, flirted, competed, shared pirated software and original poetry in equal measure. A BBS called The WELL (Whole Earth 'Lectronic Link), founded in 1985, hosted some of the most consequential online conversations of the decade: Grateful Dead fans, hackers, journalists, writers, scientists. Stewart Brand and Larry Brilliant ran it. It cost $8 a month plus $2 an hour. It felt like a private club and a public square simultaneously.

The BBS era is the ur-text of online community. Everything that followed — Usenet, AOL, MySpace, Reddit, Twitter — is a variation on what BBSs worked out first: that people, given a shared text channel, will form a society. They will develop norms, hierarchies, rituals, in-jokes, feuds. They will care about it. They will miss it when it's gone.

**Usenet** (1980) was different: a distributed message system that ran on university and research computers connected by ARPANET and, later, the internet proper. No single machine hosted it. Messages propagated across a network of servers. The hierarchy was organized by topic: `rec.arts.movies`, `comp.lang.c`, `alt.sex`, `sci.math`. The `alt.*` hierarchy was ungoverned, created by people who wanted to talk about things the official hierarchy wouldn't allow.

Usenet was where internet culture was first made. The flame war was invented there. The FAQ was invented there — people got tired of answering the same questions from newcomers every month, so they wrote the Frequently Asked Questions document and posted it at the start of each month. The word "spam" for unwanted messages comes from a 1994 Usenet incident: two immigration lawyers sent the same advertisement to every newsgroup simultaneously. The community was outraged. The lawyers made money. The lesson was noted.

**Gopher** (1991) almost won. Developed at the University of Minnesota, Gopher was a hierarchical document system: menus of links, text files at the leaves. It was clean, fast, and easy to navigate. Before the web, Gopher was the primary way to browse information on the internet. Libraries used it. Universities used it. In 1993, Gopher traffic exceeded web traffic.

Then Minnesota announced they would charge licensing fees for the server software. Web server software was free. Within a year, Gopher was in decline. This is one of the earliest examples of a pattern the web repeated many times: the technically superior option losing to the free one. Free beats better, almost every time, when the alternatives are close enough.

---

## Lynx and the Democracy of Text

**Lynx** (1992) is a text-mode web browser. It runs in a terminal. It has no images, no fonts, no color beyond what your terminal supports. You navigate with arrow keys. Links are highlighted. You press enter to follow one.

Lynx is still actively maintained. You can install it right now and use it. The web it shows you is a different web — stripped of everything that is not information. Forms work. Text works. The structure of pages, when you remove the visual noise, is often surprising: how much of a page is navigation, advertisement, decoration. Lynx shows you the bones.

The people who built Lynx — Lou Montulli, Michael Grobe, Charles Rezac at the University of Kansas — were not trying to build a minimal browser. They were building the only browser they could build, given the hardware they had. The terminals in university computing labs could not render graphics. If the web was going to be useful to those students, it had to work in text.

This is a recurring pattern in computing: the constraint produces a clarity that the unconstrained version loses. Lynx is a better reading tool than Chrome, for reading. It is a worse browsing tool than Chrome, for browsing. The question is what you are trying to do.

Lynx also matters for **accessibility**. Screen readers — the software that reads web pages aloud to blind and low-vision users — work like Lynx: they see the document structure, not the visual presentation. A page that works in Lynx generally works with a screen reader. A page that breaks in Lynx often breaks for blind users. Web developers who never test in Lynx often build pages that exclude people.

The web was, in its original design, supposed to be accessible by any device with any rendering capability. Berners-Lee's proposal says so explicitly. The browser wars made it otherwise.

---

## Mosaic and the Visual Revolution

In January 1993, a student at the National Center for Supercomputing Applications at the University of Illinois submitted the first version of a browser to the NCSA FTP server. His name was Marc Andreessen. He was twenty-one years old. The browser was called Mosaic.

Mosaic rendered images inline. Before Mosaic, images on the web opened in a separate window — you clicked a link, a viewer launched, the image appeared somewhere else. Mosaic put the image inside the document, the way a magazine does. Tim Berners-Lee, who had invented the web two years earlier and cared deeply about its design, objected to the `<IMG>` tag. He felt that inline images would pollute the clean document model he had designed. He proposed alternatives. He was ignored.

The `<IMG>` tag shipped. The web became visual. Within eighteen months, Mosaic had over a million users.

The other thing Mosaic did was make the web feel fast. Earlier browsers were slow, clunky, hard to configure. Mosaic installed easily and worked. The hyperlink — which existed before Mosaic — suddenly felt like a feature rather than a concept. You could follow a chain of links across the world in a few minutes. The documents were on servers in Illinois and Geneva and Tokyo, and Mosaic made the distance feel like nothing.

This is what the web actually is, at its base: a linked document system. HTTP is the protocol for requesting documents. HTML is the language for marking them up. URLs are the addresses. Mosaic did not invent any of these. It made them feel obvious.

Andreessen graduated in December 1993. By April 1994, he was in California, co-founding Mosaic Communications Corporation with Jim Clark, a Silicon Valley veteran who had founded Silicon Graphics. The company later renamed itself Netscape Communications. The browser they built — Netscape Navigator — was Mosaic rewritten from scratch, faster and more capable.

Netscape's IPO in August 1995 is one of the founding myths of the dot-com era. The company had never turned a profit. The stock was priced at $14, raised to $28 on the morning of the offering, and opened trading at $71. It closed at $58. Jim Clark made $663 million. Andreessen, on the cover of *Time* magazine, barefoot on a throne, was twenty-four.

The message the IPO sent was simple and wrong and world-changing: **the internet is worth more than we can currently calculate**. That belief, held by enough people with enough money, produced a decade of investment that built the infrastructure the modern internet runs on — and then crashed.

---

## The Browser Wars

In 1995, Microsoft released Internet Explorer 1.0. It was licensed from Spyglass, which had licensed Mosaic from NCSA. It was not very good. Microsoft did not particularly care whether it was good. Microsoft cared whether Netscape would survive.

Bill Gates had written an internal memo in May 1995 called "The Internet Tidal Wave." The memo is a remarkable document: a man who had missed the internet entirely, suddenly seeing it. Gates understood — correctly — that a browser powerful enough to run applications could become an alternative operating system. If Netscape Navigator became the platform, Windows became just the thing that ran Netscape. Microsoft's monopoly would be under threat.

The solution was brutal and effective: **bundle Internet Explorer with Windows and make Netscape unable to compete with free**. IE 3.0 (1996) was competitive. IE 4.0 (1997) was better than Navigator. And it cost nothing, because it was part of Windows, and Windows was on every PC shipped.

Netscape fought by innovating. JavaScript — invented by Brendan Eich in ten days in 1995, under orders to make it look like Java for marketing reasons — made pages dynamic. Frames, forms, cookies: Netscape added features and IE copied them. The features were sometimes incompatible. Web developers wrote `best viewed in Netscape Navigator` or `best viewed in Internet Explorer 4.0` on their pages. The web fractured into two dialects.

The Department of Justice sued Microsoft for antitrust violations in 1998. The government argued that bundling IE with Windows, and pressuring PC manufacturers not to ship Netscape, was illegal monopolization. The trial produced some of the most colorful testimony in the history of technology: Gates's deposition, in which he professed not to understand the word "concerned" in his own emails, was played as video in the courtroom. The judge found for the government and ordered Microsoft broken up. An appeals court reversed the breakup order. Microsoft settled, with conditions that satisfied no one.

Netscape had already lost. The browser wars ended not with a battle but with an attrition. Navigator's market share fell from 86% in 1996 to 28% in 1998. In November 1998, AOL acquired Netscape for $4.2 billion in stock. Internet Explorer had 97% market share by 2002. The web had one browser, owned by the company that owned the operating system.

This was a catastrophe, recognized as such by the people inside it. A monoculture of browsers means the browser owner determines what the web can do. Standards bodies — the W3C, which Berners-Lee ran — could propose specifications, but implementation was Microsoft's decision. Features that Microsoft liked shipped. Features that threatened Windows did not.

---

## The Phoenix

In January 1998, the week of the AOL acquisition, Netscape open-sourced its browser. The source code was posted on a website called mozilla.org. The project was named Mozilla — a portmanteau of Mosaic and Godzilla, which had been Netscape's internal mascot for the Navigator codebase.

The release was hailed as a turning point. An army of volunteers would improve the code, out-competing Microsoft through collective intelligence. This did not happen. The Netscape codebase was a disaster: four million lines of C++, full of platform-specific hacks accumulated over four years of browser-war urgency. The code was undocumented, inconsistent, and barely portable. Volunteers looked at it and left.

Jamie Zawinski — jwz — had been one of Netscape's original engineers. He had written the `about:` page, the email client, much of the Unix code. He had fought for the open-source release and believed in it. He watched the Mozilla project struggle and published one of the most clear-eyed postmortems in software history:

> "I used to be an optimist about open source. Now I think it's mostly a religion."

He left Netscape in 1999. He opened a nightclub in San Francisco called DNA Lounge and ran it on open source software and wrote about it publicly. His blog is still there. He is still angry. He is usually right.

The Mozilla project's decision, in 2000, to abandon the Netscape codebase and rewrite from scratch, was controversial and ultimately correct. The new engine, called **Gecko**, was cleaner, faster, and standards-compliant in ways Netscape's code never was. But the rewrite took years. The Netscape 6.0 release in 2000, based on the still-unstable new engine, was widely considered worse than Netscape 4.7. The perception of failure deepened.

Meanwhile, inside the Mozilla project, a small team began building a stripped-down browser. The full Mozilla suite — browser, email client, HTML editor, chat client — was bloated and slow. The stripped-down version had only the browser. It was fast. It was small.

It was named Phoenix. Then Firebird. Then Firefox, after trademark disputes with other projects. The naming chaos is a window into how open source projects actually work: committees, competing priorities, technical decisions made by consensus and political decisions made by whoever shouted loudest.

**Firefox 1.0 shipped on November 9, 2004.**

The release was funded, in part, by a full-page advertisement in the New York Times — bought with donations from users. Ten thousand people donated money to buy an ad for software they got for free. The ad listed the names of all ten thousand donors in small print. It was one of the most effective technology marketing events of the decade, and it cost almost nothing compared to what Microsoft spent on IE.

Firefox 1.0 was excellent. It was fast, standards-compliant, and had features IE lacked: tabs, a built-in pop-up blocker, better security. It gained 100 million downloads in its first year. By 2009, Firefox had 32% of the browser market. IE had fallen below 60% for the first time in a decade.

The Mozilla Foundation — a non-profit spun out from the AOL-owned Mozilla project in 2003 — makes most of its money from a deal with Google: Google pays Mozilla to be the default search engine in Firefox. This arrangement has funded Firefox development since 2005. It is an interesting structural fact: the main alternative to Chrome, the browser made by Google, is funded by Google. The incentives here are not simple.

---

## Google, Yahoo, and the Shape of Knowing

In 1994, two Stanford graduate students named David Filo and Jerry Yang built a website called "Jerry and David's Guide to the World Wide Web." It was a directory — a list of websites, organized by category, maintained by humans who decided what belonged where. It was renamed Yahoo!.

The Yahoo directory worked because the web was small. By 1994, there were perhaps 10,000 websites. Humans could catalog them. The directory model assumed that the web was a library, and libraries have librarians. You could browse: click through categories until you found what you wanted. Computers, Software, Operating Systems, Unix, Berkeley. The path had a logic.

The directory was also a statement about knowledge: that it has a shape, that the shape can be known, that experts can map it. Yahoo's editors decided what was worth listing. Their choices were the web's canon.

By 1998, there were tens of millions of websites. The directory model was breaking. No team of humans could catalog a web that was growing faster than they could read. Yahoo used other search engines — AltaVista, Inktomi — to fill the gaps. The search results were poor. People knew they were poor and used them anyway, because there was nothing better.

In a Stanford computer science department office, two graduate students named Sergey Brin and Larry Page were building something better. Their insight was mathematical. **The web is a graph.** Pages are vertices; links are edges. A link from page A to page B is a vote: A is saying B is worth reading. But not all votes are equal. A vote from a page that many others vote for is worth more than a vote from a page nobody links to.

This observation — that the importance of a page is a function of the importance of the pages that link to it — is circular. It is also an eigenvector problem. If you build the adjacency matrix of the web and find its dominant eigenvector, each component of that vector is the "rank" of the corresponding page. Brin and Page called their algorithm **PageRank**, naming it partly after the web pages it ranked and partly after Larry Page himself.

The algorithm worked. The original paper — "The Anatomy of a Large-Scale Hypertextual Web Search Engine," 1998 — described a system that could search 25 million pages with better results than anything else available. Google's search was faster and more accurate because it used the structure of the web itself as evidence about what the web contained.

Yahoo's model said: here is what we think is important. Google's model said: here is what the web thinks is important. Google was right that these were different things. It was also right that the second question was more interesting and more answerable.

Google launched in 1998. The name is a misspelling of "googol" — 10 to the power of 100, chosen to suggest the scale of the information they planned to organize. The interface was deliberately minimal: a white page, a text box, two buttons. This was partly aesthetic and partly the result of the founders not knowing much HTML. The simplicity looked like a design choice. It worked as one.

Yahoo understood, eventually, that Google was a threat. In 2002, Yahoo offered to buy Google for $3 billion. Google declined. In 2003, Yahoo acquired Overture (formerly GoTo.com), which had invented the model of selling search result placement to advertisers. Google had developed its own auction-based advertising system (AdWords, AdSense) and was already making serious money from it. The two companies were on different trajectories.

In 2008, Microsoft offered to buy Yahoo for $44.6 billion. Yahoo declined. Microsoft walked away. By 2017, Verizon acquired Yahoo's core internet business for $4.5 billion — a tenth of what Microsoft had offered. The decline of Yahoo is one of the cleanest stories in technology: a human-curated system that refused to believe the algorithm had won, until long after it had.

---

## The Moment Before Phones

There is a period, roughly 2002 to 2007, that deserves its own name. Call it the **browser zenith**: the moment when the web browser had won the platform war and the smartphone had not yet arrived, and everything — everything — was moving into the browser.

**Email.** Hotmail (1996) was the first major web-based email service. You accessed your email through a browser instead of a desktop client. This seemed strange and then normal and then obvious. Microsoft bought Hotmail in 1997 for $400 million. In 2004, Google launched Gmail, with one gigabyte of storage at a time when Hotmail offered 2 megabytes. The storage number was so extreme that people assumed it was an April Fools' joke. (Gmail launched on April 1. It was not a joke.) Gmail was fast, searchable, and keyboard-navigable in ways web apps weren't supposed to be. It rewrote expectations.

**Maps.** Before Google Maps (2005), getting directions meant printing them from MapQuest before you left. MapQuest was fine. It worked. You unfolded the printout at stoplights. Google Maps introduced something different: a map you could drag. Before Maps, web interfaces were stationary — you clicked, the page reloaded, the new page appeared. Google Maps moved smoothly, fetching new tiles as you dragged, without reloading. The technology behind this was called **AJAX** — Asynchronous JavaScript and XML — and Maps was the demonstration that convinced the rest of the web it was possible.

**Documents.** Google acquired Writely in 2006 and renamed it Google Docs. For the first time, a word processor ran in the browser. Microsoft Office was not dead — was nowhere near dead — but the premise had changed. The document lived in the cloud. You could share a link instead of an attachment. Multiple people could edit simultaneously. This was technically extraordinary and felt, in use, completely ordinary.

**Video.** YouTube launched in February 2005. By the end of 2006, when Google acquired it for $1.65 billion, 65,000 videos were being uploaded per day. The bandwidth cost of running YouTube was staggering. It was not obvious how YouTube would make money. Google bought it anyway. The browser, with the Flash plugin (Adobe's multimedia platform), could now play video. The television had a competitor.

The technical achievement behind all of this was **JavaScript's rehabilitation**. JavaScript had been a joke language for years: slow, inconsistent across browsers, good only for form validation and annoying pop-up windows. Then V8 — Google's JavaScript engine, released with Chrome in 2008 — made JavaScript fast. Not "acceptable" fast. Actually fast. The JIT compiler inside V8 compiled JavaScript to native machine code at runtime, making it approach the speed of C for many operations. Suddenly the browser could run real software.

This is the moment the browser became an operating system. Not metaphorically. Actually. Gmail, Docs, Maps, YouTube — these were applications. They loaded in a browser instead of installing on disk. The operating system underneath them (Windows, Mac OS X, later Linux) became irrelevant to the user experience. You could switch computers and your stuff was still there. You didn't install anything. You just logged in.

The people who understood what was happening in 2005 were building for a future where the operating system was the browser and the browser was the internet. They were right. They were also, within three years, overtaken by something they had not predicted.

---

## Net Neutrality

In 2003, a Columbia Law School professor named Tim Wu published a paper called "Network Neutrality, Broadband Discrimination." The paper was short, readable, and introduced a term that would define a decade of policy argument.

**Net neutrality** is the principle that internet service providers must treat all internet traffic equally — that Comcast cannot charge more for Netflix traffic than for YouTube traffic, cannot slow down competitors' services, cannot create "fast lanes" for customers willing to pay. The internet, under the net neutrality principle, is a dumb pipe. It carries bits without inspecting or preferring any of them.

The history of communications technology is a history of this tension. The telephone company could not (in the US, by law) decide whose calls to transmit and whose to delay based on content. The railroad could not (after a long political fight) charge different rates to ship Standard Oil's barrels versus a competitor's. The principle is: the infrastructure of commerce must not be used to dominate commerce.

The internet was built with net neutrality as a technical fact, not a legal requirement. The original network was designed so that routers simply forwarded packets — they did not read them, they did not prioritize them. The intelligence was at the edges, not the center. This architectural choice was not political; it was a simplicity decision by engineers building a research network. But it had political consequences: it meant that a startup with a better idea could put its server on the internet and reach every user the same way that an established company could. The barrier to entry was low because the network was neutral.

By 2005, broadband internet service providers — cable and telephone companies — had spent billions building fiber and cable networks and wanted a return. One approach was simple: charge users more for more bandwidth. Another approach was more aggressive: charge the services that users accessed. If Netflix used a lot of bandwidth and AT&T customers watched a lot of Netflix, why shouldn't Netflix pay AT&T for the privilege of reaching AT&T customers?

The answer — the net neutrality answer — is that this recreates the railroad problem. The ISP becomes a toll collector and a gatekeeper. The ISP can favor its own streaming service over Netflix. It can slow down a competitor's VoIP service to protect its phone revenue. It can negotiate with some services for "fast lane" access and slow everything else to unusable speeds. The structural incentive is to make the open internet worse so that the ISP's preferred services look better.

The political fight over net neutrality ran from roughly 2005 to 2017 (and has not ended). The FCC under the Obama administration classified broadband internet as a "telecommunications service" under Title II of the Communications Act in 2015, giving it the authority to enforce neutrality rules. The FCC under the Trump administration reversed this classification in 2017, removing those protections. Court cases continue. States have passed their own neutrality laws. The federal status remains contested.

The technical debate ended years before the political one began. The internet's founding architecture was neutral. The question was whether the pipes that delivered it would remain so after they became commercial infrastructure owned by a handful of very large companies.

---

## The iPhone Arrives

On January 9, 2007, Steve Jobs stood on a stage in San Francisco and introduced a device he described as "an iPod, a phone, and an internet communicator." He paused between each item. The audience understood before he finished.

The iPhone was not the first smartphone. There had been PDAs, Blackberries, Windows Mobile devices. What the iPhone had was a real browser — Safari, running WebKit, rendering the actual web. Not a mobile-adapted version. Not WAP. The web.

Steve Jobs, introducing the iPhone, said: "Boy, are we patenting it."

The moment the iPhone shipped — June 29, 2007 — the browser zenith ended. The browser had won the platform war. Now the platform the browser ran on was a pocket computer with a touch screen, connected to a cellular network, always present.

The web adapted, as it always adapts. Responsive design, mobile-first development, app stores alongside browsers: the next decade of web history is the negotiation between the open browser-based web and the closed app ecosystem that Apple and Google built on top of it. That negotiation continues.

But the moment before the phone — those five years or so when the browser was everything and the web was winning — was real. The people who built Gmail and Google Maps and YouTube were building, without quite saying so, the operating system for human life. They were right. The phone made it portable.

Everything that came after the phone — social media, the attention economy, the algorithmic feed, the surveillance advertising business model — grew in the space those five years cleared. The browser made the web easy. Google made the web findable. The phone made it inescapable.

---

## What It Adds Up To

The story of the browser is the story of literacy acquiring a new medium.

Gutenberg's press made books cheap. The book stayed in the library, the study, the church. The browser made publishing cheap. The web was everywhere that had a wire, and then everywhere that had a signal. Publishing, which had required a press and a distribution network and an editor and a printer, now required a text box and an internet connection.

This is not a small thing. It is, arguably, the largest expansion of the reading and writing public since the invention of movable type. The question that follows — what do people write when they can write anything, and who decides what gets read? — is the question the social network answered, badly and profitably, in the decade after.

The browser is a reading technology. The social network is an attention technology. They share a substrate (the web, HTTP, HTML) but have different purposes and different consequences. Understanding both — as engineering choices, made by specific people for specific reasons — is what this unit is for.

The code is the argument. Reading the code is reading the argument.

---
