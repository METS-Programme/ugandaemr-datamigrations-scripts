from data_import import map_to_ugandaemr
from common import *

eid_summary_map = {}
eid_summary_map = map_to_ugandaemr(eid_summary_map, '1', '')
eid_summary_map = map_to_ugandaemr(eid_summary_map, '2', '')
eid_summary_map = map_to_ugandaemr(eid_summary_map, '3', '')
eid_summary_map = map_to_ugandaemr(eid_summary_map, '4', '')
eid_summary_map = map_to_ugandaemr(eid_summary_map, '5', '')
eid_summary_map = map_to_ugandaemr(eid_summary_map, '6', '90200', answer_dict=entry_point)
eid_summary_map = map_to_ugandaemr(eid_summary_map, '7', '')
eid_summary_map = map_to_ugandaemr(eid_summary_map, '8', '')
eid_summary_map = map_to_ugandaemr(eid_summary_map, '9', '')
eid_summary_map = map_to_ugandaemr(eid_summary_map, '10', '99771')  # Date of NVP start
eid_summary_map = map_to_ugandaemr(eid_summary_map, '11', '99773')  # Date of Cotrim initiation
eid_summary_map = map_to_ugandaemr(eid_summary_map, '12', '99776')  # EID Mother's first name
eid_summary_map = map_to_ugandaemr(eid_summary_map, '13', '99775')  # EID Mother's surname
eid_summary_map = map_to_ugandaemr(eid_summary_map, '14', '162889')  # EID Mother's telephone number
eid_summary_map = map_to_ugandaemr(eid_summary_map, '15', '162884')  # EID Mother's district
eid_summary_map = map_to_ugandaemr(eid_summary_map, '16', '162885')  # EID Mother's county
eid_summary_map = map_to_ugandaemr(eid_summary_map, '17', '162886')  # EID Mother's sub-county
eid_summary_map = map_to_ugandaemr(eid_summary_map, '18', '162887')  # EID Mother's village
eid_summary_map = map_to_ugandaemr(eid_summary_map, '19', '162888')  # EID Mother's parish
eid_summary_map = map_to_ugandaemr(eid_summary_map, '20', '99137')  # Patient village
eid_summary_map = map_to_ugandaemr(eid_summary_map, '21', '162866')  # LC1 Chairman
eid_summary_map = map_to_ugandaemr(eid_summary_map, '22', '162867')  # Outreach Introduction Method
eid_summary_map = map_to_ugandaemr(eid_summary_map, '23', '162868')  # Directions to caregiver's home address
eid_summary_map = map_to_ugandaemr(eid_summary_map, '24', '162869')  # Alternative Contact Person
eid_summary_map = map_to_ugandaemr(eid_summary_map, '25', '90269', answer_dict=relationship)  # Relationship
eid_summary_map = map_to_ugandaemr(eid_summary_map, '26', '162870')  # Alternative Telephone No
eid_summary_map = map_to_ugandaemr(eid_summary_map, '27', '162871',
                                   answer_dict=no_yes)  # Has This Person been disclosed to?
eid_summary_map = map_to_ugandaemr(eid_summary_map, '28', '99570')  # Delivered By
eid_summary_map = map_to_ugandaemr(eid_summary_map, '29', '5630', answer_dict=mode_of_delivery)  # METHOD OF DELIVERY
eid_summary_map = map_to_ugandaemr(eid_summary_map, '30', '162872', answer_dict=no_yes)  # Mother received ARV for PMTCT
eid_summary_map = map_to_ugandaemr(eid_summary_map, '31', '99777')  # EID Mother's ANC No.
eid_summary_map = map_to_ugandaemr(eid_summary_map, '32', '99783',
                                   answer_dict=mothers_arvs_for_pmtct)  # Mother's ARVs for eMTCT - ANC
eid_summary_map = map_to_ugandaemr(eid_summary_map, '33', '99787', answer_dict=infant_arvs)  # Infant's ARVs
eid_summary_map = map_to_ugandaemr(eid_summary_map, '34', '162873',
                                   answer_dict=no_yes)  # Mother in care at an ART Clinic
eid_summary_map = map_to_ugandaemr(eid_summary_map, '35', '162875')  # Mother ART Clinic
eid_summary_map = map_to_ugandaemr(eid_summary_map, '36', '162874')  # EID Mother's ART NO.
eid_summary_map = map_to_ugandaemr(eid_summary_map, '37', '99783',
                                   answer_dict=mothers_arvs_for_pmtct)  # Mother's ARVs for eMTCT - ANC
eid_summary_map = map_to_ugandaemr(eid_summary_map, '38', '99784',
                                   answer_dict=mothers_arvs_for_pmtct)  # Mother's ARVs for eMTCT - Delivery
eid_summary_map = map_to_ugandaemr(eid_summary_map, '39', '99785',
                                   answer_dict=mothers_arvs_for_pmtct)  # Mother's ARVs for eMTCT - Postnatal
