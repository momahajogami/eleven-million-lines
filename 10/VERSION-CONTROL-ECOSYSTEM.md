# The King and Its Alternatives
## Version Control, Package Management, and the Infrastructure of Collaboration

*A narrative for Unit 10*

---

## Before Git There Was Chaos

The history of version control is the history of programmers trying to answer one question: if ten people are editing the same file, what happens?

The naive answer is: the last one to save wins. This is what happens with a shared network drive. It is catastrophic. Work disappears. Nobody knows what changed or who changed it or why. The file is simultaneously everyone's and nobody's.

The first serious answers to this problem were **RCS** (Revision Control System, 1982) and **CVS** (Concurrent Versions System, 1990). RCS locked files: when you edited a file, you checked it out, nobody else could touch it, you checked it back in. CVS relaxed the locking: multiple people could edit simultaneously and the system would attempt to merge their changes automatically, flagging conflicts for humans to resolve.

CVS was dominant through the 1990s. It was also, by general consensus, terrible. It had no atomic commits — a commit that touched ten files could fail halfway through, leaving the repository in an inconsistent state. Renaming a file was effectively impossible without losing its history. Branching was slow and painful. The repository was a single central server; if the server went down, nobody could work.

**Subversion** (SVN, 2000) was built explicitly to be CVS but fixed. Atomic commits. Better branching. Proper file renaming. It succeeded. Through the early 2000s, Subversion was the standard. SourceForge, which hosted the majority of open source projects in that era, used Subversion. Google Code used Subversion. The Apache Software Foundation used Subversion. If you were doing version control in 2003, you were probably using Subversion.

Subversion kept the central server model. There was one canonical repository. You checked out from it, made changes, committed back. The server was the truth. If you were offline, you could look at your working copy but you could not commit, could not diff against history, could not do anything that required the repository. The server was not optional.

This seemed natural. This is how version control had always worked. The server held the history. You held a working copy. The history was not yours to keep.

---

## BitKeeper and the Rupture

The Linux kernel was maintained through 2002 using a combination of email patches and a system called BitKeeper. BitKeeper was proprietary — owned by a company called BitMover — but Larry McVoy, its author, allowed Linux kernel developers to use it for free on the condition that they not work on competing version control systems.

BitKeeper was genuinely good. It was distributed: every developer had a full copy of the repository history, not just a working copy. You could commit offline. You could branch freely. You could merge across repositories. The model was different from Subversion in a fundamental way: there was no canonical server. There were many repositories, and they could synchronize with each other.

In 2005, a developer reverse-engineered the BitKeeper protocol. McVoy revoked the free license for kernel developers. The kernel project needed a new version control system.

Linus Torvalds wrote Git in April 2005. The first commit was on April 3. By April 7 it could host its own development. By June 16, the Linux 2.6.12 kernel release was managed with Git. The entire system was written in about ten days of focused work.

Git is distributed in the same way BitKeeper was distributed: every clone is a full copy of the entire repository history. There is no server you depend on. You can commit, branch, merge, diff, log, and do everything else entirely offline. When you push to GitHub, you are synchronizing your local repository with a remote one. The remote is convenient. It is not the truth. Your local copy is equally authoritative.

This is the architectural choice that made Git what it became. Not just technically — culturally. If the repository is distributed, collaboration does not require a central authority. You can fork. You can maintain your own version indefinitely. You can accept or reject patches on your own terms. The power that in Subversion lived on the server lives, in Git, with every person who has a clone.

---

## Mercurial and the Road Not Taken

Git was not the only distributed version control system to emerge from the BitKeeper rupture. **Mercurial** (hg) was written by Matt Mackall, also in April 2005, also in response to the BitKeeper situation, also rapidly. The two systems were developed simultaneously, independently, and are architecturally similar.

Mercurial's design philosophy was different from Git's. Where Git exposes its internal model directly — the object store, the index, the ref system — Mercurial hides the implementation behind a cleaner interface. Git commands are terse and sometimes surprising; Mercurial commands are verbose and consistent. Git's branching model is powerful and complex; Mercurial's is simpler and more constrained.

Many people who tried both in 2005 and 2006 preferred Mercurial. It was easier to learn. The error messages were better. The documentation was clearer. Mozilla chose Mercurial for Firefox development. Python chose Mercurial. Several large projects made the same choice.

Git won anyway. The reasons are debated. GitHub, which launched in 2008, supported Git only. GitHub's network effects — the pull request model, the social coding features, the discoverability — were decisive. Once enough projects were on GitHub, the gravity was strong. Mercurial had Bitbucket; Bitbucket eventually added Git support; eventually Bitbucket dropped Mercurial support entirely in 2020.

The Mercurial story is the Gopher story again. The technically comparable or arguably superior option losing to the one with better network effects and a company behind it. The history of infrastructure is full of this pattern. The winner is not always the best. The winner is the one that got to critical mass first, or had the right institutional backing, or happened to be in the right place when the network effect kicked in.

