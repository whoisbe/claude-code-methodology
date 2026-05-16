# Skills

A skill is a natural-language reusable function for an LLM. It is a small directory — usually a `SKILL.md` plus any supporting files — that describes a workflow in enough detail that the model can execute it reliably without me re-explaining the steps each time. Skills are how I bring DRY to AI-driven work: if I have written the same instructions three times in three different chats, that is a skill waiting to be extracted.

## When something becomes a skill

I do not try to design skills up front. They emerge. The two signals I watch for:

- **I notice I am running the same predictable sequence of actions across multiple chats or projects.** "Render a chart packet from the journal, then validate the output, then update the manifest" used to be a paragraph I retyped. Now it is a skill.
- **The applicability across projects becomes obvious.** A workflow that is genuinely specific to one repo lives in that repo's CLAUDE.md. A workflow I am going to want in three different projects next month belongs in a skill.

If I am not sure yet, I leave the instructions inline until the third repetition. Premature skillification is its own tax — a skill that does not yet know its own boundaries tends to get rewritten more often than the inline version it replaced.

Anthropic also ships a `skill-creator` skill that handles the scaffolding when you're ready to extract one — it's worth using rather than hand-rolling the directory and frontmatter yourself.

## How skills live and get invoked

Skills live in `~/.claude/skills/` on my machine. Each skill is a directory; the entry point is a `SKILL.md` file with frontmatter declaring the skill's name and a short description of when it should fire. Claude Code reads the available skills at session start and decides when to invoke one based on the description. The description is the most important field — it is the only thing the model sees when deciding whether the skill applies.

A few practical conventions I've settled on:

- The description should describe the *trigger condition*, not the implementation. "Use when the user asks to render a chart packet" is better than "Renders chart packets."
- Skills should fail loudly when their preconditions are not met, not silently do the wrong thing.
- A skill that branches more than two or three ways is probably two skills.

## What's in here

[`examples/`](./examples/) will grow over time as I extract sanitized versions of skills from my active projects. For now it's empty — the README is the contract, the examples are the demonstration.
