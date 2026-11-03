import React, { useState } from 'react';
import { StyleSheet, Text, View, TextInput, TouchableOpacity, SafeAreaView } from 'react-native';

export default function App() {
  // 1. Durum (State) tanımlamaları
  const [examScore, setExamScore] = useState('');
  const [assignmentScore, setAssignmentScore] = useState('');
  const [result, setResult] = useState(null);

  // 2. Başarı notu hesaplama fonksiyonu
  const handleCalculate = () => {
    const exam = parseFloat(examScore);
    const assignment = parseFloat(assignmentScore);

    // Girdilerin sayı olup olmadığını kontrol etme
    if (!isNaN(exam) && !isNaN(assignment)) {
      const successScore = (exam * 0.7) + (assignment * 0.3);
      setResult(successScore.toFixed(2)); // Sonucu virgülden sonra 2 basamak olarak gösterir
    } else {
      setResult('Lütfen geçerli sayılar giriniz!');
    }
  };

  // 3. Formu sıfırlama fonksiyonu
  const handleReset = () => {
    setExamScore('');
    setAssignmentScore('');
    setResult(null);
  };

  return (
    <SafeAreaView style={styles.container}>
      <Text style={styles.title}>Başarı Notu Hesaplama</Text>

      {/* Sınav Notu Giriş Alanı */}
      <Text style={styles.label}>Sınav Notu (%70):</Text>
      <TextInput
        style={styles.input}
        placeholder="Örn: 80"
        keyboardType="numeric" // Yalnızca sayısal klavyeyi açar
        value={examScore}
        onChangeText={(text) => setExamScore(text)}
      />

      {/* Ödev Notu Giriş Alanı */}
      <Text style={styles.label}>Ödev Notu (%30):</Text>
      <TextInput
        style={styles.input}
        placeholder="Örn: 90"
        keyboardType="numeric" // Yalnızca sayısal klavyeyi açar
        value={assignmentScore}
        onChangeText={(text) => setAssignmentScore(text)}
      />

      {/* Butonlar */}
      <View style={styles.buttonRow}>
        <TouchableOpacity style={styles.calculateButton} onPress={handleCalculate}>
          <Text style={styles.buttonText}>Hesapla</Text>
        </TouchableOpacity>

        <TouchableOpacity style={styles.resetButton} onPress={handleReset}>
          <Text style={styles.buttonText}>Sıfırla</Text>
        </TouchableOpacity>
      </View>

      {/* Sonuç Alanı */}
      <View style={styles.resultBox}>
        <Text style={styles.resultLabel}>Başarı Notu:</Text>
        <Text style={styles.resultValue}>
          {result !== null ? result : '-'}
        </Text>
      </View>
    </SafeAreaView>
  );
}

// Giriş seviyesi sade stil tanımlamaları
const styles = StyleSheet.create({
  container: {
    flex: 1,
    padding: 20,
    backgroundColor: '#ffffff',
    justifyContent: 'center',
  },
  title: {
    fontSize: 20,
    fontWeight: 'bold',
    textAlign: 'center',
    marginBottom: 20,
  },
  label: {
    fontSize: 15,
    marginBottom: 5,
  },
  input: {
    borderWidth: 1,
    borderColor: '#ccc',
    padding: 10,
    marginBottom: 15,
    borderRadius: 4,
  },
  buttonRow: {
    flexDirection: 'row',
    justifyContent: 'space-between',
    marginBottom: 20,
  },
  calculateButton: {
    backgroundColor: '#2196F3',
    padding: 12,
    borderRadius: 4,
    flex: 0.48,
    alignItems: 'center',
  },
  resetButton: {
    backgroundColor: '#f44336',
    padding: 12,
    borderRadius: 4,
    flex: 0.48,
    alignItems: 'center',
  },
  buttonText: {
    color: '#ffffff',
    fontWeight: 'bold',
  },
  resultBox: {
    borderWidth: 1,
    borderColor: '#ccc',
    padding: 15,
    alignItems: 'center',
    borderRadius: 4,
  },
  resultLabel: {
    fontSize: 16,
    color: '#333',
  },
  resultValue: {
    fontSize: 22,
    fontWeight: 'bold',
    marginTop: 5,
  },
}); bundan daha giriş seviyesi yap cok kolay olsun kanka detay olmasın renk olmasın

---

### 🤖 Gemini Response (2026-11-03 08:19:07 UTC)

