no_yes = {'NO': '90004', 'YES': '90003'}
no_yes_1 = {'No': '1066', 'Yes': '1065'}
no_yes_pregnant = {'No': '90081', 'Yes': '90082'}
relationship = {
    'AUNT/UNCLE': '90281', 'BROTHER/SISTER': '90285', 'CHILD': '90280',
    'COUSIN': '90286', 'FRIEND': '5618', 'GRANDCHILD': '90284', 'GRANDPARENT': '90283',
    'NIECE/NEPHEW': '90282', 'NOTFAMILY': '90287', 'PARENT/FARTHER/MOTHER': '90279',
    'SPOUSE/PARTNER': '90288'
}
mode_of_delivery = {
    'BREECH': '1172',
    'CESAREAN SECTION': '1171',
    'Forceps or Vacuum Extractor Delivery': '163005',
    'Other': '5622',
    'SPONTANEOUS VAGINAL DELIVERY/NORMAL': '1170'
}
mothers_arvs_for_pmtct = {
    'ART': '163012',
    'Life long ART': '99786',
    'NONE': '1107',
    'No ART': '99782',
    'Unknown': '1067',
    'sd NVP': '163009',
    'sd NVP + AZT': '163010',
    'sd NVP + AZT/3TC': '163011'
}
infant_arvs = {
    'Daily NVP from birth through b/feeding': '163013',
    'Daily NVP from birth to 6 weeks': '162966',
    'NVP taken after 72 hours of birth': '99789',
    'No ARVs taken at birth': '99790',
    'Received NVP within 72 hours of birth': '99788',
    'Unknown': '1067',
    'sd NVP': '163009',
    'sd NVP + AZT': '163010'
}

result = {
    'NEGATIVE/NEG': '664',
    'POSITIVE/POS': '703'
}
feeding_status = {
    'BREASTFED EXCLUSIVELY/EBF': '5526',
    'Complementary Feeding/CF': '99791',
    'MIXED FEEDING/MF': '6046',
    'No Longer Breastfeeding/NLB': '99793',
    'REPLACEMENT FEEDING/RF': '99089',
    'Weaning/W': '99792'
}
final_outcome = {
    'Discharged Negative': '99427',
    'Referred to ART Clinic': '99430',
    'Lost': '5240',
    'Transferred': '90306',
    'Died': '99112'
}
entry_point = {
    'PMTCT': '90012',
    'TB': '90016',
    'YCC': '99593',
    'Outreach': '90019',
    'Out Patient': '90013',
    'STI': '90015',
    'Inpatient': '90018',
    'Other': '90002'
}
test_type = {
    'PCR Test': '163006',
    'Antibody Tes/AB': '163007'
}
muac = {
    'Red': '99028',
    'Yellow': '99029',
    'Green': '99027'
}
clinical_assessment_codes = {
    'WELL': '162848',
    'LN': '162847',
    'WL': '832',
    'F': '90103',
    'OT': '90130',
    'EI': '162849',
    'G': '162850',
    'C': '107',
    'ADR': '162851',
    'RDR': '162852',
    'PNEU': '42',
    'RASH': '512',
    'Others': '90002'
}
development_milestone = {
    'Smilling': '162855',
    'Sitting': '162857',
    'Walking': '162856',
    'Controling the head': '162858',
    'Transfer Objects from one hand to hand': '162859',
    'Cognition': '162860',
    'Rolling Over': '162861',
    'Crawl': '162862',
    'Stand': '162863'
}
immunization_codes = {
    'BCG': '886',
    'OPV-0': '162831',
    'OPV-1': '162832',
    'OPV-2': '162833',
    'OPV-3': '162834',
    'DPT': '781',
    'DPT-Hep+Hib1': '162835',
    'DPT-HepB + Hib2': '162836',
    'DPT-HepB + Hib3': '162837',
    'MEASLES': '63',
    'De-Worming': '162838',
    'Vitamin A': '99356',
    'PCV-1': '163014',
    'PCV-2': '163015',
    'PCV-3': '163016',
    'Not Done': '90002'
}
drugs = {
    'Amitriptilline': '931',
    'Amoxicillin': '265',
    'Cetrizine': '779',
    'Ciprofloxacine': '740',
    'Cloxacillin': '922',
    'Coartem': '99266',
    'Dapsone': '90171',
    'Doxycycline': '95',
    'EH': '1108',
    'Erythromicin': '272',
    'Fluconazole': '747',
    'Ibuprofen': '912',
    'Ketoconazole': '926',
    'Mebendazole': '244',
    'Metronidazole': '237',
    'Multivitamins': '461',
    'Nutrition Support': '99054',
    'Nystatin': '919',
    'Paracetamol': '89',
    'RH': '1194',
    'RHE': '99127',
    'RHZ': '768',
    'RHZE': '1131',
    'RHZES': '99128',
    'Septrin': '916',
    'Vit B Complex': '329',
    'Other specify': '90002',
}

