# Unit 10 — Browsers and Social Media

*The browser is the printing press. The social graph is the audience.*

---

## The Central Argument

When Gutenberg's press made text cheap to copy, it did not immediately make writing democratic. The machine arrived before the permission. Two centuries passed before literacy spread widely enough to change the social order.

The web made publishing cheap. The browser made it visible. The social network made it personal. And somewhere in that sequence — not at a single moment, not by any single decision — writing became a medium that nearly everyone could practice, and nearly everyone did, and nearly nobody controlled.

This unit is about the engineering decisions behind that sequence: what the browser is, how it works, who built it, and what it cost to build the social layer on top. The code is here. The consequences are still arriving.

---

## The Browser as Operating System

A browser is a document renderer that learned to run programs. That is not the original intention. The original intention is in the name: you browse. You follow links. You read.

**Mosaic (1993)** — Marc Andreessen and Eric Bina at NCSA. The first browser that rendered images inline. Before Mosaic, browsers were text-only; images opened in separate windows. One design decision — `<img>` displayed in the document — changed the visual grammar of the web permanently. Tim Berners-Lee objected. He was overruled by adoption.

**Netscape Navigator (1994)** — Andreessen leaves NCSA, founds Mosaic Communications (later Netscape). The browser becomes a product. JavaScript arrives in 1995: Brendan Eich, ten days, LiveScript renamed at the last moment for marketing reasons. The browser can now execute code. The document is now an application container.

**Internet Explorer and the Browser Wars** — Microsoft bundles IE with Windows. Netscape cannot compete with free and loses the market. The casualty is standards: each browser implements its own version of everything. Web developers spend the 1990s writing code for two incompatible worlds.

**Mozilla and Firefox (2002–2004)** — Netscape open-sources the codebase before dying. The Mozilla Foundation emerges from the ruins. Firefox 1.0 ships in November 2004: standards-compliant, fast, extensible. The browser wars resume on different terms: quality instead of market power.

**WebKit and Blink** — Apple forks KHTML (from the KDE project) to build Safari. Google forks WebKit to build Blink. Chrome ships in 2008. By 2012, Chrome is the dominant browser. The rendering engine lineage: KHTML → WebKit → Blink. The engine that runs in your browser today is, in some sense, still KDE's work.

**Reading the source:**
- `mozilla-central` — Firefox, one of the largest open source repositories in existence. The JavaScript engine (SpiderMonkey), the layout engine (Gecko), the networking stack — all here.
- `WebKit` — the shared ancestor of Safari and Chrome's rendering engine. Cleaner and smaller than Gecko.
- Mosaic source — the original. Simpler than anything that came after. Read it first.

---

## The Social Graph as Data Structure

The browser delivers documents. The social network delivers people.

A social graph is a mathematical object: vertices are users, edges are relationships (friendship, follow, like). The question of what to do with that graph — how to traverse it, how to rank it, how to monetize it — is the engineering question of the 2000s.

**Friendster (2002)** — the first major social network. Viral growth, catastrophic scaling failure. The database could not handle the queries. Friendster's engineers understood the social graph; the infrastructure could not keep up. The lesson: a social network is a distributed systems problem wearing a sociology costume.

**MySpace (2003)** — grew where Friendster failed. User customization (HTML and CSS in profiles) created a baroque, chaotic aesthetic that was also deeply personal. MySpace succeeded because it let users make things — badly, enthusiastically, visibly. It was acquired by News Corp in 2005 for $580 million. By 2008 it was losing to Facebook.

**Facebook (2004)** — Mark Zuckerberg at Harvard. Originally The Facebook, restricted to .edu email addresses. The constraint was the feature: exclusivity created trust. The News Feed (2006) was controversial — users felt surveilled. The Like button (2009) reduced a complex social gesture to a single bit. Each of these decisions is an engineering choice with a social consequence.

The Facebook stack, early: PHP (famously fast to iterate with), MySQL, Memcached, Thrift (their own RPC framework, later open-sourced). Haystack (2010) — a custom object store for photos, described in a public paper. The papers are worth reading: Facebook's infrastructure problems were real research problems, and they published.

