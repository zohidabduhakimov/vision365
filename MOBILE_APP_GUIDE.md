# 📱 Vision 365 — Android va iOS Mobil Ilova Qo'llanmasi

Ushbu loyiha zamonaviy **Progressive Web App (PWA)** va **Capacitor Cross-Platform Runtime** texnologiyalari bilan to'liq jihozlangan bo'lib, uni **Android (APK)** va **iOS (iPhone/iPad)** qurilmalarida haqiqiy mobil ilova sifatida ishlatishning 3 ta oson yo'li mavjud.

---

## 1-USUL: Telefoningizga Darhol O'rnatish (PWA — Tavsiya etiladi ⚡)

Hech qanday qo'shimcha dastur (Android Studio yoki Xcode) o'rnatmasdan, to'g'ridan-to'g'ri telefoningizga o'rnatib olishingiz mumkin.

### 🌐 1-qadam: Saytni Wi-Fi orqali telefonda ochish
1. Kompyuteringizda terminalni ochib, loyiha papkasida quyidagi buyruqni bering:
   ```bash
   python serve_mobile.py
   ```
2. Terminalda sizning mahalliy Wi-Fi manzilingiz chiqadi (masalan: `http://192.168.68.86:8080`).
3. Telefoningizni shu kompyuter ulangan Wi-Fi tarmog'iga ulang va telefon brauzerida ushbu manzilni oching.

### 🍏 iOS (iPhone & iPad) ga o'rnatish:
1. Manzilni **Safari** brauzerida oching.
2. Ekranning pastki qismidagi **"Ulashish" (Share / kvadratdan yuqoriga o'q chiqqan belgi)** tugmasini bosing.
3. Chiqqan menyudan pastroqqa tushib, **"Asosiy ekranga qo'shish" (Add to Home Screen)** bandini tanlang.
4. Yuqori o'ng burchakdagi **"Qo'shish" (Add)** tugmasini bosing.
5. **Natija:** Telefoningiz ekranida **Vision 365** ilovasi paydo bo'ladi. U xuddi App Store'dan yuklab olinganidek brauzer qatorlarisiz, to'liq ekranda va offlayn rejimda ishlaydi!

### 🤖 Android (Samsung, Xiaomi, Pixel va b.) ga o'rnatish:
1. Manzilni **Google Chrome** brauzerida oching.
2. Sahifaning yuqorisidagi **"Telefonga O'rnatish"** tugmasini bosing yoki Chrome'ning yuqori o'ng burchagidagi **uch nuqta (⋮)** tugmasini bosing.
3. Menyudan **"Ilovani o'rnatish" (Install App)** yoki **"Bosh ekranga qo'shish"** bandini bosing.
4. **Natija:** Telefoningizga mustaqil ilova sifatida o'rnatiladi va ilovalar ro'yxatiga qo'shiladi!

---

## 2-USUL: GitHub Actions Orqali Tayyor `.apk` Faylni Yuklab Olish (Avtomatik ☁️)

Loyiha ichiga maxsus `.github/workflows/build-mobile.yml` skripti kiritilgan.

1. Ushbu loyihani o'zingizning **GitHub** profilingizga repository qilib yuklang (push qiling).
2. GitHub sahifangizdagi **"Actions"** bo'limiga o'ting.
3. GitHub o'zining serverlarida Android SDK va Gradle orqali ilovani avtomatik kompilyatsiya qiladi.
4. Ish yakunlangach, **"Artifacts"** bo'limidan tayyor **`Vision365-Android-Debug-APK` (`app-debug.apk`)** faylini bevosita yuklab olib, Android telefoningizga o'rnatishingiz mumkin!

---

## 3-USUL: Capacitor Orqali Native Android Studio va Xcode Loyihasini Yaratish (Dasturchilar Uchun 💻)

Agar sizda Node.js o'rnatilgan bo'lsa:

### Android Studio uchun:
```bash
# 1. Bog'liqliklarni o'rnatish
npm install

# 2. Android platformasini yaratish
npx cap add android

# 3. Android Studio'da ochish va APK qurish
npx cap open android
```
Android Studio ochilgach: `Build -> Build Bundle(s) / APK(s) -> Build APK(s)` tugmasini bosib, `.apk` fayl olasiz.

### iOS (Xcode / macOS) uchun:
```bash
# 1. iOS platformasini yaratish
npx cap add ios

# 2. Xcode dasturida ochish
npx cap open ios
```
Xcode ochilgach, uni iPhone simulyatorida yoki haqiqiy ulangan iPhone qurilmangizda ishga tushirishingiz mumkin.

---

## ⚙️ Loyihaga Kiritilgan Mobil Xususiyatlar:
- ✅ **Offline Caching:** `sw.js` (Service Worker) tufayli internet yo'q bo'lsa ham ochiladi.
- ✅ **Telegram Sinxronizatsiya:** Internet bo'lganda yangi maqsadlar va arizalar botga boradi.
- ✅ **Touch & Safe-Area Moslashuvi:** iPhone "o'yig'i" (notch) va Dynamic Island'ga moslashtirilgan.
- ✅ **Mobil Pastki Menyu (Bottom Navigation Bar):** Bir qo'l bilan boshqarish uchun qulay pastki menyu.
- ✅ **Yuqori Sifatli Ikonkalar:** 192x192, 512x512 va Apple Touch Icon standartlari ta'minlangan.
