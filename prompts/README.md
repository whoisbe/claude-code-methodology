# Kickoff Prompts

In the macro/micro architecture I use, the macro context lives in Claude Chat: it is where requirements get discovered, where architecture gets argued out, where ADRs get drafted. The micro context — Claude Code — is for implementation. The thing that bridges them is a sequence of artifacts, and the very first artifact is the kickoff prompt I write to start the macro conversation.

The opening prompt of a project does an outsized amount of work. It sets the frame the entire project will think inside. A good kickoff prompt makes the next two hours of conversation easy. A bad one makes the whole project drag.

## What makes a kickoff prompt work

After a lot of trial and error I've converged on what tends to produce good first conversations:

- **A vivid frame.** An analogy, a scenario, a sentence that captures what I am actually trying to build in human terms before any of the technical vocabulary kicks in. The model is much better at thinking with me when it can picture what we're doing.
- **The real constraint that motivates the project.** Not the feature list — the underlying thing that has to be true for this to matter. "I want to be able to do X without doing Y."
- **The technical primitive that I suspect would unlock it.** A concrete thing, named. Not a full architecture, just the one piece I have a hunch about. This anchors the conversation without preempting it.
- **Honest thinking-out-loud about what I don't know.** What I'm uncertain about, what I've already ruled out and why, where my mental model feels thin. This is the part that most reliably produces good pushback.
- **An explicit invitation to brainstorm.** Telling the model that this is the start of a conversation, not a spec — and that I want it to push back, ask, propose alternatives.

What does *not* work, in my experience: a giant pre-architected design dump with forty decision trees and a request to "review my plan." The model will dutifully review the plan. It will not catch the thing that is actually wrong, because the framing has already locked in the shape of the answer.

## What's in here

- [`kickoff-template.md`](./kickoff-template.md) — the scaffold I use when starting a new project conversation.
- [`examples/`](./examples/) — worked kickoff prompts from real projects. Empty at launch; I'll add sanitized versions as I extract them.
