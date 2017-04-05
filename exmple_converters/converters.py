def muac_converter(string):
    try:
        val = float(string)
        if val < 11.5:
            return '99028'
        elif 11.5 <= val < 12.5:
            return '99029'
        elif val >= 12.5:
            return '99027'
    except ValueError:
        if string.lower() == 'red':
            return '99028'
        elif string.lower() == 'yellow':
            return '99029'
        elif string.lower() == 'green':
            return '99027'


def tb_status_converter(string):
    if string == '1':
        return '90079'
    elif string == '2':
        return '90073'
    elif string == '3':
        return '90078'
    elif string == '4':
        return '90071'


def who_stage_converter(string):
    if string == 'I' or string == '1':
        return '90033'
    elif string == '2' or string == 'II':
        return '90034'
    elif string == '3' or string == 'III':
        return '90035'
    elif string == '4' or string == 'IV':
        return '90036'
    elif string == 'T1' or string == 'TI':
        return '90293'
    elif string == 'T2' or string == 'TII':
        return '90294'
    elif string == 'T3' or string == 'TIII':
        return '90295'
    elif string == 'T4' or string == 'TIV':
        return '90296'


def development_milestone_converter(string):
    if string.lower() in ['smi']:
        return '162855'
    elif string.lower() in ['sit']:
        return '162857'
    elif string.lower() in ['w']:
        return '162856'
    elif string.lower() in ['head']:
        return '162858'
    elif string.lower() in ['tob']:
        return '162859'
    elif string.lower() in ['cog']:
        return '162860'
    elif string.lower() in ['roll']:
        return '162861'
    elif string.lower() in ['cra']:
        return '162862'
    elif string.lower() in ['st']:
        return '162863'


def feeding_status_converter(string):
    if string.lower() in ['ebf']:
        return '5526'
    elif string.lower() in ['cf']:
        return '99791'
    elif string.lower() in ['mf']:
        return '6046'
    elif string.lower() in ['nlb']:
        return '99793'
    elif string.lower() in ['rf']:
        return '99089'
    elif string.lower() in ['w']:
        return '99792'


def immunization_code_converter(string):
    if string.lower() in ['bcg']:
        return '886'
    elif string.lower() in ['opv-0']:
        return '162831'
    elif string.lower() in ['opv-1']:
        return '162832'
    elif string.lower() in ['opv-2']:
        return '162833'
    elif string.lower() in ['opv-3']:
        return '162834'
    elif string.lower() in ['dpt']:
        return '781'
    elif string.lower() in ['dpt-hebb-hib1']:
        return '162835'
    elif string.lower() in ['dpt-hebb-hib2']:
        return '162836'
    elif string.lower() in ['dpt-hebb-hib3']:
        return '162837'
    elif string.lower() in ['measles']:
        return '63'
    elif string.lower() in ['de-worming', 'deworm', 'dewormed', 'dewarm']:
        return '162838'
    elif string.lower() in ['vitamin a']:
        return '99356'
    elif string.lower() in ['pvc-1']:
        return '163014'
    elif string.lower() in ['pvc-2']:
        return '163015'
    elif string.lower() in ['pvc-3']:
        return '163016'
    elif string.lower() in ['not done']:
        return '90002'


def clinical_assessment_code_converter(string):
    if string.lower() in ['well']:
        return '162848'
    elif string.lower() in ['ln']:
        return '162847'
    elif string.lower() in ['wl']:
        return '832'
    elif string.lower() in ['f']:
        return '90103'
    elif string.lower() in ['ot']:
        return '90130'
    elif string.lower() in ['ei']:
        return '162849'
    elif string.lower() in ['g']:
        return '162850'
    elif string.lower() in ['c']:
        return '107'
    elif string.lower() in ['adr']:
        return '162851'
    elif string.lower() in ['rdr']:
        return '162852'
    elif string.lower() in ['pneu']:
        return '42'
    elif string.lower() in ['rash']:
        return '512'
    elif string.lower() in ['others', 'o']:
        return '90002'


