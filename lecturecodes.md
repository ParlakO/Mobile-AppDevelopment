create a simple react app that displayts a welcome message and a button 
a: display the text "welcome to {your name} " usıng a text component apply inline styling to make the text blue bold and 24 pixels
b:create a button labeled click me using touchable opacity define its background color padding and border radius using stylesheet.create()
c:create an external js file named mesaages.js containing a function called getmessage() that returns the string hello from external js export this function and import into app.js 
d:when the user presses the click me button call the imported getmessage function and display the returned message on the screen

make it so easy and start level easy looking

---

### 🤖 Gemini Response (2026-11-03 08:27:04 UTC)

Hello! Here is a simple, beginner-friendly solution designed for your React Native lab work on Expo Snack.

Since Expo Snack allows you to create multiple files, we will create two files: `messages.js` and `App.js`.

---

### File 1: `messages.js`
*Create a new file named `messages.js` in Expo Snack (click the `+` icon next to files) and paste this code:*

```javascript
// messages.js

// Requirement C: Function that returns a string and is exported
export function getMessage() {
  return "Hello from external JS";
}
```

---

### File 2: `App.js`
*Paste this code into your main `App.js` file:*

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

### Explanation of How It Works:

1. **Requirement A (Inline Styling)**: We styled the `<Text>` directly using `style={{ color: 'blue', fontWeight: 'bold', fontSize: 24 }}` without using `StyleSheet`. Replace `"Alex"` with your own name!
2. **Requirement B (TouchableOpacity & StyleSheet)**: We created a button using `TouchableOpacity`. Its design (`backgroundColor`, `padding`, and `borderRadius`) is managed inside `StyleSheet.create()`.
3. **Requirement C (External File)**: `messages.js` contains `getMessage()`. We export it from `messages.js` and import it at the top of `App.js` using `import { getMessage } from './messages';`.
4. **Requirement D (Button Action)**: When the user presses the button, `handlePress` calls `getMessage()` and updates `displayedMessage` using React's `useState` hook, rendering the message on the screen.
