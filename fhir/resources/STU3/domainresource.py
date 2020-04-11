# -*- coding: utf-8 -*-
"""
Profile: http://hl7.org/fhir/StructureDefinition/DomainResource
Release: STU3
Version: 3.0.2
Revision: 11917
Last updated: 2019-10-24T11:53:00+11:00
"""


from . import resource

class DomainResource(resource.Resource):
    """ A resource with narrative, extensions, and contained resources.

    A resource that includes narrative, extensions, and contained resources.
    """

    resource_type = "DomainResource"

    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.

        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """

        self.contained = None
        """ Contained, inline Resources.
        List of `Resource` items (represented as `dict` in JSON). """

        self.extension = None
        """ Additional Content defined by implementations.
        List of `Extension` items (represented as `dict` in JSON). """

        self.modifierExtension = None
        """ Extensions that cannot be ignored.
        List of `Extension` items (represented as `dict` in JSON). """

        self.text = None
        """ Text summary of the resource, for human interpretation.
        Type `Narrative` (represented as `dict` in JSON). """

        super(DomainResource, self).__init__(jsondict=jsondict, strict=strict)

    def elementProperties(self):
        js = super(DomainResource, self).elementProperties()
        js.extend([
            ("contained", "contained", resource.Resource, "Resource", True, None, False),
            ("extension", "extension", extension.Extension, "Extension", True, None, False),
            ("modifierExtension", "modifierExtension", extension.Extension, "Extension", True, None, False),
            ("text", "text", narrative.Narrative, "Narrative", False, None, False),
        ])
        return js


import sys
try:
    from . import extension
except ImportError:
    extension = sys.modules[__package__ + '.extension']
try:
    from . import narrative
except ImportError:
    narrative = sys.modules[__package__ + '.narrative']