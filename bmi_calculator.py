import pandas as pd



def bmi_calc(input):
    data = pd.read_json(input)
    bmi = [round((x/(y/100)**2),1) for x,y in zip(data['WeightKg'],data['HeightCm'])]
    data['BMI'] = bmi
    health_risk = ['Malnutrition Risk' if x <=18.4 else 'Low Risk' 
                    if 18.5 <= x <= 24.9 else 'Enhanced Risk' if 25.0 <= x <= 29.9
                    else 'Medium Risk' if 30.0 <= x <= 34.9 else 'High Risk' if 39.9 <= x <= 35.0
                    else 'Very High Risk' if x >= 40.0 else '' for x in data['BMI']]
    data['Health Risk'] = health_risk
    bmi_category = ['Underwieght' if x == 'Malnutrition Risk' else 'Normal weight' if x == 'Low Risk'
                    else 'Overweight' if x == 'Enhanced Risk' else 'Moderatly obese' if x == 'Medium Risk'
                    else 'Severly obese' if x == 'High Risk' else 'Very severly obese' if x == 'Very High Risk'
                    else '' for x in data['Health Risk']]
    data['BMI Category'] = bmi_category
    overweight_count = data[data['BMI Category'] == 'Overweight'].shape[0]
    return data,overweight_count


