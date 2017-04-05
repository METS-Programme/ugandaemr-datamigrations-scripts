from core.common import *
from core.data_import import map_to_ugandaemr

eid_summary_map = {}
eid_summary_map = map_to_ugandaemr(eid_summary_map, None, '90200', answer_dict=entry_point)  # Entry point
eid_summary_map = map_to_ugandaemr(eid_summary_map, None, '99771')  # Date of NVP start
eid_summary_map = map_to_ugandaemr(eid_summary_map, None, '99773')  # Date of Cotrim initiation
eid_summary_map = map_to_ugandaemr(eid_summary_map, None, '99776')  # EID Mother's first name
eid_summary_map = map_to_ugandaemr(eid_summary_map, None, '99775')  # EID Mother's surname
eid_summary_map = map_to_ugandaemr(eid_summary_map, None, '162889')  # EID Mother's telephone number
eid_summary_map = map_to_ugandaemr(eid_summary_map, None, '162884')  # EID Mother's district
eid_summary_map = map_to_ugandaemr(eid_summary_map, None, '162885')  # EID Mother's county
eid_summary_map = map_to_ugandaemr(eid_summary_map, None, '162886')  # EID Mother's sub-county
eid_summary_map = map_to_ugandaemr(eid_summary_map, None, '162887')  # EID Mother's village
eid_summary_map = map_to_ugandaemr(eid_summary_map, None, '162888')  # EID Mother's parish
eid_summary_map = map_to_ugandaemr(eid_summary_map, None, '99137')  # Patient village
eid_summary_map = map_to_ugandaemr(eid_summary_map, None, '162867')  # Outreach Introduction Method
eid_summary_map = map_to_ugandaemr(eid_summary_map, None, '162866')  # LC1 Chairman
eid_summary_map = map_to_ugandaemr(eid_summary_map, None, '162868')  # Directions to caregiver's home address
eid_summary_map = map_to_ugandaemr(eid_summary_map, None, '162869')  # Alternative Contact Person
eid_summary_map = map_to_ugandaemr(eid_summary_map, None, '90269', answer_dict=relationship)  # Relationship
eid_summary_map = map_to_ugandaemr(eid_summary_map, None, '162870')  # Alternative Telephone No
eid_summary_map = map_to_ugandaemr(eid_summary_map, None, '162871',
                                   answer_dict=no_yes)  # Has This Person been disclosed to?
eid_summary_map = map_to_ugandaemr(eid_summary_map, None, '99570')  # Delivered By
eid_summary_map = map_to_ugandaemr(eid_summary_map, None, '5630', answer_dict=mode_of_delivery)  # METHOD OF DELIVERY
eid_summary_map = map_to_ugandaemr(eid_summary_map, None, '162872', answer_dict=no_yes)  # Mother received ARV for PMTCT
eid_summary_map = map_to_ugandaemr(eid_summary_map, None, '99777')  # EID Mother's ANC No.
_summary_map = map_to_ugandaemr(eid_summary_map, None, '99783',
                                answer_dict=mothers_arvs_for_pmtct)  # Mother's ARVs for eMTCT - ANC
eid_summary_map = map_to_ugandaemr(eid_summary_map, None, '99784',
                                   answer_dict=mothers_arvs_for_pmtct)  # Mother's ARVs for eMTCT - Delivery
eid_summary_map = map_to_ugandaemr(eid_summary_map, None, '99785',
                                   answer_dict=mothers_arvs_for_pmtct)  # Mother's ARVs for eMTCT - Postnatal
eid_summary_map = map_to_ugandaemr(eid_summary_map, None, '99787', answer_dict=infant_arvs)  # Infant's ARVs
eid_summary_map = map_to_ugandaemr(eid_summary_map, None, '162873',
                                   answer_dict=no_yes)  # Mother in care at an ART Clinic
eid_summary_map = map_to_ugandaemr(eid_summary_map, None, '162875')  # Mother ART Clinic
eid_summary_map = map_to_ugandaemr(eid_summary_map, None, '162874')  # EID Mother's ART NO.

