# 📱 Mobile-AppDevelopment (Gemini Destekli Otomatik Asistan)

Bu repo, her commit attığınızda (veya `prompt.md` dosyasını güncelleyip pushladığınızda) otomatik olarak **Google Gemini AI** modeline bağlanan, kod değişikliklerinizi ve commit mesajınızı analiz edip cevabı **`response.md`** dosyasına otomatik commit atan bir **GitHub Actions** botu içerir.

---

## 🚀 Nasıl Çalışır?

1. **Commit & Push:** Repoda herhangi bir dosyayı değiştirip commit attığınızda veya `prompt.md` içine bir soru/talimat yazıp pushladığınızda:
2. **GitHub Actions Tetiklenir:** `.github/workflows/gemini-bot.yml` iş akışı başlar.
3. **Gemini Analiz Eder:** Commit mesajınız, git diff (değişiklikler) ve `prompt.md` içeriği Gemini'ye gönderilir.
4. **Otomatik Geri Commit:** Gemini'nin ürettiği detaylı yanıt `response.md` dosyasına yazılır ve `[skip ci]` etiketiyle repoya geri commit edilir (böylece sonsuz döngü engellenir). Ayrıca tüm geçmiş `chat_history.md` dosyasında saklanır.

---

## ⚙️ Kurulum ve GitHub'a Yükleme Adımları

### 1. GitHub'da Yeni Repo Oluşturma
1. [github.com/new](https://github.com/new) adresine gidin.
2. Repo adı olarak **`Mobile-AppDevelopment`** yazın.
3. İster **Public** ister **Private** seçin ve **Create repository** butonuna tıklayın.

### 2. Dosyaları GitHub Reposuna Yükleme
Bu klasördeki dosyaları doğrudan GitHub web arayüzünden ("uploading an existing file") veya terminalden Git ile yükleyebilirsiniz:
```bash
git init
git branch -M main
git remote add origin https://github.com/KULLANICI_ADINIZ/Mobile-AppDevelopment.git
git add .
git commit -m "feat: ilk kurulum ve Gemini commit botu"
git push -u origin main
```

### 3. Gemini API Anahtarını Tanımlama (Zorunlu)
Gemini'nin çalışabilmesi için ücretsiz bir API anahtarına ihtiyacı vardır:
1. [Google AI Studio](https://aistudio.google.com/app/apikey) adresinden ücretsiz bir API anahtarı alın.
2. GitHub'da oluşturduğunuz repo sayfasına gidin.
3. **Settings** (Ayarlar) > **Secrets and variables** > **Actions** bölümünü açın.
4. **New repository secret** butonuna tıklayın:
   - **Name:** `GEMINI_API_KEY`
   - **Secret:** Aldığınız Gemini API anahtarı
5. **Add secret** diyerek kaydedin.

### 4. GitHub Actions Yazma İznini Açma (Önemli)
Botun cevabı repoya geri commit atabilmesi için Actions yazma iznine sahip olmalıdır:
1. GitHub reponuzda **Settings** > **Actions** > **General** sekmesine gidin.
2. Sayfanın en altındaki **Workflow permissions** başlığına inin.
3. **"Read and write permissions"** seçeneğini işaretleyip **Save** butonuna tıklayın.

---

## 📁 Proje Dosya Yapısı

- [`.github/workflows/gemini-bot.yml`](.github/workflows/gemini-bot.yml): Her commit'te çalışan GitHub Actions iş akışı.
- [`.github/scripts/gemini_bot.py`](.github/scripts/gemini_bot.py): Gemini API ile iletişim kuran ve yanıtı formatlayan Python betiği.
- [`prompt.md`](prompt.md): Gemini'ye iletmek istediğiniz soru veya mobil uygulama hedeflerinizi yazabileceğiniz ana dosya.
- [`response.md`](response.md): Gemini'nin ürettiği en son yanıtın yazıldığı dosya.
- [`chat_history.md`](chat_history.md): Önceki tüm commit yanıtlarının arşivlendiği geçmiş dosyası.
