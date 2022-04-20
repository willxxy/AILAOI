## AILAOI

### AI LA Open Innovation - pests.ai

*Team Members*

* Jimin Yoon - Developer - jiminyoo@usc.edu
* Yanhao Shen - Developer - yanhaosh@usc.edu
* Ming Wang - Developer - mwang283@usc.edu
* William Han - Developer - wjhan@uci.edu


### Introduction

Trees in the Santa Monica Mountains National Recreation Area (SMMNA) face threats from many invasive pests, particularly the invasive shot hole borer (ISHB) and the golden spotted oak borer (GSOB). To save these trees from a premature death, pests.ai has created a platform using a state of the art prediction algorithm for classifying risk of infestations for the two species in the SMMNA. 

**Model Task**:
Predict infestations in the SMMNA with machine learning and showcase results through an ArcGIS platform

**Platform Features**:
* Marker for high, medium, and no risk infestations
* Point-click landmark feature displayer
* User notification for medium - high risk infestations with respective location of infestation


### Methods 

**Machine Learning**

*Data Used*: ISHB_consolidated.csv and Inspected_GSOB_Trees_0.csv files

*Task*: Predict location of high, medium, and no risk infestations of ISHB and GSOB

*Classifier*: XGBoost

*Evaluation*: ROC AUC Score


**User Interface**

[Python API](https://developers.arcgis.com/python/) for [ArcGIS dashboard](https://learngis2.maps.arcgis.com/apps/dashboards/e24632dc37fc484985e3a355e665512e)


### Pipeline
need to add



### Contributions

* High accuracy machine learning model

| Dataset        | Model         |       Accuracy       | Micro-Average ROC curve, AUC | Macro-Average ROC curve, AUC |
| -------------- | ------------- | -------------------- | ---------------------------- | ---------------------------- |
| GSOB           | XGBoost       |       ~ 0.966        |            ~ 0.99            |           ~ 0.99             |
|                |               |                      |                              |                              |
| ISHB           |               |       ~ 0.780        |            ~ 0.90            |           ~ 0.89             |

* Fast notification module
* User-friendly dashboard
* Strong scalibility (applied on other regions)
* End to End workflow for real data


### Future Work

* Involve more data, such as shp.file and landsat
* Create a database to store and show historical infection status
* Deploy the service on the cloud and update the real data for users
* Analyse data by time sequence
* Conbine current classifier with deep learning models

