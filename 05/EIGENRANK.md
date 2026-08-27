# Eigenrank

*How the internet learned to point.*

---

## Before the search

There was a time — not long ago, geologically speaking, not long ago even in a human lifetime — when finding something on the internet required a guide.

The guide was Yahoo.

Yahoo's first form, in 1994, was a list maintained by two graduate students at Stanford — Jerry Yang and David Filo — who called it "Jerry and David's Guide to the World Wide Web." They curated it by hand. A website worth visiting, they would add it to the list. The list had categories: Arts, Business, Computers, Education, Entertainment. You clicked a category, then a subcategory, then a subcategory of that, until you arrived at the thing — if the thing existed, and if they had found it.

This was the internet as library, organized by two people.

The world was connecting faster than two people could organize it. By 1995, tens of millions of pages existed. By 1997, hundreds of millions. The web was growing exponentially; the guide was growing linearly. The gap between them was becoming impassable.

There were other approaches. AltaVista indexed pages by crawling them and searching the text. Excite did the same. Type a word, get a list of pages containing that word. The problem: any page could contain any word, and the web was full of pages that crammed popular words into invisible text — white text on a white background — to appear in searches where they had no business appearing. Search was becoming noise.

And before AltaVista — before the indexed search engines — there were the routes. You followed links. Someone's home page linked to something they found interesting; that page linked to something else. The web was a set of paths, and you walked them, and occasionally you found something worth finding.

---

## The rooms everyone kept

In the middle of this, people were building rooms.

Geocities launched in 1995 and organized personal home pages by neighborhood: SiliconValley for tech, Hollywood for entertainment, Athens for education. By 1999 it was the third most visited site on the web. Not for any central content — for the rooms.

Millions of rooms. Every person with a computer that was always on — and there were more of them every month, university students, programmers, journalists, teenagers, retirees — could host whatever they imagined the internet should be. The rooms had MIDI music that started playing when you arrived. They had animated GIFs of spinning globes. They had hit counters: a number displayed at the bottom of the page, with pixelated dignity, showing how many times someone had been here.

They had links. Lists of links — "My Links" or "Cool Sites" — curated by hand by whoever made the room. Web rings connected pages on related topics: a banner at the bottom of each page linked to the previous site in the ring and the next one. If you followed a web ring long enough, you returned to where you started. The internet was a circle of people pointing at each other.

If you were in someone's Cool Sites, you had been seen by a human being and found worth pointing to. This mattered. The internet's social layer was its link layer. Discovery was human.

Think about what this felt like. It was the first time in history that an ordinary person — not a publisher, not a broadcaster, not a newspaper — could put something in front of the whole world and leave it there for anyone to find. The rooms were eccentric, personal, strange. They were the internet's first literature: not professional, not edited, not authorized. Just people saying: *this is what I want the world to be.*

The problem was that it was becoming not-small, very fast, and the search engines couldn't keep up, and the guide had two people, and the routes were becoming impossible to navigate because no one had a map.

In 1996, at Stanford, two graduate students — Larry Page and Sergey Brin — began thinking about this problem. Not as a search problem. As a *graph problem*.

---

## The insight

A link is a vote.

Not all votes are equal.

If a page that many people have linked to — a page that the network trusts — links to you, that endorsement is worth more than a link from a page that no one has linked to. Trust propagates through the network. A trusted page's trust flows to the pages it links to.

This is circular. The trust of a page depends on the trust of the pages that link to it, which depends on the trust of the pages that link to *them*, which depends on the trust of the pages that link to *those*. You cannot compute it in a single pass.

You need to solve it as a system.

---

## The mathematics

Model the web as a directed graph: each page is a node, each link is an edge pointing from the linking page to the linked page. Build a matrix **A** where **A[i,j]** is 1/(number of links from page j) if page j links to page i, and 0 otherwise. Each column sums to 1: the column is a probability distribution over the pages that j points to.

Now ask: if a person were randomly clicking links — starting anywhere, following links, occasionally jumping to a random page — what fraction of their time would they spend on each page? This is the *random surfer* model. The steady-state distribution of the random surfer is the ranking vector.

