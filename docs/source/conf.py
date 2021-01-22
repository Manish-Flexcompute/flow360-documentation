# Configuration file for the Sphinx documentation builder.
#
# This file only contains a selection of the most common options. For a full
# list see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Path setup --------------------------------------------------------------

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#
import os
# import sys
# import re
# import codecs
# import sys, os
# sys.path.insert(0, os.path.abspath("c:\users\manis\appdata\local\packages\pythonsoftwarefoundation.python.3.9_qbz5n2kfra8p0\localcache\local-packages\python39\site-packages"))
# sys.path.append(os.path.abspath('extensions\nbsphinx\src'))
# sys.path.append('C:\\users\\manis\\appdata\\local\\packages\\pythonsoftwarefoundation.python.3.9_qbz5n2kfra8p0\\localcache\\local-packages\\python39\\site-packages\\')

#here = os.path.abspath(os.path.dirname(__file__))
#sys.path.append(os.path.abspath('../'))
#print(sys.path)
#
#def read(*parts):
#    with codecs.open(os.path.join(here, *parts), 'r') as fp:
#        return fp.read()
#
#def find_version(*file_paths):
#    version_file = read(*file_paths)
#    version_match = re.search(r"^__version__ = ['\"]([^'\"]*)['\"]",
#                              version_file, re.M)
#    if version_match:
#        return version_match.group(1)
#    raise RuntimeError("Unable to find version string.")
#

# import sphinx
import sphinx_rtd_theme
# import nbsphinx

# -- Project information -----------------------------------------------------

project = 'Flow360'
copyright = '2021, Flexcompute Inc.'
author = 'Flexcompute Inc.'

master_doc = 'index'

# -- General configuration ---------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
        "nbsphinx",
        ]

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = ['_build', '**.ipynb_checkpoints']

# nbsphinx_allow_errors = True

# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#

html_theme = 'sphinx_rtd_theme'

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['_static']

html_context = {
    'css_files': [
        '_static/theme_overrides.css',  # override wide tables in RTD theme
        ],
    }

html_theme_path = ['_themes']
