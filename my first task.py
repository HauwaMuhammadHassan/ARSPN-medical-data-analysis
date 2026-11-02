import numpy as np
family_height = [1.60,1.64,1.40,1.70,1.66]
family_weight = [55,34,66,45,20]
family_height_array = np.array (family_height)
family_weight_array = np.array(family_weight)

print(family_height_array)
print(family_weight_array)
print("average height:", family_height_array.mean())
print("average weight:", family_weight_array.mean())


#creating a dictionary
Modality_info={
    "CT": "Computed Tomography",
     "X-ray" : "plain radiography",
     "MRI": "magnetic resonance imaging",
     "USS" : "ultrasonography",
     "FL": "flouroscopy",
     "NM" : "nuclear medicine"
     }

print(Modality_info["CT"])
Modality_info["mammography"] = "Breast imaging modality"
print("total modalities:" ,len(Modality_info))

#changing the description of a modality
Modality_info["X-ray"] = "conventional radiography"
print(Modality_info)