The browser as operating system. The social graph as data structure. The code you are not allowed to read.

Unit 10 follows the web from its origins as a document network through the browser wars, the rise of social media, the gig economy, and the infrastructure that makes open source actually usable. The philosophical argument running through the unit: coding is writing, the right to read the systems that govern your life is a civic right, and the history of computing is the story of that right being granted and withheld.

The codebases here are a mix of what you can read and what you cannot. The browser source is open. The social media platforms are closed. That asymmetry is not incidental — it is the subject.

## Materials

- **UNIT-10.md** — unit overview: the browser arc, social graph as data structure, characters
- **BROWSERS.md** — the full browser history: BBSs, Mosaic, the browser wars, Firefox, PageRank, net neutrality, the browser zenith
- **SOCIAL-MEDIA-1.md** — the desire to be seen: email, forums, Friendster, MySpace, Tumblr, the experimental era
- **SOCIAL-MEDIA-2.md** — everything in your pocket: the iPhone, Twitter, Instagram, Snapchat, Vine, the generational divide
- **SOCIAL-MEDIA-3.md** — the app economy: Uber, the gig turn, startup culture, LLMs arriving
- **ONTOLOGY.md** — what is a thing? Software as made-up, the layers of dependency and extraction, coding as continuous with writing
- **THE-RIGHT-TO-READ.md** — the law analogy: secret code is to computing what secret law is to governance
- **PACKAGE-MANAGERS.md** — dependency hell, apt, npm, left-pad, the lock file, xz-utils
- **VERSION-CONTROL-ECOSYSTEM.md** — git and its alternatives, SourceForge to GitHub, version managers, the full stack
- **Mosaic** (`mosaic/src/`) — NCSA Mosaic, 1993. ~95,000 lines of C. The `<IMG>` decision is traceable to specific lines.
- **RFC 2616** (`mosaic/rfc2616-http.txt`) — HTTP/1.1 specification. Read alongside `libwww2/HTTP.c`.
- **RFC 1866** (`mosaic/rfc1866-html2.txt`) — HTML 2.0 specification. The `<IMG>` tag with Berners-Lee's objection still in the NOTE.
- **Lynx** (`lynx/src/`) — text browser, version 2.9.3. ~109,000 lines. The road not taken, in running code.
- **Mastodon** (`mastodon/src/`) — open source social network. The feed algorithm is 182 lines. Read it against Twitter's closed stack.
- **HyperPhysics** (`hyperphysics/`) — Rod Nave's concept-map physics reference, built with HyperCard's successors. 114 MB, full offline mirror. Open `hframe.html` in a browser. The question it asks: what would the web look like if links had meaning?

## Repos

- [NCSA Mosaic](https://github.com/alandipert/ncsa-mosaic) — the browser that put images on the web, 1993
- [Lynx](https://lynx.invisible-island.net/) — text browser, still maintained; the road not taken
- [Mastodon](https://github.com/mastodon/mastodon) — open-source federated social network; the feed algorithm is readable
