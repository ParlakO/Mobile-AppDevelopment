(bak buraya alt tarafa checkbox ekle aynı kod temasında ve radıo button ekle sorular sorup )import { useState } from 'react';
import { Button, SafeAreaView, Text, TextInput, View } from 'react-native';

export default function SumCalculator() {
  const [first, setFirst] = useState('');
  const [second, setSecond] = useState('');
  const [result, setResult] = useState(null);

  const handleSum = () => {
    const total = Number(first) + Number(second);
    setResult(Number.isFinite(total) ? total : null);
  };

  return (
    <SafeAreaView style={{ flex: 1, backgroundColor: '#f8fafc' }}>
      <View
        style={{
          flex: 1,
          justifyContent: 'center',
          padding: 24,
          gap: 16,
        }}
      >
        <Text style={{ fontSize: 20, fontWeight: '600', color: '#0f172a' }}>
          Add two numbers
        </Text>
        <View
          style={{
            borderRadius: 16,
            backgroundColor: '#fff',
            padding: 20,
            gap: 16,
            shadowColor: '#000',
            shadowOpacity: 0.05,
            shadowRadius: 12,
            elevation: 2,
          }}
        >
          <TextInput
            placeholder="First number"
            keyboardType="numeric"
            value={first}
            onChangeText={setFirst}
            style={{
              borderWidth: 1,
              borderColor: '#d4d4d8',
              borderRadius: 10,
              paddingHorizontal: 12,
              paddingVertical: 12,
            }}
          />
          <TextInput
            placeholder="Second number"
            keyboardType="numeric"
            value={second}
            onChangeText={setSecond}
            style={{
              borderWidth: 1,
              borderColor: '#d4d4d8',
              borderRadius: 10,
              paddingHorizontal: 12,
              paddingVertical: 12,
            }}
          />
          <Button title="Calculate sum" onPress={handleSum} />
          <View>
            <Text style={{ color: '#475569' }}>Result:</Text>
            <Text style={{ fontSize: 24, fontWeight: '700', color: '#2563eb' }}>
              {result === null ? 'Enter two valid numbers' : result}
            </Text>
          </View>
        </View>
      </View>
    </SafeAreaView>
  );
}
