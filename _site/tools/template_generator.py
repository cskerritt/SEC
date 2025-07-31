import json
import logging
import html
from pathlib import Path

LOGGER = logging.getLogger(__name__)


def load_template(template_path: Path) -> str:
    """Load the HTML template from a file."""
    try:
        with open(template_path, "r", encoding="utf-8") as f:
            return f.read()
    except OSError as exc:
        LOGGER.error("Failed to read template %s: %s", template_path, exc)
        raise

def build_list(items, tag="li"):
    """Return HTML list items with escaped content."""
    return "\n".join(
        f"        <{tag}>{html.escape(str(item))}</{tag}>" for item in items
    )


def generate_pages(
    json_path: str | Path = "city_data.json",
    output_dir: Path = Path("locations/cities"),
    template_path: Path = Path(__file__).parent / "templates" / "city_template.html",
):
    """Generate city HTML pages from JSON data."""
    try:
        with open(json_path, "r", encoding="utf-8") as f:
            data = json.load(f)
    except FileNotFoundError:
        LOGGER.error("JSON file not found: %s", json_path)
        return
    except json.JSONDecodeError as exc:
        LOGGER.error("Failed to parse JSON %s: %s", json_path, exc)
        return

    template = load_template(template_path)

    output_dir = Path(output_dir)
    output_dir.mkdir(parents=True, exist_ok=True)

    for city_key, info in data.items():
        if not isinstance(info, dict):
            LOGGER.warning("Skipping malformed city entry for %s", city_key)
            continue

        courts = build_list(
            [
                f"<strong>{c.get('name', 'Unknown')}</strong> - {c.get('description', '')}"
                for c in info.get("courts", [])
                if isinstance(c, dict)
            ]
        )
        industries = build_list(info.get("industries", []))
        services = build_list(info.get("service_areas", []))

        html = template.format(
            filename=info.get("filename", f"{city_key}.html"),
            city_slug=info.get("city_slug", city_key),
            city_display=info.get("city_display", city_key.title()),
            state_abbrev=info.get("state_abbrev", ""),
            court_items=courts,
            industry_items=industries,
            service_items=services,
        )

        outfile = output_dir / info.get("filename", f"{city_key}.html")
        try:
            with open(outfile, "w", encoding="utf-8") as f_out:
                f_out.write(html)
        except OSError as exc:
            LOGGER.error("Failed to write %s: %s", outfile, exc)
            continue
        LOGGER.info("Generated %s", outfile)

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    generate_pages()
