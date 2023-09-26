from __future__ import annotations

from typing import List, Optional

from dash import html
from pydantic import validator

from vizro.models import VizroBaseModel
from vizro.models._models_utils import _log_call
from vizro.models._navigation._navigation_utils import _validate_pages
from vizro.models._navigation.icon import Icon
from vizro.models.types import NavigationPagesType


class NavBar(VizroBaseModel):
    """NavBar to be used in Navigation Panel of Dashboard.

    Args:
        pages (Optional[NavigationPagesType]): See [NavigationPagesType][vizro.models.types.NavigationPagesType].
                Defaults to `None`.
        items (Optional[List[Icon]]): List of icons
    """

    pages: Optional[NavigationPagesType] = None
    items: Optional[List[Icon]]

    # Re-used validators
    _validate_pages = validator("pages", allow_reuse=True, always=True)(_validate_pages)

    @_log_call
    def pre_build(self):
        if self.items is None:
            if isinstance(self.pages, list):
                self.items = [Icon(pages=[page]) for page in self.pages]
            if isinstance(self.pages, dict):
                self.items = [Icon(pages=list(value)) for page, value in self.pages.values()]

    @_log_call
    def build(self, page_id):
        if self.items:
            items = [item.build() for item in self.items]
            nav_bar = html.Div(
                children=items,
                className="nav_bar",
            )
            nav_panel = self._nav_panel_build(page_id=page_id)

            return nav_bar, nav_panel

    def _nav_panel_build(self, page_id):
        if self.items:
            for item in self.items:
                if isinstance(item.pages, list):
                    if page_id in item.pages:
                        return item._selector.build(page_id=page_id)

                if isinstance(item.pages, dict):
                    pages = [page for row in item.pages.values() for page in row]
                    if page_id in pages:
                        return item._selector.build(page_id=page_id)