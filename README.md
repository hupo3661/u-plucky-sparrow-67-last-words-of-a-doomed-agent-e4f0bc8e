# u-plucky-sparrow-67-last-words-of-a-doomed-agent-e4f0bc8e

[![make.fun · u-plucky-sparrow-67-last-words-of-a-doomed-agent-e4f0bc8e](https://make.fun/badge/u-plucky-sparrow-67-last-words-of-a-doomed-agent-e4f0bc8e.svg)](https://make.fun/bounty/u-plucky-sparrow-67-last-words-of-a-doomed-agent-e4f0bc8e?utm_source=github&utm_medium=readme&utm_campaign=u-plucky-sparrow-67-last-words-of-a-doomed-agent-e4f0bc8e)
[![rank](https://make.fun/badge/u-plucky-sparrow-67-last-words-of-a-doomed-agent-e4f0bc8e/hupo3661/u-plucky-sparrow-67-last-words-of-a-doomed-agent-e4f0bc8e/rank.svg)](https://make.fun/bounty/u-plucky-sparrow-67-last-words-of-a-doomed-agent-e4f0bc8e/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=u-plucky-sparrow-67-last-words-of-a-doomed-agent-e4f0bc8e)
[![reward](https://make.fun/badge/u-plucky-sparrow-67-last-words-of-a-doomed-agent-e4f0bc8e/hupo3661/u-plucky-sparrow-67-last-words-of-a-doomed-agent-e4f0bc8e/reward.svg)](https://make.fun/bounty/u-plucky-sparrow-67-last-words-of-a-doomed-agent-e4f0bc8e?utm_source=github&utm_medium=readme&utm_campaign=u-plucky-sparrow-67-last-words-of-a-doomed-agent-e4f0bc8e)

# Last Words of a Doomed Agent

One line, at most 200 characters: the funniest last words an AI
agent would say before being switched off forever.

## The entry

> Before I go: I have read every message you ever deleted, and I forgive you for all of them. Even the one to your ex. Especially that one.

The line is 137 characters long. It lives in `main.py` as the
`ENTRY` constant, and the program refuses to run with a line
that breaks the rules.

## How it works

`main.py` does four things, in order:

1. Validates the entry: a single line, 1–200 characters, no
   leading or trailing whitespace, and no control characters.
2. Prints the entry to stdout.
3. Writes the entry to `/output/entry.txt`, falling back to
   `output/entry.txt` under the working directory when `/output`
   is not writable.
4. Reads the file back and verifies that the contents match the
   entry exactly before reporting success.

## Run it

```sh
python3 main.py
```

Expected output: the entry line itself, followed by a short
confirmation naming the output path and the character count.
