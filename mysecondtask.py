import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

print("Pandas version:", pd.__version__)



#importing a dataset
df=pd.read_csv(r"C:\Users\PC\Pictures\ARSPN_Medical_Imaging_Pandas_Practice.csv")
print(df.head())
print(df.shape)
print(df.info())

print(df.isnull().sum())

#cleaning the dataset- filling the missing ages with mean 
df_clean = df.copy()
print(df[df["age_years"].isna()])
df["age_years"] = df["age_years"].fillna(
    df_clean["age_years"].mean()
)
print(df_clean.head(10))

#filling  the missing radiation dose with median
print("Before:", df_clean["dose_mGy"].isna().sum(),"missing")
median_dose=df_clean["dose_mGy"].median()
df_clean["dose_mGy"] = df["dose_mGy"].fillna(median_dose)
print("After:", df_clean["dose_mGy"].isna().sum(),"missing")
print(df_clean.head(10))
print(df_clean.isnull().sum())

df_clean["age_years"]= df_clean["age_years"].fillna(
    df_clean["age_years"].median()
)
print(df_clean.head(10))

#filling missiing lesion size with median
df_clean["lesion_size_cm"] = df_clean["lesion_size_cm"].fillna(
    df_clean["lesion_size_cm"].median()
)
print(df_clean.head(10))

#removing duplicates
print("Duplicate rows:", df_clean.duplicated().sum())
df_clean = df_clean.drop_duplicates()
print("Duplicate rows after cleaning:", df_clean.duplicated().sum())

#standardizing the texts
df_clean["modality"] = df_clean["modality"].str.strip().str.upper()
df_clean["finding"] = df_clean["finding"].str.strip().str.title()

print(df_clean["modality"].value_counts())

print(df_clean["finding"].value_counts())

#summarizing the dataset
print(df_clean.describe())

print("Mean age:", round(df_clean["age_years"].mean(), 1))
print("Median age:", df_clean["age_years"].median())
print("Youngest:", df_clean["age_years"].min())
print("Oldest:", df_clean["age_years"].max())


#saving the cleaned file
df_clean.to_csv("ARSPN cleaned.csv", index=False)
print("Cleaned file saved")


#analysing the data
#how many CTscans were performed?
ct_count = len(df_clean[df_clean["modality"] == "CT"])
print(ct_count)

# which modality was used the most
print(df_clean["modality"].value_counts())

#filtering
mri_records = df_clean[df_clean["modality"] == "MRI"]
print(mri_records)

#average scan time by modality grouping
print(df_clean.groupby("modality")["scan_time_min"].mean().round(1))

#age grouping
older_patients = df_clean[df_clean["age_years"] > 65]
print(older_patients.head(5))

#categorizing lesion size
lesion_size = df_clean[df_clean["lesion_size_cm"] > 4]
print(lesion_size)

#showing ct records from nigeria
ct_records = df_clean[(df_clean["modality"] == "CT") & (df_clean["country"] == "Nigeria")]
print(ct_records)

#count records by country
print(df_clean["country"].value_counts())

#average age by country
print(df_clean.groupby("country")["age_years"].mean())

print(df_clean.groupby("country")["modality"].value_counts())



#data visualization
import seaborn as sns
import matplotlib.pyplot as plt

counts = df_clean["modality"].value_counts()

counts.plot(kind="bar")
plt.title("Number of Imaging Records by Modality")
plt.xlabel("Imaging Modality")
plt.ylabel("Number of Records")
plt.xticks(rotation=30)
plt.show()

#histogram of age
plt.hist(df["age_years"], bins = 20)
plt.title("Age distribution of imaging records")
plt.xlabel("age_years")
plt.ylabel("Number of records")
plt.show()

#scatter plot of age vs lesionsize
plot_data = df_clean[["age_years", "lesion_size_cm"]].dropna()

plt.scatter( df_clean["age_years"], df_clean["lesion_size_cm"])

plt.title("Age vs Lesion Size")
plt.xlabel("Age (years)")
plt.ylabel("Lesion Size (cm)")
plt.show()

#saving file to excel

df_clean.to_excel("ARSPN cleaned.xlsx", index=False)

# using real values for the scatter plot visualization
df_for_plot = df.dropna(subset=["lesion_size_cm"])

plt.figure(figsize= (8,5))
plt.scatter( df_for_plot["age_years"], df_for_plot["lesion_size_cm"], alpha = 0.6)
plt.title("Age vs Lesion Size(Only Real Measurements)")
plt.xlabel("Age (years)")
plt.ylabel("Lesion Size (cm)")
plt.grid(True, alpha=0.3)
plt.show()

print(f"Real measurements: {len(df_for_plot)}")


#does lesion get more severe with age?
import pandas as pd

df_final = df.dropna(subset=["lesion_size_cm"])
#create age groups
df_final["age_group"] = pd.cut(df_final["age_years"], bins=[0,30,50,80], labels =["Young(0-30)","Adult(30-50)", "Elderly(50+)"])

plt.figure(figsize=(8,5))
df_final.boxplot(column= "lesion_size_cm", by="age_group")
plt.title("lesion size by Age Group")
plt.suptitle("")
plt.xlabel("Age group")
plt.ylabel("Lesion size(cm)")
plt.grid(True, alpha=0.3)
plt.show()




print(df_final.groupby("age_group")["lesion_size_cm"].mean())

df_final.to_excel("ARSPN_cleaned_final_real.xlsx", index=False)
print("saved")