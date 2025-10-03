# 🤖 GeminiAI - Advanced AI Applications Collection

A comprehensive collection of AI-powered applications built with Google's Gemini AI, featuring progressive complexity levels from basic chatbots to advanced document processing systems.

![Python](https://img.shields.io/badge/python-v3.8+-blue.svg)
![Streamlit](https://img.shields.io/badge/streamlit-latest-red.svg)
![Gemini AI](https://img.shields.io/badge/Gemini%20AI-2.0--flash--lite-green.svg)
![License](https://img.shields.io/badge/license-MIT-blue.svg)

## 📋 Table of Contents

- [Overview](#overview)
- [Features](#features)
- [Project Structure](#project-structure)
- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Usage](#usage)
- [Applications](#applications)
  - [Level 1: Basic AI Applications](#level-1-basic-ai-applications)
  - [Level 2: Interactive AI Tools](#level-2-interactive-ai-tools)
  - [Level 3: Advanced AI Systems](#level-3-advanced-ai-systems)
- [Configuration](#configuration)
- [Contributing](#contributing)
- [License](#license)

## 🌟 Overview

This repository contains a progressive collection of AI applications built using Google's Gemini AI model, organized in three complexity levels. Each level demonstrates different aspects of AI integration, from simple text generation to complex document analysis and database interactions.

## ✨ Features

- **🔥 Latest Gemini AI Integration**: Uses Google's Gemini 2.0 Flash Lite model
- **📱 User-Friendly Interface**: All applications built with Streamlit
- **📊 Progressive Complexity**: Three levels from beginner to advanced
- **🔒 Secure Configuration**: Environment variable-based API key management
- **📄 Multi-format Support**: PDF, image, and video transcript processing
- **💾 Database Integration**: SQL chatbot with database connectivity
- **🎯 Specialized Tools**: ATS resume analysis, nutrition tracking, and more

## 📁 Project Structure

```
GeminiAi/
├── 📄 README.md
├── 📄 requirements.txt
├── 🔧 .env
├── 🚫 .gitignore
├── 📁 level1/                    # Basic AI Applications
│   ├── 🤖 app.py                # Simple Q&A Chatbot
│   └── 🖼️ imageGen.py           # Image Analysis Tool
├── 📁 level2/                    # Interactive AI Tools
│   ├── 💬 qnaChat.py            # Enhanced Q&A with Memory
│   ├── 📄 invoiceChat.py        # Invoice Processing
│   ├── 🥗 Nutrient_Find.py      # Nutrition Analysis
│   └── 📺 YTtanscriber.py       # YouTube Transcript Summarizer
└── 📁 level3/                    # Advanced AI Systems
    ├── 📝 ATS.py                # Resume Analysis System
    └── 📁 sqlChatbot/           # SQL Database Chatbot
        ├── 🗣️ sqlChat.py        # Main SQL Chat Interface
        ├── 💬 multi_pdf_chat.py  # Multi-PDF RAG System
        ├── 🔧 sql.py            # SQL Query Engine
        └── 🗄️ test.db           # Sample SQLite Database
```

## 🔧 Prerequisites

- **Python 3.8+**
- **Google Gemini API Key** (Get it from [Google AI Studio](https://makersuite.google.com/app/apikey))
- **Git** (for cloning the repository)

## ⚡ Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/Arshp-svg/GeminiAi-.git
   cd GeminiAi-
   ```

2. **Create a virtual environment** (recommended)
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Set up environment variables**
   ```bash
   # Create .env file and add your Gemini API key
   echo "GEMINI_API_KEY=your_api_key_here" > .env
   ```

## 🚀 Usage

Navigate to any application directory and run:

```bash
streamlit run app_name.py
```

**Example:**
```bash
# Run the basic chatbot
streamlit run level1/app.py

# Run the YouTube transcriber
streamlit run level2/YTtanscriber.py

# Run the ATS system
streamlit run level3/ATS.py
```

## 🎯 Applications

### Level 1: Basic AI Applications

#### 🤖 Simple Q&A Chatbot (`app.py`)
- **Purpose**: Basic text-based question-answering system
- **Features**:
  - Direct text input and response
  - Simple Gemini AI integration
  - Clean Streamlit interface
- **Use Case**: Learning AI integration fundamentals

#### 🖼️ Image Analysis Tool (`imageGen.py`)
- **Purpose**: AI-powered image analysis and description
- **Features**:
  - Image upload support (JPG, JPEG, PNG)
  - Text prompt with image analysis
  - Visual image display with AI response
- **Use Case**: Visual content analysis and accessibility

### Level 2: Interactive AI Tools

#### 💬 Enhanced Q&A Chat (`qnaChat.py`)
- **Purpose**: Advanced conversational AI with context
- **Features**:
  - Persistent conversation memory
  - Enhanced response formatting
  - Session-based interactions
- **Use Case**: Customer support and interactive assistance

#### 📄 Invoice Processing (`invoiceChat.py`)
- **Purpose**: Automated invoice data extraction and analysis
- **Features**:
  - PDF invoice upload
  - Structured data extraction
  - Financial data analysis
- **Use Case**: Accounting automation and expense tracking

#### 🥗 Nutrition Analyzer (`Nutrient_Find.py`)
- **Purpose**: Food image analysis for nutritional information
- **Features**:
  - Food image recognition
  - Nutritional breakdown
  - Health recommendations
- **Use Case**: Diet tracking and health monitoring

#### 📺 YouTube Summarizer (`YTtanscriber.py`)
- **Purpose**: Automatic video transcript summarization
- **Features**:
  - YouTube URL input
  - Transcript extraction
  - Structured note generation
  - Key points and insights extraction
- **Use Case**: Educational content review and research

### Level 3: Advanced AI Systems

#### 📝 ATS Resume Analyzer (`ATS.py`)
- **Purpose**: Comprehensive resume analysis and optimization
- **Features**:
  - PDF resume upload
  - ATS compatibility scoring
  - Skill gap analysis
  - Improvement recommendations
  - Keyword optimization
- **Use Case**: Job application optimization and HR screening

#### 🗄️ SQL Database Chatbot (`sqlChatbot/`)
Advanced database interaction system with multiple components:

- **`sqlChat.py`**: Natural language to SQL query conversion
- **`multi_pdf_chat.py`**: RAG system for PDF document querying
- **`sql.py`**: Database connection and query execution engine
- **`test.db`**: Sample SQLite database for testing

**Features**:
- Natural language database queries
- PDF document indexing and search
- Vector embeddings for semantic search
- Multiple database support
- Query result visualization

## ⚙️ Configuration

### Environment Variables

Create a `.env` file in the root directory with:

```env
GEMINI_API_KEY=your_gemini_api_key_here
```

### API Key Setup

1. Visit [Google AI Studio](https://makersuite.google.com/app/apikey)
2. Create a new API key
3. Add it to your `.env` file
4. Keep your API key secure and never commit it to version control

## 📦 Dependencies

All required packages are listed in `requirements.txt`:

- **streamlit**: Web application framework
- **google-generativeai**: Google Gemini AI SDK
- **python-dotenv**: Environment variable management
- **langchain**: LLM application framework
- **chromadb**: Vector database for embeddings
- **PyPDF2**: PDF processing
- **faiss-cpu**: Similarity search and clustering
- **sentence-transformers**: Text embeddings
- **youtube-transcript-api**: YouTube transcript extraction
- **pdf2image**: PDF to image conversion

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request. For major changes, please open an issue first to discuss what you would like to change.

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🔗 Links

- **Repository**: [https://github.com/Arshp-svg/GeminiAi-](https://github.com/Arshp-svg/GeminiAi-)
- **Google Gemini AI**: [https://deepmind.google/technologies/gemini/](https://deepmind.google/technologies/gemini/)
- **Streamlit Documentation**: [https://docs.streamlit.io/](https://docs.streamlit.io/)

## 🙏 Acknowledgments

- Google AI for providing the Gemini API
- Streamlit team for the amazing web framework
- LangChain community for the powerful LLM tools
- All contributors and users of this repository

---

⭐ **Star this repository if you find it helpful!**

Built with ❤️ by [Arshp-svg](https://github.com/Arshp-svg)