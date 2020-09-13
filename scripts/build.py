import fontforge

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
    "s", # the full empty graph
    "one", "two", "three", "four", "five", "six", "seven", "eight",
    "x", "p", "d", #X, P, Eb/D#
    "f", "c", "a", # Tf, Tc, Ta
    "q", "w", "e", "r", "t", #C1, C2, C3, C4, C5
    "g", "b", "v", "h", #G#, low B, C#, low Bb
    "hyphen", # The middle line
]

font_name = "Saxy"

if __name__ == "__main__":
    font = fontforge.font() # new font
    for char in svg_map:
        glyph = font.createMappedChar(char)
        glyph.importOutlines('../src/' + char + '.svg')
        glyph.width = 0

    #font['space'].width = 400
    font.fontname = font_name
    font.generate('../src/concat/' + font_name.lower() + '.ttf')
    font.generate('../src/concat/' + font_name.lower() + '.otf')
