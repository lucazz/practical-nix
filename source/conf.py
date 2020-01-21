# -*- coding: utf-8 -*-

project = "Practical Nix"
copyright = "2020 Thomaz Leite"
author = "Thomaz Leite"
version = release = "latest"

needs_sphinx = "1.8.3"

extensions = []

exclude_patterns = ["_build", "Thumbs.db", ".DS_Store"]

html_show_copyright = False
html_show_sourcelink = False
html_show_sphinx = False
html_static_path = ["_static"]
html_title = "Practical Nix"
html_theme = "alabaster"
html_theme_options = {
    "description": "A practical guide to building software with Nix",
    "logo": "nix-logo.svg",
    "logo_name": True,
    "logo_text_align": "center",
    "show_powered_by": False,
}
html_sidebars = {"**": ["about.html", "navigation.html"]}
html_static_path = ["_static"]

language = None

master_doc = "index"

pygments_style = None

source_suffix = ".rst"

templates_path = ["_templates"]
