kayıt ekranı oluştur mail için input box gender için radio button hobiler için checkbox

---

### 🤖 Gemini Response (2026-10-21 06:32:07 UTC)

Harika! Giriş seviyesi bir Mobil Programlama dersi için tam öğrenci ödevine uygun, sade ve anlaşılır bir kayıt ekranı hazırladım. 

Mevcut bir kod bloğu sağlamadığın için, sıfırdan Expo Snack'e direkt yapıştırabileceğin, temel React Native bileşenlerini (`TextInput`, `TouchableOpacity` ile simüle edilmiş Radio Button ve Checkbox) içeren basit bir yapı kurdum. Tasarımı bilerek çok sade tuttum (klasik gri kenarlıklar ve düz renkler), böylece bir öğrenci ödevine tamamen benziyor.

Aşağıdaki kodu doğrudan kopyalayıp [snack.expo.dev](https://snack.expo.dev) adresindeki `App.js` dosyasının içine yapıştırabilirsin:

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
  // State tanımlamaları (Form verilerini tutmak için)
  const [email, setEmail] = useState('');
  const [gender, setGender] = useState(''); // 'Kadın' veya 'Erkek'
  const [hobbies, setHobbies] = useState({
    spor: false,
    kitap: false,
    muzik: false,
  });

  // Checkbox (Hobi) durumunu değiştiren fonksiyon
  const toggleHobby = (hobbyKey) => {
    setHobbies({
      ...hobbies,
      [hobbyKey]: !hobbies[hobbyKey]
    });
  };

  const handleRegister = () => {
    alert(`Kayıt Başarılı!\nEmail: ${email}\nCinsiyet: ${gender}`);
  };

  return (
    <SafeAreaView style={styles.container}>
      <ScrollView contentContainerStyle={styles.scrollContainer}>
        
        <Text style={styles.headerTitle}>Öğrenci Kayıt Ekranı</Text>

        {/* --- MAIL İÇİN INPUT BOX --- */}
        <View style={styles.inputGroup}>
          <Text style={styles.label}>E-posta Adresi:</Text>
          <TextInput
            style={styles.input}
            placeholder="ornek@mail.com"
            value={email}
            onChangeText={setEmail}
            keyboardType="email-address"
          />
        </View>

        {/* --- GENDER İÇİN RADIO BUTTON --- */}
        <View style={styles.inputGroup}>
          <Text style={styles.label}>Cinsiyet:</Text>
          <View style={styles.radioContainer}>
            <TouchableOpacity 
              style={styles.radioButtonRow} 
              onPress={() => setGender('Kadın')}
            >
              <View style={styles.radioCircle}>
                {gender === 'Kadın' && <View style={styles.selectedRadioCircle} />}
              </View>
              <Text style={styles.radioText}>Kadın</Text>
            </TouchableOpacity>

            <TouchableOpacity 
              style={styles.radioButtonRow} 
              onPress={() => setGender('Erkek')}
            >
              <View style={styles.radioCircle}>
                {gender === 'Erkek' && <View style={styles.selectedRadioCircle} />}
              </View>
              <Text style={styles.radioText}>Erkek</Text>
            </TouchableOpacity>
          </View>
        </View>

        {/* --- HOBİLER İÇİN CHECKBOX --- */}
        <View style={styles.inputGroup}>
          <Text style={styles.label}>Hobiler:</Text>
          
          <TouchableOpacity 
            style={styles.checkboxRow} 
            onPress={() => toggleHobby('spor')}
          >
            <View style={styles.checkbox}>
              {hobbies.spor && <Text style={styles.checkmark}>X</Text>}
            </View>
            <Text style={styles.checkboxText}>Spor</Text>
          </TouchableOpacity>

          <TouchableOpacity 
            style={styles.checkboxRow} 
            onPress={() => toggleHobby('kitap')}
          >
            <View style={styles.checkbox}>
              {hobbies.kitap && <Text style={styles.checkmark}>X</Text>}
            </View>
            <Text style={styles.checkboxText}>Kitap Okumak</Text>
          </TouchableOpacity>

          <TouchableOpacity 
            style={styles.checkboxRow} 
            onPress={() => toggleHobby('muzik')}
          >
            <View style={styles.checkbox}>
              {hobbies.muzik && <Text style={styles.checkmark}>X</Text>}
            </View>
            <Text style={styles.checkboxText}>Müzik Dinlemek</Text>
          </TouchableOpacity>
        </View>

        {/* Kayıt Ol Butonu */}
        <TouchableOpacity style={styles.button} onPress={handleRegister}>
          <Text style={styles.buttonText}>Kayıt Ol</Text>
        </TouchableOpacity>

      </ScrollView>
    </SafeAreaView>
  );
}

// --- BASİT ÖĞRENCİ SEVİYESİ STİLLERİ ---
const styles = StyleSheet.create({
  container: {
    flex: 1,
    backgroundColor: '#fff',
  },
  scrollContainer: {
    padding: 20,
  },
  headerTitle: {
    fontSize: 22,
    fontWeight: 'bold',
    marginBottom: 20,
    textAlign: 'center',
  },
  inputGroup: {
    marginBottom: 15,
  },
  label: {
    fontSize: 16,
    marginBottom: 5,
    color: '#333',
  },
  input: {
    borderWidth: 1,
    borderColor: '#ccc',
    padding: 10,
    borderRadius: 5,
    fontSize: 16,
  },
  radioContainer: {
    flexDirection: 'row',
    marginTop: 5,
  },
  radioButtonRow: {
    flexDirection: 'row',
    alignItems: 'center',
    marginRight: 20,
  },
  radioCircle: {
    height: 20,
    width: 20,
    borderRadius: 10,
    borderWidth: 1,
    borderColor: '#333',
    alignItems: 'center',
    justifyContent: 'center',
    marginRight: 5,
  },
  selectedRadioCircle: {
    height: 10,
    width: 10,
    borderRadius: 5,
    backgroundColor: '#333',
  },
  radioText: {
    fontSize: 16,
  },
  checkboxRow: {
    flexDirection: 'row',
    alignItems: 'center',
    marginTop: 8,
  },
  checkbox: {
    height: 20,
    width: 20,
    borderWidth: 1,
    borderColor: '#333',
    alignItems: 'center',
    justifyContent: 'center',
    marginRight: 8,
  },
  checkmark: {
    fontSize: 14,
    fontWeight: 'bold',
  },
  checkboxText: {
    fontSize: 16,
  },
  button: {
    backgroundColor: '#007AFF',
    padding: 12,
    borderRadius: 5,
    alignItems: 'center',
    marginTop: 20,
  },
  buttonText: {
    color: '#fff',
    fontSize: 16,
    fontWeight: 'bold',
  },
});
```

### Kodun Kısa Özeti:
1. **Mail İçin Input (`TextInput`):** Kullanıcının e-posta adresini girmesi için standart bir `TextInput` ve bunu takip eden bir `email` state'i tanımlandı.
2. **Cinsiyet İçin Radio Button (`TouchableOpacity` ile):** Harici kütüphane kullanmamak için `TouchableOpacity` ve basit daire stilleri kullanılarak "Kadın" ve "Erkek" seçenekleri yapıldı. Seçilen değer `gender` state'inde tutuluyor.
3. **Hobiler İçin Checkbox (`TouchableOpacity` ile):** Yine dış paket gerektirmeyen, tıklandığında içine "X" işareti koyan basit kare kutular (`checkbox`) tasarlandı. Birden fazla seçilebilmesi için `hobbies` adında bir nesne (object) state'i kullanıldı.
