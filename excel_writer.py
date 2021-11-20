#Filler for ratings template

import pandas as pd
import numpy
from datetime import date

current_date = date.today()
current_year = current_date.year

#Transforming the excel-sheets in to Dataframes
entrypoint_data = pd.read_excel("entrypoint.xlsx")
additional_data = pd.read_excel("restaurant.xlsx")

#Funtion to import data and transform Dataframes to lists
def extractor(column_name, data):
    df = pd.DataFrame(data)
    list_of_values = df[column_name].values.tolist()
    return list_of_values

#importing data from the raw excel-sheets
osm = extractor("osm", entrypoint_data)
osm_add = extractor("restaurant_id", additional_data)
all_osm = osm + osm_add
uid_entrypoint = extractor("i", entrypoint_data)
uid_add = extractor("user_id", additional_data)
all_uids = uid_entrypoint + uid_add
rating_entry = extractor("Wie würdest Du das Restaurant gesamthaft bewerten?", entrypoint_data)
rating_add = extractor("Wie würdest Du das Restaurant gesamthaft bewerten?", additional_data)
all_ratings = rating_entry + rating_add
date = extractor("Submit Date (UTC)", entrypoint_data)
date_add = extractor("Submit Date (UTC)", additional_data)
all_date = date + date_add
gender = extractor("Dein Geschlecht", entrypoint_data)
get_age = extractor("Wie alt bist Du?", entrypoint_data)
age = numpy.array(get_age)
year_of_birth = (current_year) - age
marital_status = extractor("Familienstand", entrypoint_data)
amount_of_kids = extractor("Hast Du Kinder?", entrypoint_data)
job_status = extractor("Berufsstatus", entrypoint_data)

#Function to export data
def rating_exporter(column,list):    
    df = pd.read_excel('ratings_template.xlsx', sheet_name='Daten')
    df[column] = list
    df.to_excel("ratings_template.xlsx", sheet_name='Daten', index=0)

#exporting data in to exel-sheet "ratings_template"
rating_exporter("user_id", all_uids)
rating_exporter("restaurant_id", all_osm)
rating_exporter("rating", all_ratings)
rating_exporter("datum", all_date)

#Filler for user features template

#function to export data to the "user_features_template"
def user_feat_exporter(column, list):
    df = pd.read_excel("user_features_template.xlsx", sheet_name="Daten")
    df[column] = list
    df.to_excel("user_features_template.xlsx", sheet_name= "Daten", index=0)



#exporting all user features to the user feature sheet
user_feat_exporter("user_id", uid_entrypoint)
user_feat_exporter("geschlecht", gender)
user_feat_exporter("geburtsjahr", year_of_birth)
user_feat_exporter("familienstand", marital_status)
user_feat_exporter("kinder", amount_of_kids)
user_feat_exporter("berufsstatus", job_status)
