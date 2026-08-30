# Firefox / Mozilla

The Mozilla codebase is too large to clone locally (~3GB). Read it online via Searchfox:

- Searchfox: https://searchfox.org/mozilla-central/source

## What to read

**SpiderMonkey** (`js/src/`) — the JavaScript engine. Start with `vm/Interpreter.cpp`. This is one of the most sophisticated pieces of software in the world; read it for orientation, not mastery.

**Gecko layout** (`layout/`) — the engine that turns HTML and CSS into a visual page. `layout/base/nsCSSFrameConstructor.cpp` is where the DOM becomes a frame tree.

**Necko networking** (`netwerk/`) — HTTP, DNS, caching. The plumbing.

## jwz and the Netscape source drop

Jamie Zawinski was one of the engineers who fought to open-source the Netscape codebase before the company collapsed. His account of that period is at jwz.org. The Mozilla project exists because of that decision.

The original Netscape source drop (January 1998) was the largest open-source release of its time. The code was messy, undocumented, and platform-specific. The Mozilla project spent two years rewriting it before shipping anything usable. Firefox 1.0 shipped November 2004.

## Key characters

- **Jamie Zawinski** — engineer, author, nightclub owner. jwz.org is worth reading.
- **Brendan Eich** — invented JavaScript at Netscape, later Mozilla CEO.
- **Mitchell Baker** — CEO of Mozilla Foundation. The organizational and political story.
