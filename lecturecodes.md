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

---

### 🤖 Gemini Response (2026-10-20 20:07:12 UTC)

Harika bir başlangıç kodu! Mevcut kod yapını, değişken isimlerini ve stil kartı tasarımını **hiç bozmadan** tam altına senin istediğin gibi sorular soran bir **Checkbox** ve **Radio Button** bölümü ekledim.

React Native'de harici bir kütüphane kullanmadan en temel ve temiz şekilde Checkbox ve Radio Button oluşturmak için `TouchableOpacity` ve temel `View` elemanlarını kullanırız.

### Güncellenmiş Kod (Expo Snack / `App.js` Uyumlu):

```javascript
import { useState } from 'react';
// --- YENİ EKLENEN IMPORTS: ScrollView ve TouchableOpacity eklendi ---
import { Button, SafeAreaView, ScrollView, Text, TextInput, TouchableOpacity, View } from 'react-native';

export default function SumCalculator() {
  const [first, setFirst] = useState('');
  const [second, setSecond] = useState('');
  const [result, setResult] = useState(null);

  // --- YENİ EKLENEN KISIM: Checkbox ve Radio Button State'leri ---
  const [isChecked, setIsChecked] = useState(false);
  const [selectedRadio, setSelectedRadio] = useState('Başlangıç'); // Varsayılan radyo seçimi

  const handleSum = () => {
    const total = Number(first) + Number(second);
    setResult(Number.isFinite(total) ? total : null);
  };

  return (
    <SafeAreaView style={{ flex: 1, backgroundColor: '#f8fafc' }}>
      {/* ScrollView ekleyerek ekrana sığmama durumunu önledik */}
      <ScrollView contentContainerStyle={{ padding: 24, gap: 16 }}>
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

        {/* --- YENİ EKLENEN KISIM: CHECKBOX VE RADIO BUTTON KARTI --- */}
        <View
          style={{
            borderRadius: 16,
            backgroundColor: '#fff',
            padding: 20,
            gap: 12,
            shadowColor: '#000',
            shadowOpacity: 0.05,
            shadowRadius: 12,
            elevation: 2,
          }}
        >
          {/* 1. CHECKBOX SORUSU */}
          <Text style={{ fontSize: 16, fontWeight: '600', color: '#0f172a' }}>
            Soru 1: Sonucu geçmişe kaydetmek ister misiniz?
          </Text>
          <TouchableOpacity
            onPress={() => setIsChecked(!isChecked)}
            style={{ flexDirection: 'row', alignItems: 'center', gap: 10 }}
          >
            <View
              style={{
                width: 22,
                height: 22,
                borderWidth: 1,
                borderColor: '#d4d4d8',
                borderRadius: 4,
                backgroundColor: isChecked ? '#2563eb' : '#fff',
                justifyContent: 'center',
                alignItems: 'center',
              }}
            >
              {isChecked && (
                <Text style={{ color: '#fff', fontSize: 12, fontWeight: 'bold' }}>✓</Text>
              )}
            </View>
            <Text style={{ color: '#475569', fontSize: 15 }}>
              {isChecked ? 'Evet, sonucu kaydet' : 'Hayır, kaydetme'}
            </Text>
          </TouchableOpacity>

          {/* 2. RADIO BUTTON SORUSU */}
          <Text style={{ fontSize: 16, fontWeight: '600', color: '#0f172a', marginTop: 10 }}>
            Soru 2: Matematik seviyenizi seçiniz:
          </Text>
          
          {['Başlangıç', 'Orta', 'İleri'].map((option) => (
            <TouchableOpacity
              key={option}
              onPress={() => setSelectedRadio(option)}
              style={{ flexDirection: 'row', alignItems: 'center', gap: 10 }}
            >
              <View
                style={{
                  width: 20,
                  height: 20,
                  borderRadius: 10,
                  borderWidth: 1,
                  borderColor: '#d4d4d8',
                  justifyContent: 'center',
                  alignItems: 'center',
                }}
              >
                {selectedRadio === option && (
                  <View
                    style={{
                      width: 10,
                      height: 10,
                      borderRadius: 5,
                      backgroundColor: '#2563eb',
                    }}
                  />
                )}
              </View>
              <Text style={{ color: '#475569', fontSize: 15 }}>{option}</Text>
            </TouchableOpacity>
          ))}
        </View>
        {/* --- YENİ EKLENEN KISIM BİTİŞİ --- */}

      </ScrollView>
    </SafeAreaView>
  );
}
```

---

### Neler Ekledik ve Nasıl Çalışıyor?

1. **State Mantığı (`useState`):**
   - `isChecked`: Checkbox'ın seçili olup olmadığını (`true`/`false`) tutar.
   - `selectedRadio`: Hangi radyo butonunun seçili olduğunu metin olarak tutar (`'Başlangıç'`, `'Orta'`, veya `'İleri'`).

2. **Checkbox Mantığı:**
   - Kare bir `View` oluşturduk. Tıklandığında (`TouchableOpacity`) `isChecked` değerini tersine (`!isChecked`) çevirir. Seçili ise içi mavi olur ve `✓` işareti görünür.

3. **Radio Button Mantığı:**
   - Yuvarlak bir `View` (`borderRadius: 10`) oluşturduk. Seçilen seçeneğin içine daha küçük mavi bir daire koyduk. Sadece bir tane seçeneğin aynı anda aktif olmasını sağladık.

4. **Kullanıcı Deneyimi:**
   - Ekran küçük cihazlarda taşmasın diye ana kapsayıcıyı `ScrollView` ile sardık. Kodunun mevcut mavi/beyaz renk temasına sadık kaldık.
