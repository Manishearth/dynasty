"""Single source for the piece glyphs (10x10 viewBox).

Realia paths match the ones the playthrough page draws inline.
`python3 tools/glyphs.py` writes one standalone SVG per piece into images/.
"""
import os

WALNUT, SLATE = "#6E4A2C", "#3D5568"

GLYPHS = {
    # realia: turned walnut pieces
    "customs-house":    ("Customs House", WALNUT, "M1 9h8V6L5 3.6 1 6z"),
    "land-deed-scroll": ("Land Deed Scroll", WALNUT, "M1.4 4.2h1.2v3.4H1.4zM7.4 4.2h1.2v3.4H7.4zM2.8 5.3h4.4v1.2H2.8z"),
    "bamboo-brush":     ("Bamboo Brush", WALNUT, "M1.2 5.2h4.6v1.6H1.2zM5.8 4.4L9 5.9 5.8 7.4z"),
    "dragon-jar":       ("Dragon Jar", WALNUT, "M2.4 3.2h5.2v5.4H2.4z"),
    "wooden-bowl":      ("Wooden Bowl", WALNUT, "M1.4 4.4h7.2L6.6 8.6H3.4z"),
    "vase":             ("Vase", WALNUT, "M5 2.6c2.4 1.2 3 3 2 4.6-.7 1.2-3.3 1.2-4 0-1-1.6-.4-3.4 2-4.6z"),
    # public works
    "great-wall":    ("Great Wall link", SLATE,
                      "M1.2 3.4h1.6v1.4h1.4V3.4h1.6v1.4h1.4V3.4h1.6V8.8H1.2z"),
    "grand-canal":   ("Grand Canal section", SLATE,
                      "M.8 2.4h8.4v1.5H.8zM.8 8.1h8.4v1.5H.8zM1.3 5.9c1.2-1 2.4-1 3.7 0s2.5 1 3.7 0v1.3c-1.2 1-2.5 1-3.7 0s-2.5-1-3.7 0z"),
    "summer-palace": ("Summer Palace", SLATE,
                      "M.6 4.8C2.6 4.6 3.9 3.6 5 2.2c1.1 1.4 2.4 2.4 4.4 2.6l-.9.9h-7zM2.2 5.9h5.6v3.2H5.8V7.2H4.2v1.9H2.2z"),
    "winter-palace": ("Winter Palace", SLATE,
                      "M2 3.6C3.4 3.4 4.3 2.6 5 1.6c.7 1 1.6 1.8 3 2l-.6.7H2.6zM3.4 4.4h3.2v1H3.4z"
                      "M.6 6.2c1.8-.2 3-.6 4.4-1.1 1.4.5 2.6.9 4.4 1.1l-.8.8H1.4zM1.8 7.1h6.4v2H5.7V8H4.3v1.1H1.8z"),
    "marble-pagoda": ("Marble Pagoda", SLATE,
                      "M4.75.5h.5v1.3h-.5zM3.2 2.7 5 1.7l1.8 1zM4 2.7h2v1H4zM2.6 4.5 5 3.6l2.4.9zM3.6 4.5h2.8v1.1H3.6z"
                      "M1.9 6.5 5 5.5l3.1 1zM3 6.5h4v2.6H3zM2.2 9.1h5.6v.6H2.2z"),
    "irrigation":    ("Irrigation System", SLATE,
                      "M5 1c1.3 1.7 1.9 2.7 1.9 3.4a1.9 1.9 0 0 1-3.8 0C3.1 3.7 3.7 2.7 5 1zM1 7h8v.9H1zM1 8.6h8v.9H1z"),
    "reservoir":     ("Reservoir", SLATE,
                      "M.8 9.2 2.4 1.8h1.5v7.4zM4.6 3.4h4.6v5.8H4.6zM5.2 5c.6-.6 1.2-.6 1.8 0s1.2.6 1.8 0v.9c-.6.6-1.2.6-1.8 0s-1.2-.6-1.8 0zM5.2 7.1c.6-.6 1.2-.6 1.8 0s1.2.6 1.8 0V8c-.6.6-1.2.6-1.8 0s-1.2-.6-1.8 0z"),
}


def svg(key):
    name, color, d = GLYPHS[key]
    return (f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 10 10" width="40" height="40">'
            f'<title>{name}</title><path fill="{color}" fill-rule="evenodd" d="{d}"/></svg>\n')


if __name__ == "__main__":
    out = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "images")
    os.makedirs(out, exist_ok=True)
    for k in GLYPHS:
        with open(os.path.join(out, k + ".svg"), "w", encoding="utf-8", newline="\n") as f:
            f.write(svg(k))
    print(sorted(os.listdir(out)))
