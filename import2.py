import streamlit as st
import pickle
import pandas as pd
from googletrans import Translator
from fpdf import FPDF
from datetime import date
import base64  # Import base64 for file download

# Function to generate a download link for files
def get_download_link(file_path, text):
    with open(file_path, 'rb') as f:
        file_contents = f.read()
    b64 = base64.b64encode(file_contents).decode()
    href = f'<a href="data:application/octet-stream;base64,{b64}" download="{file_path}">{text}</a>'
    return href

# Initialize translation languages
translator = Translator()

# Function to translate text
def translate_text(text, target_language):
    if target_language != "English":
        translated_text = translator.translate(text, dest=target_language).text
    else:
        translated_text = text
    return translated_text

# Customized CSS style for selectbox
selectbox_style = """
    <style>
    .st-el {
        background-color: #f5f5f5;
        border-radius: 12px;
        padding: 10px;
        font-weight: bold;
        font-size: 16px;
    }
    </style>
"""

# Set page configuration
st.set_page_config(
    page_title='STROKE PREDICTION APP',
    layout='wide',
    initial_sidebar_state='expanded'
)

# Load the machine learning model
model = pickle.load(open('model.pkl', 'rb'))

languages = {
    "English": "en",
    "Spanish": "es",             # Spanish (Spain, Latin America)
    "French": "fr",              # French (France, Canada)
    "German": "de",              # German (Germany)
    "Italian": "it",             # Italian (Italy)
    "Portuguese": "pt",          # Portuguese (Portugal, Brazil)
    "Dutch": "nl",               # Dutch (Netherlands, Belgium)
    "Russian": "ru",             # Russian (Russia)
    "Japanese": "ja",            # Japanese (Japan)
    "Chinese (Simplified)": "zh-cn",  # Chinese (Simplified)
    "Arabic": "ar",              # Arabic (Arab countries)
    "Korean": "ko",              # Korean (South Korea, North Korea)
    "Swedish": "sv",             # Swedish (Sweden)
    "Norwegian": "no",           # Norwegian (Norway)
    "Danish": "da",              # Danish (Denmark)
    "Finnish": "fi",             # Finnish (Finland)
    "Greek": "el",               # Greek (Greece)
    "Turkish": "tr",             # Turkish (Turkey)
    "Hebrew": "he",              # Hebrew (Israel)
    "Hindi": "hi",               # Hindi (India)
    "Bengali": "bn",             # Bengali (West Bengal, Tripura)
    "Tamil": "ta",               # Tamil (Tamil Nadu, Puducherry)
    "Telugu": "te",              # Telugu (Andhra Pradesh, Telangana)
    "Marathi": "mr",             # Marathi (Maharashtra, Goa)
    "Kannada": "kn",             # Kannada (Karnataka)
    "Gujarati": "gu",            # Gujarati (Gujarat, Daman and Diu)
    "Punjabi": "pa",             # Punjabi (Punjab)
    "Odia": "or",                # Odia (Odisha)
    "Malayalam": "ml",           # Malayalam (Kerala, Lakshadweep)
    "Assamese": "as",            # Assamese (Assam, Assam)
    "Urdu": "ur",                # Urdu (Jammu and Kashmir, Telangana)
    "Sanskrit": "sa",            # Sanskrit (Scholarly language)
    "Konkani": "kok",            # Konkani (Goa, Karnataka)
    "Manipuri": "mni",           # Manipuri (Manipur)
    "Nepali": "ne",              # Nepali (Sikkim, West Bengal)
    "Sindhi": "sd",              # Sindhi (Sindh, Pakistan)
    "Maithili": "mai",           # Maithili (Bihar)
    "Kashmiri": "ks",            # Kashmiri (Jammu and Kashmir)
    "Haryanvi": "bgc",           # Haryanvi (Haryana)
    "Santali": "sat",            # Santali (Jharkhand, Odisha)
    "Khasi": "kha",              # Khasi (Meghalaya)
    "Dogri": "dgo",              # Dogri (Jammu and Kashmir)
    "Naga": "nag",               # Naga (Nagaland)
    "Mizo": "lus",               # Mizo (Mizoram)
    "Tulu": "tcy",               # Tulu (Karnataka)
    "Kokborok": "trp",           # Kokborok (Tripura)
    "Angika": "anp",             # Angika (Bihar)
    "Bodo": "brx",               # Bodo (Assam, Bodoland)
    "Kurukh": "kru",             # Kurukh (Jharkhand, Odisha)
    "Yoruba": "yo",              # Yoruba (Nigeria)
    "Swahili": "sw",             # Swahili (East Africa)
    "Tagalog": "tl",             # Tagalog (Philippines)
    "Vietnamese": "vi",          # Vietnamese (Vietnam)
    "Thai": "th",                # Thai (Thailand)
    "Indonesian": "id",          # Indonesian (Indonesia)
    "Malay": "ms",               # Malay (Malaysia)
    "Filipino": "fil",           # Filipino (Philippines)
    "Farsi": "fa",               # Farsi (Iran)
    "Polish": "pl",              # Polish (Poland)
    "Czech": "cs",               # Czech (Czech Republic)
    "Hungarian": "hu",           # Hungarian (Hungary)
    "Romanian": "ro",            # Romanian (Romania)
    "Bulgarian": "bg",           # Bulgarian (Bulgaria)
    "Ukrainian": "uk",           # Ukrainian (Ukraine)
    "Belarusian": "be",          # Belarusian (Belarus)
    "Slovak": "sk",              # Slovak (Slovakia)
    "Slovenian": "sl",           # Slovenian (Slovenia)
    "Croatian": "hr",            # Croatian (Croatia)
    "Serbian": "sr",             # Serbian (Serbia)
    "Bosnian": "bs",             # Bosnian (Bosnia and Herzegovina)
    "Macedonian": "mk",          # Macedonian (North Macedonia)
    "Albanian": "sq",            # Albanian (Albania)
    "Greek (Ancient)": "grc",    # Ancient Greek (Scholarly language)
    # Add more languages as needed
}