eid_summary_map = map_to_ugandaemr(eid_summary_map, None, '99606')  # Date of 1st PCR
eid_summary_map = map_to_ugandaemr(eid_summary_map, None, '99434', answer_dict=feeding_status)  # FS at 1st EID PCR Test
eid_summary_map = map_to_ugandaemr(eid_summary_map, None, '99435', answer_dict=result)  # 1st EID PCR Test Result
eid_summary_map = map_to_ugandaemr(eid_summary_map, None, '99438')  # Date of 1st EID PCR Test given to care provider
eid_summary_map = map_to_ugandaemr(eid_summary_map, None, '99436')  # Date of 2nd EID PCR Test
eid_summary_map = map_to_ugandaemr(eid_summary_map, None, '99794', answer_dict=feeding_status)  # FS at 2nd EID PCR Test
eid_summary_map = map_to_ugandaemr(eid_summary_map, None, '99440', answer_dict=result)  # 2nd EID PCR Test Result
eid_summary_map = map_to_ugandaemr(eid_summary_map, None,
                                   '99442')  # Date 2nd EID PCR Test result given to care provider
eid_summary_map = map_to_ugandaemr(eid_summary_map, None, '162876')  # Repeat PCR Test Date
eid_summary_map = map_to_ugandaemr(eid_summary_map, None, '162877',
                                   answer_dict=feeding_status)  # FS at EID Repeat PCR Test
eid_summary_map = map_to_ugandaemr(eid_summary_map, None, '162881', answer_dict=result)  # EID Repeat PCR Test Result
eid_summary_map = map_to_ugandaemr(eid_summary_map, None,
                                   '162882')  # Date Repeat EID PCR Test result given to care provider
eid_summary_map = map_to_ugandaemr(eid_summary_map, None, '162879')  # 18 Months Raid PCR Test Date
eid_summary_map = map_to_ugandaemr(eid_summary_map, None, '162878',
                                   answer_dict=feeding_status)  # FS at 18 Month Raid Test
eid_summary_map = map_to_ugandaemr(eid_summary_map, None, '162880',
                                   answer_dict=result)  # 18 Month Raid EID PCR Test Result
eid_summary_map = map_to_ugandaemr(eid_summary_map, None,
                                   '162883')  # Date 18 Month Raid Test result given to care provider
eid_summary_map = map_to_ugandaemr(eid_summary_map, None, '99797', answer_dict=result)  # Final EID PCR Test Result
eid_summary_map = map_to_ugandaemr(eid_summary_map, None, '99795')  # Date of final EID PCR test Result
eid_summary_map = map_to_ugandaemr(eid_summary_map, None, '99430', answer_dict=no_yes_1)  # Referred for ART Clinic
eid_summary_map = map_to_ugandaemr(eid_summary_map, None, '162981')  # EID Referred for ART Clinic Date
eid_summary_map = map_to_ugandaemr(eid_summary_map, None, '163004',
                                   answer_dict=no_yes_1)  # enrolled in HIV care program
eid_summary_map = map_to_ugandaemr(eid_summary_map, None, '162980')  # EID Care Enrollment Date
eid_summary_map = map_to_ugandaemr(eid_summary_map, None, '99751')  # Pre-ART number
eid_summary_map = map_to_ugandaemr(eid_summary_map, None, '163003', answer_dict=no_yes)  # Presumptive Referral
eid_summary_map = map_to_ugandaemr(eid_summary_map, None, '162967')  # EID Follow Up. First attempt dat
eid_summary_map = map_to_ugandaemr(eid_summary_map, None, '162968')  # EID Follow Up. First attempt method
eid_summary_map = map_to_ugandaemr(eid_summary_map, None, '162969')  # EID Follow Up. First attempt outcome
eid_summary_map = map_to_ugandaemr(eid_summary_map, None, '162971')  # EID Follow Up. Second attempt date
eid_summary_map = map_to_ugandaemr(eid_summary_map, None, '162972')  # EID Follow Up. Second attempt method
eid_summary_map = map_to_ugandaemr(eid_summary_map, None, '162973')  # EID Follow Up. Second attempt outcome (162973)
eid_summary_map = map_to_ugandaemr(eid_summary_map, None, '162975')  # EID Follow Up. Third attempt date
eid_summary_map = map_to_ugandaemr(eid_summary_map, None, '162976')  # EID Follow Up. Third attempt method
eid_summary_map = map_to_ugandaemr(eid_summary_map, None, '162977')  # EID Follow Up. Third attempt outcome
eid_summary_map = map_to_ugandaemr(eid_summary_map, None, '99428', answer_dict=final_outcome)  # EID Final Outcome
eid_summary_map = map_to_ugandaemr(eid_summary_map, None, '162979')  # EID Final Outcome Date
