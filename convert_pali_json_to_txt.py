"""
This converts the Pali json files in sutta/root/* and converts them into a format that is easier to work with while translating. This code doesn't overwrite existing translation files.
"""

import json


def format_sutta(filepath):
    """
    Reads a JSON file containing sutta data and formats it into a more readable translation format.

    Args:
        filepath (str): The path to the JSON file.

    Returns:
        str: A formatted string containing the sutta in a translation-friendly format.
    """
    with open(filepath, "r", encoding="utf-8") as f:
        data = json.load(f)

    output = ""

    for tag_segment_num, text in data.items():
        _, segment_num = tag_segment_num.split(":")
        output += f"Pali [{segment_num}]: {text}\n\n"

    return output.strip()


filepath = "suttas/root/mn/mn3_root-pli-ms.json"
if formatted_text := format_sutta(filepath):
    with open(
        filepath.replace("suttas/root/", "suttas/translation-en/").replace(
            "_root-pli-ms.json", "_translation-en-f0lie.txt"
        ),
        "x",
        encoding="utf-8",
    ) as f:
        f.write(formatted_text)
