explain the difference between props and state in react native describe how each is used in a component q1 bu 2 cümle cevap ver explain the difference between scrollview and flatlist in react native in which situations u prefer which one cok kısa ingilkizce cevaplar

---

### 🤖 Gemini Response (2026-11-03 08:03:48 UTC)

Here are the short and clear answers for your questions:

---

### **Question 1: Props vs State**
**Props** are read-only parameters passed down from a parent component to configure a child, while **State** is local data managed within a component that can change over time. In a component, props are used to display external data passed into it, whereas state is used to track interactive data like form inputs or toggle switches.

---

### **Question 2: ScrollView vs FlatList**
* **Difference:** `ScrollView` renders all its child components at once, while `FlatList` renders items lazily (only rendering what is currently visible on the screen).
* **When to use:**
  * Use **`ScrollView`** for small, fixed layouts with a known amount of content (like a settings page or a short form).
  * Use **`FlatList`** for long or dynamic lists of data (like a social media feed or product list) to keep your app fast and save memory.
