# -*- coding: utf-8 -*-
__author__ = "Paul Schifferer <dm@sweetrpg.com>"
"""
"""

from marshmallow import fields
from sweetrpg_library_model.model.volume import Volume
from sweetrpg_model_core.schema.base import BaseSchema


class VolumeSchema(BaseSchema):
    model_class = Volume

    name = fields.String(required=True)  # , load_only=True)
    slug = fields.String(required=True)  # , load_only=True)
    system = fields.String(required=True)  # , load_only=True)
    tags = fields.List(fields.Dict(keys=fields.String(required=True), values=fields.String()))
    publisher = fields.String()
    properties = fields.List(fields.Dict(keys=fields.String(), values=fields.String()))
