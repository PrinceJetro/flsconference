import requests

api_key = "re_hNcvqpL6_A74EqH8HRz3aDnkJQpNcvw7d"
url = "https://api.resend.com/emails"

headers = {
    "Authorization": f"Bearer {api_key}",
    "Content-Type": "application/json"
}

data = {
    "from": "FLS Conference <noreply@flsconference.org>",
    "to": ["tfagbayi@unilag.edu.ng"],
    "reply_to": "flsconference@unilag.edu.ng",
    "subject": "Registration Confirmation — FLS One Health Conference 2026",
    "html": """
<!DOCTYPE html>
<html>
<head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Registration Confirmation</title>
</head>
<body style="margin: 0; padding: 0; font-family: 'Inter', Arial, sans-serif; background-color: #f8f9fa; color: #191c1d;">
    <div style="max-width: 600px; margin: 0 auto; background-color: #ffffff;">
        <!-- Header -->
        <div style="background-color: #800000; padding: 30px 20px;">
            <table style="width: 100%; border-collapse: collapse;">
                <tr>
                    <td style="width: 80px; padding-right: 20px;">
                        <img src="https://dhaowhbgcuvjibjbptey.supabase.co/storage/v1/object/public/conference/images/unilag%20logo.png" alt="UNILAG Logo" style="width: 70px; height: auto; display: block;">
                    </td>
                    <td style="vertical-align: middle;">
                        <h1 style="margin: 0; color: #FFD700; font-size: 28px; font-weight: 700;">Faculty of Life Sciences</h1>
                        <p style="margin: 10px 0 0 0; color: #ffffff; font-size: 14px; letter-spacing: 2px; text-transform: uppercase;">One Health Conference 2026</p>
                    </td>
                </tr>
            </table>
        </div>

        <!-- Content -->
        <div style="padding: 40px 30px;">
            <!-- Confirmation Badge -->
            <div style="background-color: #1E428C; color: #ffffff; padding: 15px; border-radius: 8px; text-align: center; margin-bottom: 30px;">
                <p style="margin: 0; font-size: 16px; font-weight: 600; letter-spacing: 1px;">✓ REGISTRATION CONFIRMED</p>
            </div>

            <!-- Greeting -->
            <p style="font-size: 16px; line-height: 1.6; margin-bottom: 20px;">
                Dear {title} {name},
            </p>

            <p style="font-size: 16px; line-height: 1.6; margin-bottom: 20px;">
                We are pleased to confirm your registration for the <strong>First Annual FLS One Health Conference 2026</strong>. Your participation will contribute to advancing integrated research in human pathology, veterinary surveillance, and environmental health.
            </p>

            <!-- Event Details -->
            <div style="background-color: #E9ECEF; padding: 20px; margin: 30px 0; border-radius: 8px;">
                <h3 style="margin: 0 0 15px 0; color: #800000; font-size: 18px;">Conference Details</h3>
                <table style="width: 100%; border-collapse: collapse;">
                    <tr>
                        <td style="padding: 8px 0; color: #570000; font-weight: 600; width: 120px;">Date:</td>
                        <td style="padding: 8px 0;">August 4–6, 2026</td>
                    </tr>
                    <tr>
                        <td style="padding: 8px 0; color: #570000; font-weight: 600;">Venue:</td>
                        <td style="padding: 8px 0;">University of Lagos, Lagos State</td>
                    </tr>
                    <tr>
                        <td style="padding: 8px 0; color: #570000; font-weight: 600;">Theme:</td>
                        <td style="padding: 8px 0;">One Health: Preparing the Next Generation for a Changing World</td>
                    </tr>
                </table>
            </div>


            <p style="font-size: 16px; line-height: 1.6; margin-bottom: 20px; color: #800000; font-weight: 600;">
                Please read the important information below carefully:
            </p>

            <!-- Important Information -->
            <div style="background-color: #f8f9fa; border-left: 4px solid #FFD700; padding: 20px; margin: 30px 0; border-radius: 0 8px 8px 0;">
                <ul style="margin: 0; padding-left: 20px; line-height: 1.8; font-size: 15px;">
                    <li style="margin-bottom: 15px;">Only registered participants will be entitled to the conference packages and certificate.</li>
                    <li style="margin-bottom: 15px;">For authors with multiple accepted abstracts, each accepted abstract requires a registration for a chance to be featured and presented at the conference. Non-presenting co-authors can also attend the conference for FREE, however they can only be entitled to the conference packages and certificate, if they register and pay the stipulated fees as appropriate. Conference registration is online via <a href="https://www.flsconference.org/registration/" style="color: #1E428C;">https://www.flsconference.org/registration/</a>.</li>
                    <li style="margin-bottom: 15px;">All registered conference participants are expected and encouraged to commit to the full duration of the conference. Kindly take this week to check your schedule and plan accordingly to be fully committed. Every Conference attendee is expected to arrive early enough to attend the Opening Keynote address and ceremony on August 4th, 2026 by 10 am.</li>
                    <li style="margin-bottom: 15px;">A list of hotels in and near the University has been provided on the conference website <a href="https://www.flsconference.org/accommodations/" style="color: #1E428C;">https://www.flsconference.org/accommodations/</a>. Participants should try to sort out their accommodation before the conference as traffic in Lagos is legendary. We will like for every attendee to get the most of the conference by attending punctually to every session.</li>
                    <li style="margin-bottom: 15px;">Participants are encouraged to register and make all necessary payments if they have not done so. This will help us cater adequately to your needs. On-site registration could also be done at the registration desk upon arrival at no extra cost of late registration, but is highly discouraged.</li>
                    <li style="margin-bottom: 15px;">For presenting authors that might require help with poster printing, we have liaised and bargained with one of our printers to help with the printing of sticker posters at a token of #3000 (to be paid directly to him). He is Mr. Nurudeen and can be reached via call and WhatsApp chat on +234 805 604 9389. Finished posters should be sent to him in PDF format.</li>
                    <li style="margin-bottom: 15px;">The University of Lagos is in Akoka, Yaba, Mainland part of Lagos. You can use Google Maps for directions to the University of Lagos and the conference venue (J.F. Ade. Ajayi Auditorium (Main Auditorium). Please refer to our website to know more about our campus.</li>
                    <li style="margin-bottom: 15px;">We respectfully ask you to wear comfortable and smart clothing throughout the conference and prepare to network during periodic breaks. The weather forecast during the period of the conference, will be mostly cloudy with a high probability of intermittent, patchy rain or scattered thunderstorms throughout the days (typically mid-August wet season conditions). Temperatures will be between 28°C to 29°C during the day and 24°C to 25°C lows. As such, it is recommended that participants bring one form of rain attire and an umbrella in case it rains. We hope you will enjoy the natural beauty and activities on our waterfront campus.</li>
                    <li style="margin-bottom: 15px;">Should you need to buy some medications during the conference period, there is a UNILAG pharmacy on campus (besides the Campus Bus shuttle Park at CITS) and Yem Yem pharmacy. The Pharmacies open Mon-Sat: 7:00 am to 9:00 pm. For any Medical Emergency, locate the University's medical centre.</li>
                </ul>
            </div>

      <!-- What to Expect -->
        <h3 style="margin: 30px 0 15px 0; color: #800000; font-size: 18px;">What to Expect</h3>
        <ul style="margin: 0; padding-left: 20px; line-height: 1.8;">
          <li style="margin-bottom: 10px;">
            Keynote address by Prof. Emmanuel Akinola Abayomi, Lagos State Commissioner for Health
          </li>
          <li style="margin-bottom: 10px;">12 scientific sessions across 8 sub-themes</li>
          <li style="margin-bottom: 10px;">Networking with 40+ presenters and 200+ attendees</li>
          <li style="margin-bottom: 10px;">Abstract presentations and research discussions</li>
        </ul>



            <!-- Closing -->
            <p style="font-size: 16px; line-height: 1.6; margin-bottom: 20px;">
                We look forward to meeting you and closely interacting with you during the conference. We hope this will be a key period in your career development.
            </p>

            <!-- Contact -->
            <p style="font-size: 14px; line-height: 1.6; color: #666; margin-top: 30px;">
                If you have any questions, please contact us at <a href="mailto:flsconference@unilag.edu.ng" style="color: #1E428C;">flsconference@unilag.edu.ng</a>
            </p>
        </div>

        <!-- Footer -->
        <div style="background-color: #E9ECEF; padding: 30px; text-align: center; border-top: 3px solid #FFD700;">
            <p style="margin: 0 0 10px 0; color: #800000; font-weight: 600; font-size: 14px;">Faculty of Life Sciences</p>
            <p style="margin: 0; color: #666; font-size: 12px;">University of Lagos, Akoka, Lagos State, Nigeria</p>
            <p style="margin: 15px 0 0 0; color: #999; font-size: 11px;">© 2026 Faculty of Life Sciences, UNILAG. All rights reserved.</p>
        </div>
    </div>
</body>
</html>
    """,
}

try:
    response = requests.post(url, json=data, headers=headers)
    print(f"Status Code: {response.status_code}")
    print(f"Response: {response.text}")
    if response.status_code == 200:
        print("Email sent successfully!")
except Exception as e:
    print(f"Error sending email: {e}")
