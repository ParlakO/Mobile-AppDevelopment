10 kişilik dummy database yap cinsiyet seçim olsun radio buttton hobi sorulsun checkbox

---

### 🤖 Gemini Response (2026-11-03 06:20:45 UTC)

Merhaba! 

İstediğin gibi **10 kişilik dummy (örnek) veritabanı**, **Radio Button** şeklinde cinsiyet seçimi ve **Checkbox** şeklinde hobi seçimleri içeren tam uyumlu React Native kodunu hazırladım. 

Harici hiçbir kütüphane kullanmadan tamamen temel React Native bileşenleri (`TouchableOpacity`, `View`, `Text` vb.) ile hazırlanmıştır. Direkt **Expo Snack (`App.js`)** içerisine kopyalayıp çalıştırabilirsin.

### `App.js`

```javascript
import React, { useState } from 'react';
import {
  SafeAreaView,
  View,
  Text,
  TextInput,
  TouchableOpacity,
  ScrollView,
  StyleSheet,
} from 'react-native';

// 10 Kişilik Örnek (Dummy) Veritabanı
const initialPeople = [
  { id: '1', name: 'Ahmet Yılmaz', gender: 'Erkek', hobbies: ['Spor', 'Kodlama'] },
  { id: '2', name: 'Ayşe Demir', gender: 'Kadın', hobbies: ['Müzik', 'Kitap'] },
  { id: '3', name: 'Mehmet Kaya', gender: 'Erkek', hobbies: ['Spor'] },
  { id: '4', name: 'Fatma Çelik', gender: 'Kadın', hobbies: ['Kodlama', 'Müzik'] },
  { id: '5', name: 'Ali Öztürk', gender: 'Erkek', hobbies: ['Kitap'] },
  { id: '6', name: 'Zeynep Arslan', gender: 'Kadın', hobbies: ['Spor', 'Müzik'] },
  { id: '7', name: 'Can Şahin', gender: 'Erkek', hobbies: ['Kodlama'] },
  { id: '8', name: 'Elif Yıldız', gender: 'Kadın', hobbies: ['Kitap', 'Kodlama'] },
  { id: '9', name: 'Burak Aydın', gender: 'Erkek', hobbies: ['Müzik'] },
  { id: '10', name: 'Selin Özkan', gender: 'Kadın', hobbies: ['Spor', 'Kitap'] },
];

export default function App() {
  // Liste State'i (10 kişi ile başlıyor)
  const [people, setPeople] = useState(initialPeople);

  // Form State'leri
  const [name, setName] = useState('');
  const [gender, setGender] = useState('Erkek'); // Radio Button seçimi
  const [selectedHobbies, setSelectedHobbies] = useState([]); // Checkbox seçimleri (Dizi)

  // Seçilebilecek Hobiler
  const availableHobbies = ['Spor', 'Müzik', 'Kitap', 'Kodlama'];

  // Checkbox Seçim / Kaldırma Mantığı
  const toggleHobby = (hobby) => {
    if (selectedHobbies.includes(hobby)) {
      // Eğer zaten seçiliyse listeden çıkar
      setSelectedHobbies(selectedHobbies.filter((item) => item !== hobby));
    } else {
      // Seçili değilse listeye ekle
      setSelectedHobbies([...selectedHobbies, hobby]);
    }
  };

  // Yeni Kişi Ekleme
  const handleAddPerson = () => {
    if (!name.trim()) {
      alert('Lütfen bir isim giriniz.');
      return;
    }

    const newPerson = {
      id: Date.now().toString(),
      name: name,
      gender: gender,
      hobbies: selectedHobbies,
    };

    setPeople([...people, newPerson]);

    // Formu temizle
    setName('');
    setGender('Erkek');
    setSelectedHobbies([]);
  };

  return (
    <SafeAreaView style={styles.container}>
      <ScrollView contentContainerStyle={styles.scrollContent}>
        <Text style={styles.title}>Kişi Kayıt Formu</Text>

        {/* İsim Girişi */}
        <Text style={styles.label}>İsim Soyisim:</Text>
        <TextInput
          style={styles.input}
          placeholder="Örn: Mustafa Can"
          value={name}
          onChangeText={setName}
        />

        {/* Cinsiyet Seçimi - Radio Button */}
        <Text style={styles.label}>Cinsiyet (Radio Button):</Text>
        <View style={styles.radioContainer}>
          {['Erkek', 'Kadın'].map((item) => (
            <TouchableOpacity
              key={item}
              style={styles.radioButton}
              onPress={() => setGender(item)}
            >
              <View style={styles.radioOuter}>
                {gender === item && <View style={styles.radioInner} />}
              </View>
              <Text style={styles.radioText}>{item}</Text>
            </TouchableOpacity>
          ))}
        </View>

        {/* Hobiler - Checkbox */}
        <Text style={styles.label}>Hobiler (Checkbox):</Text>
        <View style={styles.checkboxContainer}>
          {availableHobbies.map((hobby) => {
            const isChecked = selectedHobbies.includes(hobby);
            return (
              <TouchableOpacity
                key={hobby}
                style={styles.checkboxItem}
                onPress={() => toggleHobby(hobby)}
              >
                <View style={[styles.checkboxBox, isChecked && styles.checkboxChecked]}>
                  {isChecked && <Text style={styles.checkmark}>✓</Text>}
                </View>
                <Text style={styles.checkboxText}>{hobby}</Text>
              </TouchableOpacity>
            );
          })}
        </View>

        {/* Kaydet Butonu */}
        <TouchableOpacity style={styles.button} onPress={handleAddPerson}>
          <Text style={styles.buttonText}>Listeye Ekle</Text>
        </TouchableOpacity>

        {/* Veritabanı Liste Gösterimi */}
        <Text style={styles.subTitle}>Kişi Listesi ({people.length} Kişi)</Text>
        {people.map((person) => (
          <View key={person.id} style={styles.card}>
            <Text style={styles.cardTitle}>{person.name}</Text>
            <Text style={styles.cardText}>Cinsiyet: {person.gender}</Text>
            <Text style={styles.cardText}>
              Hobiler: {person.hobbies.length > 0 ? person.hobbies.join(', ') : 'Yok'}
            </Text>
          </View>
        ))}
      </ScrollView>
    </SafeAreaView>
  );
}

const styles = StyleSheet.create({
  container: {
    flex: 1,
    backgroundColor: '#f9f9f9',
  },
  scrollContent: {
    padding: 15,
  },
  title: {
    fontSize: 20,
    fontWeight: 'bold',
    marginBottom: 15,
    textAlign: 'center',
  },
  subTitle: {
    fontSize: 18,
    fontWeight: 'bold',
    marginTop: 20,
    marginBottom: 10,
  },
  label: {
    fontSize: 14,
    fontWeight: 'bold',
    marginTop: 10,
    marginBottom: 5,
  },
  input: {
    borderWidth: 1,
    borderColor: '#ccc',
    backgroundColor: '#fff',
    padding: 8,
    borderRadius: 4,
  },
  // Radio Button Stilleri
  radioContainer: {
    flexDirection: 'row',
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
    borderRadius: 10,
    borderWidth: 1,
    borderColor: '#555',
    alignItems: 'center',
    justifyContent: 'center',
    marginRight: 5,
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
    flexWrap: 'wrap',
    marginBottom: 10,
  },
  checkboxItem: {
    flexDirection: 'row',
    alignItems: 'center',
    width: '50%',
    marginVertical: 5,
  },
  checkboxBox: {
    height: 20,
    width: 20,
    borderWidth: 1,
    borderColor: '#555',
    alignItems: 'center',
    justifyContent: 'center',
    marginRight: 5,
    backgroundColor: '#fff',
  },
  checkboxChecked: {
    backgroundColor: '#007AFF',
    borderColor: '#007AFF',
  },
  checkmark: {
    color: '#fff',
    fontSize: 12,
    fontWeight: 'bold',
  },
  checkboxText: {
    fontSize: 14,
  },
  // Buton ve Kart Stilleri
  button: {
    backgroundColor: '#007AFF',
    padding: 10,
    borderRadius: 4,
    alignItems: 'center',
    marginTop: 10,
  },
  buttonText: {
    color: '#fff',
    fontWeight: 'bold',
  },
  card: {
    backgroundColor: '#fff',
    borderWidth: 1,
    borderColor: '#ddd',
    padding: 10,
    borderRadius: 4,
    marginBottom: 8,
  },
  cardTitle: {
    fontSize: 16,
    fontWeight: 'bold',
  },
  cardText: {
    fontSize: 14,
    color: '#333',
    marginTop: 2,
  },
});
```

---

### Kodun Çalışma Mantığı:
1. **Dummy Database (`initialPeople`):** 10 adet hazır nesne içeren bir dizi oluşturduk. Sayfa ilk açıldığında bu liste ekrana basılır.
2. **Radio Button Mantığı:** Cinsiyet seçiminde tek bir değer (`'Erkek'` veya `'Kadın'`) tutulur. Seçilen cinsiyetin iç yuvarlağı Mavi renk alır.
3. **Checkbox Mantığı:** Birden fazla hobi seçilebileceği için `selectedHobbies` bir dizi (array) olarak tutulur. Tıklanan hobi listede varsa çıkarılır, yoksa eklenir. Seçili olduğunda kutunun içine tik (`✓`) işareti koyulur.
4. **Listeye Ekleme:** Form doldurulup "Listeye Ekle" butonuna basıldığında yeni veri duruma (State) eklenir ve liste anında güncellenir.