tb_status = {
    'No signs/1': '90079',
    'Suspect/2': '90073',
    'Diagnosed with Tb/3': '90078',
    'Tb Rx/4': '90071'
}

side_effects = {
    'AB/ABDOMINAL PAIN': '90100', 'Anaemia/ANEMIA': '90099',
    'BN/BURNING': '90095',
    'CNS/DIZZINESS': '90117',
    'Diarrhoea/DIARRHOEA': '90092',
    'FAT/FAT DISTRIBUTION CHANGES': '90116',
    'Fatigue/FATIGUE': '90093',
    'Headache/HEADACHE': '90094',
    'Jaundice/JAUNDICE': '90115',
    'Nausea/NAUSEA': '90091',
    'Rash/RASH': '90098', 'Other specify:/OTHER SPECIFY': '90002',

}

symptoms = {
    'Cough/COUGH': '90132',
    'DB/BREATHING DIFFICULTY': '90133',
    'Dementia/DEMENTIA': '90128',
    'Enceph/ENCEPHALITIS': '90129',
    'Fever/FEVER': '90131',
    'GUD/GENITAL ULCER DISEASE': '90138',
    'Headache/HEADACHE': '90094',
    'IRIS/IMMUNE RECONSTITUTION INFLAMMATORY SYNDROME': '90134',
    'Malaria/PRESUMED': '123',
    'Pneumonia/PNEUMONIA': '90127',
    'PID/PELVIC INFLAMMATORY DISEASE': '90137',
    'RTI/RESPIRATORY TRACT INFECTION, NOS': '999',
    'Thrush/THRUSH': '90130',
    'UD/URETHRAL DISCHARGE': '90136',
    'Ulcers/ULCERS': '90139',
    'URTI/RESPIRATORY TRACT INFECTION, UPPER': '106',
    'Weight loss/WEIGHT LOSS': '90135',
    'Zoster/ZOSTER': '90126',
    'KS/KAPOSIS SARCOMA': '507',
    'CCM/MENINGITIS, CRYPTOCOCCAL': '1294',
    'Other specify:/OTHER SPECIFY': '90002'
}

malnutrition = {
    'MAM/MODERATE ACUTE MALNUTRITION': '99271',
    'SAM/SEVERE ACUTE MALNUTRITION': '99272',
    'SAMO/SEVERE ACUTE MALNUTRITION WITH OEDEMA': '99273',
    'PWG/PA/POOR WEIGHT GAIN / POOR APPETITE': '99274',
}
clinical_stage = {
    '1/HIV WHO CLINICAL STAGE 1': '90033',
    '2/HIV WHO CLINICAL STAGE 2': '90034',
    '3/HIV WHO CLINICAL STAGE 3': '90035',
    '4/HIV WHO CLINICAL STAGE 4': '90036',
    'T1/HIV WHO CLINICAL STAGE T1': '90293',
    'T2/HIV WHO CLINICAL STAGE T2': '90294',
    'T3/HIV WHO CLINICAL STAGE T3': '90295',
    'T4/HIV WHO CLINICAL STAGE T4': '90296'
}
functional_status = {
    'Amb/AMBULATORY': '90037',
    'Work/WORKING': '90038',
    'Bed/BEDRIDDEN': '90039'
}

adherence = {
    'Good/GOOD ADHERENCE': '90156',
    'Fair/FAIR ADHERENCE': '90157',
    'Poor/POOR ADHERENCE': '90158'
}
