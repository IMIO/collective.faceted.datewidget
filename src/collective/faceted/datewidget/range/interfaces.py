# -*- coding: utf-8 -*-
""" Widget interfaces and schema
"""
from zope import schema
from z3c.form import field
from eea.facetednavigation.widgets.daterange.interfaces import IDateRangeSchema as ISchema
from eea.facetednavigation.widgets.daterange.interfaces import DisplaySchemata as FacetedSchemata
from eea.facetednavigation.widgets.daterange.interfaces import DefaultSchemata as DS
from eea.facetednavigation.widgets.interfaces import LayoutSchemata
from eea.facetednavigation import EEAMessageFactory as _


class IDateRangeSchema(ISchema):
    """ Schema
    """


class DefaultSchemata(DS):
    """ Schemata default
    """


class DisplaySchemata(FacetedSchemata):
    """ Schemata display
    """


__all__ = [
    IDateRangeSchema.__name__,
    DefaultSchemata.__name__,
    LayoutSchemata.__name__,
    DisplaySchemata.__name__,
]
