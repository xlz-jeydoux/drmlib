# -*- coding: utf-8 -*-
"""Sphinx documentation """

# -- Path setup --------------------------------------------------------------

import os
import subprocess
from os.path import abspath, dirname
import sys


# -- Project information -----------------------------------------------------

project = "drmlib_doc"
copyright = "Accelize"
author = "jeydoux@accelize.com"
version = "v1.2"
release = "v1.2"

sys.path.append( "/home/me/docproj/ext/breathe/" )


read_the_docs_build = os.environ.get('READTHEDOCS', None) == 'True'

if read_the_docs_build:

    subprocess.call('cd ../doxygen; doxygen doxygen.cfg', shell=True)
    subprocess.call('pip install breathe', shell=True)
    
breathe_projects = {
    "drmlib_doc":"xml/"
    }


extensions = [ "breathe" ]

source_suffix = '.rst'
master_doc = 'index'
language = 'en'
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store', '.settings']
pygments_style = 'default'


# -- Options for HTML output -------------------------------------------------

html_theme = 'sphinx_rtd_theme'

html_favicon = 'images/favicon.ico'


# -- Options for HTMLHelp output ---------------------------------------------

htmlhelp_basename = '%sdoc' % project


# -- Options for LaTeX output ------------------------------------------------

latex_elements = {}
latex_documents = [(
    master_doc, '%s.tex' % project, '%s Documentation' % project, author,
    'manual')]


# -- Options for manual page output ------------------------------------------

man_pages = [(
    master_doc, "my_name", '%s Documentation' % project,
    [author], 1)]


# -- Options for Texinfo output ----------------------------------------------

texinfo_documents = [(
    master_doc, project, '%s Documentation' % project, author, project,
    "my_description", 'Miscellaneous')]
