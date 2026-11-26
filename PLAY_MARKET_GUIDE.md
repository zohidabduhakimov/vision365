# 🚀 Google Play Market'ga Joylash Bo'yicha To'liq Qo'llanma (Play Console Guide)

Ushbu qo'llanma **"Vision 365"** ilovasini **Google Play Market (Google Play Console)** da muvaffaqiyatli nashr qilish uchun barcha qadamlarni o'z ichiga oladi.

---

## 📌 1. Google Play Console Talabi: `.aab` (Android App Bundle)

Google Play 2021-yildan boshlab barcha yangi ilovalar uchun `.apk` o'rniga **`.aab` (Android App Bundle)** formatini majburiy qilib belgilagan. 
Siz uchun loyihada **avtomatik `.aab` va `.apk` yaratuvchi** tizim tayyorlandi!

---

## ⚡ 2. Tayyor `.aab` Faylni Qayerdan Olasiz? (1 Tugma Bilan)

Loyiha ichiga maxsus avtomatik robot — `.github/workflows/build-playstore.yml` o'rnatildi:

1. Ushbu yangi fayllarni GitHub'ga yuklaysiz (`git push`).
2. GitHub'dagi repository sahifangizga kirasiz: **`https://github.com/zohidabduhakimov/vision365`**
3. Yuqoridagi **"Actions"** bo'limiga o'tasiz.
4. U yerda **"Build Google Play Store Bundle (AAB) & APK"** avtomatik ishga tushadi (taxminan 2-3 daqiqa).
5. Jarayon tugagach, **Artifacts** bo'limidan quyidagi 2 ta faylni olasiz:
   - 📦 **`Vision365-PlayStore-Bundle-AAB` (`app-release.aab`)** — Play Console'ga yuklanadigan asosiy fayl!
   - 📱 **`Vision365-Release-APK` (`app-release.apk`)** — Telefoningizda oldindan o'rnatib sinab ko'rish uchun fayl.

---

## 🎨 3. Google Play Console Uchun Tayyor Grafika & Matnlar

Google Play Console'da to'ldirish kerak bo'lgan barcha ma'lumotlar oldindan tayyorlab qo'yildi:

### 1. Ilova Nomi (Title — max 30 belgi):
```
Vision 365: Maqsadlar Tizimi
```

### 2. Qisqa Tavsif (Short description — max 80 belgi):
```
1 yillik shaxsiy va karyera maqsadlarini rejalashtirish va monitoring tizimi.
```

### 3. To'liq Tavsif (Full description):
```
Vision 365 — bu 2026-yilgi shaxsiy rivojlanish, intizom, biznes va hayotiy maqsadlaringizni tizimli boshqarish uchun yaratilgan zamonaviy platforma.

ASOSIY IMKONIYATLAR:
• 365 Kunlik Jonli Hisoblagich: Yilning o'tgan va qolgan vaqtini aniq ko'rsatib turuvchi real vaqt hisoblagichi.
• 12 Oylik Strategik Xronologiya: Har bir oy va chorak (Q1-Q4) bo'yicha aniq KPI va bosqichlar xaritasi.
• 5 Ta Hayot Ustuni: Karyera va Biznes, Moliyaviy Erkinlik, Ta'lim va Ko'nikmalar, Salomatlik va Sport, Oila va Jamiyat.
• Telegram Bot Sinxronizatsiyasi: Yangi maqsad qo'shilganda yoki vazifa bajarilganda shaxsiy Telegram botingizga hisobot boradi.
• 100% Xavfsiz va Offlayn: Internet bo'lmagan holatda ham barcha ma'lumotlaringiz qurilma xotirasida saqlanadi.

Har bir buyuk hayotiy sakrash bugungi kichik, ammo qat'iy qadamdan boshlanadi!
```

### 4. Ikonka va Rasmlar (Tayyor Fayllar):
- 🖼️ **Ilova Ikonkasi (512x512 PNG):** Loyiha ichidagi `icons/icon-512.png` fayli.
- 🎨 **Asosiy Banner (Feature Graphic — 1024x500):** Loyiha ichidagi `feature-graphic.png` fayli.
- 🛡️ **Maxfiylik Siyosati (Privacy Policy URL):** Play Console talab qiladigan havola:  
  `https://vision365.vercel.app/privacy.html` (yoki `privacy.html`)

---

## 📲 4. Google Play Console'da Qadamma-Qadam Yuklash Tartibi:

1. **play.google.com/console** saytiga kiring (Google Developer akkauntingiz bilan).
2. **"Create App" (Ilova yaratish)** tugmasini bosing:
   - App name: `Vision 365`
   - Default language: `Uzbek` (yoki `English`)
   - App or Game: `App`
   - Free or Paid: `Free`
3. Chap menyudagi **"App content"** bo'limida quyidagilarni belgilang:
   - **Privacy Policy:** `https://vision365.vercel.app/privacy.html` havolasini kiriting.
   - **Target audience:** 13+ yosh.
   - **Content rating:** Oddiy so'rovnomani to'ldirasiz (barchasiga "Yo'q" deb javob beriladi, chunki ilovada nojo'ya kontent yo'q).
4. **"Main store listing"** bo'limida:
   - Yuqoridagi tayyor Tavsif, Qisqa tavsifni kiriting.
   - `icons/icon-512.png` va `feature-graphic.png` rasmlarini yuklang.
5. **"Production" (yoki "Internal testing")** bo'limiga o'ting:
   - **"Create new release"** ni bosing.
   - GitHub'dan yuklab olingan **`app-release.aab`** faylini tashlang.
   - **"Next"** va **"Save and publish"** tugmasini bosing!
6. Google mutaxassislari ilovani tekshirib (odatda 2-4 kun ichida), **Google Play Market**ga chiqaradi! 🏆
