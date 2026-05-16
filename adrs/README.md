# Architecture Decision Records

An Architecture Decision Record is a short document that captures one significant architectural choice: what was decided, what the context was, why this option won, and what we expect to live with as a consequence. The format is older than agentic coding — Michael Nygard wrote about it more than a decade ago — but it turns out to be unusually well-suited to working with LLMs.

## Why I write them

The single most expensive thing in a long Claude Code project is forgotten reasoning. I have shipped the same wrong-but-tempting refactor twice in one week because I cleared context between attempts and the second me did not remember why the first me had backed away from it. ADRs are the cheapest fix I have found.

Two specific properties make them work:

- **Durable across context-clears.** When I start a fresh Claude Code session, I can point it at the `adrs/` directory and the project's architectural memory is restored without me having to re-narrate three weeks of decisions.
- **Auditable by future-me.** When I revisit a project after a month, the ADRs let me reconstruct not just what we built but why we built it that way, and what alternatives we considered and rejected. The rationale is the part that decays fastest in my own head, and the part the ADR preserves best.

## When I write them

I write an ADR at four specific moments:

1. **Project start, immediately after feasibility and requirements.** The first three to five ADRs usually cover the big choices: storage, runtime, model strategy, deployment target. These set the frame the whole project will operate inside.
2. **Whenever a non-trivial architectural choice comes up mid-project.** "Non-trivial" means: I'd be annoyed if a teammate made this choice without writing it down. Library selection for a core dependency, schema shape, contract between two components.
3. **When the project hits a roadblock and the architecture has to pivot.** I do not delete the old ADR. I change its Status to Superseded and link forward to the new one. The old reasoning is still load-bearing for understanding the pivot.
4. **When I notice I've been making a decision implicitly and re-litigating it.** That is the signal that it deserves to be written down.

## What's in here

- [`adr-template.md`](./adr-template.md) — the template I copy when starting a new ADR.
- [`examples/`](./examples/) — real ADRs from my projects, added as I extract sanitized versions.
