from data_import import map_to_ugandaemr
from common import *

art_summary_map = {}
art_summary_map = map_to_ugandaemr(art_summary_map, '1', '90267')  # DATE POSITIVE HIV TEST CONFIRMED
art_summary_map = map_to_ugandaemr(art_summary_map, '2', '99080')  # HIV TEST
art_summary_map = map_to_ugandaemr(art_summary_map, '3', '99081')  # HIV TEST FACILITY
art_summary_map = map_to_ugandaemr(art_summary_map, '4', '90200')  # ENTRY POINT INTO HIV CARE
art_summary_map = map_to_ugandaemr(art_summary_map, '5', '99115')  # OTHER CARE ENTRY POINT
art_summary_map = map_to_ugandaemr(art_summary_map, '6', '99142')  # TREATMENT SUPPORTER NAME
art_summary_map = map_to_ugandaemr(art_summary_map, '7', '99138')  # TREATMENT SUPPORTER DISTRICT
art_summary_map = map_to_ugandaemr(art_summary_map, '8', '99139')  # TREATMENT SUPPORTER SUB COUNTY
art_summary_map = map_to_ugandaemr(art_summary_map, '9', '99140')  # TREATMENT SUPPORTER PARISH
art_summary_map = map_to_ugandaemr(art_summary_map, '10', '99141')  # TREATMENT SUPPORTER VILLAGE
art_summary_map = map_to_ugandaemr(art_summary_map, '11', '90278')  # TREATMENT SUPPORTER TELEPHONE NUMBER
art_summary_map = map_to_ugandaemr(art_summary_map, '12', '99124')  # HOME BASED CARE PROVIDED BY

# ------------ Beginning of family member group -----------------------
# Repeat this section if there is more than one family member and change the group number accordingly
art_summary_map = map_to_ugandaemr(art_summary_map, '13', '99073', group_concept=99075,
                                   group_no=1)  # NAME OF FAMILY MEMBER
art_summary_map = map_to_ugandaemr(art_summary_map, '14', '99074', group_concept=99075,
                                   group_no=1)  # AGE OF FAMILY MEMBER
art_summary_map = map_to_ugandaemr(art_summary_map, '15', '99725', group_concept=99075, group_no=1)  # Age Unit
art_summary_map = map_to_ugandaemr(art_summary_map, '16', '90253', group_concept=99075, group_no=1)  # HIV STATUS
art_summary_map = map_to_ugandaemr(art_summary_map, '17', '90270', group_concept=99075, group_no=1)  # HIV CARE STATUS
art_summary_map = map_to_ugandaemr(art_summary_map, '18', '90263', group_concept=99075,
                                   group_no=1)  # PATIENT UNIQUE IDENTIFIER
# ------------ End of family member group -----------------------


# ------------ Beginning of EID SET -----------------------
# Repeat this section if there is more than one EID
art_summary_map = map_to_ugandaemr(art_summary_map, '19', '99077', group_concept=99078,
                                   group_no=1)  # EXPOSED INFANT IDENTITY
art_summary_map = map_to_ugandaemr(art_summary_map, '20', '90261', group_concept=99078,
                                   group_no=1)  # DATE OF BIRTH
art_summary_map = map_to_ugandaemr(art_summary_map, '21', '99607', group_concept=99078,
                                   group_no=1)  # Infant Feeding Status (< 6 months)
art_summary_map = map_to_ugandaemr(art_summary_map, '22', '99608', group_concept=99078,
                                   group_no=1)  # Infant Feeding Status (> 6 months)
art_summary_map = map_to_ugandaemr(art_summary_map, '23', '99076', group_concept=99078,
                                   group_no=1)  # COTRIMOXAZOLE AT 3 MONTHS
art_summary_map = map_to_ugandaemr(art_summary_map, '24', '99606', group_concept=99078,
                                   group_no=1)  # Date of 1st PCR
art_summary_map = map_to_ugandaemr(art_summary_map, '25', '99153', group_concept=99078,
                                   group_no=1)  # HIV TEST RESULT OF INFANT
art_summary_map = map_to_ugandaemr(art_summary_map, '26', '99121', group_concept=99078,
                                   group_no=1)  # FINAL STATUS OF THE EXPOSED INFANT
art_summary_map = map_to_ugandaemr(art_summary_map, '27', '90263', group_concept=99078,
                                   group_no=1)  # PATIENT UNIQUE IDENTIFIER
