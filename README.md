# 📦 UnaRetail – Ghid de Build și Instalare

Acest proiect conține două aplicații separate: UnaRetail pentru Android și UnaRetail pentru Windows (Desktop). Acest ghid explică pas cu pas ce trebuie să instalezi, cum să configurezi mediul și cum să compilezi aplicația corect.

---

## 📁 Conținut folder

- Ghid_Build_Android.docx – pașii detaliați pentru Android
- Ghid_Build_Desktop.docx – pașii detaliați pentru Desktop (Windows)
- myapp-release-key.jks – cheia pentru semnarea aplicației Android
- server.py – fișier Python pentru instalare locală pe Android


---

## ✅ Cerințe generale

Asigură-te că ai instalate:

| Componentă                | Versiune recomandată         |
|---------------------------|------------------------------|
| Qt                       | 5.15.2                       |
| Visual Studio            | 2019 (cu MSVC 32-bit)        |
| Windows SDK              | 10                           |
| JDK                      | 8 (pentru Android build)     |
| Android SDK              | platform-tools, build-tools 31.0.0, android-31 |
| Python                   | 3.x (pentru server.py)       |

---

## 📱 Compilare și instalare aplicație Android

📄 Detalii complete în: Ghid_Build_Android.docx

1. Deschide proiectul în Qt Creator.
2. Selectează kit-ul Android.
3. Asigură-te că build-ul este pe Release.
4. Selectează ABI: armeabi-v7a.
5. Rulează build-ul.

📦 După build:

1. Mergi în folderul:
   D:\…\android-build\build\outputs\apk\release
2. Semnează APK-ul folosind:
   ```bash
   apksigner.bat sign --ks myapp-release-key.jks --ks-key-alias mia-key --ks-pass pass:unamia --key-pass pass:unamia --out UnaRetail_1.33.apk android-build-release-unsigned.apk
3. Rulează server.py:
   python server.py
4. Deschide browserul de pe telefon și accesează IP-ul afișat în terminal (ex: http://192.168.x.x:8000).

5. Apasă pe fișierul apk pentru a instala aplicația.

## 💻 Compilare aplicație Desktop (Windows)

📄 Detalii complete în: Ghid_Build_Desktop.docx

1. Deschide proiectul în Qt Creator.

2. Selectează kitul Desktop (MSVC + Windows).

3. Asigură-te că build-ul este pe Release.

4. Rulează build-ul.

5. Executabilul final se va afla în:
   D:\…\build…\release\UnaRetail.exe


## 🔗 Linkuri utile pentru instalare

1) Visual Studio 2019 Installer: https://visualstudio.microsoft.com/vs/older-downloads/

2) JDK 8: https://adoptium.net/en-GB/temurin/releases/

4) Python 3: https://www.python.org/downloads/


