import fontforge

import os

import generate_svgs

master_svg = "MASTER.svg"
output_dir = "generated"
template_svg = "template.svg"
master_char = "s"

extensions_to_redist = ['.ttf', '.otf', '.woff2']

# list of characters to use
svg_map = []
font_name = "Saxy"
font_comments = "This font is useful to generate saxophone fingering diagrams."
space_size = 450


def set_font_attributes(font):

    font.fontname = font_name
    font.familyname = font_name
    font.fullname = font_name
    font.comment = font_comments
    font.fontlog = font_comments
    font.design_size = 3

def add_kerning(font):
    s_index = svg_map.index(master_char)

    offsets = [0] * len(svg_map) ** 2
    for index in range(len(svg_map)):
        offsets[index + len(svg_map) * index] = space_size

    for index in range(len(svg_map)):
        offsets[index * len(svg_map) + s_index] = space_size

    # for i in range(len(svg_map_without_space)):
    #     print(offsets[len(svg_map_without_space) * i: len(svg_map_without_space) * (i + 1)])

    offsets_tuple = tuple(offsets)

    font.addLookup("kern", "gpos_pair", None, [["kern", [["latn", ["dflt"]]]]])
    #font.addLookupSubtable("kern", "kern-1")
    font.addKerningClass("kern", "kern-1", tuple(svg_map), tuple(svg_map), tuple(offsets_tuple))

if __name__ == "__main__":
    svg_map = generate_svgs.generate(master_svg, output_dir, template_svg, "", ["nine"])

    font = fontforge.font()  # new font
    for char in svg_map:
        glyph = font.createMappedChar(char)
        glyph.importOutlines(os.path.join(output_dir, char + '.svg'))
        glyph.width = 0

    # import merge char
    merge_char = font.createMappedChar(master_char)
    merge_char.importOutlines('merge.svg')
    merge_char.width = 0
    svg_map.append(master_char)

    # Normal space char is to large
    glyph = font.createMappedChar("space")
    glyph.width = space_size

    # font['.notdef'].width = 400

    set_font_attributes(font)
    add_kerning(font)

    for ext in extensions_to_redist:
        font.generate('../redist/' + font_name.lower() + ext, flags=('round', 'opentype'))

    font.close()
