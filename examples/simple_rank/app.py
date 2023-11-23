"""

This should be a simple to boot, stand alone shiny app (not shinylive for now), that uses a local SqlLite database through SqlAlchemy (which can be later moved to be provided via the zs-state and zs-data mesh system), to run a simple rank choice widget demo

from looking at this example, it should be easy to integrate a standalone, sqlite backed instance into a website

and it should be VERY easy to integrate into another Shiny app, or Starlette based HTTP service

"""

app = App(app_ui, server)
