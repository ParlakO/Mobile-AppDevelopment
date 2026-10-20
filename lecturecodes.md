kaydolmak için checkboxlı bir hoıbi bölümmü ve radio buttonlu gender ekle

---

### 🤖 Gemini Response (2026-10-20 15:14:52 UTC)

Here is the complete, self-contained `App.js` code for your Expo Snack that adds a hobby selection section with checkboxes and a gender selection section with radio buttons to your registration form.

### Expo Snack Code (`App.js`)

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
  // State for text inputs
  const [name, setName] = useState('');
  const [email, setEmail] = useState('');

  // State for Gender (Radio Button simulation)
  const [gender, setGender] = useState(null);

  // State for Hobbies (Checkbox simulation)
  const [hobbies, setHobbies] = useState({
    reading: false,
    sports: false,
    music: false,
  });

  // Toggle checkbox state
  const toggleHobby = (hobbyKey) => {
    setHobbies({
      ...hobbies,
      [hobbyKey]: !hobbies[hobbyKey],
    });
  };

  const handleRegister = () => {
    alert(`Registered!\nName: ${name}\nEmail: ${email}\nGender: ${gender}\nHobbies: ${Object.keys(hobbies).filter(h => hobbies[h]).join(', ')}`);
  };

  return (
    <SafeAreaView style={styles.container}>
      <ScrollView contentContainerStyle={styles.scrollContainer}>
        <Text style={styles.title}>Create Account</Text>

        {/* Name Input */}
        <TextInput
          style={styles.input}
          placeholder="Full Name"
          placeholderTextColor="#888"
          value={name}
          onChangeText={setName}
        />

        {/* Email Input */}
        <TextInput
          style={styles.input}
          placeholder="Email Address"
          placeholderTextColor="#888"
          value={email}
          onChangeText={setEmail}
          keyboardType="email-address"
        />

        {/* Gender Section (Radio Buttons) */}
        <Text style={styles.label}>Gender:</Text>
        <View style={styles.radioGroup}>
          {['Male', 'Female', 'Other'].map((option) => (
            <TouchableOpacity
              key={option}
              style={styles.radioButtonContainer}
              onPress={() => setGender(option)}
            >
              <View style={styles.radioOuter}>
                {gender === option && <View style={styles.radioInner} />}
              </View>
              <Text style={styles.radioLabel}>{option}</Text>
            </TouchableOpacity>
          ))}
        </View>

        {/* Hobbies Section (Checkboxes) */}
        <Text style={styles.label}>Hobbies:</Text>
        <View style={styles.checkboxGroup}>
          {[
            { key: 'reading', label: 'Reading Books' },
            { key: 'sports', label: 'Playing Sports' },
            { key: 'music', label: 'Listening to Music' },
          ].map((item) => (
            <TouchableOpacity
              key={item.key}
              style={styles.checkboxContainer}
              onPress={() => toggleHobby(item.key)}
            >
              <View style={styles.checkbox}>
                {hobbies[item.key] && <Text style={styles.checkmark}>✓</Text>}
              </View>
              <Text style={styles.checkboxLabel}>{item.label}</Text>
            </TouchableOpacity>
          ))}
        </View>

        {/* Submit Button */}
        <TouchableOpacity style={styles.button} onPress={handleRegister}>
          <Text style={styles.buttonText}>Register</Text>
        </TouchableOpacity>

      </ScrollView>
    </SafeAreaView>
  );
}

const styles = StyleSheet.create({
  container: {
    flex: 1,
    backgroundColor: '#f5f5f5',
  },
  scrollContainer: {
    padding: 20,
  },
  title: {
    fontSize: 24,
    fontWeight: 'bold',
    marginBottom: 20,
    textAlign: 'center',
    color: '#333',
  },
  input: {
    backgroundColor: '#fff',
    paddingHorizontal: 15,
    paddingVertical: 12,
    borderRadius: 8,
    borderWidth: 1,
    borderColor: '#ddd',
    marginBottom: 15,
    fontSize: 16,
  },
  label: {
    fontSize: 16,
    fontWeight: '600',
    marginTop: 10,
    marginBottom: 8,
    color: '#444',
  },
  radioGroup: {
    flexDirection: 'row',
    justifyContent: 'space-between',
    marginBottom: 15,
  },
  radioButtonContainer: {
    flexDirection: 'row',
    alignItems: 'center',
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
  radioLabel: {
    fontSize: 14,
    color: '#333',
  },
  checkboxGroup: {
    marginBottom: 20,
  },
  checkboxContainer: {
    flexDirection: 'row',
    alignItems: 'center',
    marginBottom: 10,
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
    fontSize: 14,
    color: '#333',
  },
  button: {
    backgroundColor: '#007AFF',
    padding: 15,
    borderRadius: 8,
    alignItems: 'center',
    marginTop: 10,
  },
    buttonText: {
    color: '#fff',
    fontSize: 16,
    fontWeight: 'bold',
  },
});
```

---

### How it Works (Explanation for Students):

1. **State Management (`useState`)**:
   - `gender`: Stores a single string value (e.g., `'Male'`) because only one option can be selected at a time.
   - `hobbies`: Stores an object containing boolean values (`true`/`false`) for each hobby so multiple options can be selected independently.

2. **Simulating Radio Buttons (`gender`)**:
   - We use `TouchableOpacity` wrapping a custom view structure (`radioOuter` and `radioInner`). 
   - When clicked, `setGender(option)` updates the state. If the current option matches the selected gender state, a small inner circle (`radioInner`) appears.

3. **Simulating Checkboxes (`hobbies`)**:
   - We use `TouchableOpacity` with a square box (`checkbox`). 
   - Clicking a hobby calls `toggleHobby(item.key)`, which reverses the boolean value of that specific hobby in our state object using the spread operator (`...hobbies`). A checkmark (`✓`) renders conditionally if the value is `true`.

4. **Flexbox Layout**:
   - `flexDirection: 'row'` is used in the radio button container and checkbox container to align the selection indicator (`View`) and the descriptive `Text` side-by-side horizontally.