Mercurial is still maintained. It is still used by some large projects. Facebook used it internally for their main repository for years — the scale of their codebase made certain Git operations impractical. They built extensive tooling on top of Mercurial to handle a monorepo of that size, and contributed much of it back. Then they migrated to a Git-compatible system anyway.

---

## The Alternatives That Stayed Themselves

Not every version control system tried to win the Git war. Some solved different problems for different people and remained themselves.

**Darcs** (2002) is based on patch theory — a mathematical framework for representing changes to files as commutative patches rather than snapshots. The fundamental object in Darcs is not a commit (a snapshot of the entire repository at a moment) but a patch (a precise description of a change). Patches can be applied in different orders if they don't conflict. You can pick a single patch out of a series and apply it elsewhere without taking everything that came before it.

This is mathematically elegant. It is also, for large repositories, slow — the patch dependency computation is expensive. Darcs has a devoted following among people who care about the mathematical foundations of version control. It has not scaled to large projects. It remains a small, principled tool that does what it does correctly.

**Fossil** (2006) was written by D. Richard Hipp, who also wrote SQLite. The entire Fossil repository — history, wiki, bug tracker, forum — lives in a single SQLite database file. One file. You can copy it with `cp`. You can back it up with `rsync`. The entire project history is self-contained and portable in a way that Git, which scatters objects across a directory tree, is not.

Fossil is used by SQLite. Hipp runs his most important project on his own tool, which is the best possible endorsement. Fossil's interface is simpler than Git. Its branching model is intentionally more conservative. It will not let you rewrite history the way Git will — the history is permanent, which is either a feature or a bug depending on your philosophy.

The Fossil design embodies an argument: a project is not just code. It is code plus discussion plus bug reports plus documentation plus history. Version control systems that manage only code are managing only part of what a project is. Fossil manages the whole thing. One file, everything in it, portable anywhere.

---

## SourceForge and the Hosting Layer

Version control solves the problem of tracking changes. It does not solve the problem of where to put the repository so that other people can find and use it.

**SourceForge** launched in 1999 as the first major open source project hosting platform. It provided CVS repositories, mailing lists, bug trackers, file download hosting, and a directory of projects. At its peak in the mid-2000s, SourceForge hosted over 100,000 projects and was the first place you looked for open source software.

SourceForge's arc is told in Unit 05: the acquisition by Geeknet, the acquisition by Dice Holdings, the deterioration of the service, the addition of adware to installers, the controversy, the slow decline. The story of SourceForge is the story of a commons being acquired and monetized until it stopped being a commons.

**Google Code** (2006-2016) was Google's attempt at a hosting platform. Subversion and later Mercurial repositories, issue tracking, code review. Google shut it down in 2016. All projects were migrated or archived. The projects that were still active had mostly already moved to GitHub. The ones that hadn't were, in many cases, abandoned.

**GitHub** (2008) changed everything in the way that Gmail changed email: by being so much better than what came before that the improvement felt qualitative rather than quantitative. The pull request model — fork a repository, make changes, propose them back via a web interface — made contributing to open source projects dramatically easier. The social features — following developers, watching repositories, starring projects — made it a discovery platform as well as a hosting platform. The web-based code browser made it possible to read code without cloning anything.

GitHub was acquired by Microsoft in 2018 for $7.5 billion. The open source community's reaction was mixed: some left for alternatives, most stayed. GitHub has remained largely as it was, operating as a mostly free public service for open source projects.

**GitLab** (2011) is the open source alternative to GitHub. The entire GitLab platform is open source and self-hostable. If you want to run your own GitHub-equivalent, entirely under your control, GitLab is the standard choice. Many European universities and companies host their own GitLab instances. The European Commission runs one. The preference for self-hosted infrastructure — keeping the data and the tool within your own jurisdiction — is a real and reasonable position, and GitLab exists to serve it.

**Sourcehut** (~2018, sr.ht) is the principled minimalist alternative. No JavaScript required to browse. Mailing-list-based patch submission — the way Linus accepts patches for the Linux kernel — instead of pull requests. Plain, fast, Unix-aligned. Drew DeVault built it because he wanted a hosting platform that reflected the values of the software it hosted. Sourcehut is mentioned in this course's own `meta/PUBLISH.md` as the aesthetically correct mirror for a course about reading code the old way.

---

## Version Managers: One Layer Down

A package manager installs libraries for a language. But which version of the language?

Python 2 and Python 3 are not compatible. You may have projects that need Python 2.7 (old, maintained legacy code) and projects that need Python 3.11 (current). They cannot share an interpreter. You need both versions installed simultaneously, and you need each project to use the right one.

This is the problem that **version managers** solve. They manage not the packages for a language but the language runtime itself — one layer below the package manager.

**pyenv** manages Python versions. `pyenv install 3.11.0`. `pyenv local 3.11.0` sets the Python version for the current directory. When you `cd` into a project, pyenv intercepts the `python` command and points it at the right version. The project's `.python-version` file, committed to the repository, records which Python it needs.

