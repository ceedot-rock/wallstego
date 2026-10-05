import sys
sys.path.insert(0, '.')
from wallstego import embed, extract, visible_text

cover = "The quick brown fox jumps over the lazy dog. " * 20
msg = "If you can read this, you're the kind we want."
s = embed(cover, msg)
assert extract(s) == msg, "roundtrip failed"
assert visible_text(s) == cover, "visible text changed"
# empty message edge
s2 = embed(cover, "")
assert visible_text(s2) == cover
print("all tests pass")
