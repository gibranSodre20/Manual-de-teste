# Configuration file for the Sphinx documentation builder.

# -- Permite destacar as linhas das tabelas via .CSS
from docutils import nodes
from docutils.parsers.rst import roles


def alterar_texto_role(name, rawtext, text, lineno, inliner, options={}, content=[]):
    node = nodes.inline(rawtext, text, classes=['alterar-texto'])
    return [node], []

roles.register_local_role('alterar-texto', alterar_texto_role)

# -- Project information
project = 'Manual de Teste'
copyright = '2026, Teste'
author = 'Teste'

release = 'v. 1.0'
version = 'v. 1.0'

# -- General configuration
extensions = [
    'sphinx.ext.duration',
    'sphinx.ext.doctest',
    'sphinx.ext.autodoc',
    'sphinx.ext.autosummary',
    'sphinx.ext.intersphinx',
]

intersphinx_mapping = {
    'python': ('https://docs.python.org/3/', None),
    'sphinx': ('https://www.sphinx-doc.org/en/master/', None),
}
intersphinx_disabled_domains = ['std']

templates_path = ['_templates']

# -- Permite destacar as linhas "kbd" das tabelas via .CSS
html_static_path = ['_static']
html_css_files = ['custom.css',]

# -- Options for HTML output
html_theme = 'sphinx_rtd_theme'

# -- Options for EPUB output
epub_show_urls = 'footnote'

# -- Options for PDF output
latex_documents = [
    ('index', 'project.tex', 'Project Documentation',
     'Author', 'manual'),
]

# html_logo = "_static/img/logo-pncp-transparente-branco.png"

# html_theme_options = {
#     'logo_only': False,
#     'display_version': True,
# }

# Arquivo para injetar javascript
# html_js_files = [
#     ("readthedocs.js", {"defer": "defer"}),
# ]