**nvm** (Node Version Manager) does the same for Node.js. `nvm install 18`. `nvm use 18`. An `.nvmrc` file in the project directory. The Node.js ecosystem moves fast; a project from two years ago may need a Node version that is incompatible with a project from last month.

**rbenv** and **rvm** do it for Ruby. **rustup** does it for Rust, but with a twist: rustup also manages the Rust toolchain's channels (stable, beta, nightly), allowing you to run the latest nightly compiler for a project that needs cutting-edge features while keeping stable for everything else.

**asdf** is the version manager that manages version managers: one tool, one interface, plugins for every language. `asdf install python 3.11.0`. `asdf install nodejs 18.0.0`. One configuration file, `.tool-versions`, listing every language and version a project needs. The Unix principle — one tool, composable — applied to the problem of managing the tools.

The version manager sits below the package manager in the stack. The full dependency chain, from bottom to top:

```
hardware
  └── operating system
        └── system package manager (apt, pacman, brew)
              └── version manager (pyenv, nvm, rustup, asdf)
                    └── language package manager (pip, npm, cargo, gem)
                          └── your code
```

Each layer depends on the one below it. Each layer has its own tools, its own conventions, its own failure modes. The version manager breaks because the shell configuration is wrong. The package manager breaks because the version manager chose the wrong runtime. The runtime breaks because the system package manager installed an incompatible library. The stack is tall and each level can fail independently.

Understanding the stack is part of what this course is for. Not to memorize the tools — the tools change constantly — but to understand the layers, and what each layer is responsible for, and where in the stack a given problem lives. When something doesn't work, knowing which layer is broken tells you where to look.

---

## The Interdependencies

These systems are not independent. They are deeply entangled.

Git and GitHub and npm are entangled in a specific way: npm packages can specify dependencies by GitHub repository URL, not just by registry name. `"foo": "github:username/repo"` in a `package.json` fetches directly from GitHub. This means GitHub outages break npm builds. In 2020 a GitHub outage cascaded into npm build failures worldwide. Two systems from two companies, owned by the same company, failing together.

Package managers use version control internally. `pip install git+https://github.com/user/repo.git` installs a Python package directly from a Git repository. Cargo can do the same. The package registry and the version control host are separate systems that frequently substitute for each other.

Version control hosts have become package registries. GitHub's Container Registry hosts Docker images. GitHub Packages hosts npm, Maven, NuGet, and RubyGems packages. The line between "place where code is stored" and "place where packages are distributed" has blurred.

Operating system package managers and language package managers overlap in uncomfortable ways. If you install Python via `apt`, you get the system Python — the version Debian or Ubuntu decided to ship, often a version behind. If you then install packages with `pip` into the system Python, you may break system tools that depend on that Python installation. The language community's solution (virtual environments, version managers) and the OS community's solution (system packages) are in tension. The user is in the middle.

This tension is not resolved. It is managed. Every developer has a setup that works for them, arrived at through trial and error, fragile in specific ways they have learned to work around. The setup is not documented anywhere authoritative because there is no authoritative answer. The tools are designed by different communities with different assumptions, and the combinations are not fully tested.

This is the honest picture of the infrastructure. It works, mostly. It is not clean. The layers were built by different people at different times for different purposes, and they were composed after the fact into a stack that nobody fully designed. It holds together through convention and community knowledge and a lot of `~/.bashrc` configuration.

---

## What the Stack Means

The stack of version control, hosting platforms, version managers, and package managers is the infrastructure of collaborative software development. It is what makes it possible for a developer anywhere in the world to clone a repository, install its dependencies, run its tests, make a change, and propose that change back to the project — in an afternoon, without contacting anyone, without asking permission.

This is extraordinary. It did not exist in 1990. It barely existed in 2000. By 2010 it was standard. By now it is so standard that developers who learned to program after 2010 have difficulty imagining the alternative.

The alternative was: you mailed a patch to a mailing list, waited for a maintainer to review it, hoped the maintainer was active, hoped the patch applied cleanly to their version of the code, hoped they agreed with your approach. Weeks. Sometimes months. Sometimes nothing.

The stack compressed this to hours. The pull request, the CI system that runs tests automatically on your proposed change, the code review tools, the merge button: the entire workflow is visible and readable in the same way the code is. The tooling is open source. The protocols are public. You can run your own GitHub. You can inspect every step of the process.

The right to read applies here too. The infrastructure of collaboration is not proprietary. It is open, documented, forkable. You can understand how it works by reading it. You can improve it by contributing to it. You can replace it with something better.

This is what the open source ecosystem actually is: not just code, but the tools for building code, the tools for distributing code, the tools for collaborating on code, the tools for managing versions of code — all of it open, all of it readable, all of it built by the same community that uses it.

The eleven codebases in this course were all built using some version of this stack. The stack is older than some of the codebases. Reading the codebases without understanding the stack is like reading a book without knowing what a printing press is.

---
