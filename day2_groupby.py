import pandas as pd
df = pd.read_excel(r"C:\Users\PC\Documents\my firstcode\ARSPN_cleaned_final_real.xlsx")

#average lesion size by modality
modality_avg = df.groupby("modality")["lesion_size_cm"].mean()
print(modality_avg)

# average lesion size per age group
age_avg = df.groupby("age_group")["lesion_size_cm"].mean()
print(age_avg)

#modality+age_group combination
combine= df.groupby(["modality","age_group"])["lesion_size_cm"].mean()
print(combine)
pivot = df.pivot_table(
    values="lesion_size_cm",
    index="modality",
    columns="age_group",
    aggfunc="mean",
)
print(pivot)