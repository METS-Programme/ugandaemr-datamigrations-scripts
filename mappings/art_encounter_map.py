from data_import import map_to_ugandaemr
from common import *

art_encounter_map = {}
art_encounter_map = map_to_ugandaemr(art_encounter_map, '1', '')
art_encounter_map = map_to_ugandaemr(art_encounter_map, '2', '')
art_encounter_map = map_to_ugandaemr(art_encounter_map, '3', '')
art_encounter_map = map_to_ugandaemr(art_encounter_map, '4', '90069')  # SCHEDULED PATIENT VISIST
art_encounter_map = map_to_ugandaemr(art_encounter_map, '5', '5096')  # Return date
art_encounter_map = map_to_ugandaemr(art_encounter_map, '6', '99024')  # Duration(Months since baseline):
art_encounter_map = map_to_ugandaemr(art_encounter_map, '7', '99025')  # Duration:(Months on current regimen)
art_encounter_map = map_to_ugandaemr(art_encounter_map, '8', '90236')  # BODY WEIGHT
art_encounter_map = map_to_ugandaemr(art_encounter_map, '9', '5090')  # Height (cm)
art_encounter_map = map_to_ugandaemr(art_encounter_map, '10', '99030')  # MID-UPPER ARM CIRCUMFERENCE-CODE
art_encounter_map = map_to_ugandaemr(art_encounter_map, '11', '90216')  # TUBERCULOSIS STATUS
art_encounter_map = map_to_ugandaemr(art_encounter_map, '12', '90217')  # TUBERCULOSIS TREATMENT START DATE
art_encounter_map = map_to_ugandaemr(art_encounter_map, '13', '90310')  # TUBERCULOSIS TREATMENT STOP DATE
art_encounter_map = map_to_ugandaemr(art_encounter_map, '14', '')
art_encounter_map = map_to_ugandaemr(art_encounter_map, '15', '90227')  # MEDICATION OR OTHER SIDE EFFECTS
art_encounter_map = map_to_ugandaemr(art_encounter_map, '16', '90251')  # SYMPTOM, DIAGNOSIS, OR OPPORTUNISTIC INFECTION
art_encounter_map = map_to_ugandaemr(art_encounter_map, '17', '90235')  # HISTORY OF FUNCTIONAL STATUS
art_encounter_map = map_to_ugandaemr(art_encounter_map, '18', '90203')  # WHO HIV CLINICAL STAGE
art_encounter_map = map_to_ugandaemr(art_encounter_map, '19', '90156')  # ADHERENCE TO COTRIMOXZOLE
art_encounter_map = map_to_ugandaemr(art_encounter_map, '20',
                                     '99033')  # TRIMETHOPRIM AND SULFAMETHOXAZOLE DAYS DISPENSED
art_encounter_map = map_to_ugandaemr(art_encounter_map, '21', '99037')  # TRIMETHOPRIM AND SULFAMETHOXAZOLE DOSAGE

art_encounter_map = map_to_ugandaemr(art_encounter_map, '22', '99604')  # INH DOSAGE
art_encounter_map = map_to_ugandaemr(art_encounter_map, '23', '1193') # CURRENT DRUGS USED
art_encounter_map = map_to_ugandaemr(art_encounter_map, '24', '90221') # ANTI-RETROVIRAL DRUG ADHERENCE ASSESSMENT CODE
art_encounter_map = map_to_ugandaemr(art_encounter_map, '25', '90223') # REASON FOR MISSING ANTI-RETROVIRAL DRUG ADMINISTRATION SCHEDULE
art_encounter_map = map_to_ugandaemr(art_encounter_map, '26', '90315') # CURRENT ARV REGIMEN
art_encounter_map = map_to_ugandaemr(art_encounter_map, '27', '99038') # AR REGIMEN DOSE
art_encounter_map = map_to_ugandaemr(art_encounter_map, '28', '99036') # ARV REGIMEN DAYS DISPENSED
art_encounter_map = map_to_ugandaemr(art_encounter_map, '29', '5497') # CD4 COUNT
art_encounter_map = map_to_ugandaemr(art_encounter_map, '30', '730') # CD4%
