import matplotlib.pyplot as plt
import numpy as np
import statistics # import the statistics module to use mean and standard deviation for later use. 

from patient import * 

# get the path from the csv so the code is able to read the csv and then sort and filter the data.
filename = "/Users/roychen/Desktop/Comp BME/Module 1 HW/Metadata and Protein Data for Module 1.csv"
Patient.instantiate_from_csv(filename)

#Sort and filter patients by age at Death. display if death age is available, if not assign a value (9999) so it will be push it to the end of the sorted list.
Patient.all_patients.sort(
    key=lambda p: p.age_at_death if p.age_at_death is not None else 9999,
    reverse=False
)
# label text so we know what is being displayed.
print("First 30 patients sorted by Age at Death:")
for patient in Patient.all_patients[:30]:
    print(patient)

# Filter and print a subset based on two attributes (minium and maxium age at death of 80 and 89.999 and a thal values bigger than 3 )
died_80s_thal_gt3 = Patient.filter(
    Patient.all_patients,
    min_age_at_death=80,
    max_age_at_death=89.999,
    min_thal=3
)
# Print the total number of patients who died in their 80s and have a Thal value greater than 3.
# len, counts how mant patients and then prints the first 15 patients that fits the rules.
print(f"\nNumber of patients who died in their 80s with Thal > 3 = {len(died_80s_thal_gt3)}")
print("First 15 of that subset:")
for patient in died_80s_thal_gt3[:15]:
    print(patient)


# Create an empty list to store ABeta42 value for male and female
abeta42_female = []
abeta42_male = []
# loop and filter the list for all female patients that have dementia and add patient with no ABeta42 to list for both male and female
for patient in Patient.filter(Patient.all_patients, sex="Female", cognitive_status="Dementia"):
    if patient.abeta42 is not None:
        abeta42_female.append(patient.abeta42)

for patient in Patient.filter(Patient.all_patients, sex="Male", cognitive_status="Dementia"):
    if patient.abeta42 is not None:
        abeta42_male.append(patient.abeta42)

# Check that both groups have at least 2 data points and then, if there is atleast 2 data points, calculate the mean and standard deviation of ABeta42 for both male and female. 
if len(abeta42_female) >= 2 and len(abeta42_male) >= 2:
    mean_f = statistics.mean(abeta42_female)
    mean_m = statistics.mean(abeta42_male)
    stdev_f = statistics.stdev(abeta42_female)
    stdev_m = statistics.stdev(abeta42_male)

# Labels the two bars on the x axis
    groups = ["Female (Dementia)", "Male (Dementia)"]
    means = [mean_f, mean_m]
    stdevs = [stdev_f, stdev_m]

# Create a figure for the bar graph and label and draw the graph with all points, in x  and y axis. title, labels, and save the figure as a png file.
    plt.figure()
    plt.bar(groups, means, yerr=stdevs, capsize=10)
    plt.title("Mean ± SD ABeta42 in Dementia Patients by Sex")
    plt.xlabel("Group")
    plt.ylabel("ABeta42 (pg/ug)")
    plt.tight_layout()
    plt.savefig("bar_ABeta42_dementia_by_sex.png", dpi=300)
    plt.show()
else:
    print("\nNot enough dementia ABeta42 data to compute mean/stdev for BOTH sexes.")

#Create an empty list to store ages at death and create a list to store patients's ABeta42 values.  
age_list = []
abeta42_list = []
# Loop through every patient in the patient dataset and filter to only include patients that have an age at death and ABeta42 value.
for patient in Patient.all_patients:
    #filters out patients with missing age or ABeta42 data so that only valid data points are included in the scatter plot.
    if patient.age_at_death is not None and patient.abeta42 is not None:
        age_list.append(patient.age_at_death)
        abeta42_list.append(patient.abeta42)

plt.figure()
plt.scatter(age_list, abeta42_list)
plt.xlabel("Age at Death (years)")
plt.ylabel("ABeta42 (pg/ug)")
plt.title("Scatter Plot: ABeta42 vs Age at Death")
plt.tight_layout()
plt.savefig("scatter_ABeta42_vs_AgeAtDeath.png", dpi=300)
plt.show()





