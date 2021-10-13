# -*- coding: utf-8 -*-
__author__ = "Paul Schifferer <dm@sweetrpg.com>"
"""
"""

from sweetrpg_library_model.model.author import Author
from sweetrpg_library_model.db.author.schema import AuthorSchema
import json
from datetime import datetime


author_json = """
{
    "_id": "this-is-ignored",
    "name": "Joe Bob",
    "created_at": "2021-09-13T07:55:00.001",
    "created_by": "test",
    "updated_at": "2021-09-13T07:55:00.001",
    "updated_by": "test",
    "tags": [{"name": "tag", "value": "tag"}],
    "properties": [
        {"name": "value", "value": "1", "kind": "int"}
    ]
}
"""
author_datetime = datetime(2021, 9, 13, 7, 55, 0, 1000)
author_dict = {
    "_id": "another-id",
    "name": "Billy",
    "created_at": datetime(2021, 9, 15, 7, 35, 0, 2000),
    "created_by": "test",
    "updated_at": datetime(2021, 9, 15, 7, 35, 0, 2001),
    "updated_by": "test",
    "deleted_at": datetime(2021, 9, 15, 7, 35, 0, 2001),
    "deleted_by": "test",
    "tags": [{"name": "tag", "value": "tag"}],
    "properties": [{"name": "value", "value": "1", "kind": "int"}],
}


def test_load_author_from_json():
    j = json.loads(author_json)
    schema = AuthorSchema()
    a = schema.load(j)
    assert a is not None
    assert isinstance(a, Author)
    assert a.id == "this-is-ignored"
    assert a.name == "Joe Bob"
    assert len(a.tags) == 1
    t = a.tags[0]
    assert t["name"] == "tag"
    assert t["value"] == "tag"
    assert len(a.properties) == 1
    p = a.properties[0]
    assert p["name"] == "value"
    assert p["value"] == "1"
    assert p["kind"] == "int"
    assert a.created_at == author_datetime
    assert a.created_by == "test"
    assert a.created_at == author_datetime
    assert a.updated_by == "test"
    assert a.deleted_at is None
    assert a.deleted_by is None


def test_load_author_from_dict():
    schema = AuthorSchema()
    a = schema.load(author_dict)
    assert a is not None
    assert isinstance(a, Author)
    assert a.id == "another-id"
    assert a.name == "Billy"
    assert len(a.tags) == 1
    t = a.tags[0]
    assert t["name"] == "tag"
    assert t["value"] == "tag"
    assert len(a.properties) == 1
    p = a.properties[0]
    assert p["name"] == "value"
    assert p["value"] == "1"
    assert p["kind"] == "int"
    assert a.created_at == datetime(2021, 9, 15, 7, 35, 0, 2000)
    assert a.created_by == "test"
    assert a.updated_at == datetime(2021, 9, 15, 7, 35, 0, 2001)
    assert a.updated_by == "test"
    assert a.deleted_at == datetime(2021, 9, 15, 7, 35, 0, 2001)
    assert a.deleted_by == "test"
