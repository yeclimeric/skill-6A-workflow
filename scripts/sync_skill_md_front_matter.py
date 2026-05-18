import json
import os


def _yaml_escape(s: str) -> str:
    return (
        s.replace("\\", "\\\\")
        .replace("\"", "\\\"")
        .replace("\n", "\\n")
        .replace("\r", "\\r")
        .replace("\t", "\\t")
    )


def _yaml_scalar(v) -> str:
    if v is None:
        return "null"
    if isinstance(v, bool):
        return "true" if v else "false"
    if isinstance(v, (int, float)):
        return str(v)
    if isinstance(v, str):
        return f"\"{_yaml_escape(v)}\""
    raise TypeError(f"unsupported scalar type: {type(v)}")


def _to_yaml(obj: dict, key_order: list[str]) -> str:
    lines: list[str] = []
    for k in key_order:
        if k not in obj:
            continue
        v = obj[k]
        if isinstance(v, list):
            lines.append(f"{k}:")
            for item in v:
                lines.append(f"  - {_yaml_scalar(item)}")
            continue
        lines.append(f"{k}: {_yaml_scalar(v)}")
    return "\n".join(lines)


def main() -> None:
    repo_root = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
    metadata_path = os.path.join(repo_root, "metadata.json")
    skill_md_path = os.path.join(repo_root, "SKILL.md")

    with open(metadata_path, "r", encoding="utf-8") as f:
        metadata = json.load(f)

    key_order = [
        "name",
        "description",
        "version",
        "author",
        "tags",
        "trigger",
        "category",
        "permissions",
    ]
    yaml_body = _to_yaml(metadata, key_order).strip()
    front_matter = f"---\n{yaml_body}\n---\n\n"

    with open(skill_md_path, "r", encoding="utf-8") as f:
        skill_md = f.read()

    if skill_md.startswith("---\n"):
        parts = skill_md.split("---\n", 2)
        if len(parts) < 3:
            raise RuntimeError("INVALID_SKILL_MD_FRONT_MATTER")
        skill_md = front_matter + parts[2]
    else:
        skill_md = front_matter + skill_md

    with open(skill_md_path, "w", encoding="utf-8") as f:
        f.write(skill_md)


if __name__ == "__main__":
    main()

