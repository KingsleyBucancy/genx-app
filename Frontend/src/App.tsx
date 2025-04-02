import { useState } from 'react';
import { Mic, MicOff, Sparkles, ArrowRight, Cpu, BrainCircuit } from 'lucide-react';
import { Sandpack } from "@codesandbox/sandpack-react";



function App() {
  const [isListening, setIsListening] = useState(false);
  const [transcript, setTranscript] = useState('');
  const [code, setCode] = useState('');
  
  
  const generateCode = async () => {
    const response = await fetch(`${import.meta.env.VITE_API_URL}/generate_code`,  {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ idea: transcript })
    });
  
    const data = await response.json();
    setCode(data.code);
  };
  
// Speech recognition setup
  const startListening = () => {
    if ('webkitSpeechRecognition' in window) {
      const recognition = new (window as any).webkitSpeechRecognition();
      recognition.continuous = false;
      recognition.interimResults = false;

      recognition.onstart = () => {
        setIsListening(true);
      };

      recognition.onresult = (event: any) => {
        const transcript = event.results[0][0].transcript;
        setTranscript(transcript);
      };

      recognition.onend = () => {
        setIsListening(false);
      };

      recognition.start();
    } else {
      alert('Speech recognition is not supported in this browser.');
    }
  };



  return (
    <div className="min-h-screen bg-gradient-to-br from-gray-900 to-black text-white">
      {/* Navigation */}
      <nav className="border-b border-gray-800">
        <div className="container mx-auto px-4 py-4">
          <div className="flex items-center justify-between">
            <div className="flex items-center gap-2">
              <div className="relative">
                <Cpu className="w-8 h-8 text-blue-400 absolute" />
                <BrainCircuit className="w-8 h-8 text-purple-400 opacity-75 animate-pulse" />
              </div>
              <span className="text-2xl font-bold bg-clip-text text-transparent bg-gradient-to-r from-blue-400 to-purple-600">
                GenX
              </span>
            </div>
            <button className="px-4 py-2 rounded-lg bg-gray-800 hover:bg-gray-700 transition-colors">
              Sign In
            </button>
          </div>
        </div>
      </nav>

      {/* Hero Section */}
      <div className="container mx-auto px-4 py-16">
        <div className="max-w-4xl mx-auto text-center">
          <h1 className="text-5xl md:text-7xl font-bold mb-8 bg-clip-text text-transparent bg-gradient-to-r from-blue-400 to-purple-600">
            BUILD YOUR STARTUP WITH AI
          </h1>
          <p className="text-xl text-gray-300 mb-12">
            Transform your ideas into reality with GenX AI - Your intelligent startup companion
          </p>
          
          {/* Voice Input Section */}
          <div className="bg-gray-800/50 backdrop-blur-lg rounded-2xl p-8 mb-12 shadow-xl">
            <div className="flex flex-col items-center gap-6">
              <button
                onClick={startListening}
                className={`p-6 rounded-full transition-all duration-300 ${
                  isListening 
                    ? 'bg-purple-600 animate-pulse'
                    : 'bg-blue-600 hover:bg-blue-700'
                }`}
              >
                {isListening ? (
                  <Mic className="w-8 h-8" />
                ) : (
                  <MicOff className="w-8 h-8" />
                )}
              </button>
              <p className="text-lg">
                {isListening 
                  ? "I'm listening... Speak now"
                  : "Tap the microphone to start"}
              </p>
              {transcript && (
                <div className="w-full bg-gray-700/50 rounded-lg p-4 mt-4">
                  <p className="text-gray-300">{transcript}</p>
                </div>
              )}
            </div>
          </div>

          {/* CTA Button */}
          <button
           onClick={generateCode}
           className="bg-gradient-to-r from-blue-600 to-purple-600 text-white px-8 py-4 rounded-full text-lg font-semibold flex items-center gap-2 mx-auto hover:shadow-lg hover:scale-105 transition-all duration-300">
            Start Your Project <ArrowRight className="w-5 h-5" />
            </button>
            {code && (
            <div className="mt-12">
              <h2 className="text-xl font-bold text-purple-400 mb-4">Live Preview:</h2>
              <div className="rounded-xl overflow-hidden border border-gray-700 shadow-lg">
                <Sandpack
                template="react"
                files={{
                  "/App.js": code,
                }}
                options={{
                  showNavigator: true,
                  showTabs: true,
                  showLineNumbers: true,
                  wrapContent: true,
                }}
                />
                </div>
                </div>
                )}
              </div>

        {/* Features Grid */}
        <div className="grid md:grid-cols-3 gap-8 mt-24">
          <div className="bg-gray-800/30 rounded-xl p-6">
            <Sparkles className="w-12 h-12 text-blue-400 mb-4" />
            <h3 className="text-xl font-semibold mb-2">AI-Powered Insights</h3>
            <p className="text-gray-400">Get intelligent recommendations and insights for your startup journey</p>
          </div>
          <div className="bg-gray-800/30 rounded-xl p-6">
            <Mic className="w-12 h-12 text-purple-400 mb-4" />
            <h3 className="text-xl font-semibold mb-2">Voice Commands</h3>
            <p className="text-gray-400">Natural interaction with advanced voice recognition technology</p>
          </div>
          <div className="bg-gray-800/30 rounded-xl p-6">
            <ArrowRight className="w-12 h-12 text-green-400 mb-4" />
            <h3 className="text-xl font-semibold mb-2">Guided Workflow</h3>
            <p className="text-gray-400">Step-by-step assistance to bring your vision to life</p>
          </div>
        </div>
      </div>
    </div>
  );
}

export default App;
