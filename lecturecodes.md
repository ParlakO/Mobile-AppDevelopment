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
}); bunu ingilizce yap not yazma kesinlikle

---

### 🤖 Gemini Response (2026-11-03 08:20:14 UTC)

```javascript
import React, { useState } from 'react';
import { StyleSheet, Text, View, TextInput, TouchableOpacity, SafeAreaView } from 'react-native';

export default function App() {
  // State variables
  const [examScore, setExamScore] = useState('');
  const [assignmentScore, setAssignmentScore] = useState('');
  const [result, setResult] = useState('');

  // Calculation function
  const handleCalculate = () => {
    const exam = parseFloat(examScore);
    const assignment = parseFloat(assignmentScore);

    if (!isNaN(exam) && !isNaN(assignment)) {
      const total = (exam * 0.7) + (assignment * 0.3);
      setResult(total.toFixed(2));
    } else {
      setResult('Invalid Input!');
    }
  };

  // Reset function
  const handleReset = () => {
    setExamScore('');
    setAssignmentScore('');
    setResult('');
  };

  return (
    <SafeAreaView style={styles.container}>
      <Text style={styles.title}>Grade Calculator</Text>

      {/* Exam Score Input */}
      <Text>Exam Score (%70):</Text>
      <TextInput
        style={styles.input}
        placeholder="e.g. 80"
        keyboardType="numeric"
        value={examScore}
        onChangeText={setExamScore}
      />

      {/* Assignment Score Input */}
      <Text>Assignment Score (%30):</Text>
      <TextInput
        style={styles.input}
        placeholder="e.g. 90"
        keyboardType="numeric"
        value={assignmentScore}
        onChangeText={setAssignmentScore}
      />

      {/* Buttons */}
      <TouchableOpacity style={styles.button} onPress={handleCalculate}>
        <Text>Calculate</Text>
      </TouchableOpacity>

      <TouchableOpacity style={styles.button} onPress={handleReset}>
        <Text>Reset</Text>
      </TouchableOpacity>

      {/* Result */}
      <View style={styles.resultBox}>
        <Text>Result: {result}</Text>
      </View>
    </SafeAreaView>
  );
}

// Basic and simple styles
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
