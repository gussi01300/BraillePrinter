BRAILLE_MAP = {
    ' ': {'unicode':'U+2800','dot_position_code':'000000'},
    'a': {'unicode':'U+2801','dot_position_code':'100000'},
    'b': {'unicode':'U+2803','dot_position_code':'110000'},
    'c': {'unicode':'U+2809','dot_position_code':'100100'},
    'd': {'unicode':'U+2819','dot_position_code':'100110'},
    'e': {'unicode':'U+2811','dot_position_code':'100010'},
    'f': {'unicode':'U+280B','dot_position_code':'110100'},
    'g': {'unicode':'U+281B','dot_position_code':'110110'},
    'h': {'unicode':'U+2813','dot_position_code':'110010'},
    'i': {'unicode':'U+280A','dot_position_code':'010100'},
    'j': {'unicode':'U+281A','dot_position_code':'010110'},
    'k': {'unicode':'U+2805','dot_position_code':'101000'},
    'l': {'unicode':'U+2807','dot_position_code':'111000'},
    'm': {'unicode':'U+280D','dot_position_code':'101100'},
    'n': {'unicode':'U+281D','dot_position_code':'101110'},
    'o': {'unicode':'U+2815','dot_position_code':'101010'},
    'p': {'unicode':'U+280F','dot_position_code':'111100'},
    'q': {'unicode':'U+281F','dot_position_code':'111110'},
    'r': {'unicode':'U+2817','dot_position_code':'111010'},
    's': {'unicode':'U+280E','dot_position_code':'011100'},
    't': {'unicode':'U+281E','dot_position_code':'011110'},
    'u': {'unicode':'U+2825','dot_position_code':'101001'},
    'v': {'unicode':'U+2827','dot_position_code':'111001'},
    'w': {'unicode':'U+283A','dot_position_code':'010111'},
    'x': {'unicode':'U+282D','dot_position_code':'101101'},
    'y': {'unicode':'U+283D','dot_position_code':'101111'},
    'z': {'unicode':'U+2835','dot_position_code':'101011'}
}

def unicode2char(uni):
    return chr(int(uni.replace('U+',''),16))

def unicode2dot_position_code(uni):
    return bin(int(uni.replace('U+',''),16) - 0x2800)[2:].zfill(6)


txt = "The quick brown fox jumps over the lazy dog"
braille = ""
for i in range(0,len(txt)):
    print(unicode2dot_position_code(BRAILLE_MAP[txt[i].lower()]['unicode']))
    braille = braille + unicode2char(BRAILLE_MAP[txt[i].lower()]['unicode'])

print(braille)