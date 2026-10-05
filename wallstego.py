#!/usr/bin/env python3
"""wallstego: hide real messages inside regular text via zero-width characters.
ZWSP (U+200B) = 0, ZWNJ (U+200C) = 1, ZWJ (U+200D) = end-of-message marker.
Visible text is untouched; the payload rides between words.
"""
import sys

ZWSP = "\u200b"  # 0
ZWNJ = "\u200c"  # 1
ZWJ = "\u200d"   # terminator
ALPHABET = {ZWSP, ZWNJ, ZWJ}


def embed(cover: str, message: str) -> str:
    data = message.encode("utf-8")
    bits = "".join(f"{b:08b}" for b in data)
    payload = "".join(ZWSP if bit == "0" else ZWNJ for bit in bits) + ZWJ
    words = cover.split(" ")
    # spread payload evenly across word gaps; payload rides glued to the
    # preceding word so no visible spacing changes
    gaps = len(words) - 1
    if gaps < 1:
        return cover + payload
    per_gap, rem = divmod(len(payload), gaps)
    parts = []
    idx = 0
    for i, w in enumerate(words):
        parts.append(w)
        if i < gaps:
            take = per_gap + (1 if (i + 1) <= rem else 0)
            parts.append(payload[idx:idx + take])
            idx += take
        if i < gaps:
            parts.append(" ")
    return "".join(parts)


def extract(stego: str) -> str:
    seq = "".join(c for c in stego if c in ALPHABET)
    # cut at first terminator
    if ZWJ in seq:
        seq = seq[:seq.index(ZWJ)]
    bits = "".join("0" if c == ZWSP else "1" for c in seq)
    # drop trailing partial byte
    bits = bits[: len(bits) // 8 * 8]
    data = bytes(int(bits[i:i + 8], 2) for i in range(0, len(bits), 8))
    return data.decode("utf-8")


def visible_text(stego: str) -> str:
    return "".join(c for c in stego if c not in ALPHABET)


if __name__ == "__main__":
    cmd = sys.argv[1]
    if cmd == "embed":
        cover = open(sys.argv[2]).read()
        msg = open(sys.argv[3]).read()
        sys.stdout.write(embed(cover, msg))
    elif cmd == "extract":
        sys.stdout.write(extract(open(sys.argv[2]).read()))
    elif cmd == "check":
        stego = open(sys.argv[2]).read()
        cover = open(sys.argv[3]).read()
        print("visible identical:", visible_text(stego) == cover)
