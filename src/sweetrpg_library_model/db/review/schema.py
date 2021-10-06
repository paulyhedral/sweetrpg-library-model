# -*- coding: utf-8 -*-
__author__ = "Paul Schifferer <dm@sweetrpg.com>"
"""
"""

from marshmallow import fields, INCLUDE
from sweetrpg_library_model.model.review import Review
from sweetrpg_model_core.schema.base import BaseSchema


class ReviewSchema(BaseSchema):
    model_class = Review

    title = fields.String(required=True)  # , load_only=True)
    text = fields.String(required=True)  # , load_only=True)
    volume = fields.Str(required=True)
