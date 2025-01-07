import os
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail

# Lue ympäristömuuttujat
EMAIL_FROM = os.getenv("EMAIL_FROM")
EMAIL_TO = os.getenv("EMAIL_TO")

sent_notifications = {}

def send_email_notification(free_slots):
    """
    Lähettää sähköpostin uusista vapaista tennisvuoroista.

    Args:
        free_slots (dict): Vapaat vuorot ja niiden tiedot.
    """
    global sent_notifications
    body_content = "Uusia vapaita tennisvuoroja saatavilla:\n\n"
    email_needed = False

    for time_slot, courts in free_slots.items():
        if time_slot not in sent_notifications:
            sent_notifications[time_slot] = set()

        for court, status in courts.items():
            if status == "Vapaa" and court not in sent_notifications[time_slot]:
                body_content += f"Aika: {time_slot}, Kenttä: {court}\n"
                sent_notifications[time_slot].add(court)
                email_needed = True

    if not email_needed:
        print("Ei uusia vapaita vuoroja, sähköpostia ei lähetetä.")
        return

    message = Mail(
        from_email=EMAIL_FROM,
        to_emails=EMAIL_TO,
        subject="Uusia vapaita tennisvuoroja saatavilla!",
        html_content=f"<pre>{body_content}</pre>"
    )

    try:
        sg = SendGridAPIClient(os.getenv("SENDGRID_API_KEY"))
        response = sg.send(message)
        print(f"Sähköpostin lähetys onnistui. Statuskoodi: {response.status_code}")
    except Exception as e:
        print(f"Sähköpostin lähettäminen epäonnistui: {e}")

