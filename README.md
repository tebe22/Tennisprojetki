# Tennisprojekti 🎾

Tämä projekti on Pythonilla rakennettu sovellus, joka tarkistaa vapaat tennisvuorot paikalliselta varausjärjestelmältä, näyttää ne selkeässä web-käyttöliittymässä ja lähettää sähköposti-ilmoituksia uusista vapaista vuoroista. Sovellusta ajetaan **Raspberry Pi 5**:llä, ja se on etäohjattavissa **WireGuard VPN**:n avulla.

---

## 🌟 Miksi tein tämän projektin?

Paikallisella hallilla tennis on erittäin suosittu harrastus, ja vapaita vuoroja on usein vaikea saada. Huomasin, että vuorojen jatkuva tarkistaminen varausjärjestelmästä oli aikaa vievää ja turhauttavaa. Tästä syntyi idea automatisoida tämä prosessi.

rakensin järjestelmän, joka tarkistaa vapaat vuorot puolestani ja ilmoittaa niistä heti sähköpostitse. Samalla päätin hyödyntää projektissa Raspberry Pi:tä palvelimen alustana ja toteuttaa turvallisen etäohjausmahdollisuuden WireGuard VPN:n avulla.

---

## 📸 Käyttöliittymä
![image](https://github.com/user-attachments/assets/9667c2ee-71ed-4037-88aa-7d0ec6928d8b)




> Sovellus tarjoaa selkeän web-käyttöliittymän vapaita vuoroja varten. Käyttöliittymän kautta voit myös käynnistää ja sammuttaa taustalla toimivan automaattisen tarkistusskriptin.

---

## ✨ Ominaisuudet
- Tarkistaa vapaat tennisvuorot automaattisesti 30 sekunnin välein.
- Näyttää varaustiedot selkeässä web-käyttöliittymässä.
- Lähettää sähköposti-ilmoituksia uusista vapaista vuoroista (SendGrid API).
- Sovellus toimii **Raspberry Pi 5** Laitteella.
- **WireGuard VPN** avulla sovellusta voi ohjata turvallisesti etänä.

---

## 🛠️ Käytetyt teknologiat ja laitteet

### Ohjelmistot
- **Python 3**: Sovelluksen backend-koodaus.
- **Flask**: Web-käyttöliittymän toteutus.
- **BeautifulSoup**: HTML-tiedon jäsentämiseen varausjärjestelmästä.
- **SendGrid API**: Sähköpostien lähettämiseen.
- **WireGuard**: VPN-etäyhteys sovelluksen ohjaamiseen.

### Laitteet
- **Raspberry Pi 5**: Sovelluksen käyttöjärjestelmänä (Raspbian OS).
- Raspberry Pi toimii Flask-palvelimen ja automatisoidun taustaprosessin alustana.

---

