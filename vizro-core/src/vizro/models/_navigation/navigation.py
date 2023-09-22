from __future__ import annotations

from typing import TYPE_CHECKING, Optional, Union

from pydantic import PrivateAttr, validator

from vizro.models import VizroBaseModel
from vizro.models._models_utils import _log_call
from vizro.models.types import NavigationPagesType
from vizro.models._navigation._navigation_utils import _validate_pages

if TYPE_CHECKING:
    from vizro.models._navigation.accordion import Accordion
    from vizro.models._navigation.nav_bar import NavBar


class Navigation(VizroBaseModel):
    """Navigation in [`Dashboard`][vizro.models.Dashboard] to structure [`Pages`][vizro.models.Page].

    Args:
        pages (Optional[NavigationPagesType]): See [NavigationPagesType][vizro.models.types.NavigationPagesType].
            Defaults to `None`.
    """

    pages: Optional[NavigationPagesType] = None
    selector: Optional[Union[Accordion, NavBar]] = None

    # validators
    _validate_pages = validator("pages", allow_reuse=True, always=True)(_validate_pages)

    @_log_call
    def pre_build(self):
        self._set_selector()

    def _set_selector(self):
        from vizro.models._navigation.accordion import Accordion
        if self.selector is None:
            self.selector = Accordion(pages=self.pages)

    @_log_call
    def build(self):
        return self.selector.build()
