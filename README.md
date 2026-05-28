# 🎬 MorseFlix Pro — Interactive Morse Code Translator & Synthesizer

**MorseFlix Pro** is a high-fidelity, single-page web application that converts standard English text to international Morse code (and vice-versa) in real-time. Designed with a premium, glassmorphic Netflix-inspired dark theme, it leverages advanced browser APIs to synthesize audio and generate downloadable audio files directly in the browser.

🚀 **Live Demo:** [Deploy your live link here using GitHub Pages]

---

## ✨ Features

### 1. ⚡ Real-Time Auto-Translation
* **Zero-Click Conversion:** Automatically detects whether you are typing standard English or Morse code (`.` and `-`), translating your input instantly as you type.
* **Smart Detection:** Dynamic status badge indicating current input format (Text vs. Morse).

### 🎹 2. Web Audio API Synthesizer Deck
* **WPM Speed Control:** Adjust playback speed from **10 WPM to 45 WPM** using an interactive slider.
* **Pitch Control:** Set the oscillator frequency from **300 Hz to 1000 Hz** to customize the audio tone.
* **Volume Slider:** Adjust the output gain envelope smoothly to prevent click sounds during playback.
* **Dynamic LED Sync:** A virtual glowing LED indicator flashes in millisecond-perfect sync with audio dots and dashes.

### 💾 3. WAV Audio File Exporter
* **Offline File Generation:** Renders the customized Morse code audio sequence using an `OfflineAudioContext` and dynamically packages it into a standard **16-bit PCM WAV file** for local download.

### 📝 4. LocalStorage History Logs
* **Session Persistence:** Saves your translations to a log panel backed by `LocalStorage` so your entries persist across browser reloads.

### 📖 5. Search-Filterable Cheat Sheet
* **Interactive Chart:** A responsive card grid displaying character mappings, filterable by letters, numbers, and punctuation marks.

---

## 🛠️ Tech Stack & APIs Used
* **Frontend:** Semantic HTML5, Vanilla CSS3 (Custom variables, glassmorphic filters).
* **Animations:** GSAP (GreenSock Animation Platform) for loading layouts and toast slide-ins.
* **Audio Engine:** Browser **Web Audio API** (`OscillatorNode`, `GainNode`, `OfflineAudioContext`).
* **Storage:** Browser **Web Storage API** (`LocalStorage`).
* **Icons:** FontAwesome v6.

---

## 🚀 How to Run the Project Locally
No servers, compilers, or command-line dependencies are required!

1. Clone this repository to your machine:
   ```bash
   git clone https://github.com/Sarvesh0508/Morse-Code-Translator.git
   ```
2. Double-click the **`index.html`** file to open it in Google Chrome, Microsoft Edge, or Opera.

---

## 📦 Creating a Deployment Release Package
To create a clean release package for manual distribution, run the following command in your terminal to package only the production files into a ZIP archive:

```bash
# Using tar (cross-platform)
tar -a -c -f morse_code_translator.zip index.html README.md
```

This creates a clean **`morse_code_translator.zip`** file ready to be attached to your **GitHub Releases** page.
