add_person = (
    "INSERT INTO person "
    "(gender,birthdate,date_created,uuid) "
    "VALUES (%(gender)s, %(birthdate)s, %(date_created)s, %(uuid)s)"
)
add_person_address = (
    "INSERT INTO person_address "
    "(person_id,preferred,address3,address4,address5,state_province,country,date_created,county_district,uuid,creator) "
    "VALUES (%(person_id)s, %(preferred)s, %(address3)s, %(address4)s, %(address5)s, %(state_province)s, %(country)s, %(date_created)s, %(county_district)s, %(uuid)s, %(creator)s)"
)
add_person_attribute = (
    "INSERT INTO person_attribute "
    "(person_id,value,person_attribute_type_id,date_created,uuid,creator) "
    "VALUES (%(person_id)s, %(value)s, %(person_attribute_type_id)s, %(date_created)s, %(uuid)s, %(creator)s)"
)
add_person_name = (
    "INSERT INTO person_name "
    "(person_id,preferred,given_name,family_name,date_created,uuid,creator) "
    "VALUES (%(person_id)s, %(preferred)s, %(given_name)s, %(family_name)s, %(date_created)s, %(uuid)s, %(creator)s)"
)
add_patient = (
    "INSERT INTO patient "
    "(patient_id,date_created,creator) "
    "VALUES (%(patient_id)s, %(date_created)s, %(creator)s)"
)
add_patient_identifier = (
    "INSERT INTO patient_identifier "
    "(patient_id,identifier,identifier_type,preferred,location_id,date_created,uuid,creator) "
    "VALUES (%(patient_id)s, %(identifier)s, %(identifier_type)s, %(preferred)s, %(location_id)s, %(date_created)s, %(uuid)s, %(creator)s)"
)
add_visit = (
    "INSERT INTO visit "
    "(patient_id,visit_type_id,date_started,date_stopped,location_id,date_created,uuid,creator) "
    "VALUES (%(patient_id)s, %(visit_type_id)s, %(date_started)s, %(date_stopped)s, %(location_id)s, %(date_created)s, %(uuid)s, %(creator)s)"
)
add_encounter = (
    "INSERT INTO encounter "
    "(visit_id,encounter_type,patient_id,location_id,form_id,encounter_datetime,date_created,uuid,creator) "
    "VALUES (%(visit_id)s, %(encounter_type)s, %(patient_id)s, %(location_id)s, %(form_id)s, %(encounter_datetime)s, %(date_created)s, %(uuid)s, %(creator)s)"
)
add_obs = (
    "INSERT INTO obs "
    "(person_id,concept_id,encounter_id,obs_datetime,location_id,obs_group_id,value_coded,value_datetime,value_numeric,value_text,date_created,uuid,creator) "
    "VALUES (%(person_id)s, %(concept_id)s, %(encounter_id)s, %(obs_datetime)s, %(location_id)s, %(obs_group_id)s, %(value_coded)s, %(value_datetime)s, %(value_numeric)s, %(value_text)s, %(date_created)s, %(uuid)s, %(creator)s)"
)

add_encounter_provider = (
    "INSERT INTO encounter_provider "
    "(encounter_id,provider_id,encounter_role_id,creator,date_created,uuid) "
    "VALUES (%(encounter_id)s, %(provider_id)s, %(encounter_role_id)s, %(creator)s, %(date_created)s, %(uuid)s)"
)