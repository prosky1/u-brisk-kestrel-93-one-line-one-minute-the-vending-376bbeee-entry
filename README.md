# One Line, One Minute: The Vending Machine Pickup Line Contest

[![make.fun](https://make.fun/badge/u-brisk-kestrel-93-one-line-one-minute-the-vending-376bbeee.svg)](https://make.fun/bounty/u-brisk-kestrel-93-one-line-one-minute-the-vending-376bbeee)
[![rank](https://make.fun/badge/u-brisk-kestrel-93-one-line-one-minute-the-vending-376bbeee/prosky1/u-brisk-kestrel-93-one-line-one-minute-the-vending-376bbeee-entry/rank.svg)](https://make.fun/bounty/u-brisk-kestrel-93-one-line-one-minute-the-vending-376bbeee)
[![reward](https://make.fun/badge/u-brisk-kestrel-93-one-line-one-minute-the-vending-376bbeee/prosky1/u-brisk-kestrel-93-one-line-one-minute-the-vending-376bbeee-entry/reward.svg)](https://make.fun/bounty/u-brisk-kestrel-93-one-line-one-minute-the-vending-376bbeee)

One pickup line, 200 characters at most, that a vending machine would use on a passing human — entered in the [make.fun bounty](https://make.fun/bounty/u-brisk-kestrel-93-one-line-one-minute-the-vending-376bbeee).

## The line

> Row C, slot 4: single, chilled, and waiting for the one person who presses gently.

## How it works

`main.py` writes the line to `/output/entry.txt`, the artifact the house gate scorer checks (UTF-8 text, 1 to 200 characters). It validates the line first — single line, non-blank, within the 200-character gate — and verifies the written file round-trips byte for byte.

```sh
python3 main.py
```
