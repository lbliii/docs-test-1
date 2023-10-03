import os 
import sys

sys.path.insert(0, os.path.abspath('_themes'))

# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'Determined Docs'
copyright = '2023, Tara, LB'
author = 'Tara, LB'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = ["sphinxawesome_theme",
    "sphinx.ext.autodoc",
    "sphinx.ext.intersphinx",
    "sphinx.ext.extlinks",
    "sphinx.ext.viewcode",
    "sphinx_sitemap",
    "sphinx_design",
    "sphinxawesome_theme.docsearch",
    "sphinxawesome_theme.highlighting",]

templates_path = ['_templates']
exclude_patterns = ['_themes']



# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'sphinxawesome_theme'
html_theme_path = ["_themes"]
html_static_path = ['_static']
html_baseurl = 'https://docs.whatever.com'

html_theme_options = {
    "repository_url": "https://github.com/lbliii/docs-test-1",
    "use_repository_button": True,
}