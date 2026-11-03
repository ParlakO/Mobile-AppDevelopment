// messages.js

// Requirement C: Function that returns a string and is exported
export function getMessage() {
  return "Hello from external JS";
}










import React, { useState } from 'react';
import { StyleSheet, Text, View, TouchableOpacity, SafeAreaView } from 'react-native';

// Requirement C: Import the getMessage function from messages.js
import { getMessage } from './messages';

export default function App() {
  // State to store the message when button is clicked
  const [displayedMessage, setDisplayedMessage] = useState('');

  // Requirement D: Function to handle button press
  const handlePress = () => {
    const msg = getMessage(); // Call external function
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
}); expo snackde çalışsın english

---

### 🤖 Gemini Response (2026-11-03 08:29:23 UTC)

Hi there! Your code is already structured very well and meets all your requirements. 

To run this in **Expo Snack** (snack.expo.dev), you need to create two separate files in the Snack sidebar because your code imports a function from an external file (`messages.js`).

---

### 🛠️ How to set this up in Expo Snack:

1. Open [snack.expo.dev](https://snack.expo.dev).
2. On the **left sidebar** under the "Files" tab, click the **+ (Plus icon)** to create a new file and name it:  
   `messages.js`
3. Paste the **`messages.js`** code below into that new file.
4. Click back on **`App.js`** in the sidebar and paste the **`App.js`** code below into it.

---

### 📄 File 1: `messages.js`

```javascript
// messages.js

// Requirement C: Function that returns a string and is exported
export function getMessage() {
  return "Hello from external JS";
}
```

---

### 📄 File 2: `App.js`

```javascript
import React, { useState } from 'react';
import { StyleSheet, Text, View, TouchableOpacity, SafeAreaView } from 'react-native';

// Requirement C: Import the getMessage function from messages.js
import { getMessage } from './messages';

export default function App() {
  // State to store the message when button is clicked
  const [displayedMessage, setDisplayedMessage] = useState('');

  // Requirement D: Function to handle button press
  const handlePress = () => {
    const msg = getMessage(); // Call external function
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

### 💡 What this code does:
1. **`messages.js`**: Exports a helper function named `getMessage()` that returns a simple string (`"Hello from external JS"`).
2. **`App.js`**:
   * Imports `getMessage` from `./messages`.
   * Sets up a state variable `displayedMessage` using `useState('')`.
   * When you tap the **"Click Me"** button, `handlePress` calls `getMessage()` and updates the state.
   * Re-renders the screen to display the updated text dynamically!
