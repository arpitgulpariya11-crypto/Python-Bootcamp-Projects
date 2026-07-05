#!/usr/bin/env python
# coding: utf-8

# # BMI Calculator

# In[ ]:


# condition - BMI -> Classification -> Health Risk
             Under 18.5  -> Underweight    -> Mimimal
             18.5 - 24.9 -> Normal weight  -> Minimal
             25 - 29.9   -> Overweight     -> Increased
             30 - 34.9   -> Obese          -> High
             35 - 39.9   -> Severely Obese -> Very High
             40 and Over -> Morbidly Obese -> Extramely High 


# In[9]:


def calculate_bmi():
    # 1. Gather user inputs with proper data conversion
    name = input(str('Enter your name:'))

    weight = float(input('Enter your weight in kg'))

    height = int(input('Enter your height in inches'))

    # 2. BMI = (weight in kg x 39.37**2)/(height*height in inches)

    BMI = (round(weight*(39.37**2)/height**2,2))

    print(f'{name}, your calculated BMI is : {BMI}.')

    if BMI>0:
        if BMI<18.5:
            print('you are underweight',' and your health risk are mimimal.')
        elif BMI>18.5 :
            print('you are Normal weight',' and your health risk are mimimal.')
        elif BMI>25 :
            print('you are Overweight',' and your health risk are Increased.')
        elif BMI>30 :
            print('you are Obese',' and your health risk are High.')
        elif BMI>35 :
            print('you are Severely Obese',' and your health risk are Very High.')
        else:
            print('you are Severely Morbidly Obese',' and your health risk are Extramely High.')
    else:
            print('Please Enter Valide Measures')

calculate_bmi()


# In[ ]:





# In[ ]:




