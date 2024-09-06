"""Welcome to Reflex! This file outlines the steps to create a basic app."""

import reflex as rx

from rxconfig import config
from .components.navbar import navbar
from .views.body import body
from .views.footer import footer
from .views.header import header


class State(rx.State):
    """The app state."""

    ...
# style = {
#     # Background
#     "background_repeat": "repeat-y",
#     "background_size": r"10000% 10000%",
#     "background": "#334c3a",
#     "background": "linear-gradient(45deg, #334c3a, #527a53)",
#     "animation": "gradientFlow 10s ease infinite",
# }

# stylesheets = ["css/animation.css"]


def index() -> rx.Component:
    # Welcome Page (Index)
    return rx.box(
        navbar(),
        header(),
        body(),
        footer(),
        spacing = '4'
    )


# stylesheets=stylesheets,style =style
app = rx.App()
app.add_page(
    index,
    title='U.E. Colegio Santa Lucia'
)
