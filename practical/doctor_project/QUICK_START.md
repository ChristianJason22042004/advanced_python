# 🚀 QUICK START GUIDE - Doctor Project

## 5-Minute Setup

### Step 1: Start Server
```bash
cd doctor_project
python manage.py runserver
```

### Step 2: Access Admin
- URL: `http://127.0.0.1:8000/admin/`
- Create superuser first: `python manage.py createsuperuser`

### Step 3: Add Sample Doctors
Option A - Via Admin Panel:
- Go to `http://127.0.0.1:8000/admin/doctor/doctor/`
- Click "Add Doctor"
- Fill form and save

Option B - Via Django Shell:
```bash
python manage.py shell
>>> exec(open('sample_data.py').read())
```

### Step 4: View Doctors
- Doctor List: `http://127.0.0.1:8000/doctors/`
- Doctor Detail: `http://127.0.0.1:8000/doctors/1/`
- API: `http://127.0.0.1:8000/api/doctors/`

---

## File Structure

```
doctor_project/
├── manage.py
├── db.sqlite3
├── sample_data.py          ← Sample doctors script
├── README.md               ← Full documentation
│
├── doctor_project/
│   ├── settings.py        ← Configuration
│   ├── urls.py            ← Main routing
│   ├── wsgi.py
│   └── asgi.py
│
└── doctor/
    ├── models.py          ← Doctor model (12 fields)
    ├── admin.py           ← Admin interface
    ├── views.py           ← 4 view functions
    ├── urls.py            ← App routing
    ├── migrations/
    │   └── 0001_initial.py
    └── templates/doctor/
        ├── base.html      ← Base layout
        ├── doctor_list.html
        └── doctor_detail.html
```

---

## Key Features

✅ Doctor model with 12 fields  
✅ Admin interface with filtering & search  
✅ Doctor listing page  
✅ Doctor profile page  
✅ REST API (JSON)  
✅ Form validation  
✅ Modern responsive design  
✅ Fully documented code  

---

## Important URLs

| URL | Purpose |
|-----|---------|
| `/admin/` | Django admin panel |
| `/doctors/` | All doctors list |
| `/doctors/1/` | Doctor detail (ID=1) |
| `/doctors/?specialization=cardiology` | Filter by specialty |
| `/doctors/specialty/cardiology/` | Specialty view |
| `/api/doctors/` | API list (JSON) |

---

## Quick Commands

```bash
# Run server
python manage.py runserver

# Create admin user
python manage.py createsuperuser

# Add sample data
python manage.py shell
>>> exec(open('sample_data.py').read())

# Make migrations
python manage.py makemigrations

# Apply migrations
python manage.py migrate

# Access Django shell
python manage.py shell

# Create backup
python manage.py dumpdata > backup.json

# Restore backup
python manage.py loaddata backup.json
```

---

## Doctor Model Fields

| Field | Type | Notes |
|-------|------|-------|
| first_name | CharField | Doctor's first name |
| last_name | CharField | Doctor's last name |
| specialization | CharField | 15+ medical specialties |
| email | EmailField | Unique, required |
| phone | CharField | 10 digits validation |
| experience_years | IntegerField | Years of experience |
| hospital_affiliation | CharField | Associated hospital |
| consultation_fee | DecimalField | Fee in USD |
| is_available | BooleanField | Accepting new patients |
| bio | TextField | Professional biography |
| created_at | DateTimeField | Auto-set on creation |
| updated_at | DateTimeField | Auto-update on save |

---

## Admin Features

**Filtering:**
- By specialization
- By availability
- By experience level
- By creation date

**Searching:**
- By name (first/last)
- By email
- By specialty

**Bulk Actions:**
- Mark available
- Mark unavailable

---

## Django Shell Examples

```python
from doctor.models import Doctor

# Create doctor
Doctor.objects.create(
    first_name="John",
    last_name="Smith",
    specialization="cardiology",
    email="john@hospital.com",
    phone="9876543210",
    experience_years=15,
    consultation_fee=100.00
)

# Get all doctors
Doctor.objects.all()

# Filter by specialty
Doctor.objects.filter(specialization="cardiology")

# Filter available doctors
Doctor.objects.filter(is_available=True)

# Get specific doctor
Doctor.objects.get(pk=1)

# Update doctor
doctor = Doctor.objects.get(pk=1)
doctor.is_available = False
doctor.save()

# Delete doctor
doctor.delete()

# Count doctors
Doctor.objects.count()
Doctor.objects.filter(specialization="cardiology").count()

# Helper methods
doctor.get_full_name()      # "John Smith"
doctor.get_display_name()  # "Dr. John Smith"
doctor.years_experience_level()  # "Expert" / "Senior" etc
```

---

## API Examples

```bash
# Get all doctors
curl http://127.0.0.1:8000/api/doctors/

# Filter by specialty
curl "http://127.0.0.1:8000/api/doctors/?specialization=cardiology"

# Get available doctors only
curl "http://127.0.0.1:8000/api/doctors/?available_only=true"

# Limit results
curl "http://127.0.0.1:8000/api/doctors/?limit=5"

# Combine filters
curl "http://127.0.0.1:8000/api/doctors/?specialization=surgery&available_only=true&limit=10"
```

---

## Customization Examples

### Add New Specialty

Edit `doctor/models.py`:
```python
SPECIALIZATION_CHOICES = [
    # ... existing choices
    ('radiology', 'Radiology'),  # Add this
]
```

Run:
```bash
python manage.py makemigrations
python manage.py migrate
```

### Add New Field

Edit `doctor/models.py`:
```python
license_number = models.CharField(max_length=50, unique=True)
```

Run:
```bash
python manage.py makemigrations
python manage.py migrate
```

### Customize Admin Display

Edit `doctor/admin.py` - Change these:
```python
list_display = (...)      # Columns in list
list_filter = (...)       # Sidebar filters
search_fields = (...)     # Searchable fields
fieldsets = (...)         # Form organization
```

---

## Troubleshooting

**Server won't start:**
```bash
python manage.py migrate
python manage.py runserver
```

**Admin page not found:**
- Make sure migrations are applied: `python manage.py migrate`

**Can't see doctors on page:**
- Add doctors via admin or sample_data.py script

**Phone validation error:**
- Phone must be exactly 10 digits (no spaces/dashes)

**Email not unique error:**
- Email is unique, use different email

---

## Next Steps

1. ✅ Start server and access application
2. ✅ Add test doctors via admin
3. ✅ Browse doctor list and profiles
4. ✅ Test API endpoints
5. ✅ Customize as needed

---

## Need Help?

Refer to:
- Full README.md for complete documentation
- Django docs: https://docs.djangoproject.com/
- Code comments in models.py, admin.py, views.py

---

**Happy coding! 🎉**
