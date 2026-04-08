# Smart Study AI Agent

## Overview
The Smart Study AI Agent is a Python-based intelligent system designed to assist students in learning and revising academic content efficiently. It processes study materials in the form of PDF or text files, extracts key topics, and provides meaningful outputs such as answers, summaries, important questions, and flashcards.

This project demonstrates the use of basic Artificial Intelligence concepts and Natural Language Processing (NLP) techniques to transform unstructured study material into structured and useful information.

---

## Objectives
- To reduce time spent searching through study material  
- To automatically extract important topics and definitions  
- To assist students in quick revision  
- To provide an intelligent and interactive learning experience  

---

## Features
- Load study material (PDF / TXT)  
- Intelligent question answering system  
- Automatic summary generation  
- Important question generation  
- Flashcards for revision  
- Keyword-based search  
- Chat mode for interactive queries  
- Eliminates duplicate and irrelevant outputs  
- Accurate topic-based results  

---

## How It Works
1. The system accepts a file (PDF or TXT) as input  
2. Extracts and cleans the text content  
3. Splits the content into meaningful sentences  
4. Identifies topics using pattern recognition  
5. Stores structured data (Topic → Explanation)  
6. Matches user queries with stored topics  
7. Generates accurate and relevant output  

---

## System Architecture

```
User Input
   ↓
File Loader (PDF/TXT)
   ↓
Text Processing (Cleaning and Formatting)
   ↓
Sentence Segmentation
   ↓
Topic Extraction (Pattern Matching)
   ↓
Knowledge Base (Topic → Explanation)
   ↓
AI Engine (Matching Logic)
   ↓
Output Module
   ↓
User Interface
```

---

## Technologies Used
- Python  
- PyPDF2 (for PDF text extraction)  
- Regular Expressions (re) (for text processing)  
- Basic NLP techniques  

---

## Project Structure

```
StudyAI/
│
├── study_agent.py      # Main application file  
├── ai_notes.txt        # Sample input file  
├── README.md           # Project documentation  
```

---

## Installation

1. Install Python (version 3 or above)

2. Install required dependency:
```
pip install PyPDF2
```

---

## How to Run

1. Open terminal or VS Code  
2. Navigate to project directory  
3. Run the program
4. Enter the file path when prompted  

---

## Key Highlights
- Clean and structured outputs  
- Accurate topic-based responses  
- No duplicate or irrelevant questions  
- Fully offline system  
- Simple and user-friendly interface  

---

## Author
Boddu Dhanya Akshaya

---

## License
This project is developed for educational purposes.
