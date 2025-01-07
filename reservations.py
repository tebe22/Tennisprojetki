'import requests
from bs4 import BeautifulSoup
from datetime import datetime

SLOTS_URL = "https://varaus.hukka.net/index.php?func=mod_rc_v2"

def check_free_slots():
    """
    Hakee vapaat tennisvuorot annettuun URL-osoitteeseen.
    Palauttaa: 
        dict: Aikaväli ja kentän tila ("Vapaa" tai "Varattu").
    """
    try:
        response = requests.get(SLOTS_URL, timeout=10)
        response.raise_for_status()
        return parse_slots_from_response(response)
    except requests.exceptions.RequestException as e:
        print(f"Virhe haettaessa varaustietoja: {e}")
        return {}

def parse_slots_from_response(response):
    """
    Jäsentää varaustiedot palvelimen vastauksesta.
    Palauttaa:
        dict: Aikaväli ja kenttien tilat.
    """
    soup = BeautifulSoup(response.text, "html.parser")
    rows = soup.find_all("tr")
    free_slots = {}
    current_time = datetime.now()
    is_today = "cdate" not in SLOTS_URL or current_time.strftime("%d.%m.%Y") in SLOTS_URL

    for row in rows:
        time_slot = row.find("th", class_="datarow")
        if time_slot:
            time_slot_text = time_slot.text.strip()
            start_time_str = time_slot_text.split("-")[0].strip()
            start_time = datetime.strptime(start_time_str, "%H:%M").replace(
                year=current_time.year, month=current_time.month, day=current_time.day
            )

            if is_today and (start_time < current_time or 
                            (current_time.hour + 1 == start_time.hour and current_time.minute >= 30)):
                continue

            td_elements = row.find_all("td")
            for index, td in enumerate(td_elements, start=1):
                court_name = f"Tennis {index}"
                td_classes = td.get("class", [])
                status = "Vapaa" if "res_success" in td_classes else "Varattu"
                free_slots.setdefault(time_slot_text, {})[court_name] = status
    return free_slots
