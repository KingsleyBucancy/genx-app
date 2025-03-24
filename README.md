# 🧠 GenX — Voice-to-App AI Builder

**GenX** is an AI-powered tool that transforms voice input into working web applications using GPT-4. Just say an idea like "Build a task manager" — and GenX will generate and preview a functional React app instantly.

---

## 📦 Tech Stack

### 🎨 Frontend
- React + Vite
- TypeScript
- TailwindCSS
- Sandpack (for live React preview)
- Web Speech API (voice input)

### 🧠 Backend
- FastAPI (Python)
- OpenAI GPT-4 (via API)
- Pydantic (request validation)
- CORS
- dotenv (environment management)

---

## 📁 Project Structure

---

## 🚀 Local Development

### 1️⃣ Backend Setup (FastAPI + OpenAI)

```bash
cd Backend
python3 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
pip install -r requirements.txt
```

> Create a `.env` file in `/Backend`:

```env
OPENAI_API_KEY=sk-xxxxxxxxxxxxxxxxxxxxxxxxxxxx
```

> Start the server:

```bash
uvicorn main:app --reload --port 8000
```

Backend will be live at: `http://localhost:8000`

---

### 2️⃣ Frontend Setup (React + Vite)

```bash
cd Frontend
npm install
```

> Create a `.env` file in `/Frontend`:

```env
VITE_API_URL=http://localhost:8000
```

> Start the dev server:

```bash
npm run dev
```

Frontend will be live at: `http://localhost:5173`

---

### 🧪 How to Use Locally

1. Visit `http://localhost:5173`
2. Click the microphone button to speak an app idea
3. A transcript of your voice is captured
4. Click "Start Your Project"
5. The app sends your idea to the backend
6. The backend sends it to GPT-4 and receives working React code
7. The generated app is displayed live using Sandpack

---

## 🧠 How It Works

1. **Voice-to-Text**: Uses Web Speech API to transcribe your spoken idea
2. **Prompt Builder**: Backend formats your idea into a structured GPT-4 prompt
3. **AI Generation**: GPT-4 returns working React code
4. **Live Preview**: Sandpack renders the generated app in real-time

---

## 📋 Features

- 🎙️ Voice-powered input
- 🧠 GPT-4 powered app generation
- ⚛️ Real-time React preview via Sandpack
- ✍️ Prompt abstraction via `prompt_builder.py`
- ⚙️ Clean modular FastAPI backend
- 🔐 `.env` support for API key security

---

## 🛠 To-Do / Future Ideas

- ✅ Basic React app generation
- ✅ Voice input support
- ✅ Live code rendering
- ⏳ Backend app generation (Node.js / Flask)
- ⏳ Code export/download as zip
- ⏳ Multi-component app support
- ⏳ User login & workspace saving
- ⏳ Dark/light theme toggle

---

## 🤝 Contributing

Contributions are welcome!  
Feel free to fork the repo, open issues, or submit pull requests.

