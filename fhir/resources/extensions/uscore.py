# -*- coding: utf-8 -*-
"""
Extended on Release: R4
Version: 4.0.1
Author: alexmbennett2
"""
import typing

from pydantic import Field, root_validator

# from fhir.resources import extension, fhirtypes
from fhir.resources import fhirtypes


class BirthSex(): #extension.Extension):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    Optional Extensions Element.
    Optional Extension Element - found in all resources.
    """

    resource_type = Field("BirthSex", const=True)

    url: fhirtypes.Uri = Field(
        None,
        alias="url",
        title="identifies the meaning of the extension",
        description=(
            "Source of the definition for the extension code - a logical name or a "
            "URL."
        ),
        # if property is element of this resource.
        element_property=True,
        element_required=True,
    )

    valueCode: fhirtypes.Code = Field(
        None,
        alias="valueCode",
        title="Value of birth sex",
        description=(
            "Value of birth sex extension - must be one of a constrained set of the data "
            "types (see [Extensibility](extensibility.html) for a list)."
        ),
        # if property is element of this resource.
        element_property=True,
        # Choice of Data Types. i.e value[x]
        enum_values=['F', 'M']
    )