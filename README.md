# Uganda EMR import script

These scripts help in the importation of data into UgandaEMR

The csv forms are UgandaEMR customised forms converted to csv

The mappings are column numbers mapped to UgandaEMR concepts

We will add all the concepts and descriptions which you can then edit to just add the corresponding column in the data

### The import process

```python
from data_import import read, register, construct_obs, transform_list, group_data
from mappings.eid_summary_map import eid_summary_map
from mappings.eid_encounter_map import eid_encounter_map

eid_registration = read('./test_data/eid/eid_summary.csv')
eid_encounters = read('./test_data/eid/eid_encounters.csv')

eid_summary_variables = read('./csv_forms/eid_summary.csv')
eid_encounter_variables = read('./csv_forms/eid_encounter.csv')

summary_variables = transform_list(eid_summary_variables)
encounter_variables = transform_list(eid_encounter_variables)

# Register patients
register(eid_registration[1:], names_column=4, gender_column=6, birth_date_column=7,
         address_columns=[None, 1, None, None, None, None], identifier_columns={'2': '6'})
# Summary page and observations
construct_obs(eid_registration[1:], identifier_column=2, form_id=12, visit_column=3, encounter_type=16,
              mapped_dict=eid_summary_map, concept_answer_map=summary_variables, location_id=2)
#Encounter page and observations
construct_obs(eid_encounters[1:], identifier_column=1, form_id=11, visit_column=2, encounter_type=12,
              mapped_dict=eid_encounter_map, concept_answer_map=encounter_variables, location_id=2)

```

The import process is as follows,
Assumption is that each csv file has a column that identifies a patient uniquely


1. First register patients
..* The first argument takes the data that to be imported, for our case we read a csv file
..* The second argument is the names column number on the data, if the are more than one columns numbers should be put in a list
..* The third argument is the column number corresponding to the gender
..* The fourth argument is the column number corresponding to the birth date
..* The fifth argument are address columns, country, district, county, sub_county, parish, village in that order if not applicable just put None
..* The last argument is dictionary of identifiers, the key is the column corresponding to column in the data, and the value is identifier_type id in UgandaEMR



