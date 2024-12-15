"""
This script converts translated .txt files into JSON files that can be used by hh-suttas or suttacentral websites.
"""

import json
import re


def extract_segments_to_dict(text, prefix, sutta):
    """
    Extracts segments from text based on a given prefix and sutta identifier.

    Args:
        text (str): The input text to extract segments from.
        prefix (str): The prefix indicating the type of content (e.g., 'EN').
        sutta (str): The sutta identifier to prepend to segment numbers.

    Returns:
        dict: A dictionary mapping segment numbers to their content.
    """
    pattern = rf"^{prefix} \[(.*?)\]: (.*)"
    matches = re.findall(pattern, text, re.MULTILINE)
    return {sutta + match[0]: match[1] for match in matches}


def add_trailing_whitespace(pali_json, translated_dict):
    """
    Adds trailing whitespace to translated segments if the corresponding Pali segment ends with whitespace.

    Args:
        pali_json (dict): The dictionary containing Pali segments.
        translated_dict (dict): The dictionary containing translated segments.

    Returns:
        dict: The updated translated dictionary with adjusted trailing whitespace.
    """
    for segment_num, text in pali_json.items():
        if segment_num in translated_dict and text.endswith(" "):
            translated_dict[segment_num] += " "
    return translated_dict


translation_filepath = "suttas/translation-en/mn/mn3_translation-en-f0lie.txt"
pali_filepath = "suttas/root/mn/mn3_root-pli-ms.json"

with open(pali_filepath, "r", encoding="utf-8") as f:
    pali_json = json.load(f)

with open(translation_filepath, "r", encoding="utf-8") as f:
    text = f.read()
    en_translation_dict = extract_segments_to_dict(text, "EN", "mn3:")
    en_translation_dict = add_trailing_whitespace(pali_json, en_translation_dict)
    en_comments_dict = extract_segments_to_dict(text, "EN-COMMENT", "mn3:")

translation_output_path = translation_filepath.replace(".txt", ".json")
with open(translation_output_path, "w", encoding="utf-8") as f:
    json.dump(en_translation_dict, f, indent=2)

comment_output_path = (
    translation_filepath.replace("/translation-en", "/comment")
    .replace("translation", "comment")
    .replace(".txt", ".json")
)
with open(comment_output_path, "w", encoding="utf-8") as f:
    json.dump(en_comments_dict, f, indent=2)