Harika bir istek! İlk başlayanlar için renkleri, karmaşık düzenleri (flex layout) ve detaylı stilleri çıkarıp kodu olabilecek **en sade ve en anlaşılır** haline getirdim.

Tüm renkli butonları, karmaşık `flex: 0.48` gibi oranları kaldırdık. Sadece siyah/beyaz, düz kenarlıklı ve en temel bileşenlerden oluşan bir yapı haline getirdik.

### Güncellenmiş Basit Kod (`App.js`)

```javascript
import React, { useState } from 'react';
import { StyleSheet, Text, View, TextInput, TouchableOpacity, SafeAreaView } from 'react-native';

export default function App() {
  // Durum (State) değişkenleri
  const [examScore, setExamScore] = useState('');
  const [assignmentScore, setAssignmentScore] = useState('');
  const [result, setResult] = useState('');

  // Hesaplama fonksiyonu
  const handleCalculate = () => {
    const exam = parseFloat(examScore);
    const assignment = parseFloat(assignmentScore);

    if (!isNaN(exam) && !isNaN(assignment)) {
      const total = (exam * 0.7) + (assignment * 0.3);
      setResult(total.toFixed(2));
    } else {
      setResult('Girdi Hatalı!');
    }
  };

  // Sıfırlama fonksiyonu
  const handleReset = () => {
    setExamScore('');
    setAssignmentScore('');
    setResult('');
  };

  return (
    <SafeAreaView style={styles.container}>
      <Text style={styles.title}>Not Hesaplama</Text>

      {/* Sınav Notu Girişi */}
      <Text>Sınav Notu (%70):</Text>
      <TextInput
        style={styles.input}
        placeholder="Örn: 80"
        keyboardType="numeric"
        value={examScore}
        onChangeText={setExamScore}
      />

      {/* Ödev Notu Girişi */}
      <Text>Ödev Notu (%30):</Text>
      <TextInput
        style={styles.input}
        placeholder="Örn: 90"
        keyboardType="numeric"
        value={assignmentScore}
        onChangeText={setAssignmentScore}
      />

      {/* Butonlar */}
      <TouchableOpacity style={styles.button} onPress={handleCalculate}>
        <Text>Hesapla</Text>
      </TouchableOpacity>

      <TouchableOpacity style={styles.button} onPress={handleReset}>
        <Text>Temizle</Text>
      </TouchableOpacity>

      {/* Sonuç */}
      <View style={styles.resultBox}>
        <Text>Sonuç: {result}</Text>
      </View>
    </SafeAreaView>
  );
}

// En temel ve sade stiller (Renkler ve detaylar kaldırıldı)
const styles = StyleSheet.create({
  container: {
    flex: 1,
    padding: 20,
    justifyContent: 'center',
  },
  title: {
    fontSize: 18,
    fontWeight: 'bold',
    textAlign: 'center',
    marginBottom: 15,
  },
  input: {
    borderWidth: 1,
    borderColor: '#000000',
    padding: 8,
    marginTop: 5,
    marginBottom: 15,
  },
  button: {
    borderWidth: 1,
    borderColor: '#000000',
    padding: 10,
    alignItems: 'center',
    marginBottom: 10,
  },
  resultBox: {
    borderWidth: 1,
    borderColor: '#000000',
    padding: 10,
    alignItems: 'center',
    marginTop: 10,
  },
});
```

---

### Neleri Sadeleştirdik?
1. **Renkler Kaldırıldı:** Mavi ve kırmızı buton renkleri yerine sadece basit siyah çerçeveli (`borderWidth: 1`, `borderColor: '#000000'`) kutular kullanıldı.
2. **Düzen Basitleştirildi:** Butonları yan yana koymak için kullanılan karmaşık esnek alanlar (`buttonRow`, `flex: 0.48`) kaldırıldı. Butonlar alt alta sıralandı.
3. **Kısa Ok Yapısı:** `onChangeText={(text) => setExamScore(text)}` ifadesi daha kısa olan `onChangeText={setExamScore}` şekline getirildi.
4. **Karmaşık Stil Kuralları Silindi:** `borderRadius`, gölgeler ve özel yazı renkleri tamamen temizlendi. Tamamen bir öğrencinin ilk derste yazacağı kadar yalın hale getirildi.

Bu kodu **Expo Snack (snack.expo.dev)** üzerine doğrudan yapıştırıp çalıştırabilirsin!
