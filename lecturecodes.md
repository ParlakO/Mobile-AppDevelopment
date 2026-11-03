# 🤖 Gemini Response (2026-11-03 08:35:44 UTC)

Here is your self-contained, beginner-friendly React Native code ready to copy and paste directly into **`App.js`** on [Expo Snack](https://snack.expo.dev).

### `App.js`

```javascript
import React, { useState } from 'react';
import { StyleSheet, Text, View, TouchableOpacity, SafeAreaView } from 'react-native';

// --- HELPER FUNCTION (Placed at top for single-file Expo Snack testing) ---
function getMessage() {
  return "Hello from external JS";
}
// ------------------------------------------------------------------------

export default function App() {
  // State to store the message when the button is pressed
  const [displayedMessage, setDisplayedMessage] = useState('');

  // Function to handle button press
  const handlePress = () => {
    const msg = getMessage(); // Call function
    setDisplayedMessage(msg); // Update state to display message on screen
  };

  return (
    <SafeAreaView style={styles.container}>
      
      {/* Title text using inline styling */}
      <Text style={{ color: 'blue', fontWeight: 'bold', fontSize: 24 }}>
        Welcome to Alex
      </Text>

      {/* Button using TouchableOpacity styled with StyleSheet */}
      <TouchableOpacity style={styles.myButton} onPress={handlePress}>
        <Text style={styles.buttonText}>Click Me</Text>
      </TouchableOpacity>

      {/* Display the returned message on screen */}
      <Text style={styles.messageText}>{displayedMessage}</Text>

    </SafeAreaView>
  );
}

// Simple beginner-level StyleSheet
const styles = StyleSheet.create({
  container: {
    flex: 1,
    backgroundColor: '#ffffff',
    alignItems: 'center',
    justifyContent: 'center',
    padding: 20,
  },
  myButton: {
    backgroundColor: 'green',
    padding: 12,
    borderRadius: 5,
    marginTop: 20,
  },
  buttonText: {
    color: 'white',
    fontSize: 16,
  },
  messageText: {
    marginTop: 20,
    fontSize: 18,
    color: '#333333',
  },
});
```

---

### Key Takeaways & Explanation:
1. **Single-File Setup**: The `getMessage()` helper function is declared directly at the top of `App.js`. This allows you to test your logic on Expo Snack immediately without creating extra files or module exports.
2. **State Management**: We use `useState('')` to keep track of the text message. When you click the button, `handlePress()` runs, fetches the message string from `getMessage()`, and updates the state.
3. **Beginner Layout & Styling**: The layout uses standard Flexbox (`justifyContent: 'center'`, `alignItems: 'center'`) inside a `SafeAreaView` to keep elements centered and clean.
