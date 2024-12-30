import random
from django.core.mail import send_mail

def generate_otp():
    """Generate a 6-digit OTP."""
    return random.randint(100000, 999999)

def send_otp_email(email, otp):
    """Send OTP via email."""
    subject = 'Your OTP for Account Verification'
    message = f'Your OTP is {otp}. It will expire in 10 minutes.'
    send_mail(subject, message, 'santoshshrestha002@gmail.com', [email])

def send_otp_sms(phone_number, otp):
    """Send OTP via SMS (use an SMS gateway service)."""
    # Integrate with an SMS provider like Twilio or others
    print(f'Sending OTP {otp} to phone number {phone_number}')
