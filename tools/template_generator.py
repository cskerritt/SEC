import json
import os
from pathlib import Path

TEMPLATE = """<!DOCTYPE html>
<html lang=\"en\">
<head>
    <meta charset=\"UTF-8\">
    <meta name=\"viewport\" content=\"width=device-width, initial-scale=1.0\">
    <title>{city_display} Forensic Economist | {state_abbrev} Economic Damage Expert | Court-Qualified | Skerritt Economics</title>
    <meta name=\"description\" content=\"Leading forensic economist in {city_display}. Expert economic damage analysis, business valuations, and litigation support for {city_display} attorneys. Court-qualified expert witness with extensive federal and state court experience.\">
    <meta name=\"keywords\" content=\"forensic economist {city_slug}, forensic economist {state_abbrev}, economic damage expert {city_slug}, business valuation {city_display}, expert witness economist, litigation support {city_slug}\">
    <link rel=\"icon\" type=\"image/x-icon\" href=\"../../favicon.ico\">
    <link rel=\"canonical\" href=\"https://skerritteconomics.com/locations/cities/{filename}\">
    <meta property=\"og:title\" content=\"{city_display} Forensic Economist | {state_abbrev} Economic Damage Expert | Skerritt Economics\">
    <meta property=\"og:description\" content=\"Leading forensic economist in {city_display}. Expert economic damage analysis for attorneys.\">
    <meta property=\"og:url\" content=\"https://skerritteconomics.com/locations/cities/{filename}\">
    <meta property=\"og:type\" content=\"website\">
    <meta property=\"og:locale\" content=\"en_US\">
    <meta name=\"twitter:card\" content=\"summary_large_image\">
    <meta name=\"geo.region\" content=\"US-{state_abbrev}\">
    <meta name=\"geo.placename\" content=\"{city_display}\">

    <link rel=\"stylesheet\" href=\"../../css/styles.css\">
    <link rel=\"stylesheet\" href=\"../../css/locations.css\">
</head>
<body>
    <h1>{city_display} Forensic Economist</h1>
    <p>Professional forensic economic services in {city_display}, {state_abbrev}. Serving law firms with detailed economic damage analysis and business valuation.</p>

    <h2>Court Experience</h2>
    <ul>
{court_items}
    </ul>

    <h2>Industries Served</h2>
    <ul>
{industry_items}
    </ul>

    <h2>Service Areas</h2>
    <ul>
{service_items}
    </ul>
</body>
</html>"""

def build_list(items, tag="li"):    
    return "\n".join(f"        <{tag}>{item}</{tag}>" for item in items)


def generate_pages(json_path="city_data.json", output_dir=Path("locations/cities")):
    with open(json_path, "r", encoding="utf-8") as f:
        data = json.load(f)

    output_dir = Path(output_dir)
    output_dir.mkdir(parents=True, exist_ok=True)

    for city_key, info in data.items():
        courts = build_list([f"<strong>{c['name']}</strong> - {c['description']}" for c in info.get('courts', [])])
        industries = build_list(info.get('industries', []))
        services = build_list(info.get('service_areas', []))

        html = TEMPLATE.format(
            filename=info['filename'],
            city_slug=info['city_slug'],
            city_display=info['city_display'],
            state_abbrev=info['state_abbrev'],
            court_items=courts,
            industry_items=industries,
            service_items=services,
        )

        outfile = output_dir / info['filename']
        with open(outfile, 'w', encoding='utf-8') as f_out:
            f_out.write(html)
        print(f"Generated {outfile}")

if __name__ == "__main__":
    generate_pages()
