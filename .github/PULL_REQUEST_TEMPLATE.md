## What changed

<!-- One or two sentences. -->

## Checks

- [ ] `python3 test_wallstego.py` passes (prints "all tests pass")
- [ ] Roundtrip verified: `embed` then `extract` returns the original message
- [ ] `visible_text` of stego output matches the original cover text
- [ ] No zero-width characters leak into visible output of `embed`
