design the ui of a react native app that calculates a students success score based o on their exam score and assignment score 
a: create a user interface containing 2 buttons labeled calculate and reset and a section for displaying the result both inputs fields must accept only numeric values 
b: when calculate pressed app must calculate succes score using the following formula and the calculated succes score must be displayed in interface succes score = (examscore*0.7)+(assignmentscore*0.3)
c: when the reset button pressed both input fields and displayed result must be cleared

---

### 🤖 Gemini Response (2026-11-03 08:15:46 UTC)

Here is a complete, beginner-friendly React Native app designed for **Expo Snack** that fulfills all parts of your assignment.

### `App.js`

```javascript
import React, { useState } from 'react';
import {
  SafeAreaView,
  StyleSheet,
  Text,
  View,
  TextInput,
  TouchableOpacity,
} from 'react-native';

export default function App() {
  // State variables for inputs and calculation result
  const [examScore, setExamScore] = useState('');
  const [assignmentScore, setAssignmentScore] = useState('');
  const [result, setResult] = useState(null);

  // Function to calculate the success score
  const handleCalculate = () => {
    const exam = parseFloat(examScore);
    const assignment = parseFloat(assignmentScore);

    // Check if both inputs are valid numbers
    if (!isNaN(exam) && !isNaN(assignment)) {
      const score = exam * 0.7 + assignment * 0.3;
      setResult(score.toFixed(2)); // Display rounded to 2 decimal places
    } else {
      setResult('Please enter valid numeric values!');
    }
  };

  // Function to reset all inputs and display
  const handleReset = () => {
    setExamScore('');
    setAssignmentScore('');
    setResult(null);
  };

  return (
    <SafeAreaView style={styles.container}>
      <View style={styles.card}>
        <Text style={styles.title}>Student Success Score Calculator</Text>

        {/* Exam Score Input */}
        <Text style={styles.label}>Exam Score (70%):</Text>
        <TextInput
          style={styles.input}
          placeholder="Enter exam score"
          keyboardType="numeric"
          value={examScore}
          onChangeText={setExamScore}
        />

        {/* Assignment Score Input */}
        <Text style={styles.label}>Assignment Score (30%):</Text>
        <TextInput
          style={styles.input}
          placeholder="Enter assignment score"
          keyboardType="numeric"
          value={assignmentScore}
          onChangeText={setAssignmentScore}
        />

        {/* Buttons Row */}
        <View style={styles.buttonRow}>
          <TouchableOpacity style={styles.calcButton} onPress={handleCalculate}>
            <Text style={styles.buttonText}>Calculate</Text>
          </TouchableOpacity>

          <TouchableOpacity style={styles.resetButton} onPress={handleReset}>
            <Text style={styles.buttonText}>Reset</Text>
          </TouchableOpacity>
        </View>

        {/* Result Display Section */}
        {result !== null && (
          <View style={styles.resultBox}>
            <Text style={styles.resultText}>
              {typeof result === 'number' || !isNaN(result)
                ? `Success Score: ${result}`
                : result}
            </Text>
          </View>
        )}
      </View>
    </SafeAreaView>
  );
}

const styles = StyleSheet.create({
  container: {
    flex: 1,
    backgroundColor: '#f2f2f2',
    justifyContent: 'center',
    padding: 20,
  },
  card: {
    backgroundColor: '#ffffff',
    padding: 20,
    borderRadius: 8,
    borderWidth: 1,
    borderColor: '#ccc',
  },
  title: {
    fontSize: 18,
    fontWeight: 'bold',
    textAlign: 'center',
    marginBottom: 20,
    color: '#333',
  },
  label: {
    fontSize: 14,
    marginBottom: 5,
    color: '#333',
  },
  input: {
    borderWidth: 1,
    borderColor: '#ccc',
    borderRadius: 5,
    padding: 10,
    marginBottom: 15,
    fontSize: 16,
    backgroundColor: '#fff',
  },
  buttonRow: {
    flexDirection: 'row',
    justifyContent: 'space-between',
    marginTop: 10,
  },
  calcButton: {
    backgroundColor: '#28a745',
    padding: 12,
    borderRadius: 5,
    flex: 0.48,
    alignItems: 'center',
  },
  resetButton: {
    backgroundColor: '#dc3545',
    padding: 12,
    borderRadius: 5,
    flex: 0.48,
    alignItems: 'center',
  },
  buttonText: {
    color: '#ffffff',
    fontWeight: 'bold',
    fontSize: 16,
  },
  resultBox: {
    marginTop: 20,
    padding: 15,
    backgroundColor: '#e9ecef',
    borderRadius: 5,
    borderWidth: 1,
    borderColor: '#ccc',
    alignItems: 'center',
  },

