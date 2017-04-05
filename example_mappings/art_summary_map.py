from core.data_import import map_to_ugandaemr

art_summary_map = {}
art_summary_map = map_to_ugandaemr(art_summary_map, None, '90267')  # DATE POSITIVE HIV TEST CONFIRMED
art_summary_map = map_to_ugandaemr(art_summary_map, None, '99080')  # HIV TEST
art_summary_map = map_to_ugandaemr(art_summary_map, None, '99081')  # HIV TEST FACILITY
art_summary_map = map_to_ugandaemr(art_summary_map, None, '90200')  # ENTRY POINT INTO HIV CARE
art_summary_map = map_to_ugandaemr(art_summary_map, None, '99115')  # OTHER CARE ENTRY POINT
art_summary_map = map_to_ugandaemr(art_summary_map, None, '99142')  # TREATMENT SUPPORTER NAME
art_summary_map = map_to_ugandaemr(art_summary_map, None, '99138')  # TREATMENT SUPPORTER DISTRICT
art_summary_map = map_to_ugandaemr(art_summary_map, None, '99139')  # TREATMENT SUPPORTER SUB COUNTY
art_summary_map = map_to_ugandaemr(art_summary_map, None, '99140')  # TREATMENT SUPPORTER PARISH
art_summary_map = map_to_ugandaemr(art_summary_map, None, '99141')  # TREATMENT SUPPORTER VILLAGE
art_summary_map = map_to_ugandaemr(art_summary_map, None, '90278')  # TREATMENT SUPPORTER TELEPHONE NUMBER
art_summary_map = map_to_ugandaemr(art_summary_map, None, '99124')  # HOME BASED CARE PROVIDED BY

# ------------ Beginning of family member group -----------------------
# Repeat this section if there is more than one family member and change the group number accordingly
art_summary_map = map_to_ugandaemr(art_summary_map, None, '99073', group_concept=99075,
                                   group_no=1)  # NAME OF FAMILY MEMBER
art_summary_map = map_to_ugandaemr(art_summary_map, None, '99074', group_concept=99075,
                                   group_no=1)  # AGE OF FAMILY MEMBER
art_summary_map = map_to_ugandaemr(art_summary_map, None, '99725', group_concept=99075, group_no=1)  # Age Unit
art_summary_map = map_to_ugandaemr(art_summary_map, None, '90253', group_concept=99075, group_no=1)  # HIV STATUS
art_summary_map = map_to_ugandaemr(art_summary_map, None, '90270', group_concept=99075, group_no=1)  # HIV CARE STATUS
art_summary_map = map_to_ugandaemr(art_summary_map, None, '90263', group_concept=99075,
                                   group_no=1)  # PATIENT UNIQUE IDENTIFIER
# ------------ End of family member group -----------------------


# ------------ Beginning of EID SET -----------------------
# Repeat this section if there is more than one EID
art_summary_map = map_to_ugandaemr(art_summary_map, None, '99077', group_concept=99078,
                                   group_no=1)  # EXPOSED INFANT IDENTITY
art_summary_map = map_to_ugandaemr(art_summary_map, None, '90261', group_concept=99078,
                                   group_no=1)  # DATE OF BIRTH
art_summary_map = map_to_ugandaemr(art_summary_map, None, '99607', group_concept=99078,
                                   group_no=1)  # Infant Feeding Status (< 6 months)
art_summary_map = map_to_ugandaemr(art_summary_map, None, '99608', group_concept=99078,
                                   group_no=1)  # Infant Feeding Status (> 6 months)
art_summary_map = map_to_ugandaemr(art_summary_map, None, '99076', group_concept=99078,
                                   group_no=1)  # COTRIMOXAZOLE AT 3 MONTHS
art_summary_map = map_to_ugandaemr(art_summary_map, None, '99606', group_concept=99078,
                                   group_no=1)  # Date of 1st PCR
