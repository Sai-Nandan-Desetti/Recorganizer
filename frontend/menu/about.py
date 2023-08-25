"""
This module defines the about page of the app.
"""
from frontend.utils import ui


def show_about_page():
    ui.set_title('About')
    ui.display_text('This is an app for organizing medical video recordings.')
