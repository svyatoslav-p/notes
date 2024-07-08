# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'notes'
copyright = ''
author = ''

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
    'myst_parser',
    'sphinx_design',
    'sphinx_copybutton',
    'sphinx_togglebutton',
]

templates_path = ['_templates']
exclude_patterns = ['_build', 'Thumbs.db']

language = 'ru'

source_suffix = {
    '.rst': 'restructuredtext',
    '.md': 'markdown',
    '.html': 'html',
}

# -- Extensions configuration ------------------------------------------------
myst_links_external_new_tab = True
myst_enable_extensions = [
    'colon_fence',
    'tasklist',
    'fieldlist',
]

copybutton_exclude = '.linenos, .gp, .go'
copybutton_prompt_text = '$ '

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'sphinx_book_theme'
html_static_path = ['_static']
html_css_files = [
    'myst.css',
]
html_title = ''
html_logo = 'assets/images/logo.png'
html_favicon = './favicon.png'
html_sourcelink_suffix = ''

html_theme_options = {
    'github_url': 'https://github.com/svyatoslav-p/notes',
    'repository_url': 'https://github.com/svyatoslav-p/notes',
    'use_repository_button': False,
    'use_issues_button': False,
    'use_edit_page_button': False,
    'path_to_docs': 'docs',
    'home_page_in_toc': True,
    'show_navbar_depth': 3,
    'extra_footer': '',
}

import os
import sys

sys.path.insert(0, os.path.abspath('.'))

def setup(app):
    import custom_directives
    custom_directives.setup(app)
