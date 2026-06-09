from django.db import models

class Registration(models.Model):
    TITLE_CHOICES = [
        ('Mr', 'Mr.'),
        ('Mrs', 'Mrs.'),
        ('Ms', 'Ms.'),
        ('Miss', 'Miss'),
        ('Dr', 'Dr.'),
        ('Prof', 'Prof.'),
        ('Other', 'Other'),
    ]

    CATEGORY_CHOICES = [
        ('Undergraduate Student Pass', 'Undergraduate Student Pass (₦5,000)'),
        ('Postgraduate Delegate', 'Postgraduate Delegate (₦15,000)'),
        ('Academic & Regular Delegate', 'Academic & Regular Delegate (₦30,000)'),
        ('International Delegate', 'International Delegate ($100)'),
    ]

    TRACK_CHOICES = [
        ('Emerging and re-emerging infectious diseases', 'Emerging and re-emerging infectious diseases'),
        ('Non-communicable diseases: monogenic and complex traits', 'Non-communicable diseases: monogenic and complex traits'),
        ('Zoonotic spillover prevention in wildlife–livestock contact zones', 'Zoonotic spillover prevention in wildlife–livestock contact zones'),
        ('Antimicrobial resistance at the human–animal–environment interface', 'Antimicrobial resistance at the human–animal–environment interface'),
        ('Conservation, climate change and environmental health', 'Conservation, climate change and environmental health'),
        ('Forensics, integrated data systems and Bio-surveillance', 'Forensics, integrated data systems and Bio-surveillance'),
        ('Drug discovery and design', 'Drug discovery and design'),
        ('Food security, biosecurity and safety', 'Food security, biosecurity and safety'),
    ]

    title = models.CharField(max_length=10, choices=TITLE_CHOICES)
    name = models.CharField(max_length=255)
    email = models.EmailField()
    institution = models.CharField(max_length=255)
    category = models.CharField(max_length=50, choices=CATEGORY_CHOICES)
    track = models.CharField(max_length=100, choices=TRACK_CHOICES)
    dietary_requirements = models.CharField(max_length=255, blank=True)
    payment_reference = models.CharField(max_length=255, blank=True)
    receipt = models.FileField(upload_to='receipts/', blank=True, null=True)
    pref_plenary = models.BooleanField(default=True)
    pref_poster = models.BooleanField(default=True)
    pref_dinner = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.title} {self.name} - {self.email}"


class ContactMessage(models.Model):
    SUBJECT_CHOICES = [
        ('General Support / Questions', 'General Support / Questions'),
        ('Abstract Submission Portal Support', 'Abstract Submission Portal Support'),
        ('Sponsorship & Exhibitor Space', 'Sponsorship & Exhibitor Space'),
        ('Payment & Invoicing Inquiries', 'Payment & Invoicing Inquiries'),
    ]

    name = models.CharField(max_length=255)
    email = models.EmailField()
    subject = models.CharField(max_length=100, choices=SUBJECT_CHOICES)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} - {self.subject}"


class AbstractSubmission(models.Model):
    TRACK_CHOICES = [
        ('1. Emerging and re-emerging infectious diseases', '1. Emerging and re-emerging infectious diseases'),
        ('2. Non-communicable diseases: monogenic and complex traits', '2. Non-communicable diseases: monogenic and complex traits'),
        ('3. Zoonotic spillover prevention in wildlife–livestock contact zones', '3. Zoonotic spillover prevention in wildlife–livestock contact zones'),
        ('4. Antimicrobial resistance at the human–animal–environment interface', '4. Antimicrobial resistance at the human–animal–environment interface'),
        ('5. Conservation, climate change and environmental health', '5. Conservation, climate change and environmental health'),
        ('6. Forensics, integrated data systems and Bio-surveillance', '6. Forensics, integrated data systems and Bio-surveillance'),
        ('7. Drug discovery and design', '7. Drug discovery and design'),
        ('8. Food security, biosecurity and safety', '8. Food security, biosecurity and safety'),
    ]

    PRESENTATION_TYPE_CHOICES = [
        ('Oral Presentation', 'Oral Presentation'),
        ('Poster Presentation', 'Poster Presentation'),
    ]

    author_name = models.CharField(max_length=255)
    email = models.EmailField()
    affiliation = models.CharField(max_length=255)
    track = models.CharField(max_length=100, choices=TRACK_CHOICES)
    presentation_type = models.CharField(max_length=50, choices=PRESENTATION_TYPE_CHOICES)
    abstract_title = models.CharField(max_length=255)
    document = models.FileField(upload_to='abstracts/')
    guidelines_confirmed = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.abstract_title} by {self.author_name}"
