# Linus Torvalds

*He didn't write a manifesto. He posted a message on a newsgroup saying he was working on something, "just a hobby, won't be big and professional." Then he shipped it.*

---

## Two things in a weekend

Linus Benedict Torvalds has done two things that most people consider impossible.

In 1991, over the course of a few months in a Helsinki apartment, he wrote the Linux kernel — the operating system core that now runs Android phones, the world's supercomputers, the servers that host the internet, and the International Space Station. He was twenty-one. He started because he wanted Unix on his home computer and couldn't afford it.

In 2005, after a dispute with the company that made the version control system the Linux kernel used, he wrote a replacement. He wrote it in ten days. That replacement was Git. It is now the standard version control system for almost all software development on earth, and the foundation on which GitHub, GitLab, and the entire modern open source infrastructure is built.

Both of these are absurd facts. Neither one seems like a thing a person can do. He did both of them.

---

## The Linux announcement

On August 25, 1991, Linus posted to the comp.os.minix newsgroup:

> Hello everybody out there using minix —
>
> I'm doing a (free) operating system (just a hobby, won't be big and professional like gnu) for 386(486) AT clones. This has been brewing since april, and is starting to get ready. I'd like any feedback on things people like/dislike in minix, as my OS resembles it somewhat (same physical layout of the file-system (due to practical reasons) among other things).
>
> I've currently ported bash(1.08) and gcc(1.40), and things seem to work. This implies that I'll get something practical within a few months, and I'd like to know what features most people would want. Any suggestions are welcome, but I won't promise I'll implement them :-)
>
> Linus (torvalds@kruuna.helsinki.fi)
>
> PS. Yes — it's free of any minix code, and it has a multi-threaded fs. It is NOT portable (uses 386 task switching etc), and it probably never will support anything other than AT-harddisks, as that's all I have :-(.

"Just a hobby, won't be big and professional." This is the most underestimated prediction in the history of software.

The casualness is not false modesty. It is accurate reporting of his state of mind in August 1991. He was solving his own problem. He did not know it would become anything. What made it become something was that he shared it — put it in front of the people who could improve it — and that the license (GPL) made their improvements accumulate and return.

That is the mechanism: Linus wrote a starting point, the license made collaboration possible, and twenty million lines of code later, the hobby was running the world.

---

## The character

Linus is the most prominent counterexample to the Stallman model of free software advocacy. He is not an idealist. He does not think of software freedom as a moral imperative. He thinks of it as a practical arrangement: sharing code produces better code faster, so he shares code.

His famous statement on the philosophy: *"I do not have some over-arching agenda. I use open source because it works."*

This drives Stallman (and others in the Free Software movement) to occasional frustration, because Linux uses the GPL — Stallman's license — and Linus has kept it on GPLv2 specifically because he disagrees with GPLv3's stance on tivoization and software patents. He is, in other words, using the political instrument Stallman built, while explicitly rejecting Stallman's politics. Stallman considers this a mistake. Linus considers this not his problem.

His management style is well documented and controversial. The Linux Kernel Mailing List is public, and Linus's responses to code submissions are sometimes brutal. He has called code "pure and utter garbage." He has told contributors their patches are "crap." In 2018, after years of criticism, he stepped back from kernel development for a period and said he was going to work on understanding the effect his communication style had on other people. He returned. The kernel development community has slowly, unevenly evolved its norms.

You are allowed to have a view on this. The relevant observation for this course: the Linux Kernel Mailing List is one of the most consequential pieces of technical discourse ever produced, and it is fully public. Forty years of architecture decisions, security debates, performance arguments, and personality conflicts — all of it archived, searchable, readable. No other engineering project of comparable scale has this record.

---

## Git

In 2005, the Linux kernel project was using BitKeeper — a proprietary version control system whose creator had given the kernel team free access. When that access was revoked, Linus could have used any of the existing free version control systems: CVS, Subversion, Arch. He evaluated them and found them inadequate. So he wrote his own.

His stated goals for git, from the beginning:

1. Speed
2. Simple design
3. Strong support for non-linear development (thousands of parallel branches)
4. Fully distributed — no central server required
5. Able to handle the Linux kernel's scale efficiently

He had a working version in ten days. The name "git" is British slang for an unpleasant or stupid person. He has said he names all his projects after himself: Linux, git.

Git's design is unusual and, to many programmers encountering it for the first time, counterintuitive. The fundamental concept is not a series of changes to files, but a series of snapshots of the entire file tree. Every commit is a complete state of the repository at a point in time, stored as a content-addressed graph of objects. The objects are blobs (file contents), trees (directory contents), and commits (pointers to trees plus metadata). The content-addressing — every object is named by the SHA-1 hash of its contents — is what makes the history immutable and the graph merge-able.

This design, which seemed idiosyncratic in 2005, turned out to be exactly right for distributed collaborative development. GitHub (2008) built an entire platform on it. Every developer in the world now works in a model that Linus designed in ten days in 2005 because he was annoyed.

---

## The contrast with Stallman

Put Stallman and Linus side by side and you have one of the most interesting intellectual contrasts in the history of software.

Stallman decided what software *should* be and worked backward to build it. The GPL is the legal instrument of a vision. Every technical decision in GNU is downstream of a moral commitment. The code is in service of the freedom.

Linus decided what software *worked* and built more of it. Git is the technical instrument of an engineering judgment. Every technical decision in Linux and git is downstream of a practical goal. The freedom is a beneficial side effect of the license choice, not the point.

The interesting thing is that they need each other. The GPL that made Linux's collaborative development model possible is Stallman's work. The kernel that proved free software could build world-class infrastructure is Linus's work. Each one, without the other, would have had less impact.

Students sometimes want to know which of them is right. The question may be less useful than asking: what does each model produce, and what does each model cost?

---

## What is in 02/git/

`02/git/` contains the git source repository, checked out sparsely. Git is written in C. It is a useful counterpoint to the compilers in this unit — where a compiler translates code from one language to another, git translates intent (what you meant to save and when) into a content-addressed graph of objects.

**Start in `builtin/`** — each file corresponds to a git subcommand. `builtin/commit.c` is `git commit`. `builtin/log.c` is `git log`. The entry point for the whole program is `git.c`.

**Read `object.h` and `object.c`** — the object model. This is the content-addressed graph: blob, tree, commit, tag. The SHA-1 hash that names every git object is computed here.

**Read `diff.c`** — the diff algorithm. Git's diff is a variant of the Myers diff algorithm. It is the thing that makes `git diff` work, and it is the same algorithm that GitHub renders when you look at a pull request.

**The porcelain and plumbing distinction:** git divides its commands into "plumbing" (low-level, scriptable, stable API) and "porcelain" (user-facing, higher-level). `git hash-object`, `git cat-file`, `git update-index` are plumbing. `git commit`, `git push`, `git merge` are porcelain. The plumbing commands expose the object model directly. Run `git cat-file -p HEAD` in any git repository to see a raw commit object. Run `git cat-file -p HEAD^{tree}` to see the tree it points to.

---

## What to do

1. Read the 1991 announcement. Read it slowly. Notice that he describes the project accurately — it does resemble Minix, it is not portable, it uses 386 task switching. He is wrong only about its scope.

2. Read the git README (`02/git/README.md`). It is characteristically direct.

3. Run `git cat-file -p HEAD` in this repository. What you are looking at is a commit object — the exact data structure defined in `object.h`. Read the hash, the tree hash, the author, the committer, the message. This is what git stores.

4. Read `02/git/builtin/commit.c`. Find where the commit object is constructed. Compare what you see to the raw object you read in step 3.

5. Read the Linux announcement. Then read a git commit message from Linus in the Linux kernel history: `git log --author="Linus Torvalds" -20` in the kernel repo if you have it, or browse kernel.org/pub/scm/linux/kernel/git/torvalds/linux.git. Notice the register: direct, specific, no apology, occasionally funny.
