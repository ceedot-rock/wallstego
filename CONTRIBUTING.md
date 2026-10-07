# Contributing to wallstego

Thanks for helping hide messages in plain sight.

## Ground rules

- wallstego is obscurity, not encryption. Never pitch it as secret-from-a-
  knowledgeable-reader; docs that imply otherwise get corrected.
- The visible text must come back byte-identical: any change that alters
  `visible_text(embed(cover, msg))` does not ship.
- Roundtrip is sacred: `extract(embed(cover, msg)) == msg` for every input,
  including empty messages and non-ASCII payloads.

## Quick check

```sh
python3 test_wallstego.py   # must print "all tests pass"
```

CI runs this plus a license/metadata check on every pull request.

## Making a change

1. Keep the scheme stable: U+200B = 0, U+200C = 1, U+200D = end-of-message.
   If you must change the alphabet, that is a new major scheme, not a tweak.
2. Add or extend coverage in `test_wallstego.py` for any new behavior.
3. Verify the CLI paths too: `embed`, `extract`, `check`.
4. Open a pull request using the template.

## Licensing

wallstego is Apache-2.0. By contributing you agree your contribution is
licensed under the Apache-2.0 license (see LICENSE).
