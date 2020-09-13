import fontforge

import math as math

# list of characters to use
# svg_map = [
#     "space", "exclam", "numbersign", "dollar", "percent",
#     "ampersand", "parenleft", "asterisk", "plus", "hyphen",
#     "period", "slash", "one", "two", "three",
#     "four", "five", "six", "eight", "at",
#     "A", "B", "C", "D", "E",
#     "G", "P", "T", "X", "asciicircum",
#     "grave", "b", "c", "e", "f",
#     "g", "j", "k", "l", "p",
#     "q", "r", "t", "v", "w",
#     "x", "nonbreakingspace", "exclamdown", "cent", "sterling",
#     "section", "ordmasculine", "atilde", "aring", "ccedilla",
#     "quotesinglbase", "trademark", "infinity",
# ]
svg_map = [
    "s",  # the full empty graph
    "one", "two", "three", "four", "five", "six", "seven",
    "eight", "nine", "zero", # 8va, low A, thumb catch
    "x", "p", "d",  # X, P, Eb/D#
    "f", "c", "a",  # Tf, Tc, Ta
    "q", "w", "e", "r", "t",  # C1, C2, C3, C4, C5
    "g", "b", "v", "h",  # G#, low B, C#, low Bb
    "hyphen",  # The middle line
]
font_name = "Saxy"
font_comments = "This font is useful to generate saxophone fingering diagrams."


def set_font_attributes(font):

    font.fontname = font_name
    font.familyname = font_name
    font.fullname = font_name
    font.comment = font_comments
    font.design_size = 1

def add_kerning(font):
    s_index = svg_map.index("s")

    offsets = [0] * len(svg_map) ** 2
    for index in range(len(svg_map)):
        offsets[index + len(svg_map) * index] = 400

    # for index in range(len(svg_map)):
    #     offsets[s_index * len(svg_map) + index] = 400

    # for i in range(len(svg_map_without_space)):
    #     print(offsets[len(svg_map_without_space) * i: len(svg_map_without_space) * (i + 1)])

    offsets_tuple = tuple(offsets)

    font.addLookup("kern", "gpos_pair", None, [["kern", [["latn", ["dflt"]]]]])
    #font.addLookupSubtable("kern", "kern-1")
    font.addKerningClass("kern", "kern-1", tuple(svg_map), tuple(svg_map), tuple(offsets_tuple))

if __name__ == "__main__":
    font = fontforge.font()  # new font
    for char in svg_map:
        glyph = font.createMappedChar(char)
        glyph.importOutlines('../src/' + char + '.svg')
        glyph.width = 0

    # Normal space char is to large
    glyph = font.createMappedChar("space")
    glyph.width = 400

    set_font_attributes(font)
    add_kerning(font)

    font.generate('../redist/' + font_name.lower() + '.ttf', flags=('round', 'opentype'))
    font.generate('../redist/' + font_name.lower() + '.otf', flags=('round', 'opentype'))
    font.generate('../redist/' + font_name.lower() + '.ufo', flags=('round', 'opentype'))
    font.generate('../redist/' + font_name.lower() + '.woff2', flags=('round', 'opentype'))
    font.generate('../redist/' + font_name.lower() + '.woff', flags=('round', 'opentype'))

    font.close()
