# Isomorphic Strings — Quick Revision

- **Pattern:** Two-way hash mapping
- **Recognition clue:** Characters must follow the same one-to-one replacement pattern.
- **Forward map:** `s` character → `t` character
- **Reverse map:** `t` character → `s` character
- **Forward conflict:** One source character tries to map to a different target.
- **Reverse conflict:** Two source characters try to share one target.
- **Pairing:** Use `zip(s, t)`.
- **Time:** `O(n)`
- **Extra space:** `O(n)`
- **Common mistake:** Using only one mapping direction.
- **Memory sentence:** Every character needs one partner, and that partner belongs only to it.
