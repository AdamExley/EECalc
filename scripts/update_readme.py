from pathlib import Path
import re

ROOT = Path(__file__).resolve().parents[1]
README_PATH = ROOT / "README.md"
PLANNING_OVERVIEW_PATH = ROOT / "docs" / "planning" / "Planning Overview.md"

START_PLANNED_FEATURES_REGEX = r"(?s).*?<!-- START-PLANNED-FEATURES -->\n"
END_PLANNED_FEATURES_REGEX = r"(?s)\n<!-- END-PLANNED-FEATURES -->.*"


def find_regex(content: str, regex: str) -> str | None:
    match = re.search(regex, content, re.DOTALL)
    if match:
        return match.group(0)
    return None


def get_pre_post_content(
    content: str, start_regex: str, end_regex: str, src_path: Path | None = None
) -> tuple[str, str]:

    # If src is provided, use it in error messages, otherwise use a generic name
    src: str | Path = src_path if src_path else "content"

    ## Find the start regex
    start_text = find_regex(content, start_regex)
    if start_text is None:  # Not found
        raise ValueError(f"Start regex '{start_regex}' not found in {src}")

    ## Find the end regex
    end_text = find_regex(content, end_regex)
    if end_text is None:  # Not found
        raise ValueError(f"End regex '{end_regex}' not found in {src}")

    ## Make sure the end regex comes after the start regex
    if find_regex(end_text, start_regex) is not None:
        raise ValueError(f"End regex '{end_regex}' found before start regex in {src}")

    return start_text, end_text


def get_subset(src: Path, start_regex: str, end_regex: str):
    # Get file content
    content = src.read_text().strip()

    # Get the start and end text via regex
    start_text, end_text = get_pre_post_content(content, start_regex, end_regex, src)

    ## Extract the text between the regexes via string indices
    start_index = content.find(start_text) + len(start_text)
    end_index = content.find(end_text, start_index)

    return content[start_index:end_index]


def get_planned_features_text() -> str:
    return get_subset(
        PLANNING_OVERVIEW_PATH,
        START_PLANNED_FEATURES_REGEX,
        END_PLANNED_FEATURES_REGEX,
    )


def inject_section(
    dst: Path, content_inject: str, start_regex: str, end_regex: str
) -> None:

    # Get file content
    content = dst.read_text().strip()

    # Get the start and end text via regex
    start_text, end_text = get_pre_post_content(content, start_regex, end_regex, dst)

    # Combine the parts with the new content
    new_content = start_text + content_inject + end_text

    # Write the new content back to the file
    dst.write_text(new_content)


def main() -> None:

    inject_section(
        README_PATH,
        get_planned_features_text(),
        START_PLANNED_FEATURES_REGEX,
        END_PLANNED_FEATURES_REGEX,
    )


if __name__ == "__main__":
    main()
