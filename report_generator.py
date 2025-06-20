"""
Generates an HTML report from scraped profile data using Jinja2 templates.
"""
from jinja2 import Environment, FileSystemLoader
import os


def generate_report(identifier, profiles, output_path):
    """
    Renders an HTML report for the given identifier and profiles list.

    Arguments:
    - identifier (str): The username or sanitized email used in the report.
    - profiles (List[dict]): Scraped profiles from info_scraper.
    - output_path (str): File path to save the generated HTML report.
    """
    # Set up Jinja2 environment; look in this directory for templates
    env = Environment(loader=FileSystemLoader(searchpath=os.path.dirname(__file__)))

    # HTML template string (could be moved to a separate .html file)
    template_str = '''
<html>
  <head>
    <meta charset="UTF-8" />
    <title>Public Profile Report: {{ identifier }}</title>
  </head>
  <body>
    <h1>Public Profile Report: {{ identifier }}</h1>
    <p>Total profiles found: {{ profiles|length }}</p>
    <ul>
    {% for p in profiles %}
      <li style="margin-bottom: 20px;">
        {% if p.image %}
          <img src="{{ p.image }}" alt="Profile image" width="80" style="vertical-align: middle;" />
        {% endif %}
        <a href="{{ p.url }}" target="_blank" style="font-size: 1.1em; font-weight: bold;">
          {{ p.name }}
        </a>
        <p>{{ p.bio }}</p>
      </li>
    {% endfor %}
    </ul>
  </body>
</html>
'''

    # Compile the template
    template = env.from_string(template_str)

    # Render with context
    rendered_html = template.render(identifier=identifier, profiles=profiles)

    # Write out to file
    with open(output_path, 'w', encoding='utf-8') as f:
        f.write(rendered_html)
