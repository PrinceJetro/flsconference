from django.shortcuts import render
from django.http import JsonResponse
from .models import Registration, ContactMessage, AbstractSubmission


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
        institution = request.POST.get('institution', '').strip()
        category = request.POST.get('category', '').strip()
        track = request.POST.get('track', '').strip()
        dietary_requirements = request.POST.get('dietary_requirements', '').strip()
        payment_reference = request.POST.get('payment_reference', '').strip()
        receipt = request.FILES.get('receipt')
        pref_plenary = request.POST.get('pref_plenary') is not None
        pref_poster = request.POST.get('pref_poster') is not None
        pref_dinner = request.POST.get('pref_dinner') is not None

        errors = []
        if not title:
            errors.append('Please select your title.')
        if not name:
            errors.append('Your full name is required.')
        if not email:
            errors.append('A valid email address is required.')
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
                    institution=institution,
                    category=category,
                    track=track,
                    dietary_requirements=dietary_requirements,
                    payment_reference=payment_reference,
                    receipt=receipt,
                    pref_plenary=pref_plenary,
                    pref_poster=pref_poster,
                    pref_dinner=pref_dinner,
                )
                context['registration_success'] = True
            except Exception as exc:
                errors.append('Server error while saving registration: %s' % str(exc))
                context['registration_errors'] = errors
                context.update({
                    'title': title,
                    'name': name,
                    'email': email,
                    'institution': institution,
                    'category': category,
                    'track': track,
                    'dietary_requirements': dietary_requirements,
                    'payment_reference': payment_reference,
                    'pref_plenary': pref_plenary,
                    'pref_poster': pref_poster,
                    'pref_dinner': pref_dinner,
                })
        else:
            context['registration_errors'] = errors
            context.update({
                'title': title,
                'name': name,
                'email': email,
                'institution': institution,
                'category': category,
                'track': track,
                'dietary_requirements': dietary_requirements,
                'payment_reference': payment_reference,
                'pref_plenary': pref_plenary,
                'pref_poster': pref_poster,
                'pref_dinner': pref_dinner,
            })

    if request.headers.get('Accept', '').find('application/json') != -1:
        if context.get('registration_success'):
            return JsonResponse({'success': True})
        return JsonResponse({'errors': [{'message': message} for message in context.get('registration_errors', ['Unknown error'])]}, status=400)

    return render(request, 'registration_one_health_conference.html', context)


def speakers(request):
    return render(request, 'speakers_one_health_conference.html')


def special_guests(request):
    return render(request, 'special_guests_one_health_conference.html')


def partners_sponsors(request):
    return render(request, 'partners_sponsors.html')


def program(request):
    return render(request, 'program_one_health_conference.html')