def drugs_converter(string):
    if string.lower() in ['amitriptilline']:
        return '931'
    elif string.lower() in ['amoxicillin']:
        return '265'
    elif string.lower() in ['cetrizine']:
        return '779'
    elif string.lower() in ['ciprofloxacine']:
        return '740'
    elif string.lower() in ['cloxacillin']:
        return '922'
    elif string.lower() in ['coartem']:
        return '99266'
    elif string.lower() in ['dapsone']:
        return '90171'
    elif string.lower() in ['doxycycline']:
        return '95'
    elif string.lower() in ['eh']:
        return '1108'
    elif string.lower() in ['erythromicin']:
        return '272'
    elif string.lower() in ['fluconazole']:
        return '747'
    elif string.lower() in ['ibuprofen']:
        return '912'
    elif string.lower() in ['ketoconazole']:
        return '926'
    elif string.lower() in ['mebendazole']:
        return '244'
    elif string.lower() in ['metronidazole']:
        return '237'
    elif string.lower() in ['multivitamins', 'multivites', 'm/vites', 'm/vite', 'm/vits']:
        return '461',
    elif string.lower() in ['nutrition Support']:
        return '99054'
    elif string.lower() in ['nystatin']:
        return '919'
    elif string.lower() in ['paracetamol']:
        return '89'
    elif string.lower() in ['rh']:
        return '1194'
    elif string.lower() in ['rhe']:
        return '99127'
    elif string.lower() in ['rhz']:
        return '768'
    elif string.lower() in ['rhze']:
        return '1131'
    elif string.lower() in ['rhzes']:
        return '99128'
    elif string.lower() in ['septrin']:
        return '916'
    elif string.lower() in ['vit b complex']:
        return '329'
    elif string.lower() in ['other specify']:
        return '90002'


def relationship_converter(string):
    if string.lower() in [
        'aunt', 'uncle', 'auntie', 'aunt to the child', 'uncle to the child', 'brother to the mother',
        'sister to the mother'
    ]:
        return '90281',
    elif string.lower() in ['brother', 'sister']:
        return '90285',
    elif string.lower() in ['child', 'daughter', 'son']:
        return '90280',
    elif string.lower() in ['cousin']:
        return '90286',
    elif string.lower() in ['friend', 'best friend', 'friend to the mother']:
        return '5618',
    elif string.lower() in ['grandchild']:
        return '90284',
    elif string.lower() in [
        'grandparent', 'g/d mother', 'g/d father', 'grand mother', 'grandmother', 'grand father', 'grandfather',
        'g mother', 'g.mother', 'g father', 'g.father', 'gmother', 'gfather', 'grandparents', 'grand parents',
        'aunt to the mother'
    ]:
        return '90283',
    elif string.lower() in ['niece', 'nephew']:
        return '90282',
    elif string.lower() in ['notfamily']:
        return '90287',
    elif string.lower() in ['parent', 'father', 'mother']:
        return '90279',
    elif string.lower() in ['spouse', 'partner', 'husband', 'wife']:
        return '90288'
    else:
        return '90287'


def mode_of_delivery_converter(string):
    if string.lower() in ['breech']:
        return '1172'
    elif string.lower() in ['cesarean section', 'cs', 'operation', 'c-section']:
        return '1171'
    elif string.lower() in ['forceps or vacuum extractor delivery']:
        return '163005'
    elif string.lower() in ['other']:
        return '5622'
    elif string.lower() in ['spontaneous vaginal delivery', 'normal', 'sdv']:
        return '1170'


def entry_point_converter(string):
    if string.lower() in ['pmtct program', 'pmtct']:
        return '90012'
    elif string.lower() in ['tb']:
        return '90016'
    elif string.lower() in ['ycc']:
        return '99593'
    elif string.lower() in ['outreach']:
        return '90019'
    elif string.lower() in ['out patient']:
        return '90013'
    elif string.lower() in ['sti']:
        return '90015'
    elif string.lower() in ['inpatient']:
        return '90018'
    elif string.lower() in ['other']:
        return '90002'
    else:
        return '90012'