art_summary_map = map_to_ugandaemr(art_summary_map, None, '99153', group_concept=99078,
                                   group_no=1)  # HIV TEST RESULT OF INFANT
art_summary_map = map_to_ugandaemr(art_summary_map, None, '99121', group_concept=99078,
                                   group_no=1)  # FINAL STATUS OF THE EXPOSED INFANT
art_summary_map = map_to_ugandaemr(art_summary_map, None, '90263', group_concept=99078,
                                   group_no=1)  # PATIENT UNIQUE IDENTIFIER
# ------------ End of EID SET -----------------------

# ------------ PEP group -----------------------
art_summary_map = map_to_ugandaemr(art_summary_map, None, '99056', group_concept=99066,
                                   group_no=1)  # POST EXPOSURE PROPHYLAXIS
art_summary_map = map_to_ugandaemr(art_summary_map, None, '99154', group_concept=99066,
                                   group_no=1)  # PEP REGIMEN START DATE
art_summary_map = map_to_ugandaemr(art_summary_map, None, '99057', group_concept=99066,
                                   group_no=1)  # POST EXPOSURE PROPHYLAXIS FACILITY
art_summary_map = map_to_ugandaemr(art_summary_map, None, '99130', group_concept=99066, group_no=1)  # PEP REGIMEN
# ------------ End of PEP -----------------------

# ------------ HEP-B PRIOR ART SET -----------------------
art_summary_map = map_to_ugandaemr(art_summary_map, None, '99594', group_concept=99598,
                                   group_no=1)  # Hep-B prior ART
art_summary_map = map_to_ugandaemr(art_summary_map, None, '99595', group_concept=99598,
                                   group_no=1)  # HEP-B prior ART REGIMEN START DATE
art_summary_map = map_to_ugandaemr(art_summary_map, None, '99596', group_concept=99598,
                                   group_no=1)  # HEP-B prior ART FACILITY
art_summary_map = map_to_ugandaemr(art_summary_map, None, '99597', group_concept=99598,
                                   group_no=1)  # HEP-B  PRIOR ART REGIMEN
# ------------ End of PEP -----------------------

# ------------ PMTCT SET -----------------------
art_summary_map = map_to_ugandaemr(art_summary_map, None, '90012', group_concept=99067,
                                   group_no=1)  # PMTCT
art_summary_map = map_to_ugandaemr(art_summary_map, None, '99155', group_concept=99067,
                                   group_no=1)  # PMTCT REGIMEN START DATE
art_summary_map = map_to_ugandaemr(art_summary_map, None, '99058', group_concept=99067,
                                   group_no=1)  # PMTCT FACILITY
art_summary_map = map_to_ugandaemr(art_summary_map, None, '99131', group_concept=99067,
                                   group_no=1)  # REGIMEN
# ------------ End of PMTCT -----------------------

# ------------ EARLIER ARV NOT TRANSFER SET -----------------------
art_summary_map = map_to_ugandaemr(art_summary_map, None, '99059', group_concept=99078,
                                   group_no=1)  # PRIOR ART NOT TRANSFER
art_summary_map = map_to_ugandaemr(art_summary_map, None, '99156', group_concept=99078,
                                   group_no=1)  # EARLIER ARV NOT TRANSFER START DATE
art_summary_map = map_to_ugandaemr(art_summary_map, None, '99060', group_concept=99078,
                                   group_no=1)  # PLACE WHERE RECEIVED ARVS FROM - NOT TRANSFER
art_summary_map = map_to_ugandaemr(art_summary_map, None, '99129', group_concept=99078,
                                   group_no=1)  # EARLIER ARVS NOT TRANSFER
# ------------ End of EARLIER ARV NOT TRANSFER SET -----------------------

