import streamlit as st

def get_activity_multiplier():
    st.write("Activity Multipliers:")
    st.write("1. Sedentary (AM = 1.2)")
    st.write("2. Light Active (AM = 1.375)")
    st.write("3. Moderately Active (AM = 1.55)")
    st.write("4. Very Active (AM = 1.75)")
    st.write("5. Extra Active (AM = 1.90)")

    choice = st.selectbox("Select your activity level:", [1, 2, 3, 4, 5], index=2)  # Default to Moderately Active
    activity_multiplier_values = [1.2, 1.375, 1.55, 1.75, 1.90]
    return activity_multiplier_values[choice - 1]

def calorie_counter():
    calories_eaten = st.number_input("Enter the amount of calories eaten in a day:")
    activity_multiplier = get_activity_multiplier()
    weight_kg = st.number_input("Enter your weight in kilograms:")
    height_cm = st.number_input("Enter your height in centimeters:")
    age_years = st.number_input("Enter your age in years:")
    cals_burnt = st.number_input("How many calories did you burn with your workout?")

    is_male = st.checkbox("Are you male?")  # Checkbox for gender selection
    if not is_male:
        bmr = 10 * weight_kg + 6.25 * height_cm - 5 * age_years - 161
    else:
        bmr = 10 * weight_kg + 6.25 * height_cm - 5 * age_years + 5

    tdee = bmr * activity_multiplier + cals_burnt
    final_calorie = tdee - calories_eaten

    return final_calorie

# Example usage:
result = calorie_counter()

st.write("Calorie Summary:")
if result > 0:
    st.write(f"You are in a calorie DEFICIT of value {result}")
elif result == 0:
    st.write("You have burnt NOTHING!")
else:
    st.write(f"You are in a calorie SURPLUS of value {result}")