def mothers_arvs_for_pmtct_converter(string):
    if string.lower() in ['art', 'haart']:
        return '163012'
    elif string.lower() in ['life long art']:
        return '99786'
    elif string.lower() in ['none']:
        return '1107'
    elif string.lower() in ['no art']:
        return '99782'
    elif string.lower() in ['unknown']:
        return '1067'
    elif string.lower() in ['sdnvp']:
        return '163009'
    elif string.lower() in ['sdnvp+azt']:
        return '163010'
    elif string.lower() in ['sdnvp+azt/3tc']:
        return '163011'


def infant_arvs_converter(string):
    if string.lower() in ['daily nvp from birth through b/feeding', 'dailynvp fmbirththru b/feeding']:
        return '163013'
    elif string.lower() in ['daily nvp from birth to 6 weeks', 'dailynvp fmbrth to 6wks']:
        return '162966'
    elif string.lower() in ['nvp taken after 72 hours of birth']:
        return '99789'
    elif string.lower() in ['no arvs taken at birth']:
        return '99790'
    elif string.lower() in ['received nvp within 72 hours of birth']:
        return '99788'
    elif string.lower() in ['unknown']:
        return '1067'
    elif string.lower() in ['sdnvp']:
        return '163009'
    elif string.lower() in ['sdnvp+azt']:
        return '163010'


def result_converter(string):
    if string.lower() in ['negative', 'neg']:
        return '664'
    elif string.lower() in ['positive', 'pos']:
        return '703'


def final_outcome_converter(string):
    if string.lower() in ['discharged negative']:
        return '99427'
    elif string.lower() in ['referred to art clinic']:
        return '99430'
    elif string.lower() in ['lost']:
        return '5240'
    elif string.lower() in ['transferred']:
        return '90306'
    elif string.lower() in ['died']:
        return '99112'


def symptoms_converter(string):
    if string.lower() in ['cough']:
        return '90132'
    elif string.lower() in ['db', 'difficulty in breathing']:
        return '90133'
    elif string.lower() in ['dementia']:
        return '90128'
    elif string.lower() in ['enceph', 'encephalitis']:
        return '90129'
    elif string.lower() in ['fever']:
        return '90131'
    elif string.lower() in ['gud', 'genital ulcer disease']:
        return '90138'
    elif string.lower() in ['headache']:
        return '90094'
    elif string.lower() in ['iris', 'immune reconstitution inflammatory syndrome']:
        return '90134'
    elif string.lower() in ['malaria', 'presumed']:
        return '123'
    elif string.lower() in ['pneumonia']:
        return '90127'
    elif string.lower() in ['pid', 'pelvic inflammatory disease']:
        return '90137'
    elif string.lower() in ['rti', 'respiratory tract infection', 'nos']:
        return '999'
    elif string.lower() in ['thrush']:
        return '90130'
    elif string.lower() in ['ud', 'urethral discharge']:
        return '90136'
    elif string.lower() in ['ulcers']:
        return '90139'
    elif string.lower() in ['urti', 'respiratory tract infection upper']:
        return '106'
    elif string.lower() in ['eeight loss']:
        return '90135'
    elif string.lower() in ['zoster']:
        return '90126'
    elif string.lower() in ['ks', 'kaposis sarcoma']:
        return '507'
    elif string.lower() in ['ccm', 'meningitis cryptococcal']:
        return '1294'
    elif string.lower() in ['other']:
        return '90002'


def side_effect_converter(string):
    if string.lower() in ['ab', 'abdominal pain']:
        return '90100'
    elif string.lower() in ['anaemia']:
        return '90099'
    elif string.lower() in ['bn', 'burning']:
        return '90095'
    elif string.lower() in ['cns', 'dizziness']:
        return '90117'
    elif string.lower() in ['diarrhoea']:
        return '90092'
    elif string.lower() in ['fat', 'fat distribution changes']:
        return '90116'
    elif string.lower() in ['fatigue']:
        return '90093'
    elif string.lower() in ['headache']:
        return '90094'
    elif string.lower() in ['jaundice']:
        return '90115'
    elif string.lower() in ['nausea']:
        return '90091'
    elif string.lower() in ['rash']:
        return '90098'
    elif string.lower() in ['other specify']:
        return '90002'


