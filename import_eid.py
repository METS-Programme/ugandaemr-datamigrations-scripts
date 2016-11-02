from data_import import read, register, construct_obs, transform_list, group_data
from mappings.eid_summary_map import eid_summary_map
from mappings.eid_encounter_map import eid_encounter_map

eid_registration = read('./test_data/eid/eid_summary.csv')
eid_encounters = read('./test_data/eid/eid_encounters.csv')

eid_summary_variables = read('./csv_forms/eid_summary.csv')
eid_encounter_variables = read('./csv_forms/eid_encounter.csv')

summary_variables = transform_list(eid_summary_variables)
encounter_variables = transform_list(eid_encounter_variables)

# Register patients
register(eid_registration[1:], names_column=4, gender_column=6, birth_date_column=7,
         address_columns=[None, 1, None, None, None, None], identifier_columns={'2': '6'})
# Summary page and observations
construct_obs(eid_registration[1:], identifier_column=2, form_id=12, visit_column=3, encounter_type=16,
              mapped_dict=eid_summary_map, concept_answer_map=summary_variables, location_id=2)
# Encounter page and observations
construct_obs(eid_encounters[1:], identifier_column=1, form_id=11, visit_column=2, encounter_type=12,
              mapped_dict=eid_encounter_map, concept_answer_map=encounter_variables, location_id=2)
