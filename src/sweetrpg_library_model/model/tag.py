# -*- coding: utf-8 -*-
__author__ = "Paul Schifferer <dm@sweetrpg.com>"
"""
"""

import logging
from sweetrpg_model_core.model.base import BaseModel


class Tag(BaseModel):
    """A model object representing a tag value attached to an object."""

    def __init__(self, *args, **kwargs):
        """Creates a new Tag object.

        :key str name: The name of the tag.
        """
        logging.debug("args: %s, kwargs: %s", args, kwargs)

        super().__init__(args, kwargs)

        self.name = kwargs.get("name")
