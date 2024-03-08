import sqlite3
import os
from django.shortcuts import render
from django.http import JsonResponse
import requests
from django.contrib import auth
from django.contrib.auth.models import User

# Create your views here.
def chatbot(request):
    if request.method == 'POST':
        message = request.POST.get('message')

 #        response = query({
 #        "inputs": f'''<|system|>You are providing preliminary information as a medical assistant.\n
 # Offer a preliminary diagnosis based on the user's query.\n
 # Answer in bullet points\n
 # Mandatorily include the medical specialization at the end of the answer in one word.</s> <|user|>{message}</s> <|assistant|>''',
 #    })
 #        print(response)
        response = resp1
        db_path = os.path.abspath('/home/deepakachu/Desktop/MedMatch0/chatbot/doctors_database.db')

        # Create an instance of the DoctorDatabase class with the correct path
        doctors_db = DoctorDatabase(db_name=db_path)
        doctor_list, area = fetch_specialist_list(response, doctors_db)
        # print(doctor_list, area)
        response = resp1+get_final_response(doctor_list, area)
        print(response)

        return JsonResponse({'message':message, 'response':response})
        # return response

    return render(request, 'chatbot/chatbot.html')


import requests

API_URL = "https://api-inference.huggingface.co/models/HuggingFaceH4/zephyr-7b-gemma-v0.1"
headers = {"Authorization": "Bearer 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"}



def query(payload):
    payload["max_tokens"] = 2000  # Adjust the value based on your desired length
    delimiter = "<|assistant|>"
    response = requests.post(API_URL, headers=headers, json=payload)
    return response.json()[0]['generated_text'].split(delimiter, 1)[-1].strip()

def login(request):
    return render(request, 'chatbot/login.html')

def logout(request):
    auth.logout(request)
# def register(request):
#     if request.method == 'POST':
#         username = request.POST['username']
#         email = request.POST['email']
#         password1 = request.POST['password1']
#         password2 = request.POST['password2']
#
#         if password1 != password2:
#             error_message = "Passwords don't match"
#             return render(request, 'chatbot/register.html', {'error_message':error_message})
#         else:
#             try:
#
class Doctor:
    def __init__(self, name, specialization, contact_number, email=None,
                 office_address=None,
                 experience_years=None, education=None,
                 languages_spoken=None, availability=None):
        self.doctor_data = {
            'name': name,
            'specialization': specialization,
            'contact_number': contact_number,
            'email': email,
            'office_address': office_address,
            'experience_years': experience_years,
            'education': education,
            'languages_spoken': languages_spoken,
            'availability': availability,
        }

class DoctorDatabase:
    def __init__(self, db_name='/home/deepakachu/Desktop/MedMatch0/chatbot/doctors_database.db'):
        self.conn = sqlite3.connect(db_name)
        self.cursor = self.conn.cursor()
        self.create_table()

    def create_table(self):
        self.cursor.execute('''
        CREATE TABLE IF NOT EXISTS Doctors (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        specialization TEXT NOT NULL,
        contact_number TEXT NOT NULL,
        email TEXT,
        office_address TEXT,
        experience_years INTEGER,
        education TEXT,
        languages_spoken TEXT,
        availability TEXT
            )
        ''')
        self.conn.commit()

    def insert_doctor(self, doctor_data):
        query = '''
            INSERT INTO Doctors (
                name, specialization, contact_number, email, office_address,
                experience_years,
                education, languages_spoken, availability
            )
            VALUES (
                :name, :specialization, :contact_number, :email,
                :office_address, :experience_years,
                :education, :languages_spoken, :availability
            )
        '''
        self.cursor.execute(query, doctor_data)
        self.conn.commit()

    def get_doctors_by_specialization(self, specialization):
        query = '''
            SELECT * FROM Doctors
            WHERE specialization = ?
        '''
        self.cursor.execute(query, (specialization,))
        doctors = self.cursor.fetchall()
        return doctors

    def close_connection(self):
        self.conn.close()


def fetch_specialist_list(paragraph, doctors_db):
    words = paragraph.split()
    found_doctors = []
    medical_area = None

    for word in words:
        doctors_with_specialization = doctors_db.get_doctors_by_specialization(word)
        if doctors_with_specialization:
            found_doctors.extend(doctors_with_specialization)
            medical_area = word
            break

    # Close the connection
    doctors_db.close_connection()

    if found_doctors:
      return found_doctors, medical_area

    else:
      return None, medical_area


def get_final_response(doctor_list=None, speciality=None):
    if doctor_list is None:
        return "\n\nBased on the diagnosis, no suitable specialists found in the database, please visit your nearest general physician"

    response = f"\n\nBased on the diagnosis, here are the doctors from our database that specialize in {speciality}\n"

    for doctor in doctor_list:
        # print(doctor)
        response += (
            f"- Name: {doctor[1]}\n"
            f"  Specialization: {doctor[2]}\n"
            f"  Contact Number: {doctor[3]}\n"
            f"  Email: {doctor[4]}\n"
            f"  Office Address: {doctor[5]}\n"
            f"  Experience (Years): {doctor[6]}\n"
            f"  Education: {doctor[7]}\n"
            f"  Languages Spoken: {doctor[8]}\n"
            f"  Availability: {doctor[9]}\n\n"
        )

    return response



resp1 = '''Preliminary Diagnosis:

Based on your query, it seems that you are experiencing flaky rashes and itchy skin. This could be caused by several factors, including allergies, eczema, or psoriasis. However, without conducting a thorough physical examination and gathering additional information, it is difficult to provide a definitive diagnosis.

Preliminary Recommendation:

If the rashes are causing significant discomfort or are not improving with over-the-counter treatments, it may be best to consult a dermatologist for further evaluation and treatment.

Additional Information:

It is essential to note that a flaky rash could be a symptom of a more severe underlying condition, such as psoriasis or eczema. If left untreated, these conditions can lead to complications, including skin infections and increased risk of developing mental health disorders.

In case of an emergency, contact the following emergency medical services in India:

* National Emergency Medical Services: 108
* Apollo Hospitals: 1860 108 3333
* Fortis Hospitals: 1860 2666 3333

Specialist's Response:

Dermatology'''