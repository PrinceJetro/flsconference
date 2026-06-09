from pathlib import Path
import re

replacements = {
    'href="unilag logo.png"': 'href="{% static \'images/unilag logo.png\' %}"',
    'src="unilag logo.png"': 'src="{% static \'images/unilag logo.png\' %}"',
    'src="./unilag logo.png"': 'src="{% static \'images/unilag logo.png\' %}"',
    'src="Faculty of life science building.png"': 'src="{% static \'images/Faculty of life science building.png\' %}"',
    'src="commissioner.jpg"': 'src="{% static \'images/commissioner.jpg\' %}"',
    'src="dean_headshot.jpg"': 'src="{% static \'images/dean_headshot.jpg\' %}"',
    'src="dean_headshot.png"': 'src="{% static \'images/dean_headshot.png\' %}"',
    'src="folawiyo.png"': 'src="{% static \'images/folawiyo.png\' %}"',
    'src="call_for_abstract.jpeg"': 'src="{% static \'images/call_for_abstract.jpeg\' %}"',
    'href="Abstract Sample_Template.pdf"': 'href="{% static \'documents/Abstract Sample_Template.pdf\' %}"',
    'src="images/Dr. Temitope Fadipe.jpeg"': 'src="{% static \'images/Dr. Temitope Fadipe.jpeg\' %}"',
    'src="./images/lagos ministry of health logo.png"': 'src="{% static \'images/lagos ministry of health logo.png\' %}"',
}

root = Path(__file__).resolve().parent
template_dir = root / 'templates'
if not template_dir.exists():
    raise FileNotFoundError(f"Template directory not found: {template_dir}")

for html_path in sorted(template_dir.glob('*.html')):
    text = html_path.read_text(encoding='utf-8')
    if '{% load static %}' not in text:
        text = re.sub(r'<!DOCTYPE html>\r?\n', '<!DOCTYPE html>\n{% load static %}\n', text, count=1)
    for old, new in replacements.items():
        text = text.replace(old, new)
    text = text.replace('onerror="this.src=\'dean_headshot.png\'"', 'onerror="this.src=\'{% static \'images/dean_headshot.png\' %}\'"')
    html_path.write_text(text, encoding='utf-8')
    print(f'Updated {html_path.name}')
