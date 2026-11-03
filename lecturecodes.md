design the ui of a react native app that calculates a students success score based o on their exam score and assignment score 
a: create a user interface containing 2 buttons labeled calculate and reset and a section for displaying the result both inputs fields must accept only numeric values 
b: when calculate pressed app must calculate succes score using the following formula and the calculated succes score must be displayed in interface succes score = (examscore*0.7)+(assignmentscore*0.3)
c: when the reset button pressed both input fields and displayed result must be cleared
çok giriş seviyesi olsun

---

### 🤖 Gemini Response (2026-11-03 08:17:00 UTC)

Merhaba! İsteğin doğrultusunda **Expo Snack** üzerinde doğrudan çalıştırabileceğin, oldukça sade ve giriş seviyesinde bir React Native uygulaması hazırladım.

### `App.js` Kodu:

```javascript
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
});
```

---

### Kısaca Nasıl Çalışıyor?

1. **State (`useState`)**: Kullanıcının girdiği `examScore` (sınav notu), `assignmentScore` (ödev notu) ve hesaplanan `result` (sonuç) verilerini hafızada tutmak için temel React state'leri kullandık.
2. **Numeric Input (`keyboardType="numeric"`)**: Metin kutularında kullanıcıların sadece sayı girebilmesini sağlamak için `keyboardType="numeric"` özelliği eklendi.
3. **Hesaplama (`handleCalculate`)**: "Hesapla" butonuna basıldığında metin ifadeleri `parseFloat()` ile sayıya çevrilip `(Sınav * 0.7) + (Ödev * 0.3)` formülü uygulanır.
4. **Sıfırlama (`handleReset`)**: "Sıfırla" butonuna basıldığında hem girdi kutularının içi temizlenir hem de ekrandaki sonuç sıfırlanır.
