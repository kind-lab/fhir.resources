# -*- coding: utf-8 -*-
"""
Release: R4
Version: 4.0.1
Validation extension by alexmbennett2
"""

def validate_elements(cls, values):
    """ Validate required and constrained types """
    errs = []
    errs = _validate_required(cls, values, errs)
    errs = _validate_enum_values(cls, values, errs)    
    _report_validation_errors(errs)    
    return values
  
def _validate_enum_values(cls, values, errs):
    """ Check that value is within enum_values list """
    for field in values:
         if (('enum_values' in cls.__fields__[field].field_info.extra) & 
             (values[field] is not None)):
             enum_values = cls.__fields__[field].field_info.extra['enum_values']
             if values[field] not in enum_values:
                 errs.append(ValueError(f"Invalid gender given: {values[field]}"))
    return errs

def _validate_required(cls, values, errs):
    """ Check if required element is present """
    for field in values:
         if 'element_required' in cls.__fields__[field].field_info.extra:
             required = cls.__fields__[field].field_info.extra['element_required']
             if required & (values[field] is None):
                 errs.append(ValueError(f"Required variable empty: {field}"))
    return errs

def _report_validation_errors(errs):
    """ Report validation errors if any """
    if len(errs) > 0:
          errors = "\n ".join([str(e).replace("\n", "\n  ") for e in errs])
          raise Exception(errors)
          
def validate_all_elements(cls, values):
      """ First validate if element is required and present 
          Second validate if the value entered is within a list of 
          values (if specified)
      """
      errs = []
      
      for field in values:
         if 'enum_values' in cls.__fields__[field].field_info.extra:
             enum_values = cls.__fields__[field].field_info.extra['enum_values']
             if values[field] not in enum_values:
                 errs.append(ValueError(f"Invalid gender given: {values[field]}"))
         if 'element_required' in cls.__fields__[field].field_info.extra:
             required = cls.__fields__[field].field_info.extra['element_required']
             if required & (values[field] is None):
                 errs.append(ValueError(f"Required variable empty: {field}"))
      if len(errs) > 0:
          errors = "\n ".join([str(e).replace("\n", "\n  ") for e in errs])
          raise Exception(errors)
      return values