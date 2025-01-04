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


def parse_translation_doc(filepath: str) -> tuple[dict[str, str], dict[str, str]]:
    """
    Parse translation file format into json files.
    """
    translation_data = {}
    comment_data = {}
    current_sutta = ""

    with open(filepath, "r", encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            # Parse SUTTA name
            if match := re.match(r"\[SUTTA (.*?)\]", line):
                current_sutta = match.group(1)
            # Parse English lines
            elif match := re.match(r"\[E (\d+(?:\.\d+)?)\] (.*)", line):
                key = f"{current_sutta}:{match.group(1)}"
                translation_data[key] = match.group(2)
            # Parse comments
            elif match := re.match(r"\[C (\d+(?:\.\d+)?)\] (.*)", line):
                key = f"{current_sutta}:{match.group(1)}"
                comment_data[key] = match.group(2)

    return translation_data, comment_data


def add_trailing_whitespace(pali_json: dict[str, str], translated_dict: dict[str, str]):
    """
    Adds trailing whitespace to translated segments if the corresponding Pali segment ends with whitespace.
    """
    for segment_num, text in pali_json.items():
        if segment_num in translated_dict and text.endswith(" "):
            translated_dict[segment_num] += " "


translation_filepath = "suttas/translation-en/mn/mn3_translation-en-f0lie.txt"
pali_filepath = find_pali_filepath(translation_filepath)

with open(pali_filepath, "r", encoding="utf-8") as f:
    pali_json = json.load(f)

translation_dict, comments_dict = parse_translation_doc(translation_filepath)
add_trailing_whitespace(pali_json, translation_dict)

translation_output_path = translation_filepath.replace(".txt", ".json")
with open(translation_output_path, "w", encoding="utf-8") as f:
    json.dump(translation_dict, f, indent=2, ensure_ascii=False)

comment_output_path = (
    translation_filepath.replace("/translation-en", "/comment")
    .replace("translation", "comment")
    .replace(".txt", ".json")
)
with open(comment_output_path, "w", encoding="utf-8") as f:
    json.dump(comments_dict, f, indent=2, ensure_ascii=False)