language = st.sidebar.selectbox("Select your language", list(languages.keys()))

# Translate function
def tr(text):
    return translate_text(text, language)

# Add customized selectbox style
st.markdown(selectbox_style, unsafe_allow_html=True)

# Header with Full Screen Image
st.markdown(
    """
    <div style="background-color:#333; padding:0; text-align:center;">
        <img src="https://images.ctfassets.net/pxcfulgsd9e2/articleImage101563/05e291b80b72bf6332662e6fa39d1f9d/Stroke-prevention-HN1410-iStock-1249957366-Cover-Sized.jpg?f=top&fit=fill&fm=webp&h=1284&q=35&w=2280" alt="Your Logo" style="max-width: 100%; height: 350px;">
    </div>
    """,
    unsafe_allow_html=True,
)

# Header
st.header(tr('STROKE PREDICTION APP'))

# Sidebar
st.sidebar.markdown(f"<h1 style='font-weight: bold; font-size: 24px;'>{tr('Choose Option')}</h1>", unsafe_allow_html=True)
tool_option = st.sidebar.selectbox(tr("Choose a Tool"), (tr("Stroke Prediction"), tr("BMI Calculator"), tr("Height to CM Converter")))

# Define a mapping dictionary for feature names
feature_name_mapping = {
    tr('age'): 'age',
    tr('avg_glucose_level'): 'avg_glucose_level',
    tr('bmi'): 'bmi',
    tr('gender_Male'): 'gender_Male',
    tr('ever_married_Yes'): 'ever_married_Yes',
    tr('work_type_Govt_job'): 'work_type_Govt_job',
    tr('work_type_Never_worked'): 'work_type_Never_worked',
    tr('work_type_Private'): 'work_type_Private',
    tr('work_type_Self-employed'): 'work_type_Self-employed',
    tr('work_type_children'): 'work_type_children',
    tr('Residence_type_Urban'): 'Residence_type_Urban',
    tr('smoking_status_formerly smoked'): 'smoking_status_formerly smoked',
    tr('smoking_status_smokes'): 'smoking_status_smokes'
}

# Initialize pred_prob variable with a default value
pred_prob = [0.0]