art_summary_map = map_to_ugandaemr(art_summary_map, None, '99110')  # TRANSFER IN
art_summary_map = map_to_ugandaemr(art_summary_map, None, '99109')  # TRANSFER INPLACE
art_summary_map = map_to_ugandaemr(art_summary_map, None, '90297')  # DATE DETERMINED MEDICALLY ELIGIBLE TO START ART
art_summary_map = map_to_ugandaemr(art_summary_map, None, '99083')  # ELIGIBLE FOR ART STAGE
art_summary_map = map_to_ugandaemr(art_summary_map, None, '99082')  # ELIGIBLE FOR ART CD4
art_summary_map = map_to_ugandaemr(art_summary_map, None, '99600')  # TB FOR ART
art_summary_map = map_to_ugandaemr(art_summary_map, None, '99601')  # BREAST FEEDING
art_summary_map = map_to_ugandaemr(art_summary_map, None, '99602')  # ELIGIBLE FOR ART PREGNANT
art_summary_map = map_to_ugandaemr(art_summary_map, None,
                                   '90299')  # DATE DETERMINED MEDICALLY ELIGIBLE AND RAEDY TO START ART

# ------------ BASELINE REGIMEN SET -----------------------
art_summary_map = map_to_ugandaemr(art_summary_map, None, '99161', group_concept=99162,
                                   group_no=1)  # BASELINE REGIMEN START DATE
art_summary_map = map_to_ugandaemr(art_summary_map, None, '99061', group_concept=99162,
                                   group_no=1)  # BASELINE REGIMEN
art_summary_map = map_to_ugandaemr(art_summary_map, None, '99268', group_concept=99162,
                                   group_no=1)  # BASELINE REGIMEN OTHER
art_summary_map = map_to_ugandaemr(art_summary_map, None, '99069', group_concept=99162,
                                   group_no=1)  # BASELINE WEIGHT
art_summary_map = map_to_ugandaemr(art_summary_map, None, '99070', group_concept=99162,
                                   group_no=1)  # BASELINE STAGE
art_summary_map = map_to_ugandaemr(art_summary_map, None, '99061', group_concept=99162,
                                   group_no=1)  # BASELINE CD4
art_summary_map = map_to_ugandaemr(art_summary_map, None, '99071', group_concept=99162,
                                   group_no=1)  # BASELINE PREGNANCY
art_summary_map = map_to_ugandaemr(art_summary_map, None, '99072', group_concept=99162,
                                   group_no=1)  # BASELINE WEIGHT
art_summary_map = map_to_ugandaemr(art_summary_map, None, '99603', group_concept=99162,
                                   group_no=1)  # BASELINE LACTATING
# ------------ End of BASELINE REGIMEN SET -----------------------

art_summary_map = map_to_ugandaemr(art_summary_map, None, '99160')  # TRANSFER IN REGIMEN START DATE
art_summary_map = map_to_ugandaemr(art_summary_map, None, '90206')  # NAME OF LOCATION TRANSFERRED FROM
art_summary_map = map_to_ugandaemr(art_summary_map, None, '99064')  # TRANSFER IN REGIMEN
art_summary_map = map_to_ugandaemr(art_summary_map, None, '99269')  # TRANSFER IN REGIMEN OTHER

# ------------ FIRST LINE REGIMEN SET  -----------------------
art_summary_map = map_to_ugandaemr(art_summary_map, None, '99163', group_concept=99062,
                                   group_no=1)  # FIRST LINE REGIMEN SUBSTITION DATE
art_summary_map = map_to_ugandaemr(art_summary_map, None, '90315', group_concept=99062,
                                   group_no=1)  # CURRENT ARV REGIMEN
art_summary_map = map_to_ugandaemr(art_summary_map, None, '99146', group_concept=99062,
                                   group_no=1)  # OTHER FIRST LINE REGIMEN SPECIFY
art_summary_map = map_to_ugandaemr(art_summary_map, None, '90246', group_concept=99062,
                                   group_no=1)  # REASON FOR SUBSTITUTION WITHIN REGIMEN
# ------------ End of FIRST LINE REGIMEN SET  -----------------------


