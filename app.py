#   Importing responsories
import sys
from pyfiglet import Figlet, FontNotFound


def main():

    #   Initalizing command-line arguments
    arg = ['-f', '--font', '-h', '--help']

    fonts = [
        #   Available fonts
        #   Adopted from : http://www.figlet.org/fontdb.cgi
        "3-d", "3x5", "5lineoblique", "acrobatic", "alligator", "alligator2",
        "alphabet", "avatar", "banner", "banner3-D", "banner3", "banner4",
        "barbwire", "basic", "bell", "big", "bigchief", "binary",
        "block", "bubble", "bulbhead", "calgphy2", "caligraphy", "catwalk",
        "chunky", "coinstak", "colossal", "computer", "contessa", "contrast",
        "cosmic", "cosmike", "cricket", "cursive", "cyberlarge", "cybermedium",
        "cybersmall", "diamond", "digital", "doh", "doom", "dotmatrix",
        "drpepper", "eftichess", "eftifont", "eftipiti", "eftirobot", "eftitalic",
        "eftiwall", "eftiwater", "epic", "fender", "fourtops", "fuzzy",
        "goofy", "gothic", "graffiti", "hollywood", "invita", "isometric1",
        "isometric2", "isometric3", "isometric4", "italic", "ivrit", "jazmine",
        "jerusalem", "katakana", "kban", "larry3d", "lcd", "lean",
        "letters", "linux", "lockergnome", "madrid", "marquee", "maxfour",
        "mike", "mini", "mirror", "mnemonic", "morse", "moscow",
        "nancyj-fancy", "nancyj-underlined", "nancyj", "nipples", "ntgreek", "o8",
        "ogre", "pawp", "peaks", "pebbles", "pepper", "poison",
        "puffy", "pyramid", "rectangles", "relief", "relief2", "rev",
        "roman", "rot13", "rounded", "rowancap", "rozzo", "runic",
        "runyc", "sblood", "script", "serifcap", "shadow", "short",
        "slant", "slide", "slscript", "small", "smisome1", "smkeyboard",
        "smscript", "smshadow", "smslant", "smtengwar", "speed", "stampatello",
        "standard", "starwars", "stellar", "stop", "straight", "tanja",
        "tengwar", "term", "thick", "thin", "threepoint", "ticks",
        "ticksslant", "tinker-toy", "tombstone", "trek", "tsalagi", "twopoint",
        "univers", "usaflag", "wavy", "weird"]

    if "-h" in sys.argv[1] or "--help" in sys.argv[1]:

        print("Available fonts :")

        for i in fonts:
            print(i)
    try:

        #   Ensure the command-line arguments does not exceed 3 arguments
        if len(sys.argv) > 3:
            raise Exception('To many command-line arguments')

        #   Ensure the command-line command exsists
        if sys.argv[1] not in arg:
            raise Exception("Command not found python app.py")


        #   Ensure the font exists
        if not Figlet(font=str(sys.argv[2])):
            raise FontNotFound("Font not available -h or --help for available fonts")

    except (FontNotFound, ValueError, Exception) as e:

        sys.exit(
            f"Error : {e}\nUSEAGE : python pyfiglet.py [Optional : -f / --fonts] [Optional : font name]")

    #   Initializing a prompt
    prompt = input('Type a text:')

    #   Ensure the command-line arguments equals 1
    if len(sys.argv) == 1:

        print(Figlet().renderText(prompt))

    print(Figlet(font=str(sys.argv[2])).renderText(prompt))
    sys.exit()

if __name__ == '__main__':
    main()
