# 🤖 Gemini Response (2026-11-03 08:17:58 UTC)

Here is a complete, beginner-friendly React Native code for your student success score calculator. You can copy and paste this directly into `App.js` on **[Expo Snack](https://snack.expo.dev)**.

### `App.js`

```javascript
import React, { useState } from 'react';
import { StyleSheet, Text, View, TextInput, TouchableOpacity, SafeAreaView } from 'react-native';

export default function App() {
  // State variables for input values and calculation result
  const [examScore, setExamScore] = useState('');
  const [assignmentScore, setAssignmentScore] = useState('');
  const [result, setResult] = useState(null);

  // Function to calculate the success score
  const calculateScore = () => {
    const exam = parseFloat(examScore);
    const assignment = parseFloat(assignmentScore);

    // Validate that inputs are valid numbers
    if (!isNaN(exam) && !isNaN(assignment)) {
      const score = (exam * 0.7) + (assignment * 0.3);
      setResult(score.toFixed(2)); // Round result to 2 decimal places
    } else {
      setResult('Please enter valid numbers!');
    }
  };

  // Function to reset all inputs and results
  const resetFields = () => {
    setExamScore('');
    setAssignmentScore('');
    setResult(null);
  };

  return (
    <SafeAreaView style={styles.container}>
      <Text style={styles.title}>Student Success Score Calculator</Text>

      {/* Exam Score Input Section */}
      <Text style={styles.label}>Exam Score (70%):</Text>
      <TextInput
        style={styles.input}
        placeholder="e.g. 80"
        keyboardType="numeric"
        value={examScore}
        onChangeText={(text) => setExamScore(text)}
      />

      {/* Assignment Score Input Section */}
      <Text style={styles.label}>Assignment Score (30%):</Text>
      <TextInput
        style={styles.input}
        placeholder="e.g. 90"
        keyboardType="numeric"
        value={assignmentScore}
        onChangeText={(text) => setAssignmentScore(text)}
      />

      {/* Action Buttons */}
      <View style={styles.buttonContainer}>
        <TouchableOpacity style={styles.calculateButton} onPress={calculateScore}>
          <Text style={styles.buttonText}>Calculate</Text>
        </TouchableOpacity>

        <TouchableOpacity style={styles.resetButton} onPress={resetFields}>
          <Text style={styles.buttonText}>Reset</Text>
        </TouchableOpacity>
      </View>

      {/* Result Display Section */}
      <View style={styles.resultBox}>
        <Text style={styles.resultLabel}>Success Score:</Text>
        <Text style={styles.resultValue}>
          {result !== null ? result : '-'}
        </Text>
      </View>
    </SafeAreaView>
  );
}

// Simple beginner-level styling
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
    fontSize: 14,
    marginBottom: 5,
  },
  input: {
    borderWidth: 1,
    borderColor: '#ccc',
    padding: 10,
    marginBottom: 15,
    borderRadius: 4,
  },
  buttonContainer: {
    flexDirection: 'row',
    justifyContent: 'space-between',
    marginBottom: 20,
  },
  calculateButton: {
    backgroundColor: '#007AFF',
    padding: 12,
    flex: 0.48,
    alignItems: 'center',
    borderRadius: 4,
  },
  resetButton: {
    backgroundColor: '#8E8E93',
    padding: 12,
    flex: 0.48,
    alignItems: 'center',
    borderRadius: 4,
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
    marginBottom: 5,
  },
  resultValue: {
    fontSize: 22,
    fontWeight: 'bold',
  },
});
```

---

### How the Code Works:

1. **State Management (`useState`)**:
   - `examScore` and `assignmentScore` store what the user types into the input fields as text strings.
   - `result` holds the calculated score (or an error message) to display on the screen.

2. **Numeric Inputs (`keyboardType="numeric"`)**:
   - Setting `keyboardType="numeric"` on `<TextInput>` forces mobile keyboards to show numbers only.

3. **Calculation (`calculateScore`)**:
   - `parseFloat()` converts text inputs to floating-point numbers.
   - Applies the formula: `(exam * 0.7) + (assignment * 0.3)`.
   - Uses `.toFixed(2)` to limit output formatting to two decimal places.

4. **Reset Logic (`resetFields`)**:
   - Clears both input state variables (`''`) and sets `result` back to `null`.
