from .initial_assessment import survey_mappings as ia_map
from pprint import pprint

survey_mappings = ia_map

def only_with_allowed_keys(src_dict, not_allowed_keys):
  return {x: src_dict[x] for x in src_dict if x not in not_allowed_keys}

not_in_itsp_review = {"Have you ever previously accessed alcohol and / or drug treatment?",
                      "What is your highest level of education?",
                      "What is your principal income source?",
                      "Do you have a GP or medical centre that you regularly attend?",
                      "Have you ever been diagnosed with a mental health issue?",
                      "Have you served a custodial sentence in the past?"
                     }

ini_as = survey_mappings['initial_assessment']

# TODO TODO include these TODO TODO TODO TODO TODO TODO TODO TODO
# TODO  struct_transform_funcs
# TODO  incomplete_if_empty

itsp_review = { **ini_as['values_table'], 'bit_fields' : ini_as['bit_fields'], 
                'numeric_fields' : ini_as['numeric_fields']}

itsp_review['field_table'] = only_with_allowed_keys(
                                ini_as['field_table'],
                                not_in_itsp_review)

survey_mappings['itsp_review'] = itsp_review

pprint(itsp_review)