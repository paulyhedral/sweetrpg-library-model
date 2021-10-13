# -*- coding: utf-8 -*-
__author__ = "Paul Schifferer <dm@sweetrpg.com>"
"""
"""

from marshmallow import fields
from sweetrpg_library_model.model.system import System
from sweetrpg_model_core.schema.base import BaseSchema


class SystemSchema(BaseSchema):
    model_class = System

    name = fields.String(required=True)  # , load_only=True)
    tags = fields.List(fields.Dict(keys=fields.String(required=True), values=fields.String()))
