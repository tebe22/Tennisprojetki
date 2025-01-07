# Tennisprojekti 🎾

Tämä projekti on Pythonilla rakennettu sovellus, joka tarkistaa vapaat tennisvuorot paikalliselta varausjärjestelmältä, näyttää ne selkeässä web-käyttöliittymässä ja lähettää sähköposti-ilmoituksia uusista vapaista vuoroista. Sovellusta ajetaan **Raspberry Pi 5**:llä, ja se on etäohjattavissa **WireGuard VPN**:n avulla.

---

## 🌟 Miksi tein tämän projektin?

Paikallisella hallilla tennis on erittäin suosittu harrastus, ja vapaita vuoroja on usein vaikea saada. Huomasin, että vuorojen jatkuva tarkistaminen varausjärjestelmästä oli aikaa vievää ja turhauttavaa. Tästä syntyi idea automatisoida tämä prosessi.

Halusin rakentaa järjestelmän, joka tarkistaa vapaat vuorot puolestani ja ilmoittaa niistä heti sähköpostitse. Samalla päätin hyödyntää projektissa Raspberry Pi:tä palvelimen alustana ja toteuttaa turvallisen etäohjausmahdollisuuden WireGuard VPN:n avulla.

Tämän projektin avulla pystyin yhdistämään kiinnostukseni tennikseen ja ohjelmointiin, ja samalla opin hyödyllisiä teknologioita, kuten Flaskia, BeautifulSoupia ja VPN-konfiguraatiota.

---

## 📸 Kuvakaappaus
![Käyttöliittymäkuvaus](![image](https://github.com/user-attachments/assets/174c9d9b-f858-4e4d-b634-c22dbf456d81)
)

> Sovellus tarjoaa selkeän web-käyttöliittymän vapaita vuoroja varten. Käyttöliittymän kautta voit myös käynnistää ja sammuttaa taustalla toimivan automaattisen tarkistusskriptin.

---

## ✨ Ominaisuudet
- Tarkistaa vapaat tennisvuorot automaattisesti 30 sekunnin välein.
- Näyttää varaustiedot selkeässä web-käyttöliittymässä.
- Lähettää sähköposti-ilmoituksia uusista vapaista vuoroista (SendGrid API).
- Sovellus toimii **Raspberry Pi 5** -laitteella, mikä mahdollistaa energiatehokkaan jatkuvan käytön.
- **WireGuard VPN** -ratkaisun ansiosta sovellusta voi ohjata etänä turvallisesti.

---

## 🛠️ Käytetyt teknologiat ja laitteet

### Ohjelmistot
- **Python 3**: Sovelluksen backend-koodaus.
- **Flask**: Web-käyttöliittymän toteutus.
- **BeautifulSoup**: HTML-tiedon jäsentämiseen varausjärjestelmästä.
- **SendGrid API**: Sähköpostien lähettämiseen.
- **WireGuard**: VPN-etäyhteys sovelluksen turvalliseen ohjaamiseen.

### Laitteet
- **Raspberry Pi 5**: Sovelluksen käyttöjärjestelmänä (Raspbian OS).
- Raspberry Pi toimii Flask-palvelimen ja automatisoidun taustaprosessin alustana.

---

## 🖥️ Asennusohjeet Raspberry Pi:lle

1. **Asenna tarvittavat ohjelmistot Raspberry Pi:llä:**
   Päivitä järjestelmä ja asenna Python:
   ```bash
   sudo apt update && sudo apt upgrade -y
   sudo apt install python3 python3-pip python3-venv
