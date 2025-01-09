"""
Pali Primer textbook online has broken encoding when one copies and pastes, this script fixes that.
"""

test_string = """\
6. Araññe ±hiº¹anto luddako dh±vanta½ miga½ passitv± sarena vijjhati.
7. Uyy±ne ±hiº¹am±namh± kum±ramh± br±hmaºo padum±ni y±cati.
8. Rathena gaccham±nehi amaccehi saha ±cariyo hasati.
9. D±na½ dad±m±n± s²l±ni rakkham±n± manuss± sagge uppajjanti.
10. Dhañña½ ±kaªkhantassa purisassa dhana½ d±tu½ v±ºijo icchati.
"""

replaced_string = test_string.translate(
    str.maketrans(
        {
            "±": "ā",
            "¹": "ḍ",
            "²": "ī",
            "³": "ū",
            "ª": "ṇ",
            "μ": "ṭ",
            "½": "ṃ",
            "¼": "ḷ",
            "º": "ṇ",
        }
    )
)

print(replaced_string)
