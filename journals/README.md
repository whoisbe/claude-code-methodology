# Journals

The single most useful habit I have picked up working with agentic coding tools is to journal everything. Not because journals are inherently virtuous, but because the human in the loop has a finite attention budget and the tools do not. If I do not externalize what was decided, what was built, and what is still open, then I am the bottleneck — and a tired, leaky bottleneck at that. Journaling is how I get attention off my own working memory and into a place the next session of either me or the model can pick it up.

## Two artifacts

I keep journaling deliberately minimal. Two artifacts do almost all the work:

- **`sprint-output.md`** — written at the end of each sprint by Claude Code. It captures what the micro context actually did: files modified, features built, decisions made, open questions surfaced. I upload this back into the macro context (Claude Chat) at the start of the next sprint so the architectural conversation knows what just happened. Without this file the macro context drifts away from reality fast.
- **`decisions-log.md`** — a running, project-level log. One line per decision, with a date and (if applicable) a link to the full ADR. Designed to be scannable in thirty seconds. When I open a project after two weeks away, this is the first file I read.

The ADRs in [`../adrs/`](../adrs/) are the deep version; the decisions log is the index.

## Sprint discipline

A sprint, in my usage, is a focused unit of work — usually a few hours, sometimes a day or two — with a single clear goal. Sprints have a beginning and an end, and the end matters as much as the beginning: at the boundary, I clear the Claude Code context.

That sounds destructive. It is the opposite. Long-running contexts accumulate distractions, half-considered options, and stale assumptions. A cleared context is sharper. The sprint-output file is what makes context-clearing safe — it carries forward exactly what needs to carry forward, and nothing else.

The discipline is: do not end a sprint without writing the output file. Do not start a sprint without reading the previous one.

## What's in here

- [`sprint-output-template.md`](./sprint-output-template.md) — the structure I have Claude Code fill in at sprint end.
- [`decisions-log-template.md`](./decisions-log-template.md) — the running project-level log.
