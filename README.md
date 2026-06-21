<div align="center">

# 📚 Insightify

### AI-powered study companion for lecture analysis and smart revision

Transform YouTube lectures and study notes into concise summaries, revision material, viva questions, and practice MCQs in seconds.

</div>

---

## Overview

Insightify is a full-stack AI application designed to help students learn more efficiently from long-form educational content.

Students often spend significant time revisiting lecture videos, reading lengthy notes, and preparing revision material before examinations. Insightify streamlines this process by automatically extracting key information and generating structured study resources using Large Language Models.

The platform supports both YouTube lecture analysis and direct note summarization, making it useful for self-learning, revision, and exam preparation.

---

## Key Features

### 🎥 YouTube Lecture Analysis

Paste a YouTube lecture URL and automatically generate:

* Lecture Summary
* Key Concepts
* Revision Notes
* Viva Questions
* Practice MCQs

### 📝 Notes Summarizer

Convert lengthy study material into:

* Concise Summaries
* Important Topics
* Revision-Friendly Notes
* Viva Preparation Questions
* Multiple Choice Questions

### 🤖 AI-Powered Processing

Leverages modern LLM capabilities through Groq to transform unstructured educational content into actionable learning resources.

### 🌙 Modern User Experience

* Clean interface
* Responsive layout
* Dark / Light mode support
* Fast processing workflow

---

## System Architecture

```text
YouTube URL / Study Notes
            │
            ▼
      Content Extraction
            │
            ▼
      Groq AI Processing
            │
            ▼
 ┌───────────────────────┐
 │ Summary               │
 │ Key Concepts          │
 │ Revision Notes        │
 │ Viva Questions        │
 │ Practice MCQs         │
 └───────────────────────┘
```

---

## Tech Stack

### Frontend

* HTML5
* CSS3
* JavaScript

### Backend

* Flask

### AI & APIs

* Groq API
* Llama 3.3 70B Versatile
* YouTube Transcript API

### Development Tools

* Git
* GitHub
* Render

---

## Project Structure

```text
Insightify
│
├── app.py
├── requirements.txt
│
├── templates
│   └── index.html
│
├── static
│   ├── style.css
│   └── script.js
│
└── services
    ├── groq_service.py
    └── youtube_service.py
```

---

## Installation

### Clone Repository

```bash
git clone <repository-url>
cd Insightify
```

### Create Virtual Environment

```bash
python3 -m venv venv
source venv/bin/activate
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Configure Environment Variables

```env
GROQ_API_KEY=your_api_key
```

### Run Application

```bash
python3 app.py
```

Open:

```text
http://127.0.0.1:5000
```

---

## Challenges Solved

* Processing long-form educational content efficiently
* Extracting structured learning material from unstructured text
* Integrating external AI services into a web application
* Building a responsive frontend without heavy frameworks
* Managing transcript extraction and AI prompt workflows

---

## What I Learned

Through this project I gained hands-on experience with:

* Full Stack Development
* RESTful API Design
* Flask Backend Development
* AI API Integration
* Prompt Engineering
* Frontend Development
* Client-Server Communication
* Working with External APIs
* Deployment Workflows

---

## Future Enhancements

* PDF Upload Support
* DOCX Upload Support
* Flashcard Generation
* Study Planner Integration
* Chat with Notes
* Export as PDF
* Multi-language Support

---

## Author

Built to explore the intersection of AI and education by creating practical tools that help students study more effectively.
