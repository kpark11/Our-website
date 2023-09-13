#!/usr/bin/env python
# coding: utf-8


import dash
from dash import html

dash.register_page(__name__, path='/')

dash.layout = html.Div([
    html.H1('This is our Home page'),
    html.Div('This is our Home page content.'),
])

