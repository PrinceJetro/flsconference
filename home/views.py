from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
from django.contrib.admin.views.decorators import staff_member_required
from .models import Registration, ContactMessage, AbstractSubmission, SpecialGuest, Speaker


def home(request):
    return render(request, 'home.html')


def about(request):
    return render(request, 'about_one_health_conference.html')


def abstract_submission(request):
    context = {}
    if request.method == 'POST':
        author_name = request.POST.get('author_name', '').strip()
        email = request.POST.get('email', '').strip()
        affiliation = request.POST.get('affiliation', '').strip()
        track = request.POST.get('track', '').strip()
        presentation_type = request.POST.get('presentation_type', '').strip()
        abstract_title = request.POST.get('abstract_title', '').strip()
        guidelines_confirmed = request.POST.get('guidelines_read') is not None
        document = request.FILES.get('document')

        errors = []
        if not author_name:
            errors.append('Corresponding author name is required.')
        if not email:
            errors.append('A valid email address is required.')
        if not affiliation:
            errors.append('Institutional affiliation is required.')
        if not track:
            errors.append('Thematic track selection is required.')
        if not presentation_type:
            errors.append('Presentation type selection is required.')
        if not abstract_title:
            errors.append('Abstract title is required.')
        if not document:
            errors.append('Please upload your Word document (.doc or .docx).')
        elif not document.name.lower().endswith(('.doc', '.docx')):
            errors.append('The abstract document must be a .doc or .docx file.')
        if not guidelines_confirmed:
            errors.append('You must confirm that you have read the submission guidelines.')

        if not errors:
            AbstractSubmission.objects.create(
                author_name=author_name,
                email=email,
                affiliation=affiliation,
                track=track,
                presentation_type=presentation_type,
                abstract_title=abstract_title,
                document=document,
                guidelines_confirmed=guidelines_confirmed,
            )
            context['abstract_success'] = True
        else:
            context['abstract_errors'] = errors
            context.update({
                'author_name': author_name,
                'email': email,
                'affiliation': affiliation,
                'track': track,
                'presentation_type': presentation_type,
                'abstract_title': abstract_title,
                'guidelines_read': guidelines_confirmed,
            })

    return render(request, 'abstract_submission_one_health_conference.html', context)


def contact(request):
    context = {}
    if request.method == 'POST':
        name = request.POST.get('name', '').strip()
        email = request.POST.get('email', '').strip()
        subject = request.POST.get('subject', '').strip()
        message = request.POST.get('message', '').strip()

        errors = []
        if not name:
            errors.append('Your full name is required.')
        if not email:
            errors.append('A valid email address is required.')
        if not subject:
            errors.append('Please select a subject for your inquiry.')
        if not message:
            errors.append('Please write your message.')

        if not errors:
            ContactMessage.objects.create(
                name=name,
                email=email,
                subject=subject,
                message=message,
            )
            context['contact_success'] = True
        else:
            context['contact_errors'] = errors
            context.update({
                'name': name,
                'email': email,
                'subject': subject,
                'message': message,
            })

    return render(request, 'contact_one_health_conference.html', context)


def registration(request):
    context = {}
    if request.method == 'POST':
        title = request.POST.get('title', '').strip()
        name = request.POST.get('name', '').strip()
        email = request.POST.get('email', '').strip()
        phone_number = request.POST.get('phone_number', '').strip()
        institution = request.POST.get('institution', '').strip()
        category = request.POST.get('category', '').strip()
        track = request.POST.get('track', '').strip()
        dietary_requirements = request.POST.get('dietary_requirements', '').strip()
        payment_reference = request.POST.get('payment_reference', '').strip()
        receipt = request.FILES.get('receipt')
        pref_list = request.POST.getlist('technical_preferences')
        technical_preferences = ", ".join(pref_list)
        pref_plenary = any(p in technical_preferences for p in ['Morning Plenary Presentations', 'Morning plenary sessions'])
        pref_poster = any(p in technical_preferences for p in ['Scientific Poster Session', 'Scientific poster sessions'])
        pref_dinner = any(p in technical_preferences for p in ['Closing Gala Dinner'])

        errors = []
        if not title:
            errors.append('Please select your title.')
        if not name:
            errors.append('Your full name is required.')
        if not email:
            errors.append('A valid email address is required.')
        if not phone_number:
            errors.append('Your phone number is required.')
        if not institution:
            errors.append('Your institution or affiliation is required.')
        if not category:
            errors.append('Please select a registration category.')
        if not track:
            errors.append('Please select a preferred track.')
        if receipt and not receipt.content_type.startswith('image/'):
            errors.append('Receipt upload must be an image file.')

        if not errors:
            try:
                Registration.objects.create(
                    title=title,
                    name=name,
                    email=email,
                    phone_number=phone_number,
                    institution=institution,
                    category=category,
                    track=track,
                    dietary_requirements=dietary_requirements,
                    payment_reference=payment_reference,
                    receipt=receipt,
                    pref_plenary=pref_plenary,
                    pref_poster=pref_poster,
                    pref_dinner=pref_dinner,
                    technical_preferences=technical_preferences,
                )
                context['registration_success'] = True
            except Exception as exc:
                errors.append('Server error while saving registration: %s' % str(exc))
                context['registration_errors'] = errors
                context.update({
                    'title': title,
                    'name': name,
                    'email': email,
                    'phone_number': phone_number,
                    'institution': institution,
                    'category': category,
                    'track': track,
                    'dietary_requirements': dietary_requirements,
                    'payment_reference': payment_reference,
                    'technical_preferences': pref_list,
                })
        else:
            context['registration_errors'] = errors
            context.update({
                'title': title,
                'name': name,
                'email': email,
                'phone_number': phone_number,
                'institution': institution,
                'category': category,
                'track': track,
                'dietary_requirements': dietary_requirements,
                'payment_reference': payment_reference,
                'technical_preferences': pref_list,
            })

    if request.headers.get('Accept', '').find('application/json') != -1:
        if context.get('registration_success'):
            return JsonResponse({'success': True})
        return JsonResponse({'errors': [{'message': message} for message in context.get('registration_errors', ['Unknown error'])]}, status=400)

    return render(request, 'registration_one_health_conference.html', context)


def speakers(request):
    speakers = Speaker.objects.all().order_by('order', 'id')
    return render(request, 'speakers_one_health_conference.html', {'speakers': speakers})


def speaker_detail(request, speaker_id):
    speaker = get_object_or_404(Speaker, id=speaker_id)
    return render(request, 'speaker_detail.html', {'speaker': speaker})


def special_guests(request):
    guests = SpecialGuest.objects.all().order_by('order', 'id')
    return render(request, 'special_guests_one_health_conference.html', {'guests': guests})


def guest_detail(request, guest_id):
    guest = get_object_or_404(SpecialGuest, id=guest_id)
    return render(request, 'guest_detail.html', {'guest': guest})


def partners_sponsors(request):
    return render(request, 'partners_sponsors.html')


def accommodations(request):
    return render(request, 'accommodations_one_health_conference.html')


def program(request):
    return render(request, 'program_one_health_conference.html')


@staff_member_required
def registered_participants(request):
    registrations = Registration.objects.all().order_by('-created_at')
    for reg in registrations:
        if reg.technical_preferences:
            reg.pref_list = [p.strip() for p in reg.technical_preferences.split(',') if p.strip()]
        else:
            reg.pref_list = []
    return render(request, 'registered_participants.html', {'registrations': registrations})