if tool_option == tr("Stroke Prediction"):
    st.sidebar.markdown(f"<h1 style='font-weight: bold;'>{tr('Input features')}:</h1>", unsafe_allow_html=True)
    age = st.sidebar.slider(tr('Age:'), 1, 100, 20, key="age_slider")
    avg_glucose_level = st.sidebar.slider(tr('Glucose level'), 1.0, 500.0, 70.0, key="glucose_slider")
    bmi = st.sidebar.slider(tr('What is your BMI?'), 1.0, 100.0, 24.9, key="bmi_slider")
    ever_married = st.sidebar.selectbox(tr("Are you married?"), (tr('Yes'), tr('No')))
    gender = st.sidebar.selectbox(tr("What is your gender?"), (tr('Male'), tr('Female')))
    work_type = st.sidebar.selectbox(tr("Which of the following best describes your work type?"), (tr('Private'), tr('Self-employed'), tr('Govt_job'), tr('children'), tr('Never_worked')))
    residence_type = st.sidebar.selectbox(tr("What is your residence type?"), (tr('Urban'), tr('Rural')))
    smoking_status = st.sidebar.selectbox(tr("What is your smoking status?"), (tr('formerly smoked'), tr('never smoked'), tr('smokes')))

    ever_married_indx = 1 if ever_married == tr('Yes') else 0
    gender_indx = 1 if gender == tr('Male') else 0

    work_type_input = work_type
    work_type_indx = {
        tr('Private'): 0,
        tr('Self-employed'): 0,
        tr('Govt_job'): 0,
        tr('children'): 0,
        tr('Never_worked'): 0,
    }
    work_type_indx[work_type_input] = 1

    residence_type_indx = 1 if residence_type == tr('Urban') else 0

    smoking_status_input = smoking_status
    smoking_status_formerly_smoked_indx = 1 if smoking_status_input == tr('formerly smoked') else 0
    smoking_status_smokes_indx = 1 if smoking_status_input == tr('smokes') else 0

    data = {
        feature_name_mapping[tr('age')]: [age],
        feature_name_mapping[tr('avg_glucose_level')]: [avg_glucose_level],
        feature_name_mapping[tr('bmi')]: [bmi],
        feature_name_mapping[tr('gender_Male')]: [gender_indx],
        feature_name_mapping[tr('ever_married_Yes')]: [ever_married_indx],
        feature_name_mapping[tr('work_type_Govt_job')]: [work_type_indx[tr('Govt_job')]],
        feature_name_mapping[tr('work_type_Never_worked')]: [work_type_indx[tr('Never_worked')]],
        feature_name_mapping[tr('work_type_Private')]: [work_type_indx[tr('Private')]],
        feature_name_mapping[tr('work_type_Self-employed')]: [work_type_indx[tr('Self-employed')]],
        feature_name_mapping[tr('work_type_children')]: [work_type_indx[tr('children')]],
        feature_name_mapping[tr('Residence_type_Urban')]: [residence_type_indx],
        feature_name_mapping[tr('smoking_status_formerly smoked')]: [smoking_status_formerly_smoked_indx],
        feature_name_mapping[tr('smoking_status_smokes')]: [smoking_status_smokes_indx]
    }

    test_df = pd.DataFrame(data)

    if st.sidebar.button(tr("Predict Stroke Probability")):
        pred_prob = model.predict_proba(test_df)[:, 1]
        st.subheader(tr('Output'))
        st.write(f"<b>{tr('Predicted probability of having a stroke')}:</b> {pred_prob[0] * 100:.2f}%", unsafe_allow_html=True)

elif tool_option == tr("BMI Calculator"):
    st.sidebar.markdown(f"<h1 style='font-weight: bold;'>{tr('BMI Calculator')}:</h1>", unsafe_allow_html=True)
    weight_kg = st.sidebar.number_input(tr("Enter your weight (kg):"))
    height_cm = st.sidebar.number_input(tr("Enter your height (cm):"))

    if st.sidebar.button(tr("Calculate BMI")):
        height_m = height_cm / 100
        bmi = weight_kg / (height_m ** 2)
        st.subheader(tr('BMI Calculator'))
        st.write(f"{tr('Your BMI is')} {bmi:.2f}")
        st.write(tr('Interpretation:'))
        if bmi < 18.5:
            st.write(tr('Underweight'))
        elif 18.5 <= bmi < 24.9:
            st.write(tr('Normal Weight'))
        elif 25 <= bmi < 29.9:
            st.write(tr('Overweight'))
        else:
            st.write(tr('Obese'))

elif tool_option == tr("Height to CM Converter"):
    st.sidebar.markdown(f"<h1 style='font-weight: bold;'>{tr('Height to CM Converter')}:</h1>", unsafe_allow_html=True)
    feet = st.sidebar.number_input(tr("Feet:"))
    inches = st.sidebar.number_input(tr("Inches:"))

    if st.sidebar.button(tr("Convert to CM")):
        height_cm = (feet * 30.48) + (inches * 2.54)
        st.subheader(tr('Height to CM Converter'))
        st.write(f"{tr('Your height is')} {height_cm:.2f} cm")

