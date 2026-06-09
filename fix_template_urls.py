from pathlib import Path

replacements = {
    'href="index.html"': 'href="{% url \'home\' %}"',
    'href="about_one_health_conference.html"': 'href="{% url \'about\' %}"',
    'href="abstract_submission_one_health_conference.html"': 'href="{% url \'abstract_submission\' %}"',
    'href="contact_one_health_conference.html"': 'href="{% url \'contact\' %}"',
    'href="registration_one_health_conference.html"': 'href="{% url \'registration\' %}"',
    'href="speakers_one_health_conference.html"': 'href="{% url \'speakers\' %}"',
    'href="special_guests_one_health_conference.html"': 'href="{% url \'special_guests\' %}"',
    'href="program_one_health_conference.html"': 'href="{% url \'program\' %}"',
    'href="partners_sponsors.html"': 'href="{% url \'partners_sponsors\' %}"',
}

root = Path(__file__).resolve().parent
for html_path in sorted((root / 'templates').glob('*.html')):
    text = html_path.read_text(encoding='utf-8')
    for old, new in replacements.items():
        text = text.replace(old, new)
    html_path.write_text(text, encoding='utf-8')
    print(f'Updated URLs in {html_path.name}')
