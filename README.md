# empower_data0
Dataset used to create machine learning models in the paper 

LP Bueno, M., Schippers, A., Kazlauskaitė, M., Brito, J., Campos, J., Vera, L., ... & Thill, S. (2025, May). Predicting Performance in Gamified Cognitive Executive Functioning Tasks for Neurodiverse Children Using Machine Learning. In International Conference on Human-Computer Interaction (pp. 116-127). Cham: Springer Nature Switzerland.

Paper available at:
https://repository.ubn.ru.nl/handle/2066/320895

Contact: marcos.depaulabueno@donders.ru.nl


## Dataset important information:

- This dataset is split into units: Pilot3 and Validation_RO (further spilt into _validation_RO_1 and _validation_RO_2) 
- There are no duplicate participants in any of units. Each participant has been recorded only once.
- The identifiers are **unique** and **consistent** only in the context of a unit 
- For each participant (id_student) there have been one or multiple activities (id_activity)
- The list of behavioral data features and their possible values can be found in **normalization_factors.py**. In this file, the lists assigned to minimum and maximum values correspond to different levels (first element for Level 1, and so on).

## Data structure

The files in the dataset have the following structure:


- **studentID** - identifier of the participant; unique and consistent only in the context of a unit
- **country** - indicates the recording country
- **activityID** - identifier of the recording activity; unique and consistent only in the context of a unit
- **activitytype** - indicates the played game; behavioral data column names depends on the played game 
- **level** - indicates the level of  **activitytype**; can be either 1, 2 or 3
- Game-specific behavioral features; for a full list of available features and their possible values, see **normalization_factors.py**

## How to use this dataset

The files included in the dataset are in CSV format, each of them being archived as a ZIP.

To replicate the results reported in the paper or to perform further analyses, we recommend starting by concatenating all `.csv` files based on **activitytype**. The resulting dataset can then be analyzed in its raw form or normalized using **normalization_factors.py**.


**Acknowledgement**

The acquisition of this data and the research leading to these results have been carried out in the "EMPOWER. Design and evaluation of technological support tools to empower stakeholders in digital education" project, which has received funding from the European Union's Horizon Europe programme, under grant agreement No 101060918. Views and opinions expressed are, however, those of the author(s) only and do not necessarily reflect those of the European Union. Neither the European Union nor the granting authority can be held responsible for them.

