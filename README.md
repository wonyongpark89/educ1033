# EDUC1033 lecture decks

Slide decks for EDUC1033, served with GitHub Pages.

| Week | Topic | Deck | PDF |
|---|---|---|---|
| 9 | The teaching profession under pressure | [w9/](https://www.wonyongpark.com/educ1033/w9/) | [PDF](w9/EDUC1033-W9-Teaching-profession-slides.pdf) |

## Editing a deck

Each week's source lives in `<week>/src/deck.html`, with images in `<week>/src/img/`.
Build the self-contained `index.html` (images inlined, slides numbered) with:

```
python tools/build.py w9
```

In the deck: arrow keys, Space or click to move; F full screen; O overview; S speaker notes.
