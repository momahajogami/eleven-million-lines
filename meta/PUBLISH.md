# Publishing Plan — Eleven Million Lines You Should Know

**Website live deadline: September 2, 2026.**

Two weeks from push to first wave of attention.

---

## Before anything goes out

- [ ] Repo is pushed to GitHub (`eleven-million-lines`, public)
- [ ] README.md reads well as a standalone landing page for a stranger
- [ ] At least one unit feels complete enough to show (01 is the anchor)
- [ ] Website is live at a real URL (see below)

---

## Week One — Lay the foundation

### Day 1–2: Push and dress the repo

```bash
git remote add origin https://github.com/YOUR_USERNAME/eleven-million-lines.git
git push -u origin main
```

- Add a `LICENSE` (MIT for the course materials; codebases have their own)
- Pin the repo on your GitHub profile
- Add topics/tags: `education`, `computer-science`, `open-source`, `unix`, `course`
- Make sure the repo description is one strong sentence

### Day 3–4: Write the announcement post

Write it once. Post it everywhere (adapted). Core draft lives at `meta/ANNOUNCE.md` (not yet written — create it before posting anything).

The post should answer:
- What is this?
- Who is it for?
- What exists right now?
- How do you follow along or get involved?

Tone: personal, direct, a little proud. Not a press release.

### Day 5–6: Set up the website

- Get a domain (suggestions: `elevenmillionlines.com`, `11mlinesyoushouldknow.com`, or something shorter)
- Deploy from `website/` in this repo via GitHub Pages or Netlify
- It should be live before the first announcement goes out

### Day 7: Rest. Read what you built. Read it like a stranger.

---

## Week Two — Announce

### Day 8: Hacker News

Post as **Show HN: Eleven Million Lines You Should Know — a course on reading landmark codebases**

Rules:
- Submit between 8–10am Eastern (peak traffic)
- The title does the work — don't oversell it
- Be in the thread all day to answer questions
- Do not post and disappear

HN is the right first venue. The audience is exactly right: programmers who remember what it felt like to first open a real codebase and feel lost.

### Day 9: Lobste.rs

Smaller, more focused. Tag: `programming`, `education`, `unix`. Same announcement, slightly adapted. The Lobste.rs crowd will appreciate the Lions' Commentary reference immediately.

### Day 10: Reddit

- r/programming (large, noisy, but volume matters)
- r/compsci (more academic)
- r/unix (unit 01 specifically)
- r/emacs (unit 03)
- r/haskell (unit 06 — the GHC crowd will have opinions)

Post in each separately, framed to the audience. Don't cross-post the exact same text.

### Day 11: Academic and educator channels

- SIGCSE mailing list (CS education — this is the most important academic list)
- edu-sig (Python educators list — odd fit but active)
- Direct email to 2–3 CS educators you respect, asking for a read and honest reaction
- Your Ohio contacts specifically — this is where it launches first

### Day 12: Mastodon / academic social

- Post on Mastodon (fosstodon.org is the right instance for this crowd)
- Tag relevant accounts in the fediverse — open source educators, university CS folks
- LinkedIn if you have academic connections there (frame it for educators, not developers)

### Day 13–14: Follow up and iterate

- Respond to every substantive comment or question from the week
- Note what questions people ask — those are gaps in the README or course materials
- Update `meta/sessions/` with what the reception looked like

---

## Platform alternatives to GitHub

GitHub is the right primary home — the audience is already there. But consider mirrors or alternatives for philosophical alignment:

**Sourcehut (`sr.ht`)** — strongest fit aesthetically. Plain, fast, no JavaScript required. Deeply Unix-aligned. The kind of platform Lions' Commentary would live on if it were born today. Worth mirroring here. Mailing-list-based contribution model also fits the course's ethos.

**Codeberg** — European, nonprofit, Gitea-based. Good for the free-software community (unit 03 crowd). Secondary mirror.

**GitLab** — if you ever want CI/CD for the website or automated builds. Self-hostable if you want full control eventually.

**Not recommended:** Bitbucket (in decline), SourceForge (unit 05 covers its betrayal — would be ironic).

**Long-term:** A self-hosted Gitea instance at your own domain would be the classical choice. Not urgent now. File it under "when the course has an institution behind it."

---

## What success looks like at two weeks

- 200+ GitHub stars (achievable on HN with a good thread)
- 3–5 substantive emails from educators or people who want to contribute
- One unit that people are actually reading and talking about
- A website that doesn't embarrass you

Success is not viral. Success is the right 50 people finding it and taking it seriously.

---

## Files to create before posting

- [ ] `meta/ANNOUNCE.md` — the core announcement text
- [ ] `LICENSE` in repo root
- [ ] `website/index.html` (see `website/` directory)
- [ ] GitHub repo description + topics set
