# -*- coding: utf-8 -*-
"""Sphinx documentation """

# -- Path setup --------------------------------------------------------------

import os
import subprocess
from os.path import abspath, dirname
import sys


# -- Project information -----------------------------------------------------

project = "drmlib"
copyright = "Accelize"
author = "jeydoux@accelize.com"
version = "v1.2"
release = "v1.2"

sys.path.append( "/home/me/docproj/ext/breathe/" )


read_the_docs_build = os.environ.get('READTHEDOCS', None) == 'True'

if read_the_docs_build:

    ##subprocess.call('cd ../doxygen; doxygen doxygen.cfg', shell=True)
    #subprocess.call('pip install breathe', shell=True)
    #subprocess.call('doxygen doxygen.cfg', shell=True)  
    #subprocess.call('doxygen ../build/doc/Doxyfile', shell=True) 
    

    #subprocess.call('cd ../doxygen; doxygen doxygen.cfg', shell=True)
    subprocess.call('pip install breathe', shell=True)
    subprocess.call('pip install cmake', shell=True)
    subprocess.call('env', shell=True)
    subprocess.call('sh -c \"$(curl -fsSL https://raw.githubusercontent.com/Linuxbrew/install/master/install.sh)\" ', shell=True)
    subprocess.call('brew install libjsoncpp', shell=True)
    subprocess.call('sudo apt-get  --assume-yes install libjsoncpp-dev', shell=True)
    subprocess.call('sudo apt-get  --assume-yes install libcurl4-openssl-dev', shell=True)
    subprocess.call('sudo apt-get  --assume-yes install unifdef', shell=True)
    subprocess.call('cd .. && mkdir build && cd build && cmake -DDOC=ON .. && make && cd ..  ', shell=True)  
    #subprocess.call('cd ../doxygen; doxygen doxygen.cfg', shell=True)  
    subprocess.call('doxygen ../build/doc/Doxyfile', shell=True) 
    
    
    
    
breathe_projects = {
    "drmlib":"xml/"
    }


extensions = [ "breathe" ]

source_suffix = '.rst'
master_doc = 'index'
language = 'en'
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store', '.settings']
pygments_style = 'default'


# -- Options for HTML output -------------------------------------------------

html_theme = 'sphinx_rtd_theme'

html_favicon = '_static/favicon.ico'


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
