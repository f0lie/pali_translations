"""
This script converts translated .txt files into JSON files that can be used by hh-suttas or suttacentral websites.
"""

import json
import re
import os


def find_pali_filepath(translation_filepath: str, root_dir: str = "suttas/root") -> str:
    """
    Finds the corresponding Pali filepath based on the translation filepath.
    """
    translation_filepath = translation_filepath.replace("\\", "/").replace("//", "/")

    match = re.search(r"suttas/translation-en/(.+?)/(.+?)_", translation_filepath)
    if not match:
        raise ValueError(
            f"Could not extract common part from translation filepath: {translation_filepath}"
        )
    common_part = match.group(1) + os.sep + match.group(2)

    for dirpath, dirnames, filenames in os.walk(root_dir):
        for filename in filenames:
            joined_path = os.path.join(dirpath, filename)
            normalized_path = os.path.normpath(joined_path)

            if common_part in normalized_path and filename.endswith(".json"):
                return normalized_path

    raise ValueError(f"No matching Pali file found for: {translation_filepath}")


def extract_segments_to_dict(text: list[str], filter: str) -> dict[str, str]:
    """
    Extracts segments from text based on a given filter.
    """
    current_sutta = ""
    output_dict = {}
    filter_pattern = rf"^{filter} \[(.*?)\]: (.*)"

    for line in text:
        if line.startswith("SUTTA:"):
            current_sutta = line.split(": ")[1].strip()
        if matched := re.match(filter_pattern, line):
            section_number = matched.group(1)
            text = matched.group(2)
            output_dict[current_sutta + ":" + section_number] = text

    return output_dict


def add_trailing_whitespace(
    pali_json: dict[str, str], translated_dict: dict[str, str]
) -> dict[str, str]:
    """
    Adds trailing whitespace to translated segments if the corresponding Pali segment ends with whitespace.
    """
    new_translated_dict = translated_dict.copy()
    for segment_num, text in pali_json.items():
        if segment_num in new_translated_dict and text.endswith(" "):
            new_translated_dict[segment_num] += " "
    return new_translated_dict


translation_filepath = "suttas/translation-en/mn/mn3_translation-en-f0lie.txt"
pali_filepath = find_pali_filepath(translation_filepath)

with open(pali_filepath, "r", encoding="utf-8") as f:
    pali_json = json.load(f)

with open(translation_filepath, "r", encoding="utf-8") as f:
    lines = f.readlines()
    en_translation_dict = extract_segments_to_dict(lines, "EN")
    en_translation_dict = add_trailing_whitespace(pali_json, en_translation_dict)
    en_comments_dict = extract_segments_to_dict(lines, "EN-COMMENT")

translation_output_path = translation_filepath.replace(".txt", ".json")
with open(translation_output_path, "w", encoding="utf-8") as f:
    json.dump(en_translation_dict, f, indent=2, ensure_ascii=False)

comment_output_path = (
    translation_filepath.replace("/translation-en", "/comment")
    .replace("translation", "comment")
    .replace(".txt", ".json")
)
with open(comment_output_path, "w", encoding="utf-8") as f:
    json.dump(en_comments_dict, f, indent=2, ensure_ascii=False)
