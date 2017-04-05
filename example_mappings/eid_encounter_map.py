from core.common import *
from core.data_import import map_to_ugandaemr

eid_encounter_map = {}
eid_encounter_map = map_to_ugandaemr(eid_encounter_map, None, '162992')  # EID Encounter Type
eid_encounter_map = map_to_ugandaemr(eid_encounter_map, None, '99443')  # EID Visit 1 Appointment Date
eid_encounter_map = map_to_ugandaemr(eid_encounter_map, None, '99449')  # Age at EID Visit
eid_encounter_map = map_to_ugandaemr(eid_encounter_map, None, '99080', answer_dict=test_type)  # HIV TEST
eid_encounter_map = map_to_ugandaemr(eid_encounter_map, None, '99451',
                                     answer_dict=feeding_status)  # Feeding Status at EID Visit
eid_encounter_map = map_to_ugandaemr(eid_encounter_map, None, '162839', answer_dict=immunization_codes, many=True,
                                     separator_for_many='-')  # EID Immunisation Codes
eid_encounter_map = map_to_ugandaemr(eid_encounter_map, None, '162890')  # Immunization Other Specify
eid_encounter_map = map_to_ugandaemr(eid_encounter_map, None, '5090')  # Height
eid_encounter_map = map_to_ugandaemr(eid_encounter_map, None, '5089')  # Weight (kg)
eid_encounter_map = map_to_ugandaemr(eid_encounter_map, None, '99800')  # EID Visit 1 Z-Score
eid_encounter_map = map_to_ugandaemr(eid_encounter_map, None, '99801', answer_dict=muac)  # MUAC
eid_encounter_map = map_to_ugandaemr(eid_encounter_map, None, '162853',
                                     answer_dict=clinical_assessment_codes, many=True)  # Clinical Assessment Codes
eid_encounter_map = map_to_ugandaemr(eid_encounter_map, None, '163008')  # Other Clinical Assessment Codes
eid_encounter_map = map_to_ugandaemr(eid_encounter_map, None, '162864', answer_dict=development_milestone,
                                     many=True)  # Development Milestone
eid_encounter_map = map_to_ugandaemr(eid_encounter_map, None, '5314')  # HEAD CIRCUMFERENCE
eid_encounter_map = map_to_ugandaemr(eid_encounter_map, None, '99798')  # CTX given at EID Visit
eid_encounter_map = map_to_ugandaemr(eid_encounter_map, None, '99799')  # NVP given at EID Visit
eid_encounter_map = map_to_ugandaemr(eid_encounter_map, None, '162854', no_yes_1)  # Refill of ART fro the mother
eid_encounter_map = map_to_ugandaemr(eid_encounter_map, None, '1193', answer_dict=drugs,
                                     many=True)  # CURRENT DRUGS USED
eid_encounter_map = map_to_ugandaemr(eid_encounter_map, None, '99035')  # OTHER MEDICATIONS DISPENSED
eid_encounter_map = map_to_ugandaemr(eid_encounter_map, None, '162865')  # EID ACTIONS TAKEN