def functional_status_converter(string):
    if string.lower() in ['amb', 'ambulatory']:
        return '90037',
    elif string.lower() in ['work', 'working', 'walking', 'playing', 'p']:
        return '90038',
    elif string.lower() in ['bed', 'bedridden']:
        return '90039'


def arv_converter(string):
    if string.lower() in ['d4t-3tc-nvp', 'd4t,3tc,nvp']:
        return '99015'
    elif string.lower() in ['d4t-3tc-efv', 'd4t,3tc,efv']:
        return '99016'
    elif string.lower() in ['azt-3tc-nvp', 'azt,3tc,nvp']:
        return '99005'
    elif string.lower() in ['azt-3tc-efv', 'azt,3tc,efv']:
        return '99006'
    elif string.lower() in ['tdf-3tc-nvp', 'tdf,3tc,nvp']:
        return '99039'
    elif string.lower() in ['tdf-3tc-efv', 'tdf,3tc,efv']:
        return '99040'
    elif string.lower() in ['tdf-ftc-nvp', 'tdf,ftc,nvp']:
        return '99041'
    elif string.lower() in ['tdf-ftc-efv', 'tdf,ftc,efv']:
        return '99042'
    elif string.lower() in ['abc-ddi(250)-lpv/r', 'abc,ddi(250),lpv/r']:
        return '99007'
    elif string.lower() in ['abc-ddi(400)-lpv/r', 'abc,ddi(400),lpv/r']:
        return '99008'
    elif string.lower() in ['tdf-3tc-lpv/r', 'tdf,3tc,lpv/r']:
        return '99044'
    elif string.lower() in ['tdf-ftc-lpv/r', 'tdf,ftc,lpv/r']:
        return '99043'
    elif string.lower() in ['zdv-ddi(250)-lpv/r', 'azt,ddi(250),lpv/r']:
        return '99282'
    elif string.lower() in ['zdv-ddi(400)-lpv/r', 'azt,ddi(400),lpv/r']:
        return '99283'
    elif string.lower() in ['azt-3tc-lpv/r', 'azt,3tc,lpv/r']:
        return '99046'
    elif string.lower() in ['abc-ddi-lpv/r', 'abc,ddi,lpv/r']:
        return '99017'
    elif string.lower() in ['abc-ddi-nfv', 'abc-ddi-nfv']:
        return '99018'
    elif string.lower() in ['abc-ddi-sqv/r', 'abc,ddi,sqv/r']:
        return '99019'
    elif string.lower() in ['zdv-ddi-lpv/r', 'azt,ddi,lpv/r']:
        return '99045'
    elif string.lower() in ['azt-abc-lpv/r', 'azt,abc,lpv/r']:
        return '99284'
    elif string.lower() in ['abc-ddi-atv/r', 'abc,ddi,atv/r']:
        return '99285'
    elif string.lower() in ['azt-3tc-atv/r', 'azt,3tc,atv/r']:
        return '99286'
    elif string.lower() in ['abc-3tc-nvp', 'abc,3tc,nvp']:
        return '99884'
    elif string.lower() in ['abc-3tc-efv', 'abc,3tc,efv']:
        return '99885'
    elif string.lower() in ['abc-3tc-atv/r', 'abc,3tc,atv/r']:
        return '99888'
    elif string.lower() in ['abc-3tc-lpv/r', 'abc,3tc,lpv/r']:
        return '163017'
    elif string.lower() in ['tdf-3tc-atv/r', 'tdf,3tc,atv/r']:
        return '99887'
    elif string.lower() in ['other']:
        return '90002'

