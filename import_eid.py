from data_import import read, register, construct_obs, transform_list, group_data
from mappings.eid_summary_map import eid_summary_map
from mappings.eid_encounter_map import eid_encounter_map

eid_registration = read('./data/baylor/eid/eid_summary.csv')
eid_encounters = read('./data/baylor/eid/eid_encounters.csv')

eid_summary_variables = read('./csv_forms/eid_summary.csv')
eid_encounter_variables = read('./csv_forms/eid_encounter.csv')

summary_variables = transform_list(eid_summary_variables)
encounter_variables = transform_list(eid_encounter_variables)

register(eid_registration[1:], 4, 6, 7, [None, 1, None, None, None, None], {'2': '6'})
construct_obs(eid_registration[1:], 2, 12, 3, 16, eid_summary_map, summary_variables)
construct_obs(eid_encounters[1:], 1, 11, 2, 12, eid_encounter_map, encounter_variables)
