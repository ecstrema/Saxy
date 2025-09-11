![Preview of Saxy](demo_Saxy.svg?raw=true)

# Saxy

Saxy is a font for music notation of Saxophone fingerings (tablatures).

## Demo

[See it in action here](https://ecstrema.github.io/Saxy/)

## Downloading and installing

You can download Saxy from the redist folder and follow the standard procedures for installing and selecting fonts on your system.

## Requirements

This font should work in any program that handles fonts reasonably. However, some programs, like Microsoft Word, seem not to like it. It works fine in LibreOffice Writer, on the web, and in MuseScore.

# Usage

The tablature system used in this font has been based upon that outlined
by Jean-Marie Londeix in his book, "HELLO!  Mr. SAX".

Each character maps to a specific key:

 - s (stands for sax)  : The full empty graph
 - 1, 2, 3, 4, 5, 6, 7 : The center keys, 7 being the low C
 - 8, 9, 0             : 8va, low A, thumb catch
 - x, p, d             : X, P, Eb/D#
 - f, c, a             : Tf, Tc, Ta
 - q, w, e, r, t       : C1, C2, C3, C4, C5
 - g, b, v, h          : G#, low B, C#, low Bb
 - "-" (hyphen)        : The middle line


## Things and Thongs using this font

The Musescore Plugin [saxophone-fingerings](https://github.com/Marr11317/saxophone-fingerings) uses this font.

## Contributing

Contributions are welcome.

The fonts are built using [FontForge](https://fontforge.org/)'s python scripting interface. To build the font, first install FontForge, then run ffpython located in your FontForge installation directory, and run:

```bash
cd src
ffpython build.py
```

## License

This font is licensed under the SIL Open Font License, Version 1.1.
