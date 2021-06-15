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
    # errs = _validate_extensions(cls, values, errs)
    _report_validation_errors(errs)    
    return values
  
def _validate_enum_values(cls, values, errs):
    """ Check that value is within enum_values list """
    
    for field in values:
         if (('enum_values' in cls.__fields__[field].field_info.extra) & 
             (values[field] is not None)):
             enum_values = cls.__fields__[field].field_info.extra['enum_values']
             if values[field] not in enum_values:
                 errs.append(ValueError(f"Invalid {cls} given: {values[field]}"))
         elif (('enum_code_values' in cls.__fields__[field].field_info.extra) & 
             (values[field] is not None)):
             enum_code_values = cls.__fields__[field].field_info.extra['enum_code_values']
             for coding in values[field].coding:
                 if coding.code not in enum_code_values:
                     errs.append(ValueError(f"Invalid code for {cls} given: {coding.code}"))
    return errs

def _validate_required(cls, values, errs):
    """ Check if required element is present """
    for field in values:
         if 'element_required' in cls.__fields__[field].field_info.extra:
             required = cls.__fields__[field].field_info.extra['element_required']
             if required & (values[field] is None):
                 errs.append('--------------------------------')
                 errs.append(ValueError(f"Required variable empty: {field}"))
    return errs

def _validate_extensions(cls, values, errs):
    """ Check if required element is present """
    for field in values:
         if (field == 'extension') & (values[field] is not None):
             if isinstance(values[field], list):
                 for ext in values[field]:
                     print(ext.url.split('-')[-1])
                     if ext.url.split('-')[-1] == 'birthsex':
                          print('BIRTHSEX MADE IT')
                          # uscore.BirthSex(ext)
             # ext_type = values[field].url.split('-')[-1]
             # print(ext_type)
             # if ext_type == 'birthsex':
             #     print('BIRTHSEX BABY')                 
             #     print(ext_type)
             #     print('--------------')
             #     print(field)
             #     uscore.BirthSex(field)
             # # trigger validation of sub components
             # required = cls.__fields__[field].field_info.extra['element_required']
             # if required & (values[field] is None):
             #     errs.append('--------------------------------')
             #     errs.append(ValueError(f"Required variable empty: {field}"))
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
                 errs.append('--------------------------------')
                 errs.append(ValueError(f"Required variable empty: {field}"))
      if len(errs) > 0:
          errors = "\n ".join([str(e).replace("\n", "\n  ") for e in errs])
          raise Exception(errors)
      return values