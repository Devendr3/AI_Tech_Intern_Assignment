
# Task 1: Iron Lady Chatbot

A simple FAQ chatbot for Iron Lady Leadership Programs built with web technologies.

## 🛠️ Tech Stack Used

- **HTML5** - Page structure and content
- **CSS3** - Styling and layout
- **JavaScript** - Chatbot functionality and user interactions
- **No frameworks** - Built with pure web technologies

## 🚀 How to Run the Code

**Step 1:** Download the files
- Save `chatbot.html` to your computer

**Step 2:** Open in browser
- Double-click `chatbot.html` file
- It will open in your default web browser
- Start chatting immediately!

**Alternative:** For local development
```bash
# If you have Python installed
python -m http.server 8000
# Then open http://localhost:8000 in browser
```

## ✨ Features Implemented

### Required FAQ Topics:
- ✅ What programs does Iron Lady offer?
- ✅ What is the program duration?
- ✅ Is the program online or offline?
- ✅ Are certificates provided?
- ✅ Who are the mentors/coaches?

### Additional Features:
- Interactive chat interface
- Quick question buttons
- Keyword-based response matching
- Mobile-responsive design
- Real-time message display
- Enter key support

## 💬 Sample Questions You Can Ask

- "What programs do you offer?"
- "How long are the courses?"
- "Do I get a certificate?"
- "Tell me about mentors"
- "Is it online or classroom?"

## 🎯 How It Works

1. User types question or clicks quick buttons
2. JavaScript checks for keywords in the message
3. Matches keywords to pre-defined answers
4. Displays appropriate response in chat
5. Fallback response for unrecognized questions

## 📁 Project Files

```
Task1_Chatbot/
├── chatbot.html    # Complete chatbot (HTML + CSS + JS)
└── README.md     # This file
```

## 🌐 Browser Support

Works on all modern browsers:
- Chrome ✅
- Firefox ✅ 
- Safari ✅
- Edge ✅

## 🔧 Code Structure

**HTML:** Basic chat interface with input field and message area
**CSS:** Simple styling with blue/green color scheme
**JavaScript:** 
- `answers` object stores all responses
- `getAnswer()` function matches user input to responses
- `sendMessage()` handles chat functionality

---