# Add input for name, address, and contact number
name = st.text_input(tr('Name'))
address = st.text_area(tr('Address'))
contact_number = st.text_input(tr('Contact Number'))

# Add input for date of birth
date_of_birth = st.sidebar.date_input(tr('Date of Birth'), min_value=date(1900, 1, 1), max_value=date.today())

# Add a Calendar to the App:
st.sidebar.markdown(f"<h1 style='font-weight: bold;'>{tr('Calendar')}:</h1>", unsafe_allow_html=True)
selected_date = st.sidebar.date_input(tr("Select a Date"), min_value=date(2023, 1, 1), max_value=date(2023, 12, 31))
st.sidebar.button(tr("Clear Date"), key='clear_date')
formatted_date = selected_date.strftime("%d %B %Y")  # Format the selected date
st.write(tr("Date:"), formatted_date)  # Display the formatted date

# Predicted Probability to Excel and PDF
if st.sidebar.button(tr("Export Results")):
    # Calculate predicted probability before exporting
    if tool_option == tr("Stroke Prediction"):
        pred_prob = model.predict_proba(test_df)[:, 1]

    # Create a DataFrame with the result
    result_df = pd.DataFrame({
        tr("Name"): [name],
        tr("Address"): [address],
        tr("Contact Number"): [contact_number],
        tr("Date"): [formatted_date],  # Use the formatted date
        tr("Age"): [age],
        tr("Average Glucose Level"): [avg_glucose_level],
        tr("BMI"): [bmi],
        tr("Gender"): [gender],
        tr("Marital Status"): [ever_married],
        tr("Work Type"): [work_type],
        tr("Residence Type"): [residence_type],
        tr("Smoking Status"): [smoking_status],
        tr("Date of Birth"): [date_of_birth.strftime('%d %B %Y')],
        tr("Predicted Probability of Stroke"): [pred_prob[0] * 100]  # Include predicted probability as a percentage
    })

    # Save to Excel
    result_df.to_excel('stroke_prediction_result.xlsx', index=False)

    # Create a PDF report
    class PDF(FPDF):
        def header(self):
            self.set_font("Arial", "B", 12)
            self.cell(0, 10, tr("Stroke Prediction Report"), 0, 1, "C")

        def footer(self):
            self.set_y(-15)
            self.set_font("Arial", "I", 8)
            self.cell(0, 10, f"{tr('Page')} {self.page_no()}", 0, 0, "C")

        def chapter_title(self, title):
            self.set_font("Arial", "B", 12)
            self.cell(0, 10, title, 0, 1, "L")
            self.ln(10)

        def chapter_body(self, body):
            self.set_font("Arial", "", 12)
            self.multi_cell(0, 10, body)
            self.ln()

    pdf = PDF()
    pdf.add_page()
    pdf.chapter_title(tr("Patient Information"))
    pdf.chapter_body(f"{tr('Name')}: {name}")
    pdf.chapter_body(f"{tr('Address')}: {address}")
    pdf.chapter_body(f"{tr('Contact Number')}: {contact_number}")
    pdf.chapter_body(f"{tr('Date of Birth')}: {date_of_birth.strftime('%d %B %Y')}")
    pdf.chapter_body(f"{tr('Date')}: {formatted_date}")  # Use the formatted date
    pdf.chapter_title(tr("Stroke Prediction"))
    pdf.chapter_body(f"{tr('Age')}: {age}")
    pdf.chapter_body(f"{tr('Average Glucose Level')}: {avg_glucose_level}")
    pdf.chapter_body(f"{tr('BMI')}: {bmi}")
    pdf.chapter_body(f"{tr('Gender')}: {gender}")
    pdf.chapter_body(f"{tr('Marital Status')}: {ever_married}")
    pdf.chapter_body(f"{tr('Work Type')}: {work_type}")
    pdf.chapter_body(f"{tr('Residence Type')}: {residence_type}")
    pdf.chapter_body(f"{tr('Smoking Status')}: {smoking_status}")
    pdf.chapter_body(f"{tr('Predicted Probability of Stroke')}: {pred_prob[0] * 100:.2f}%")  # Include predicted probability as a percentage

    pdf_file_path = 'stroke_prediction_report.pdf'
    pdf.output(pdf_file_path)

    # Provide download links for both files
    st.markdown(get_download_link('stroke_prediction_result.xlsx', tr("Download Excel Report")), unsafe_allow_html=True)
    st.markdown(get_download_link(pdf_file_path, tr("Download PDF Report")), unsafe_allow_html=True)
