dostum bana kayıt sayfası oluştur gender seçme radio button hobiler checkbox olsun

---

### 🤖 Gemini Response (2026-10-20 15:11:29 UTC)

Selam! Expo Snack üzerinde doğrudan çalıştırabileceğin, yeni başlayanlar için son derece anlaşılır ve temiz bir **Kayıt Ol (Registration)** ekranı hazırladım. 

İstediğin gibi cinsiyet seçimi için **Radio Button (Radyo Düğmesi)** mantığını, hobiler için ise **Checkbox (Onay Kutusu)** mantığını ekstra kütüphane kurmadan, tamamen saf React Native bileşenleriyle (`TouchableOpacity` kullanarak) kodladım. Böylece Expo Snack'te hatasız ve hızlıca çalışır.

### Expo Snack İçin Hazır Kod (`App.js`)

Aşağıdaki kodun tamamını kopyalayıp doğrudan Expo Snack'teki `App.js` dosyasının üzerine yapıştırabilirsin:

```jsx
import React, { useState } from 'react';
import { 
  StyleSheet, 
  Text, 
  View, 
  TextInput, 
  TouchableOpacity, 
  SafeAreaView, 
  ScrollView 
} from 'react-native';

export default function App() {
  // State tanımlamaları (Kullanıcının girdilerini tutmak için)
  const [name, setName] = useState('');
  const [email, setEmail] = useState('');
  const [password, setPassword] = useState('');
  
  // Gender (Cnsiyet) için state: 'Erkek', 'Kadin' veya ''
  const [gender, setGender] = useState('');
  
  // Hobbies (Hobiler) için state: birden fazla seçilebilir, bu yüzden nesne (object) kullanıyoruz
  const [hobbies, setHobbies] = useState({
    spor: false,
    muzik: false,
    kitap: false,
  });

  // Hobilerin durumunu tersine çeviren fonksiyon (Checkbox mantığı)
  const toggleHobby = (hobbyKey) => {
    setHobbies({
      ...hobbies,
      [hobbyKey]: !hobbies[hobbyKey],
    });
  };

  const handleRegister = () => {
    alert(`Kayıt Başarılı!\nAd: ${name}\nCinsiyet: ${gender}`);
  };

  return (
    <SafeAreaView style={styles.container}>
      <ScrollView contentContainerStyle={styles.scrollContainer}>
        <Text style={styles.headerTitle}>Yeni Hesap Oluştur</Text>

        {/* Ad Soyad Input */}
        <Text style={styles.label}>Ad Soyad</Text>
        <TextInput 
          style={styles.input}
          placeholder="Adınızı girin"
          value={name}
          onChangeText={setName}
        />

        {/* E-posta Input */}
        <Text style={styles.label}>E-posta</Text>
        <TextInput 
          style={styles.input}
          placeholder="ornek@email.com"
          keyboardType="email-address"
          value={email}
          onChangeText={setEmail}
        />

        {/* Şifre Input */}
        <Text style={styles.label}>Şifre</Text>
        <TextInput 
          style={styles.input}
          placeholder="Şifrenizi girin"
          secureTextEntry={true}
          value={password}
          onChangeText={setPassword}
        />

        {/* CİNSİYET SEÇİMİ (Radio Button Mantığı) */}
        <Text style={styles.label}>Cinsiyet</Text>
        <View style={styles.radioGroup}>
          <TouchableOpacity 
            style={styles.radioOption} 
            onPress={() => setGender('Erkek')}
          >
            <View style={styles.radioOuter}>
              {gender === 'Erkek' && <View style={styles.radioInner} />}
            </View>
            <Text style={styles.radioText}>Erkek</Text>
          </TouchableOpacity>

          <TouchableOpacity 
            style={styles.radioOption} 
            onPress={() => setGender('Kadin')}
          >
            <View style={styles.radioOuter}>
              {gender === 'Kadin' && <View style={styles.radioInner} />}
            </View>
            <Text style={styles.radioText}>Kadın</Text>
          </TouchableOpacity>
        </View>

        {/* HOBİLER SEÇİMİ (Checkbox Mantığı) */}
        <Text style={styles.label}>Hobiler</Text>
        
        <TouchableOpacity style={styles.checkboxContainer} onPress={() => toggleHobby('spor')}>
          <View style={styles.checkbox}>
            {hobbies.spor && <Text style={styles.checkmark}>✓</Text>}
          </View>
          <Text style={styles.checkboxLabel}>Spor Yapmak</Text>
        </TouchableOpacity>

        <TouchableOpacity style={styles.checkboxContainer} onPress={() => toggleHobby('muzik')}>
          <View style={styles.checkbox}>
            {hobbies.muzik && <Text style={styles.checkmark}>✓</Text>}
          </View>
          <Text style={styles.checkboxLabel}>Müzik Dinlemek</Text>
        </TouchableOpacity>

        <TouchableOpacity style={styles.checkboxContainer} onPress={() => toggleHobby('kitap')}>
          <View style={styles.checkbox}>
            {hobbies.kitap && <Text style={styles.checkmark}>✓</Text>}
          </View>
          <Text style={styles.checkboxLabel}>Kitap Okumak</Text>
        </TouchableOpacity>

        {/* Kayıt Ol Butonu */}
        <TouchableOpacity style={styles.button} onPress={handleRegister}>
          <Text style={styles.buttonText}>Kayıt Ol</Text>
        </TouchableOpacity>

      </ScrollView>
    </SafeAreaView>
  );
}

// Stiller
const styles = StyleSheet.create({
  container: {
    flex: 1,
    backgroundColor: '#f5f5f5',
  },
  scrollContainer: {
    padding: 20,
  },
  headerTitle: {
    fontSize: 24,
    fontWeight: 'bold',
    color: '#333',
    marginBottom: 20,
    textAlign: 'center',
  },
  label: {
    fontSize: 14,
    fontWeight: '600',
    color: '#555',
    marginBottom: 5,
    marginTop: 10,
  },
  input: {
    backgroundColor: '#fff',
    borderWidth: 1,
    borderColor: '#ddd',
    borderRadius: 8,
    padding: 12,
    fontSize: 16,
  },
  // Radio Button Stilleri
  radioGroup: {
    flexDirection: 'row',
    marginVertical: 5,
  },
  radioOption: {
    flexDirection: 'row',
    alignItems: 'center',
    marginRight: 20,
  },
  radioOuter: {
    height: 20,
    width: 20,
    borderRadius: 10,
    borderWidth: 2,
    borderColor: '#007AFF',
    alignItems: 'center',
    justifyContent: 'center',
    marginRight: 8,
  },
  radioInner: {
    height: 10,
    width: 10,
    borderRadius: 5,
    backgroundColor: '#007AFF',
  },
  radioText: {
    fontSize: 16,
    color: '#333',
  },
  // Checkbox Stilleri
  checkboxContainer: {
    flexDirection: 'row',
    alignItems: 'center',
    marginVertical: 6,
  },
  checkbox: {
    height: 22,
    width: 22,
    borderRadius: 4,
    borderWidth: 2,
    borderColor: '#007AFF',
    alignItems: 'center',
    justifyContent: 'center',
    marginRight: 10,
    backgroundColor: '#fff',
  },
  checkmark: {
    color: '#007AFF',
    fontWeight: 'bold',
    fontSize: 14,
  },
  checkboxLabel: {
    fontSize: 16,
    color: '#333',
  },
  // Buton Stili
  button: {
    backgroundColor: '#007AFF',
    padding: 15,
    borderRadius: 8,
    alignItems: 'center',
    marginTop: 30,
  },
  buttonText: {
    color: '#fff',
    fontSize: 16,
    fontWeight: 'bold',
  },
});
```

