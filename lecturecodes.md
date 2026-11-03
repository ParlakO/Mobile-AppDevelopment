# 🤖 Gemini Response (2026-11-03 08:22:09 UTC)

Here is your complete React Native code translated into English while preserving your original component structure, styling, and logic.

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
      // --- TRANSLATED TEXT ---
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
      {/* --- TRANSLATED TEXT --- */}
      <Text style={styles.title}>Grade Calculator</Text>

      {/* Exam Score Input */}
      <Text>Exam Score (70%):</Text>
      <TextInput
        style={styles.input}
        placeholder="e.g. 80"
        keyboardType="numeric"
        value={examScore}
        onChangeText={setExamScore}
      />

      {/* Assignment Score Input */}
      <Text>Assignment Score (30%):</Text>
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
        <Text>Clear</Text>
      </TouchableOpacity>

      {/* Result Box */}
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

### Explanation of Changes:
1. **Labels & Text**:
   - `"Not Hesaplama"` $\rightarrow$ `"Grade Calculator"`
   - `"Sınav Notu (%70):"` $\rightarrow$ `"Exam Score (70%):"`
   - `"Ödev Notu (%30):"` $\rightarrow$ `"Assignment Score (30%):"`
   - `"Hesapla"` / `"Temizle"` $\rightarrow$ `"Calculate"` / `"Clear"`
   - `"Sonuç: "` $\rightarrow$ `"Result: "`
2. **Placeholders & Messages**:
   - `"Örn: 80"` $\rightarrow$ `"e.g. 80"`
   - `"Girdi Hatalı!"` $\rightarrow$ `"Invalid Input!"`
3. **Comments**: Code comments were translated into clear English without modifying any underlying state or layout logic.
