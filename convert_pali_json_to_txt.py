"""
This converts the Pali json files in sutta/root/* and converts them into a format that is easier to work with while translating. This code doesn't overwrite existing translation files.
"""

import os
import json


def format_sutta(filepath: str) -> str:
    """
    Reads a JSON file containing sutta data and formats it into a more readable translation format.
    """
    with open(filepath, "r", encoding="utf-8") as f:
        data = json.load(f)

    output = ""

    sutta_current = ""
    for tag_segment_num, text in data.items():
        sutta, segment_num = tag_segment_num.split(":")
        if sutta_current != sutta:
            output += f"SUTTA: {sutta}\n\n"
            sutta_current = sutta
        output += f"PLI [{segment_num}]: {text}\n\n"

    return output.strip()


filepath = "suttas/root/kn/dhp/dhp1-20_root-pli-ms.json"
if formatted_text := format_sutta(filepath):
    output_filepath = filepath.replace(
        "suttas/root/", "suttas/translation-en/"
    ).replace("_root-pli-ms.json", "_translation-en-f0lie.txt")
    os.makedirs(os.path.dirname(output_filepath), exist_ok=True)
    with open(output_filepath, "x", encoding="utf-8") as f:
        f.write(formatted_text)
