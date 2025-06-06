import os
from bs4 import BeautifulSoup
import pytest

HTML_DIR = os.path.dirname(os.path.dirname(__file__))

# gather all html files in repository root
HTML_FILES = [f for f in os.listdir(HTML_DIR) if f.endswith('.html')]

@pytest.mark.parametrize('filename', HTML_FILES)
def test_internal_links_exist(filename):
    path = os.path.join(HTML_DIR, filename)
    with open(path, 'r', encoding='utf-8') as f:
        soup = BeautifulSoup(f, 'html.parser')

    for a in soup.find_all('a'):
        href = a.get('href', '')
        if href.endswith('.html') and not href.startswith('http'):
            target = os.path.join(HTML_DIR, href)
            assert os.path.exists(target), f"Broken link: {href} referenced in {filename}"
# Run with: python -m pytest
