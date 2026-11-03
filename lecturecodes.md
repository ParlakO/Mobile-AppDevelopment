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
