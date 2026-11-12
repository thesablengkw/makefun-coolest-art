# Eruption at Dawn — make.fun coolest-art-01 entry

A volcanic island erupts at dawn beneath a huge vermilion sun: golden smoke
ribbons curl into a teal sky, a flight of cranes crosses the sun disc, and
ukiyo-e waves roll in the foreground. The style blends Japanese woodblock
print shapes with modern luminous digital painting — one bold composition
that reads instantly, even at thumbnail size.

## How it runs

`main.py` (Python 3, standard library only) copies the artwork file
`art.jpg` byte-for-byte to the output:

- to `$MAKEFUN_OUTPUT_DIR/entry.png` when that variable is set, or
- to `/output/entry.png` otherwise.

The copy is exact and deterministic: repeated runs write identical bytes.

Run it locally:

```sh
mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py
```

## Gate compliance

- JPEG bytes in a file named `entry.png`, as the rules allow
  (the format is told apart by its first bytes).
- 1024 × 1024 pixels (limit: 1024 × 1024).
- 411,590 bytes (limit: 1,048,576 bytes / 1 MiB).
- A complete, valid image produced by Pillow's encoder.

## Files

- `main.py` — the entry program.
- `art.jpg` — the artwork it publishes.
- `LICENSE` — MIT.
