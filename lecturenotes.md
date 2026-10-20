# 📱 Mobile App Development — Comprehensive Lecture Notes (Weeks 1–6)
*Course Reference: Mobile App Development (based on syllabus & lectures from W1 to W6)*  
*Student Notes & Key Concept Summaries — 100% English Reference*

---

## 📑 Table of Contents
1. [Weeks 1 & 2: JavaScript Fundamentals for Mobile & Web Development](#weeks-1--2-javascript-fundamentals-for-mobile--web-development)
2. [Week 3: React Fundamentals & Component Architecture](#week-3-react-fundamentals--component-architecture)
3. [Week 4: Introduction to Mobile Development with React Native & Expo](#week-4-introduction-to-mobile-development-with-react-native--expo)
4. [Weeks 5 & 6: Core React Native Mobile UI Components & Layouts](#weeks-5--6-core-react-native-mobile-ui-components--layouts)

---

## Weeks 1 & 2: JavaScript Fundamentals for Mobile & Web Development

### 1. JavaScript Runtime & Execution Environments
- **Browser vs. Standalone (Node.js):**
  - In web applications, JavaScript executes inside the browser's engine (V8, SpiderMonkey, JavaScriptCore) with access to DOM (`document`), Browser APIs (`window`, `localStorage`, `fetch`).
  - In standalone / backend or mobile bundlers (like Metro bundler in React Native), JavaScript executes on Node.js / Hermes without a browser DOM.

### 2. Variables & Scoping (`var` vs. `let` vs. `const`)
- **`var`:** Function-scoped, hoisted to the top of its scope and initialized with `undefined`. Can be re-declared and updated. (Deprecated in modern code).
- **`let`:** Block-scoped `{ ... }`. Can be updated but not re-declared within the same scope. Subject to the *Temporal Dead Zone (TDZ)* before declaration.
- **`const`:** Block-scoped `{ ... }`. Cannot be re-assigned or re-declared. For objects and arrays, the reference binding is immutable, but the internal properties/elements can still be mutated.

### 3. Data Types & Operators
- **Primitive Types:** `string`, `number`, `boolean`, `null`, `undefined`, `symbol`, `bigint`.
- **Reference Types:** `Object`, `Array`, `Function`, `Date`, `Map`, `Set`.
- **Strict Equality (`===`) vs Loose Equality (`==`):**
  - Always use `===` (strict equality) to prevent implicit type coercion.
- **Modern Operators:**
  - **Ternary Operator:** `condition ? exprIfTrue : exprIfFalse`
  - **Nullish Coalescing (`??`):** Returns the right-hand operand when left operand is `null` or `undefined` (unlike `||`, it does not treat `0` or `""` as falsy).
  - **Optional Chaining (`?.`):** Safely reads nested object properties without throwing a `TypeError` if a reference is nullish (`user?.profile?.avatar`).

### 4. Functions & Arrow Functions
- **Function Declarations:** `function greet(name) { return "Hello " + name; }` (hoisted).
- **Arrow Functions (ES6):** `const greet = (name) => `Hello ${name}`;`
  - Concise syntax with implicit returns for single expressions.
  - Lexical `this`: Arrow functions do not bind their own `this`; they inherit `this` from the enclosing lexical context.

### 5. High-Order Array Iteration Methods
- Modern mobile & React development relies heavily on functional, immutable array operations:
  - `.map()`: Transforms every element into a new array. (Heavily used in rendering JSX lists).
  - `.filter()`: Returns a new array with elements that pass a test condition.
  - `.reduce()`: Accumulates array values into a single result (e.g., sum, object mapping).
  - `.find()` / `.findIndex()`: Returns the first element or index that matches a predicate.
  - `.forEach()`: Executes a side-effect for each item without returning a new array.

### 6. ES6 Modules (`import` / `export`)
- **Named Exports:** `export const PI = 3.14; export function add(a, b) { ... }`
  - Imported as: `import { PI, add } from './mathUtils';`
- **Default Exports:** `export default function App() { ... }`
  - Imported as: `import App from './App';`

---

## Week 3: React Fundamentals & Component Architecture

### 1. Component-Based Architecture
- Applications are composed of small, independent, and reusable building blocks called **Components**.
- React adheres to a **Unidirectional Data Flow**: Data flows downwards from parent to child components via `props`.

### 2. JSX (JavaScript XML)
- A syntactic extension that allows writing HTML-like structure directly inside JavaScript files.
- **Rules of JSX:**
  - Must return a single root element (or use React Fragments `<> ... </>`).
  - All tags must be explicitly closed (`<img />`, `<br />`, `<input />`).
  - Use camelCase for attributes (e.g., `className` instead of `class`, `htmlFor` instead of `for`, `onClick` instead of `onclick`).
  - Dynamic JavaScript expressions are embedded using `{curly braces}`.

### 3. Components: Functional vs. Class Components
- Modern React exclusively favors **Functional Components** using Hooks:
  ```jsx
  export default function UserCard({ name, role }) {
    return (
      <div className="card">
        <h3>{name}</h3>
        <p>{role}</p>
      </div>
    );
  }
  ```

### 4. Props (Properties)
- Arguments passed into components to configure their behavior and appearance.
- **Immutable:** A component must never mutate its own props (props are read-only).
- **Prop Destructuring:** Unpacking properties directly in the function parameter list: `({ title, count = 0 })`.

### 5. State Management (`useState`)
- Represents internal, mutable component memory that triggers a re-render when modified.
- **Rules of State:**
  - Never mutate state directly (e.g., `count = count + 1` is illegal).
  - Always use the setter function: `setCount(prev => prev + 1)`.
  - State updates are asynchronous and batched for performance.

### 6. Side Effects (`useEffect`)
- Handles operations that interact outside the React rendering pipeline (API fetching, event listeners, timers).
  - `useEffect(() => { ... }, [])`: Runs once when component mounts (empty dependency array).
  - `useEffect(() => { ... }, [value])`: Runs on mount and whenever `value` changes.
  - Cleanup function: Returning a function from `useEffect` cleans up subscriptions/timers when unmounting.

### 7. List Rendering & The `key` Prop
- Lists are rendered using `.map()`:
  ```jsx
  <ul>
    {items.map(item => (
      <li key={item.id}>{item.title}</li>
    ))}
  </ul>
  ```
- **Why `key` matters:** React uses the unique key to track which items have changed, been added, or been removed during reconciliation. Never use array indices as keys if items can be reordered or filtered.

### 8. Forms & Controlled Components
- Form inputs have their current value bound to React state and updated via `onChange`:
  ```jsx
  const [email, setEmail] = useState("");
  <input value={email} onChange={(e) => setEmail(e.target.value)} />
  ```

---

## Week 4: Introduction to Mobile Development with React Native & Expo

### 1. What is React Native?
- An open-source framework created by Meta that allows building native mobile apps for iOS and Android using React and JavaScript.
- Unlike WebView-based hybrid apps (which render inside an embedded web browser), React Native renders real **Native platform widgets** (such as `UIView` on iOS and `android.view.View` on Android).

### 2. Architecture & The Bridge
- **JavaScript Thread:** Where your business logic, state changes, and React application code run.
- **Native Thread (Main / UI Thread):** Responsible for native platform rendering and handling touch gestures.
- **The Bridge / JSI (JavaScript Interface):** The communication layer that transmits serialized commands between the JavaScript engine and the native platform.

### 3. Toolchains: Expo vs. Bare React Native CLI
- **Expo Framework (Managed Workflow):**
  - Provides a pre-configured native runtime with ready-to-use APIs (Camera, Location, Notifications).
  - Enables rapid development with **Expo Go** without requiring Xcode (macOS) or Android Studio initially.
  - Handles cross-platform assets, app icon generation, and cloud builds (EAS Build).
- **Bare React Native CLI:**
  - Direct access to native iOS (`/ios`) and Android (`/android`) folders.
  - Necessary when writing custom C++ or Objective-C/Java native modules that require deep OS integration.

### 4. Transition from Web (HTML) to Mobile (React Native)
| Web (HTML/DOM) | React Native (Mobile Primitives) | Description |
| :--- | :--- | :--- |
| `<div>` | `<View>` | Fundamental container box with Flexbox layout |
| `<p>`, `<span>`, `<h1>` | `<Text>` | Typography wrapper (raw strings cannot exist outside `<Text>`) |
| `<input type="text">` | `<TextInput>` | Keyboard input field |
| `<img>` | `<Image>` | Displays local or remote network images |
| `<button>` | `<TouchableOpacity>` / `<Pressable>` | Touch response container with press feedback |
| `<ul>`, `<ol>` | `<FlatList>` / `<ScrollView>` | Scrollable lists and virtualized data feeds |

### 5. Styling in React Native
- Styles are defined using JavaScript objects via `StyleSheet.create({ ... })`.
- **Key Differences from Web CSS:**
  - No CSS selectors (classes, IDs, tags). Styles are passed as props: `style={styles.container}`.
  - Flexbox is enabled by default on all `<View>` elements.
  - Default `flexDirection` is `'column'` (unlike Web CSS where default is `'row'`).
  - Dimensions are unitless numbers representing device-independent pixels (dp).

---

## Weeks 5 & 6: Core React Native Mobile UI Components & Layouts

### 1. `<View>` Component
- The fundamental layout container equivalent to `<div>`.
- Supports Flexbox properties: `flex`, `flexDirection`, `justifyContent`, `alignItems`, `padding`, `margin`, `backgroundColor`, `borderRadius`.

### 2. `<Text>` Component
- Used for all typography.
- **Critical Rule:** In React Native, text strings cannot be placed directly inside a `<View>`; they must always be enclosed in a `<Text>` component.
- Supports text nesting for inline styles (e.g., bolding specific words).

### 3. `<TextInput>` Component
- Captures user keystrokes.
- **Key Props:**
  - `value`: Controlled text state.
  - `onChangeText`: Callback providing the updated text directly as a string (unlike web which passes an event object).
  - `placeholder`: Placeholder text.
  - `keyboardType`: `'default'`, `'email-address'`, `'numeric'`, `'phone-pad'`.
  - `secureTextEntry`: `true` for password masking.

### 4. `<Image>` Component
- **Local Asset:** Loaded via Node `require`:
  ```jsx
  <Image source={require('./assets/avatar.png')} style={{ width: 60, height: 60 }} />
  ```
- **Remote Network Image:** Must specify explicit width and height:
  ```jsx
  <Image source={{ uri: 'https://example.com/photo.png' }} style={{ width: 100, height: 100 }} />
  ```
- `resizeMode`: `'cover'`, `'contain'`, `'stretch'`, `'center'`.

### 5. Scrolling: `<ScrollView>` vs. `<FlatList>`
- **`<ScrollView>`:**
  - Renders all child elements immediately into memory upon loading.
  - Best for static pages, settings screens, or bounded content that fits within a few screen heights.
- **`<FlatList>` (High Performance Virtualized List):**
  - Only renders visible items on the screen plus a small offscreen buffer. Recycles views as the user scrolls.
  - Essential for dynamic, long, or unbounded data feeds.
  - **Required Props:**
    - `data`: Array of objects to render.
    - `renderItem`: Function returning JSX for an item: `({ item }) => <Card title={item.title} />`.
    - `keyExtractor`: Function returning a unique string key: `(item) => item.id.toString()`.

### 6. Interactive Touchables: `<TouchableOpacity>` vs `<Button>`
- **`<Button>`:** Simple, native-looking button with limited styling options (title and color prop only).
- **`<TouchableOpacity>`:** A wrapper that dims its child component's opacity when pressed, giving instant tactile visual feedback.
  - Accepts `onPress` callback.
  - Highly customizable with custom layout, icons, and text inside.

### 7. Form Selection Components
- **`<Checkbox>`:** Toggles a boolean value on press.
- **`<RadioButton>`:** Represents single-choice selection among mutually exclusive options.
- **`<Picker>`:** Platform-native dropdown menu or iOS wheel selector for picking an option from a list.

### 8. `<SafeAreaView>`
- Automatically applies padding to avoid device hardware constraints, including:
  - Top status bar and camera cutouts / Dynamic Island.
  - Bottom rounded corners and home indicator bar on modern iOS/Android devices.
- Ensures critical UI content is never obscured by device bezels.

---
*End of Lecture Notes (Weeks 1 to 6). Use `lecturecodes.md` to submit code requests, prompts, and practice exercises.*
