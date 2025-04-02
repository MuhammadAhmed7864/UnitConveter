# Unit Converter with Advanced UI & Animations
import streamlit as st 

# CSS Styling for Smooth Animations and Enhanced UI
st.markdown(
    """
    <style>
    body {
        background-color: #1e1e2f;
        color: white;
        font-family: 'Poppins', sans-serif;
    }
    
    h1 {
        text-align: center;
        font-size: 44px;
        color: #ffffff;
        text-shadow: 2px 2px 15px rgba(255, 255, 255, 0.3);
        padding-bottom: 10px;
        animation: fadeIn 1s ease-in-out;
    }
    
    @keyframes fadeIn {
        from { opacity: 0; transform: translateY(-20px); }
        to { opacity: 1; transform: translateY(0); }
    }

    div.stButton > button {
        background: linear-gradient(45deg, #ff7eb3, #ff758c);
        color: white;
        font-size: 20px;
        padding: 12px 24px;
        border-radius: 12px;
        border: none;
        transition: 0.4s ease-in-out;
        box-shadow: 0px 5px 20px rgba(255, 120, 150, 0.5);
        font-weight: bold;
        cursor: pointer;
        animation: popIn 1s ease-in-out;
    }
    
    div.stButton > button:hover {
        transform: scale(1.1);
        background: linear-gradient(45deg, #ff758c, #ff7eb3);
        box-shadow: 0px 10px 25px rgba(255, 120, 150, 0.8);
    }

    @keyframes popIn {
        from { opacity: 0; transform: scale(0.8); }
        to { opacity: 1; transform: scale(1); }
    }

    .result-box { 
        font-size: 22px;
        font-weight: bold;
        text-align: center;
        background: rgba(255, 255, 255, 0.2);
        padding: 20px;
        border-radius: 15px;
        margin-top: 20px;
        color: white;
        box-shadow: 0px 5px 20px rgba(255, 255, 255, 0.4);
        text-shadow: 1px 1px 10px rgba(255, 255, 255, 0.5);
        animation: glow 2s infinite alternate;
    }

    @keyframes glow {
        from { box-shadow: 0px 5px 15px rgba(255, 255, 255, 0.3); }
        to { box-shadow: 0px 10px 30px rgba(255, 255, 255, 0.6); }
    }

    .footer {
        text-align: center;
        margin-top: 50px;
        font-size: 16px;
        color: blue;
        animation: fadeIn 2s ease-in-out;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Title and Description
st.markdown("<h1>🚀 Animated Unit Converter</h1>", unsafe_allow_html=True)
st.write("Easily convert between different units of **Length, Weight, and Temperature** with a stylish UI.")

# Sidebar menu
conversion_type = st.sidebar.selectbox("Choose Conversion Type", ["Length", "Weight", "Temperature"])
value = st.number_input("Enter Value", value=0.0, min_value=0.0, step=0.10)

col1, col2 = st.columns(2)

if conversion_type == "Length":
    with col1:
        from_unit = st.selectbox("From", ["Meters", "Kilometers", "Centimeters", "Millimeters", "Miles", "Yards", "Inches", "Feet"])
    with col2:
        to_unit = st.selectbox("To", ["Meters", "Kilometers", "Centimeters", "Millimeters", "Miles", "Yards", "Inches", "Feet"])
elif conversion_type == "Weight":
    with col1:
        from_unit = st.selectbox("From", ["Kilogram", "Grams", "Milligrams", "Pounds", "Ounces"])
    with col2:
        to_unit = st.selectbox("To", ["Kilogram", "Grams", "Milligrams", "Pounds", "Ounces"])
elif conversion_type == "Temperature":
    with col1:
        from_unit = st.selectbox("From", ["Celsius", "Fahrenheit", "Kelvin"])
    with col2:
        to_unit = st.selectbox("To", ["Celsius", "Fahrenheit", "Kelvin"])

# Conversion Functions
def length_converter(value, from_unit, to_unit):
    length_units = {
        'Meters': 1, 'Kilometers': 0.001, 'Centimeters': 100, 'Millimeters': 1000,
        'Miles': 0.0006213711, 'Yards': 1.09361, 'Feet': 3.28084, 'Inches': 39.37
    }
    return (value / length_units[from_unit]) * length_units[to_unit]

def weight_converter(value, from_unit, to_unit):
    weight_units = {
        'Kilogram': 1, 'Grams': 1000, 'Milligrams': 1000000, 'Pounds': 2.2046, 'Ounces': 35.27
    }
    return (value / weight_units[from_unit]) * weight_units[to_unit]

def temp_converter(value, from_unit, to_unit):
    if from_unit == "Celsius":
        return (value * 9/5 + 32) if to_unit == "Fahrenheit" else (value + 273.15) if to_unit == "Kelvin" else value
    elif from_unit == "Fahrenheit":
        return (value - 32) * 5/9 if to_unit == "Celsius" else ((value - 32) * 5/9 + 273.15) if to_unit == "Kelvin" else value
    elif from_unit == "Kelvin":
        return (value - 273.15) if to_unit == "Celsius" else ((value - 273.15) * 9/5 + 32) if to_unit == "Fahrenheit" else value
    return value

# Convert Button with Smooth Animations
if st.button("✨ Convert Now"):
    if conversion_type == "Length":
        result = length_converter(value, from_unit, to_unit)
    elif conversion_type == "Weight":
        result = weight_converter(value, from_unit, to_unit)
    elif conversion_type == "Temperature":
        result = temp_converter(value, from_unit, to_unit)

    st.markdown(f"<div class='result-box'>{value} {from_unit} = {result:.4f} {to_unit}</div>", unsafe_allow_html=True)

# Footer
st.markdown("<div class='footer'>💡 Created with ❤️ by Muhammad Ahmed</div>", unsafe_allow_html=True)
