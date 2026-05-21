# claude-code-methodology

A public companion to the newsletter at [bharathk.dev](https://bharathk.dev). Reusable methodology artifacts for building with agentic coding tools, primarily Claude Code.

This repo distills eight months of building with Claude Code into the patterns and templates I actually reach for every day

## What's in here

Four directories, each holding one kind of artifact:

- **`adrs/`** — Architecture Decision Records. A template and (soon) real examples from my projects. ADRs are how I keep architectural memory durable across context-clears.
- **`skills/`** — Natural-language reusable functions for LLMs. Skills live in `~/.claude/skills/` and let me stop re-explaining the same workflows. Examples will land here as I extract them from active projects.
- **`prompts/`** — Kickoff prompts for the macro context (Claude Chat). The opening prompt of a project does an enormous amount of work; this directory collects templates and worked examples.
- **`journals/`** — Sprint outputs and decision logs. The handoff artifacts that bridge sprints and keep the macro context informed about what the micro context actually did.

There's also a `methodology/` directory with a short standalone explainer of the macro/micro context separation that underlies everything else.

## Who this is for

Teachers, architects, and engineers who want a more deliberate way to work with agentic coding tools. People coming from non-traditional builder backgrounds — folks who think structurally about systems but haven't shipped production code in years, or ever. Anyone who has felt that working with Claude Code is powerful but slippery, and wants more rigor without giving up the speed.

The methodology rewards investment up front and pays off over weeks, not minutes.

## How to use it

Copy anything. Fork anything. Adapt anything. The license is MIT — no attribution required, though if these artifacts help you I'd love to hear about it.

The templates are starting points, not gospel. I change mine when they stop fitting the work. You should too.

## Newsletter

The narrative context for these artifacts lives at [bharathk.dev](https://bharathk.dev). The essays explain why these patterns exist, where they came from, and where they have broken down for me. The repo is the toolkit; the newsletter is the story behind the tools.

Published so far:

<!-- ESSAYS:START -->
- **2026-05-19** — [Macro and Micro](https://whoisb.substack.com/p/macro-and-micro-how-i-manage-my-context)
- **2026-05-12** — [I Spent a Decade Teaching. Eight Months Ago I Started Building.](https://whoisb.substack.com/p/i-spent-a-decade-teaching-eight-months)
<!-- ESSAYS:END -->
