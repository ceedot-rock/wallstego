# Security Policy

wallstego is a steganography tool, not encryption. That framing matters for
what counts as a security issue here: a defect that silently corrupts the
payload, leaks payload bits into the visible text, or breaks the
embed/extract roundtrip can destroy messages people rely on carrying.

## Reporting a vulnerability

Please do not open a public issue for security problems.

- Email: corey@slidphilabs.com with the subject line `wallstego security`
- Or use GitHub's private vulnerability reporting on this repository
  (Security tab, "Report a vulnerability")

Include the affected file or function, steps or inputs to reproduce, and what
you expected versus what happened.

You can expect an acknowledgement within 3 business days. We will keep you
updated while we investigate and credit you unless you prefer to stay
anonymous.

## In scope

- Payload corruption: `extract(embed(cover, msg)) != msg` for any input
- Visible-text leakage: stego output whose `visible_text` differs from the
  original cover, or zero-width characters appearing outside the payload
- Terminator confusion: messages that decode past the U+200D terminator or
  truncate early
- The `wallstego.py` CLI's file handling (path traversal, silent overwrites)

## Not a vulnerability

- A knowledgeable reader finding the hidden payload. The README says it
  plainly: this is obscurity, not encryption. Encrypt first if the content
  must stay secret.
- A platform stripping zero-width characters on save. That's documented;
  verify with `extract` after publishing.

## Out of scope

- Social engineering, spam, or denial-of-service against any demo
