"""
This converts the Pali json files in sutta/root/* and converts them into a format that is easier to work with while translating. This code doesn't overwrite existing translation files.
"""

import os
import json


def format_sutta(data: dict) -> str:
    """
    Formats sutta data from a dictionary into a more readable translation format.
    """
    output = ""

    sutta_current = ""
    for tag_segment_num, text in data.items():
        sutta, segment_num = tag_segment_num.split(":")
        if sutta_current != sutta:
            output += f"[SUTTA {sutta}]\n\n"
            sutta_current = sutta
        output += f"{text.strip()} [{segment_num}]\n\n"

    return output.strip()


def process_single_sutta_file(
    input_filepath: str, translator_prefix: str = "_translation-en"
) -> None:
    """
    Processes a single JSON file representing a sutta and creates a corresponding
    translation file.
    """
    # Construct the output filepath
    relative_path = os.path.relpath(input_filepath, "suttas/root/")
    output_filepath = os.path.join(
        "suttas/translation-en/",
        relative_path.replace("_root-pli-ms.json", f"{translator_prefix}.txt"),
    )

    # Skip if the output file already exists
    if os.path.exists(output_filepath):
        print(f"Skipping {input_filepath} as output file already exists.")
        return

    with open(input_filepath, "r", encoding="utf-8") as f:
        data = json.load(f)

    if formatted_text := format_sutta(data):
        os.makedirs(os.path.dirname(output_filepath), exist_ok=True)
        with open(output_filepath, "w", encoding="utf-8") as f:
            f.write(formatted_text)
        print(f"Processed {input_filepath}")


def process_sutta_directory(
    root_directory: str, translator_prefix: str = "_translation-en"
) -> None:
    """
    Processes all JSON files within a directory representing a collection of suttas
    and creates corresponding translation files.

    Args:
        root_directory: The root directory containing the sutta JSON files.
        translator_prefix: The prefix to use for the output filenames
                           (e.g., "_translation-en-f0lie").
    """
    for root, _, files in os.walk(root_directory):
        for filename in sorted(files):
            if filename.endswith("_root-pli-ms.json"):
                filepath = os.path.join(root, filename)
                process_single_sutta_file(filepath, translator_prefix)


root_directory = "suttas/root/"
translator_prefix = "_translation-en-f0lie"

# Process a single file
# input_file = "suttas/root/mn/mn1_root-pli-ms.json"
# process_single_sutta_file(input_file, translator_prefix)

process_sutta_directory(root_directory, translator_prefix)