eid_summary_map = map_to_ugandaemr(eid_summary_map, '40', '99606')  # Date of 1st PCR
eid_summary_map = map_to_ugandaemr(eid_summary_map, '41', '99435', answer_dict=result)  # 1st EID PCR Test Result
eid_summary_map = map_to_ugandaemr(eid_summary_map, '42', '99434', answer_dict=feeding_status)  # FS at 1st EID PCR Test
eid_summary_map = map_to_ugandaemr(eid_summary_map, '43', '99438')  # Date of 1st EID PCR Test given to care provider
eid_summary_map = map_to_ugandaemr(eid_summary_map, '44', '99436')  # Date of 2nd EID PCR Test
eid_summary_map = map_to_ugandaemr(eid_summary_map, '45', '99440', answer_dict=result)  # 2nd EID PCR Test Result
eid_summary_map = map_to_ugandaemr(eid_summary_map, '46', '99794', answer_dict=feeding_status)  # FS at 2nd EID PCR Test
eid_summary_map = map_to_ugandaemr(eid_summary_map, '47',
                                   '99442')  # Date 2nd EID PCR Test result given to care provider
eid_summary_map = map_to_ugandaemr(eid_summary_map, '48', '162876')  # Repeat PCR Test Date
eid_summary_map = map_to_ugandaemr(eid_summary_map, '49', '162881', answer_dict=result)  # EID Repeat PCR Test Result
eid_summary_map = map_to_ugandaemr(eid_summary_map, '50', '162877',
                                   answer_dict=feeding_status)  # FS at EID Repeat PCR Test
eid_summary_map = map_to_ugandaemr(eid_summary_map, '51',
                                   '162882')  # Date Repeat EID PCR Test result given to care provider
eid_summary_map = map_to_ugandaemr(eid_summary_map, '52', '162879')  # 18 Months Raid PCR Test Date
eid_summary_map = map_to_ugandaemr(eid_summary_map, '53', '162880',
                                   answer_dict=result)  # 18 Month Raid EID PCR Test Result
eid_summary_map = map_to_ugandaemr(eid_summary_map, '54', '162878',
                                   answer_dict=feeding_status)  # FS at 18 Month Raid Test
eid_summary_map = map_to_ugandaemr(eid_summary_map, '55',
                                   '162883')  # Date 18 Month Raid Test result given to care provider
eid_summary_map = map_to_ugandaemr(eid_summary_map, '56', '99797', answer_dict=result)  # Final EID PCR Test Result
eid_summary_map = map_to_ugandaemr(eid_summary_map, '57', '99430', answer_dict=no_yes_1)  # Referred for ART Clinic
eid_summary_map = map_to_ugandaemr(eid_summary_map, '58', '162981')  # EID Referred for ART Clinic Date
eid_summary_map = map_to_ugandaemr(eid_summary_map, '59', '163004',
                                   answer_dict=no_yes_1)  # enrolled in HIV care program
eid_summary_map = map_to_ugandaemr(eid_summary_map, '60', '162980')  # EID Care Enrollment Date
eid_summary_map = map_to_ugandaemr(eid_summary_map, '61', '163003', answer_dict=no_yes)  # Presumptive Referral
eid_summary_map = map_to_ugandaemr(eid_summary_map, '62', '162967')  # EID Follow Up. First attempt dat
eid_summary_map = map_to_ugandaemr(eid_summary_map, '63', '162968')  # EID Follow Up. First attempt method
eid_summary_map = map_to_ugandaemr(eid_summary_map, '64', '162969')  # EID Follow Up. First attempt outcome
eid_summary_map = map_to_ugandaemr(eid_summary_map, '65', '162971')  # EID Follow Up. Second attempt date
eid_summary_map = map_to_ugandaemr(eid_summary_map, '66', '162972')  # EID Follow Up. Second attempt method
eid_summary_map = map_to_ugandaemr(eid_summary_map, '67', '162973')  # EID Follow Up. Second attempt outcome (162973)
eid_summary_map = map_to_ugandaemr(eid_summary_map, '68', '162975')  # EID Follow Up. Third attempt date
eid_summary_map = map_to_ugandaemr(eid_summary_map, '69', '162976')  # EID Follow Up. Third attempt method
eid_summary_map = map_to_ugandaemr(eid_summary_map, '70', '162977')  # EID Follow Up. Third attempt outcome
eid_summary_map = map_to_ugandaemr(eid_summary_map, '71', '99428', answer_dict=final_outcome)  # EID Final Outcome
eid_summary_map = map_to_ugandaemr(eid_summary_map, '72', '')
eid_summary_map = map_to_ugandaemr(eid_summary_map, '73', '162979')  # EID Final Outcome Date
eid_summary_map = map_to_ugandaemr(eid_summary_map, '74', '')
eid_summary_map = map_to_ugandaemr(eid_summary_map, '75', '')