# ------------ End of EID SET -----------------------

# ------------ PEP group -----------------------
art_summary_map = map_to_ugandaemr(art_summary_map, '28', '99056', group_concept=99066,
                                   group_no=1)  # POST EXPOSURE PROPHYLAXIS
art_summary_map = map_to_ugandaemr(art_summary_map, '29', '99154', group_concept=99066,
                                   group_no=1)  # PEP REGIMEN START DATE
art_summary_map = map_to_ugandaemr(art_summary_map, '30', '99057', group_concept=99066,
                                   group_no=1)  # POST EXPOSURE PROPHYLAXIS FACILITY
art_summary_map = map_to_ugandaemr(art_summary_map, '31', '99130', group_concept=99066, group_no=1)  # PEP REGIMEN
# ------------ End of PEP -----------------------

# ------------ HEP-B PRIOR ART SET -----------------------
art_summary_map = map_to_ugandaemr(art_summary_map, '28', '99594', group_concept=99598,
                                   group_no=1)  # Hep-B prior ART
art_summary_map = map_to_ugandaemr(art_summary_map, '29', '99595', group_concept=99598,
                                   group_no=1)  # HEP-B prior ART REGIMEN START DATE
art_summary_map = map_to_ugandaemr(art_summary_map, '30', '99596', group_concept=99598,
                                   group_no=1)  # HEP-B prior ART FACILITY
art_summary_map = map_to_ugandaemr(art_summary_map, '31', '99597', group_concept=99598,
                                   group_no=1)  # HEP-B  PRIOR ART REGIMEN
# ------------ End of PEP -----------------------

# ------------ PMTCT SET -----------------------
art_summary_map = map_to_ugandaemr(art_summary_map, '32', '90012', group_concept=99067,
                                   group_no=1)  # PMTCT
art_summary_map = map_to_ugandaemr(art_summary_map, '33', '99155', group_concept=99067,
                                   group_no=1)  # PMTCT REGIMEN START DATE
art_summary_map = map_to_ugandaemr(art_summary_map, '34', '99058', group_concept=99067,
                                   group_no=1)  # PMTCT FACILITY
art_summary_map = map_to_ugandaemr(art_summary_map, '35', '99131', group_concept=99067,
                                   group_no=1)  # REGIMEN
# ------------ End of PMTCT -----------------------

# ------------ EARLIER ARV NOT TRANSFER SET -----------------------
art_summary_map = map_to_ugandaemr(art_summary_map, '36', '99059', group_concept=99078,
                                   group_no=1)  # PRIOR ART NOT TRANSFER
art_summary_map = map_to_ugandaemr(art_summary_map, '37', '99156', group_concept=99078,
                                   group_no=1)  # EARLIER ARV NOT TRANSFER START DATE
art_summary_map = map_to_ugandaemr(art_summary_map, '38', '99060', group_concept=99078,
                                   group_no=1)  # PLACE WHERE RECEIVED ARVS FROM - NOT TRANSFER
art_summary_map = map_to_ugandaemr(art_summary_map, '39', '99129', group_concept=99078,
                                   group_no=1)  # EARLIER ARVS NOT TRANSFER
# ------------ End of EID SET -----------------------

art_summary_map = map_to_ugandaemr(art_summary_map, '40', '99110')  # TRANSFER IN
art_summary_map = map_to_ugandaemr(art_summary_map, '41', '99109')  # TRANSFER INPLACE
art_summary_map = map_to_ugandaemr(art_summary_map, '42', '90297')  # DATE DETERMINED MEDICALLY ELIGIBLE TO START ART
art_summary_map = map_to_ugandaemr(art_summary_map, '43', '99083')  # ELIGIBLE FOR ART STAGE
art_summary_map = map_to_ugandaemr(art_summary_map, '44', '99082')  # ELIGIBLE FOR ART CD4
art_summary_map = map_to_ugandaemr(art_summary_map, '45', '99600')  # TB FOR ART
art_summary_map = map_to_ugandaemr(art_summary_map, '46', '99601')  # BREAST FEEDING
art_summary_map = map_to_ugandaemr(art_summary_map, '47', '99602')  # ELIGIBLE FOR ART PREGNANT
art_summary_map = map_to_ugandaemr(art_summary_map, '48',
                                   '90299')  # DATE DETERMINED MEDICALLY ELIGIBLE AND RAEDY TO START ART