---

### Kod Nasıl Çalışıyor? (Kısa Açıklama)

1. **useState Kullanımı:** 
   - `gender` değişkeni kullanıcının seçtiği cinsiyeti tutar (`'Erkek'` ya da `'Kadın'`).
   - `hobbies` değişkeni ise bir JavaScript nesnesidir ve her hobinin `true` veya `false` durumunu saklar.
2. **Radio Button Mantığı:** 
   - Harici bir kütüphane (`react-native-radio-buttons` vb.) yüklemek yerine `TouchableOpacity` ile dışta büyük bir çember (`radioOuter`), içinde ise seçildiğinde aktifleşen küçük mavi bir daire (`radioInner`) oluşturduk. Kullanıcı tıkladığında `setGender` çalışarak durumu günceller.
3. **Checkbox Mantığı:** 
   - `TouchableOpacity` kullanarak kare bir kutu (`checkbox`) tasarladık. Üzerine tıklandığında `toggleHobby` fonksiyonu çalışır ve ilgili hobinin boolean değerini tersine çevirir (`!` operatörü ile). Eğer değer `true` ise içeriye tik işareti (`✓`) basılır.
4. **ScrollView & SafeAreaView:** 
   - Form alanları telefon ekranından uzun olabileceği için içeriği `ScrollView` içine sardık, böylece kullanıcı sayfayı aşağı kaydırabilir. `SafeAreaView` ise çentiğin (notch) altında düzgün durmasını sağlar.
