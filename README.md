# 🛡️ AI Content Moderator

[![Python](https://img.shields.io/badge/Python-3.8%2B-blue)](https://python.org)
[![Flask](https://img.shields.io/badge/Flask-2.3.3-green)](https://flask.palletsprojects.com/)
[![License](https://img.shields.io/badge/License-MIT-yellow)](LICENSE)

A real-time AI-powered content moderation system that detects harmful and inappropriate text content. Built based on patent research in automated content moderation and misinformation detection.

## ✨ Features

- **Real-time Text Analysis**: Instantly analyzes text for harmful content
- **Pattern-Based Detection**: Uses advanced regex patterns to identify toxic language
- **Risk Assessment**: Classifies content as SAFE or UNSAFE with confidence scores
- **Web Interface**: User-friendly Flask web application
- **Customizable Rules**: Easily extendable harmful pattern database

## 🎯 Demo

### Safe Content Detection
![Safe Content](demo-safe.jpg)

### Unsafe Content Detection  
![Unsafe Content](demo-unsafe.jpg)

## 🛠️ Technologies Used

- **Backend**: Python, Flask
- **AI/ML**: Custom pattern-based classification system
- **Frontend**: HTML5, CSS3, JavaScript
- **Text Processing**: Regular Expressions, Natural Language Processing concepts

## 📦 Installation

### Prerequisites
- Python 3.8 or higher
- pip package manager

### Setup
```bash
# Clone the repository
git clone https://github.com/samraiqbal-aiml/ai-content-moderation.git
cd ai-content-moderation

# Install dependencies
pip install flask

# Run the application
python app.py
