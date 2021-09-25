import pandas as pd
import datetime

sheet_id = "1gFTNs_GtnTIyyVWXmsQxwdZpGbyicZM2HJcXvCf4b3k"
sheet_name = "Sheet1"
url = f"https://docs.google.com/spreadsheets/d/{sheet_id}/gviz/tq?tqx=out:csv&sheet={sheet_name}"

sg_data = pd.read_csv(url)
dates = [datetime.datetime.strptime(date, '%Y-%m-%d').strftime("%m/%d/%Y") for date in sg_data["Date"]]
imported = [[daily_import for daily_import in sg_data["Daily Imported"]]]
local = [[daily_local for daily_local in sg_data["Daily Local transmission"]]]
icu = [[daily_icu for daily_icu in sg_data["Intensive Care Unit (ICU)"]]]
vaccination = [[daily_vacc if daily_vacc > 0 else 0 for daily_vacc in sg_data["Cumulative Individuals Vaccination Completed"]]]

imported_df = pd.DataFrame(imported, columns=dates, index=["Daily Imported"])
local_df = pd.DataFrame(local, columns=dates, index=["Daily Local"])
icu_df = pd.DataFrame(icu, columns=dates, index=["Daily ICU"])
vaccination_df = pd.DataFrame(vaccination, columns=dates, index=["Daily Fully Vaccinated"])

imported_df.to_csv("Daily Imported.csv")
local_df.to_csv("Daily Local.csv")
icu_df.to_csv("Daily ICU.csv")
vaccination_df.to_csv("Daily Fully Vaccinated.csv")