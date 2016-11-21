from itertools import groupby
from operator import itemgetter

from baylor.mappings.art_encounter_map import art_encounter_map
from baylor.mappings.eid_encounter_map import eid_encounter_map
from baylor.mappings.eid_summary_map import eid_summary_map
from core.data_import import read, transform_list, create_summary_page, register, construct_obs, group_data

eid_registration = read('./test_data/eid_summary.csv')
eid_encounters = read('./test_data/eid_encounters.csv')
# eid_art = read('./baylor/data/tbl_followup.csv')
# eid_registration = read('./baylor/data/eid_summary.csv')
# eid_encounters = read('./baylor/data/eid_encounters.csv')
# eid_art = read('./baylor/data/tbl_followup.csv')

eid_summary_variables = read('./csv_forms/eid_summary.csv')
eid_encounter_variables = read('./csv_forms/eid_encounter.csv')
art_summary_variables = read('./csv_forms/art_summary.csv')
art_encounter_variables = read('./csv_forms/art_encounter.csv')

eid_summary_variables = transform_list(eid_summary_variables)
eid_encounter_variables = transform_list(eid_encounter_variables)
art_summary_variables = transform_list(art_summary_variables)
art_encounter_variables = transform_list(art_encounter_variables)

d = [{k: list(v)} for k, v in group_data(1, eid_encounters[1:])]

print len(d)

# for k, v in d.iteritems():
#     for vs in v:
#         print vs


# Register patients
# register(eid_registration[1:], names_column=4, gender_column=6, birth_date_column=7,
#          address_columns=[None, 1, None, None, None, None], identifier_columns={'2': '6'})

# EID Summary page and observations
# construct_obs(eid_registration[1:], identifier_column=2, form_id=12, visit_column=3, encounter_type=16,
#               mapped_dict=eid_summary_map, concept_answer_map=eid_summary_variables, location_id=2)

# EID Encounter page and observations
# construct_obs(eid_encounters[1:], identifier_column=1, form_id=11, visit_column=2, encounter_type=12,
#               mapped_dict=eid_encounter_map, concept_answer_map=eid_encounter_variables, location_id=2,
#               no_eid_visit_no=True)

# create_summary_page(eid_art[1:])

# ART Encounter page and observations
# construct_obs(eid_art[1:], identifier_column=1, form_id=16, visit_column=2, encounter_type=15,
#               mapped_dict=art_encounter_map, concept_answer_map=art_encounter_variables, location_id=2,
#               no_eid_visit_no=False)
