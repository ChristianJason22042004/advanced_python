"""
Sample Data Script for Doctor Project
====================================

This script creates sample doctor records for testing the application.
Run with: python manage.py shell < sample_data.py

Or manually in Django shell:
python manage.py shell
>>> exec(open('sample_data.py').read())
"""

from doctor.models import Doctor

# Clear existing doctors (optional)
# Doctor.objects.all().delete()

# Sample doctors data
doctors_data = [
    {
        'first_name': 'John',
        'last_name': 'Smith',
        'specialization': 'cardiology',
        'email': 'john.smith@hospital.com',
        'phone': '9876543210',
        'experience_years': 15,
        'hospital_affiliation': 'City Medical Center',
        'consultation_fee': 100.00,
        'is_available': True,
        'bio': 'Dr. John Smith is a board-certified cardiologist with 15 years of experience in interventional cardiology. He specializes in coronary angiography and has published numerous peer-reviewed articles.'
    },
    {
        'first_name': 'Jane',
        'last_name': 'Doe',
        'specialization': 'surgery',
        'email': 'jane.doe@hospital.com',
        'phone': '5551234567',
        'experience_years': 12,
        'hospital_affiliation': 'General Hospital',
        'consultation_fee': 125.00,
        'is_available': True,
        'bio': 'Dr. Jane Doe is an experienced general surgeon with 12 years of practice. She specializes in minimally invasive surgical techniques and has performed over 1000 successful surgeries.'
    },
    {
        'first_name': 'Michael',
        'last_name': 'Johnson',
        'specialization': 'neurology',
        'email': 'michael.johnson@clinic.com',
        'phone': '4445556666',
        'experience_years': 18,
        'hospital_affiliation': 'Neurological Institute',
        'consultation_fee': 150.00,
        'is_available': False,
        'bio': 'Dr. Michael Johnson is a leading neurologist with expertise in neurodegenerative diseases and complex neurological conditions. He holds a fellowship from Johns Hopkins.'
    },
    {
        'first_name': 'Sarah',
        'last_name': 'Williams',
        'specialization': 'pediatrics',
        'email': 'sarah.williams@hospital.com',
        'phone': '7778889999',
        'experience_years': 8,
        'hospital_affiliation': 'Children\'s Hospital',
        'consultation_fee': 75.00,
        'is_available': True,
        'bio': 'Dr. Sarah Williams is a compassionate pediatrician dedicated to providing excellent care to children. She has a special interest in developmental pediatrics and preventive medicine.'
    },
    {
        'first_name': 'David',
        'last_name': 'Brown',
        'specialization': 'dermatology',
        'email': 'david.brown@clinic.com',
        'phone': '1112223333',
        'experience_years': 10,
        'hospital_affiliation': 'Skin Health Clinic',
        'consultation_fee': 90.00,
        'is_available': True,
        'bio': 'Dr. David Brown is a certified dermatologist with expertise in cosmetic and medical dermatology. He uses the latest technologies for skin treatments and procedures.'
    },
    {
        'first_name': 'Emily',
        'last_name': 'Davis',
        'specialization': 'orthopedics',
        'email': 'emily.davis@orthocenter.com',
        'phone': '5556667777',
        'experience_years': 14,
        'hospital_affiliation': 'Ortho Excellence Center',
        'consultation_fee': 110.00,
        'is_available': True,
        'bio': 'Dr. Emily Davis is an orthopedic surgeon specializing in joint replacement and sports medicine. She has trained with leading orthopedic surgeons worldwide.'
    },
    {
        'first_name': 'Robert',
        'last_name': 'Miller',
        'specialization': 'psychiatry',
        'email': 'robert.miller@mentalhealth.com',
        'phone': '9998887777',
        'experience_years': 20,
        'hospital_affiliation': 'Mental Health Center',
        'consultation_fee': 120.00,
        'is_available': False,
        'bio': 'Dr. Robert Miller is an experienced psychiatrist with 20 years in clinical practice. He specializes in mood disorders and psychopharmacology.'
    },
    {
        'first_name': 'Lisa',
        'last_name': 'Taylor',
        'specialization': 'general',
        'email': 'lisa.taylor@clinic.com',
        'phone': '2223334444',
        'experience_years': 6,
        'hospital_affiliation': 'Primary Care Clinic',
        'consultation_fee': 60.00,
        'is_available': True,
        'bio': 'Dr. Lisa Taylor is a dedicated general practitioner focused on preventive care and patient education. She believes in comprehensive, holistic healthcare.'
    },
    {
        'first_name': 'James',
        'last_name': 'Anderson',
        'specialization': 'ophthalmology',
        'email': 'james.anderson@eyecenter.com',
        'phone': '3334445555',
        'experience_years': 16,
        'hospital_affiliation': 'Eye Care Center',
        'consultation_fee': 95.00,
        'is_available': True,
        'bio': 'Dr. James Anderson is an ophthalmologist with expertise in cataract surgery and LASIK procedures. He is committed to restoring vision and improving quality of life.'
    },
    {
        'first_name': 'Amanda',
        'last_name': 'Martinez',
        'specialization': 'gastroenterology',
        'email': 'amanda.martinez@gi-clinic.com',
        'phone': '6667778888',
        'experience_years': 11,
        'hospital_affiliation': 'Gastrointestinal Clinic',
        'consultation_fee': 105.00,
        'is_available': True,
        'bio': 'Dr. Amanda Martinez specializes in digestive health and gastrointestinal disorders. She is skilled in endoscopic procedures and has helped many patients improve their digestive health.'
    },
]

# Create doctors
created_count = 0
for doctor_data in doctors_data:
    try:
        # Check if doctor already exists by email
        if not Doctor.objects.filter(email=doctor_data['email']).exists():
            doctor = Doctor.objects.create(**doctor_data)
            print(f"✅ Created: {doctor.get_display_name()}")
            created_count += 1
        else:
            print(f"⏭️  Skipped: {doctor_data['email']} (already exists)")
    except Exception as e:
        print(f"❌ Error creating doctor: {doctor_data.get('email', 'Unknown')} - {str(e)}")

print(f"\n📊 Summary: {created_count} new doctors created")
print(f"📈 Total doctors in database: {Doctor.objects.count()}")

# Display all doctors
print("\n📋 All Doctors:")
for doctor in Doctor.objects.all():
    print(f"  - {doctor} | Available: {doctor.is_available} | Fee: ${doctor.consultation_fee}")
