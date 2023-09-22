# Keep this import at the top to avoid circular imports since it's used in every model.
from ._base import VizroBaseModel  # noqa: I001
from ._action import Action
from ._components import Card, Graph
from ._components.form import Button, Checklist, Dropdown, RadioItems, RangeSlider, Slider
from ._controls import Filter, Parameter
from ._navigation.accordion import Accordion
from ._navigation.navigation import Navigation
from ._navigation.nav_bar import NavBar
from ._navigation.icon import Icon
from ._dashboard import Dashboard
from ._layout import Layout
from ._page import Page

Page.update_forward_refs(Button=Button, Card=Card, Filter=Filter, Graph=Graph, Parameter=Parameter, Accordion=Accordion)
Navigation.update_forward_refs(Accordion=Accordion, NavBar=NavBar, Icon=Icon)
Dashboard.update_forward_refs(Page=Page, Navigation=Navigation)
Icon.update_forward_refs(Accordion=Accordion)

# Please keep alphabetically ordered
__all__ = [
    "Accordion",
    "Action",
    "Button",
    "Card",
    "Checklist",
    "Dashboard",
    "Dropdown",
    "Filter",
    "Graph",
    "Icon",
    "Layout",
    "NavBar",
    "Navigation",
    "Page",
    "Parameter",
    "RadioItems",
    "RangeSlider",
    "Slider",
    "VizroBaseModel",
]
