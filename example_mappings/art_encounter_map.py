from core.data_import import map_to_ugandaemr

from core.common import *

art_encounter_map = {}
art_encounter_map = map_to_ugandaemr(art_encounter_map, None, '90069')  # SCHEDULED PATIENT VISIST
art_encounter_map = map_to_ugandaemr(art_encounter_map, None, '5096')  # Return date
art_encounter_map = map_to_ugandaemr(art_encounter_map, None, '99024')  # Duration(Months since baseline):
art_encounter_map = map_to_ugandaemr(art_encounter_map, None, '99025')  # Duration:(Months on current regimen)
art_encounter_map = map_to_ugandaemr(art_encounter_map, None, '90236')  # BODY WEIGHT
art_encounter_map = map_to_ugandaemr(art_encounter_map, None, '5090')  # Height (cm)
art_encounter_map = map_to_ugandaemr(art_encounter_map, None, '99030')  # MID-UPPER ARM CIRCUMFERENCE-CODE
art_encounter_map = map_to_ugandaemr(art_encounter_map, None, '460', answer_dict=no_yes)  # Oedema
art_encounter_map = map_to_ugandaemr(art_encounter_map, None, '90041', answer_dict=no_yes_1)  # PREGNANT
art_encounter_map = map_to_ugandaemr(art_encounter_map, None, '5596')  # ESTIMATED DATE OF CONFINEMENT
art_encounter_map = map_to_ugandaemr(art_encounter_map, None, '90012', answer_dict=no_yes)  # EMTCT
art_encounter_map = map_to_ugandaemr(art_encounter_map, None, '162983')  # Estimated gestational age (weeks)
art_encounter_map = map_to_ugandaemr(art_encounter_map, None, '90238',
                                     answer_dict=no_yes_pregnant)  # FAMILY PLANNING STATUS
art_encounter_map = map_to_ugandaemr(art_encounter_map, None, '374', many=True)  # METHOD OF FAMILY PLANNING
art_encounter_map = map_to_ugandaemr(art_encounter_map, None, '99270')  # AGE IN MONTHS
art_encounter_map = map_to_ugandaemr(art_encounter_map, None, '90216', answer_dict=tb_status)  # TUBERCULOSIS STATUS
art_encounter_map = map_to_ugandaemr(art_encounter_map, None, '90217')  # TUBERCULOSIS TREATMENT START DATE
art_encounter_map = map_to_ugandaemr(art_encounter_map, None, '90310')  # TUBERCULOSIS TREATMENT STOP DATE
art_encounter_map = map_to_ugandaemr(art_encounter_map, None, '90227',
                                     answer_dict=side_effects, many=True)  # MEDICATION OR OTHER SIDE EFFECTS
art_encounter_map = map_to_ugandaemr(art_encounter_map, None, '99113')  # OTHER SIDE EFFECTS
art_encounter_map = map_to_ugandaemr(art_encounter_map, None, '90251',answer_dict=symptoms)  # SYMPTOM, DIAGNOSIS, OR OPPORTUNISTIC INFECTION
art_encounter_map = map_to_ugandaemr(art_encounter_map, None,
                                     '99032')  # OPPORTUNISTIC INFECTION NOT OTHERWISE SPECIFIED
art_encounter_map = map_to_ugandaemr(art_encounter_map, None, '68')  # MALNUTRITION
art_encounter_map = map_to_ugandaemr(art_encounter_map, None, '90235')  # HISTORY OF FUNCTIONAL STATUS
art_encounter_map = map_to_ugandaemr(art_encounter_map, None, '90203')  # WHO HIV CLINICAL STAGE
art_encounter_map = map_to_ugandaemr(art_encounter_map, None, '90156')  # ADHERENCE TO COTRIMOXZOLE
art_encounter_map = map_to_ugandaemr(art_encounter_map, None,
                                     '99033')  # TRIMETHOPRIM AND SULFAMETHOXAZOLE DAYS DISPENSED
art_encounter_map = map_to_ugandaemr(art_encounter_map, None, '99037')  # TRIMETHOPRIM AND SULFAMETHOXAZOLE DOSAGE

art_encounter_map = map_to_ugandaemr(art_encounter_map, None, '99604')  # INH DOSAGE
art_encounter_map = map_to_ugandaemr(art_encounter_map, None, '99605')  # INH DAYS DISPENSED
art_encounter_map = map_to_ugandaemr(art_encounter_map, None, '1193')  # CURRENT DRUGS USED
art_encounter_map = map_to_ugandaemr(art_encounter_map, None, '99035')  # OTHER MEDICATIONS DISPENSED
art_encounter_map = map_to_ugandaemr(art_encounter_map, None, '90221')  # ANTI-RETROVIRAL DRUG ADHERENCE ASSESSMENT CODE
art_encounter_map = map_to_ugandaemr(art_encounter_map, None,
                                     '90223')  # REASON FOR MISSING ANTI-RETROVIRAL DRUG ADMINISTRATION SCHEDULE
art_encounter_map = map_to_ugandaemr(art_encounter_map, None, '99125')  # OTHER REASON FOR MISSING ARV
art_encounter_map = map_to_ugandaemr(art_encounter_map, None, '90315')  # CURRENT ARV REGIMEN
art_encounter_map = map_to_ugandaemr(art_encounter_map, None, '99126')  # CURRENT REGIMEN OTHER
art_encounter_map = map_to_ugandaemr(art_encounter_map, None, '99038')  # ARV REGIMEN DOSE
art_encounter_map = map_to_ugandaemr(art_encounter_map, None, '99036')  # ARV REGIMEN DAYS DISPENSED
art_encounter_map = map_to_ugandaemr(art_encounter_map, None, '5497')  # CD4 COUNT
art_encounter_map = map_to_ugandaemr(art_encounter_map, None, '730')  # CD4%
art_encounter_map = map_to_ugandaemr(art_encounter_map, None, '99151')  # CD4% CLASSIFICATION FOR INFANTS
art_encounter_map = map_to_ugandaemr(art_encounter_map, None, '163023')  # HIV VIRAL LOAD DATE
art_encounter_map = map_to_ugandaemr(art_encounter_map, None, '1305')  # VIRAL LOAD QUALITATIVE
art_encounter_map = map_to_ugandaemr(art_encounter_map, None, '856')  # HIV VIRAL LOAD
art_encounter_map = map_to_ugandaemr(art_encounter_map, None, '1271')  # TESTS ORDERED
art_encounter_map = map_to_ugandaemr(art_encounter_map, None, '99114')  # OTHER TESTS ORDERED
art_encounter_map = map_to_ugandaemr(art_encounter_map, None, '21')  # HEMOGLOBIN
art_encounter_map = map_to_ugandaemr(art_encounter_map, None, '856')  # HIV VIRAL LOAD