# ------------ SECOND LINE REGIMEN SET   -----------------------
art_summary_map = map_to_ugandaemr(art_summary_map, None, '99164', group_concept=99063,
                                   group_no=1)  # SECOND LINE REGIMEN SWITCH DATE
art_summary_map = map_to_ugandaemr(art_summary_map, None, '90315', group_concept=99063,
                                   group_no=1)  # CURRENT ARV REGIMEN
art_summary_map = map_to_ugandaemr(art_summary_map, None, '99147', group_concept=99063,
                                   group_no=1)  # OTHER SECOND LINE REGIMEN SPECIFY
art_summary_map = map_to_ugandaemr(art_summary_map, None, '90247', group_concept=99063,
                                   group_no=1)  # REASON FOR SUBSTITUTION WITHIN REGIMEN
# ------------ End of SECOND LINE REGIMEN SET   -----------------------

# ------------ THIRD LINE REGIMEN SET   -----------------------
art_summary_map = map_to_ugandaemr(art_summary_map, None, '162991', group_concept=162988,
                                   group_no=1)  # THIRD LINE REGIMEN SWITCH DATE
art_summary_map = map_to_ugandaemr(art_summary_map, None, '162990', group_concept=162988,
                                   group_no=1)  # CURRENT ARV REGIMEN
art_summary_map = map_to_ugandaemr(art_summary_map, None, '162989', group_concept=162988,
                                   group_no=1)  # OTHER THIRD LINE REGIMEN SPECIFY
art_summary_map = map_to_ugandaemr(art_summary_map, None, '90247', group_concept=162988,
                                   group_no=1)  # REASON FOR SUBSTITUTION WITHIN REGIMEN
# ------------ End of THIRD LINE REGIMEN SET   -----------------------


# ------------ ARV STOP SET    -----------------------
art_summary_map = map_to_ugandaemr(art_summary_map, None, '99132', group_concept=99086,
                                   group_no=1)  # ART TREATMENT INTERRUPTION
art_summary_map = map_to_ugandaemr(art_summary_map, None, '99084', group_concept=99086,
                                   group_no=1)  # ARV STOP DATE
art_summary_map = map_to_ugandaemr(art_summary_map, None, '1252', group_concept=99086,
                                   group_no=1)  # REASON ANTIRETROVIRALS STOPPED
art_summary_map = map_to_ugandaemr(art_summary_map, None, '99085', group_concept=99086,
                                   group_no=1)  # ARV RESTART DATE
# ------------ End of ARV STOP SET    -----------------------

# ------------ TRANSFER OUT SET    -----------------------
art_summary_map = map_to_ugandaemr(art_summary_map, None, '90306', group_concept=99166,
                                   group_no=1)  # TRANSFERED OUT TO ANOTHER FACILITY
art_summary_map = map_to_ugandaemr(art_summary_map, None, '99165', group_concept=99166,
                                   group_no=1)  # TRANSFER OUT DATE
art_summary_map = map_to_ugandaemr(art_summary_map, None, '90211', group_concept=99166,
                                   group_no=1)  # NAME OF LOCATION TRANSFERRED TO
# ------------ End of TRANSFER OUT SET    -----------------------

# ------------ LOST TO FOLLOWUP SET     -----------------------
art_summary_map = map_to_ugandaemr(art_summary_map, None, '5240', group_concept=99167,
                                   group_no=1)  # LOST TO FOLLOWUP
art_summary_map = map_to_ugandaemr(art_summary_map, None, '90209', group_concept=99167,
                                   group_no=1)  # DATE LOST TO FOLLOWUP
# ------------ End of LOST TO FOLLOWUP SET     -----------------------

# ------------ PATIENT DEATH SET     -----------------------
art_summary_map = map_to_ugandaemr(art_summary_map, None, '99112', group_concept=99168,
                                   group_no=1)  # DEAD
art_summary_map = map_to_ugandaemr(art_summary_map, None, '90272', group_concept=99168,
                                   group_no=1)  # DATE OF DEATH
# ------------ End of PATIENT DEATH SET     -----------------------
