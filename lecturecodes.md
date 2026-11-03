radio button checkbox içeren kayıt sayfası yap çok amatör olsun

---

### 🤖 Gemini Response (2026-11-03 07:58:41 UTC)

Merhaba! Giriş seviyesi React Native dersiniz için harici hiçbir pakete ihtiyaç duymadan, tamamen temel bileşenlerle (`View`, `Text`, `TouchableOpacity`, `TextInput`) hazırlanmış amatör seviyede bir kayıt formu kodunu aşağıda bulabilirsin.

Bu kodu doğrudan **Expo Snack** (snack.expo.dev) üzerindeki `App.js` dosyana yapıştırıp çalıştırabilirsin.

```javascript
import React, { useState } from 'react';
import {
  Text,
  View,
  StyleSheet,
  TextInput,
  TouchableOpacity,
  SafeAreaView,
  ScrollView,
} from 'react-native';

export default function App() {
  // Form alanları için durumlar (state)
  const [ad, setAd] = useState('');
  const [eposta, setEposta] = useState('');
  const [sifre, setSifre] = useState('');
  
  // Radio Button için durum (Cinsiyet seçimi - varsayılan Erkek)
  const [cinsiyet, setCinsiyet] = useState('Erkek');
  
  // Checkbox için durum (Sözleşme onayı - varsayılan false)
  const [sozlesmeKabul, setSozlesmeKabul] = useState(false);

  // Kayıt ol butonuna basılınca çalışacak fonksiyon
  const kayitol = () => {
    if (!sozlesmeKabul) {
      alert('Lütfen kullanım şartlarını kabul edin!');
      return;
    }
    alert(`Kayıt Başarılı!\nAd: ${ad}\nE-posta: ${eposta}\nCinsiyet: ${cinsiyet}`);
  };

  return (
    <SafeAreaView style={styles.container}>
      <ScrollView contentContainerStyle={styles.scrollContainer}>
        <Text style={styles.baslik}>Kayıt Formu</Text>

        {/* Metin Girdileri */}
        <Text style={styles.label}>Ad Soyad:</Text>
        <TextInput
          style={styles.input}
          placeholder="Adınızı giriniz"
          value={ad}
          onChangeText={setAd}
        />

        <Text style={styles.label}>E-posta:</Text>
        <TextInput
          style={styles.input}
          placeholder="E-postanızı giriniz"
          value={eposta}
          onChangeText={setEposta}
          keyboardType="email-address"
        />

        <Text style={styles.label}>Şifre:</Text>
        <TextInput
          style={styles.input}
          placeholder="Şifrenizi giriniz"
          value={sifre}
          onChangeText={setSifre}
          secureTextEntry={true}
        />

        {/* RADIO BUTTON (Cinsiyet Seçimi) */}
        <Text style={styles.label}>Cinsiyet:</Text>
        <View style={styles.radioGroup}>
          
          <TouchableOpacity
            style={styles.radioButton}
            onPress={() => setCinsiyet('Erkek')}>
            <View style={styles.radioOuter}>
              {cinsiyet === 'Erkek' && <View style={styles.radioInner} />}
            </View>
            <Text style={styles.radioText}>Erkek</Text>
          </TouchableOpacity>

          <TouchableOpacity
            style={styles.radioButton}
            onPress={() => setCinsiyet('Kadın')}>
            <View style={styles.radioOuter}>
              {cinsiyet === 'Kadın' && <View style={styles.radioInner} />}
            </View>
            <Text style={styles.radioText}>Kadın</Text>
          </TouchableOpacity>

        </View>

        {/* CHECKBOX (Sözleşme Onayı) */}
        <TouchableOpacity
          style={styles.checkboxContainer}
          onPress={() => setSozlesmeKabul(!sozlesmeKabul)}>
          <View style={styles.checkbox}>
            {sozlesmeKabul && <Text style={styles.checkmark}>✓</Text>}
          </View>
          <Text style={styles.checkboxText}>Kullanım şartlarını kabul ediyorum.</Text>
        </TouchableOpacity>

        {/* Kayıt Butonu */}
        <TouchableOpacity style={styles.button} onPress={kayitol}>
          <Text style={styles.buttonText}>Kayıt Ol</Text>
        </TouchableOpacity>

      </ScrollView>
    </SafeAreaView>
  );
}

// Basit ve amatör ödev stilleri
const styles = StyleSheet.create({
  container: {
    flex: 1,
    backgroundColor: '#f5f5f5',
  },
  scrollContainer: {
    padding: 20,
  },
  baslik: {
    fontSize: 22,
    fontWeight: 'bold',
    textAlign: 'center',
    marginBottom: 20,
    marginTop: 10,
  },
  label: {
    fontSize: 14,
    fontWeight: 'bold',
    marginBottom: 5,
    marginTop: 10,
  },
  input: {
    backgroundColor: '#fff',
    borderWidth: 1,
    borderColor: '#ccc',
    padding: 10,
    borderRadius: 5,
  },
  // Radio Button Stilleri
  radioGroup: {
    flexDirection: 'row',
    marginTop: 5,
    marginBottom: 10,
  },
  radioButton: {
    flexDirection: 'row',
    alignItems: 'center',
    marginRight: 20,
  },
  radioOuter: {
    height: 20,
    width: 20,
    borderRadius: 10, // Yuvarlak yapmak için
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
    fontSize: 14,
  },
  // Checkbox Stilleri
  checkboxContainer: {
    flexDirection: 'row',
    alignItems: 'center',
    marginTop: 15,
    marginBottom: 20,
  },
  checkbox: {
    width: 20,
    height: 20,
    borderWidth: 1,
    borderColor: '#ccc',
    backgroundColor: '#fff',
    alignItems: 'center',
    justifyContent: 'center',
    marginRight: 10,
  },
  checkmark: {
    fontSize: 14,
    fontWeight: 'bold',
    color: '#007AFF',
  },
  checkboxText: {
    fontSize: 13,
  },
  // Buton Stili
  button: {
    backgroundColor: '#007AFF',
    padding: 12,
    borderRadius: 5,
    alignItems: 'center',
  },
  buttonText: {
    color: '#fff',
    fontWeight: 'bold',
    fontSize: 16,
  },
});
```

---

### Nasıl Çalışıyor? (Açıklama)

1. **Radio Button Mantığı:**
   * Dışarıda yuvarlak bir çerçeve (`radioOuter`), içinde ise küçük bir yuvarlak daire (`radioInner`) oluşturduk. 
   * `cinsiyet === 'Erkek'` kontrolü ile tıklanan seçeneğe göre içteki mavi daireyi ekranda gösteriyoruz.

2. **Checkbox Mantığı:**
   * Kare şeklinde küçük bir kutu (`checkbox`) çizdik. 
   * `sozlesmeKabul` değişkeni `true` olduğunda kutunun içine metin olarak tik işareti (`✓`) koyuyoruz. Tıklandığında değer `true`/`false` olarak değişiyor.

3. **Görünüm:**
   * Ders ödevlerinde istenen sade ve basit yapıdadır. Harici paket (React Native Paper vb.) kullanılmamış, tamamen temel bileşenlerle yapılmıştır.