**Twitter (2006)** — Jack Dorsey, Noah Glass, Biz Stone, Ev Williams. The constraint is the point: 140 characters, a number derived from SMS limitations. The asymmetric follow model (unlike Facebook's mutual friendship) creates a broadcast network rather than a personal one. Twitter's early stack: Ruby on Rails, then a painful migration away from it as scale demanded more. The "fail whale" is a cultural artifact of that period.

**The attention economy** — the social network as advertising platform. Every design decision — the infinite scroll, the notification badge, the algorithmic feed — is an engineering choice with a measurable effect on time-on-site. This is not incidental. The business model requires attention. The engineering serves the business model. Understanding this is part of reading the code.

---

## Characters

**Marc Andreessen** — Mosaic, Netscape, Andreessen Horowitz. The person who made the web visual and commercial. Later, the venture capitalist who funded much of what the web became.

**Jamie Zawinski (jwz)** — Netscape engineer, wrote the original `about:` page, helped found Mozilla after Netscape's collapse. His blog (still active) is a running commentary on what the web promised and what it became. His nightclub (DNA Lounge, San Francisco) runs on open source software and he writes about it. A character worth knowing.

**Brendan Eich** — invented JavaScript in ten days. Later CEO of Mozilla, then founder of Brave. The creator of the language that runs more code than any other. The ten-day story is legend; the real story is that the language survived its own origins.

**Tim Berners-Lee** — invented the web (HTTP, HTML, URLs) at CERN in 1989-1991. Did not invent the browser as we know it. Spent the subsequent decades trying to keep the web open, decentralized, and in the public interest. The contrast between his vision and the web that exists is the tension at the center of this unit.

**Mark Zuckerberg** — founded Facebook. The trajectory from dorm room to congressional testimony is the central biography of the social web era.

**Ev Williams** — Blogger (acquired by Google), Twitter, Medium. Three successive attempts to build a public writing platform. Each one simpler and more constrained than the last. The pattern is interesting: each reduction is also a clarification of what public writing is for.

---

## The Arc: Publishing → Social → Platform

The web begins as a document network. You read; you link. The browser makes it visual. JavaScript makes it interactive. The social network makes it personal. The platform makes it commercial.

At each step, something is gained and something is lost.

**What is gained:** reach, speed, access, connection. Writing reaches more people more quickly than it ever has. A teenager in rural Ohio can publish to the same network as the New York Times.

**What is lost:** structure, permanence, editorial judgment, context. The link that organized the web gives way to the algorithmic feed. You no longer navigate — you scroll. The document that had a URL and could be linked to and quoted gives way to a post that disappears into a timeline.

The loss is architectural, not cultural. It is built into the data structures: a timeline is a stream, not a library. A stream has no index. You cannot cite a position in a stream the way you can cite a page in a book.

This is an engineering problem with a philosophical consequence. Read the code and you see the choice being made.

---

## Codebases

```
10/
├── UNIT-10.md          ← this file
├── mosaic/             ← NCSA Mosaic source (or pointer to it)
├── firefox/            ← Mozilla/Firefox orientation
├── webkit/             ← WebKit orientation
└── social/             ← Reading notes on Facebook/Twitter infrastructure papers
```

**Primary sources:**
- NCSA Mosaic source — publicly available, historically important, short enough to read
- Mozilla/Firefox source (`mozilla-central`) — too large to clone locally; read online via Searchfox
- WebKit source — clonable, architecturally instructive
- Facebook infrastructure papers: Haystack (2010), TAO (2013), Unicorn (2013)
- Twitter engineering blog posts from 2007-2012 (the scaling era)

**Paired texts:**
- Tim Berners-Lee, *Weaving the Web* (1999) — the original vision, before the social layer
- jwz's blog — the view from inside Netscape and after
- Ev Williams' notes on Medium — a builder reflecting on what he built
- *The Facebook Effect* (Kirkpatrick, 2010) — reported narrative of the early years
- Zeynep Tufekci, *Twitter and Tear Gas* (2017) — the social network as political infrastructure

---

## The Thread Back to Unit 05

Unit 05 (Culture, Spectacle and Eigenrank) ends with PageRank: Brin and Page organize the web as a graph and rank it by eigenvector. The browser delivers that graph to users. The social network replaces the link graph with the social graph. The recommendation algorithm replaces the eigenvector with something murkier and more powerful.

Unit 10 is what happens after Unit 05's map was drawn and the territory changed.

Stack Overflow (noted briefly in Unit 05 alongside SourceForge) belongs in this arc too: the knowledge commons that the social web built, and that LLMs are now displacing. Unit 11 picks that thread up.

---

## For Preschoolers and Families

The browser is a window. Before the window, you had to know where to go. The window let you look through the wall.

The social network is a room. Before the room, you had to find people one at a time. The room put everyone together.

Windows and rooms are good things. But a room where someone decides who gets to speak, and when, and how loudly — that room has a landlord. Knowing who built the room, and why, and what the rules are: that is what this unit is for.

---
