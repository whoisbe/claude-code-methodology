# Kickoff Prompt Template

*A scaffold for the opening message of a new project conversation in Claude Chat. Fill in each section in your own voice. Delete the italic guidance before sending. Keep it short — the goal is to start a good conversation, not to write a spec.*

---

## The frame

*Open with a vivid analogy, scenario, or one-sentence picture of what you're actually trying to build. Skip the technical vocabulary for now. Help the model see the thing the way you see it.*

> Example: "Imagine a chess coach who reviews your games not by telling you the engine move, but by asking you what you thought you were doing on move 17. I want to build that for trading decisions."

## The constraint that motivates this

*What is the underlying truth that has to hold for this to matter? Not the feature list — the deeper thing. "I want to be able to X without Y." "Today this takes me Z hours and I am willing to spend weeks fixing that."*

> Example: "I make the same three mistakes in live trading every month, and reading the journal back at end of week never catches them in time. I want feedback on the same day, while the decision is still warm."

## The technical primitive I suspect would unlock it

*One concrete piece, named. The thing you have a hunch about. Not a full architecture. Just the seed.*

> Example: "I think the primitive is a deterministic chart packet — a rendered PNG plus a structured JSON manifest — that I can feed to a vision model along with my methodology, and get back a structured critique."

## What I'm uncertain about

*Where is your mental model thin? What have you already ruled out and why? What are you afraid the answer is? This is the part that produces the most useful pushback.*

> Example: "I'm not sure whether to render the chart in matplotlib or in a TradingView-style web tool. I've ruled out using raw OHLC text because I want the model to see the chart the way I see it. I'm worried the vision model won't be accurate enough on small candles."

## Invitation to brainstorm

*Tell the model what kind of conversation you want. Push back. Ask. Propose alternatives. Not a review of a finished plan — a thinking partner for an unfinished one.*

> Example: "I want to brainstorm this with you before I commit to an architecture. Push back on the framing if it seems off. Ask me about anything that's underspecified. Propose alternatives I haven't considered. Once we've converged on a direction I'll ask you to help me draft ADRs."
