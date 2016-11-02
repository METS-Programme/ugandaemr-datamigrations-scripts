from data_import import map_to_ugandaemr
from common import *

eid_encounter_map = {}
eid_encounter_map = map_to_ugandaemr(eid_encounter_map, '1', '')
eid_encounter_map = map_to_ugandaemr(eid_encounter_map, '2', '')
eid_encounter_map = map_to_ugandaemr(eid_encounter_map, '3', '')
eid_encounter_map = map_to_ugandaemr(eid_encounter_map, '4', '99449')  # Age at EID Visit
eid_encounter_map = map_to_ugandaemr(eid_encounter_map, '5', '99080', answer_dict=test_type)  # HIV TEST
eid_encounter_map = map_to_ugandaemr(eid_encounter_map, '6', '99451',
                                     answer_dict=feeding_status)  # Feeding Status at EID Visit
eid_encounter_map = map_to_ugandaemr(eid_encounter_map, '7', '162839', answer_dict=immunization_codes, many=True,
                                     separator_for_many='-')  # EID Immunisation Codes
eid_encounter_map = map_to_ugandaemr(eid_encounter_map, '8', '5089')  # Weight (kg
eid_encounter_map = map_to_ugandaemr(eid_encounter_map, '9', '99801', answer_dict=muac)  # MUAC
eid_encounter_map = map_to_ugandaemr(eid_encounter_map, '10', '5090')  # Height
eid_encounter_map = map_to_ugandaemr(eid_encounter_map, '11', '162853',
                                     answer_dict=clinical_assessment_codes, many=True)  # Clinical Assessment Codes
eid_encounter_map = map_to_ugandaemr(eid_encounter_map, '12', '162864', answer_dict=development_milestone,
                                     many=True)  # Development Milestone
eid_encounter_map = map_to_ugandaemr(eid_encounter_map, '13', '5314')  # HEAD CIRCUMFERENCE
eid_encounter_map = map_to_ugandaemr(eid_encounter_map, '14', '99798')  # CTX given at EID Visit
eid_encounter_map = map_to_ugandaemr(eid_encounter_map, '15', '99799')  # NVP given at EID Visit
eid_encounter_map = map_to_ugandaemr(eid_encounter_map, '16', '99035')  # OTHER MEDICATIONS DISPENSED
eid_encounter_map = map_to_ugandaemr(eid_encounter_map, '17', '1193', answer_dict=drugs,
                                     many=True)  # CURRENT DRUGS USED
eid_encounter_map = map_to_ugandaemr(eid_encounter_map, '18', '162887')  # EID Visit Appointment Date
eid_encounter_map = map_to_ugandaemr(eid_encounter_map, '19', '')
eid_encounter_map = map_to_ugandaemr(eid_encounter_map, '20', '')
eid_encounter_map = map_to_ugandaemr(eid_encounter_map, '21', '')
