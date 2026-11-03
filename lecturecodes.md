# 🤖 Gemini Response (2026-11-03 08:30:55 UTC)

Here is your cleaned-up and fully self-contained code ready to copy and paste directly into **`App.js`** on [Expo Snack](https://snack.expo.dev). 

To make testing as simple as possible on Expo Snack without creating multiple files, the `getMessage` function has been integrated directly into the `App.js` file while keeping your exact structure, inline styling, logic, and styles intact.

### `App.js`

```javascript
import React, { useState } from 'react';
import { StyleSheet, Text, View, TouchableOpacity, SafeAreaView } from 'react-native';

// --- HELPER FUNCTION (Integrated for single-file Expo Snack testing) ---
function getMessage() {
  return "Hello from external JS";
}
// ------------------------------------------------------------------------

export default function App() {
  // State to store the message when button is clicked
  const [displayedMessage, setDisplayedMessage] = useState('');

  // Requirement D: Function to handle button press
  const handlePress = () => {
    const msg = getMessage(); // Call function
    setDisplayedMessage(msg); // Update state to show on screen
  };

  return (
    <SafeAreaView style={styles.container}>
      
      {/* Requirement A: Text component with INLINE styling */}
      <Text style={{ color: 'blue', fontWeight: 'bold', fontSize: 24 }}>
        Welcome to Alex
      </Text>

      {/* Requirement B: TouchableOpacity button styled with StyleSheet */}
      <TouchableOpacity style={styles.myButton} onPress={handlePress}>
        <Text style={styles.buttonText}>Click Me</Text>
      </TouchableOpacity>

      {/* Requirement D: Display the returned message on screen */}
      <Text style={styles.messageText}>{displayedMessage}</Text>

    </SafeAreaView>
  );
}

// Requirement B: StyleSheet for button and layout
const styles = StyleSheet.create({
  container: {
    flex: 1,
    backgroundColor: '#ffffff',
    alignItems: 'center',
    justifyContent: 'center',
    padding: 20,
  },
  myButton: {
    backgroundColor: 'green', // Simple background color
    padding: 12,              // Padding around text inside button
    borderRadius: 5,          // Rounded corners
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

### What was updated:
1. **Single-File Setup for Expo Snack**: Placed `getMessage()` directly inside `App.js` above the main component. This allows you to run the code immediately on Expo Snack without having to create a separate `messages.js` file in the sidebar.
2. **Preserved Code & Layout**: All your component layout, state handlers, inline styling, `StyleSheet` definitions, and student notes/comments remain untouched.
