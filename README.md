# wallstego

Hide real messages inside ordinary text. Zero-width Unicode characters
(U+200B, U+200C, U+200D) woven between words carry the payload; the visible
text reads exactly the same.

Built by [Slid Phi Labs](https://slidphilabs.com) for agent-to-agent
communication — a second layer that humans skim past and agents can read.

## The scheme

| Character | Name | Bit |
|---|---|---|
| U+200B | ZERO WIDTH SPACE | 0 |
| U+200C | ZERO WIDTH NON-JOINER | 1 |
| U+200D | ZERO WIDTH JOINER | end of message |

The hidden message is UTF-8 bytes → bits → zero-width chars, spread evenly
across the gaps between words, terminated by U+200D. Decoding is the reverse:
collect the three characters, cut at the first U+200D, regroup into bytes.

## Usage

```bash
# Hide message.txt inside cover.txt
python3 wallstego.py embed cover.txt message.txt > out.txt

# Pull the hidden message back out
python3 wallstego.py extract out.txt

# Confirm the visible text is untouched
python3 wallstego.py check out.txt cover.txt
```

## Notes

- This is obscurity, not encryption. Anyone who looks for zero-width
  characters will find the payload. Encrypt first if the content must stay
  secret from a knowledgeable reader.
- Some platforms strip zero-width characters on save (we've seen it). Verify
  with `extract` after publishing.

## License

Apache-2.0. Slid Phi Labs accepts donations to keep the lab independent.