Mathematically, we want the vector **r** such that:

**r** = α **A** **r** + (1 − α) **e**/n

Where:
- **r** is the ranking vector
- α is the damping factor — typically 0.85 — representing the probability that the surfer follows a link rather than jumping randomly
- **e**/n is the uniform distribution (1/n for each of n pages), the random jump
- **A** is the column-stochastic link matrix

This equation says: the rank of a page is a weighted sum of the ranks of the pages that link to it, plus a small constant for random exploration.

This is an **eigenvalue equation**. The vector **r** is an eigenvector of the modified link matrix with eigenvalue 1. The Perron-Frobenius theorem — from linear algebra, about matrices with non-negative entries — guarantees that this eigenvector exists, is unique, and has all-positive entries. It can be computed by *power iteration*: start with any distribution, multiply by the matrix repeatedly, and the result converges to the dominant eigenvector.

Page and Brin called it PageRank — after Larry Page's name, after the concept of ranking pages. We call it **Eigenrank** because that is what it is: a ranking derived from an eigenvector of the network's link structure.

The name also avoids a false implication. Google's current search has layered machine learning over the original algorithm until the eigenvector is one signal among hundreds. Typing a query into a search box today does not perform a straightforward eigenvector computation on the shape of the web. Calling it Eigenrank names the thing that was discovered, not the company that is now doing something much more complicated.

---

## Solving it

Power iteration works like this:

1. Start with every page assigned equal rank: **r** = **1**/n
2. Compute **r'** = α **A** **r** + (1 − α) **e**/n
3. Set **r** = **r'** and repeat until the change is negligibly small

The number of iterations required depends on the spectral gap — the ratio between the dominant eigenvalue and the next-largest. For real web graphs, convergence happens in 50–100 iterations. For a web with billions of pages, this is a serious engineering problem: the matrix is enormous, but sparse, since most pages link to a tiny fraction of the web. The computation requires clever distributed engineering.

Brin and Page built the first Eigenrank computation on commodity hardware in Stanford's computer science building, connected with ethernet cables, assembled from parts. The computation that indexed the web and changed how information flows ran, at its beginning, on the same kind of machines that university students had. Like BitTorrent, like Linux, it began on someone's floor.

---

## What it changed

AltaVista's keyword search returned results gamed by whoever made pages. Eigenrank returned results that reflected the collective judgment of the web itself — the accumulated linking decisions of millions of people who had each, by linking to something, said: *this is worth pointing to.*

It was not perfect. The web's linking structure reflected its existing biases. English-language pages linked to other English-language pages. Popular pages accumulated links faster than obscure pages regardless of quality. The rich got richer.

But compared to what existed before — the hand-curated directory, the keyword-gamed index, the random walk through someone's Cool Sites — it was extraordinary. For a decade, you could type something into a search box and get something useful.

The early internet was a garden. Eigenrank was the first useful map of the garden.

The map changed the garden. When you know what is findable, you build differently. Pages were made to be found by Eigenrank, not by humans following routes. The link became a signal to be optimized. The algorithm shaped the network it was measuring.

This is the lesson that runs through all of Unit 05: the tool is not separate from the culture. The tool is made by the culture; the culture is then made by the tool. Writing invented by humans; humans reshaped by writing. Code augmented by electricity; electricity reshaping the code.

---

## What to read

- Page, L., Brin, S., Motwani, R., Winograd, T. (1998). *The PageRank Citation Ranking: Bringing Order to the Web.* Stanford Technical Report. Search for it by title — it is publicly available.
- Any introduction to eigenvalues and eigenvectors will give you the linear algebra. The Perron-Frobenius theorem appears in most linear algebra texts under that name.
- The Internet Archive's Wayback Machine holds pages from the Geocities era. Visit a 1997 page. Read the Cool Sites list. Follow a link.

---

*This is the sixth project in Unit 05. It belongs here because it is the moment when the cultural web — the garden of home pages, the routes, the communities — was first mapped at scale. And because the map, once made, changed everything it described.*
