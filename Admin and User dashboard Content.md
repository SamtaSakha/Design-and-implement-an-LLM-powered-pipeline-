# 📊 Task 2: Feedback Collection & Sentiment Analysis Dashboard


This task implements a **two-dashboard Streamlit application** that enables users to submit feedback and allows administrators to analyze sentiment trends using an **LLM-powered sentiment analysis pipeline**.

The system is designed with **clear role separation**, **data persistence**, and **fault-tolerant handling of empty datasets**, making it suitable for real-world feedback analysis scenarios.

---

## 🧑‍💻 User Dashboard – Feedback Submission Interface

### 🎯 Purpose
The User Dashboard provides an intuitive interface for end users to submit textual feedback.  
Each feedback entry is automatically analyzed for sentiment using a **Large Language Model (LLM)**.

---

### 🧩 Key Features
- Text-based feedback submission
- Real-time sentiment analysis using an LLM
- Automatic storage of feedback and sentiment results
- Graceful handling of empty or newly created datasets
- Live display of previously submitted feedback

---

### 🛠️ Functional Workflow
1. The user enters feedback into a text input field.
2. Upon clicking **Submit**, the feedback is sent to the LLM pipeline.
3. The LLM classifies the sentiment (Positive / Neutral / Negative).
4. The feedback and sentiment are stored in a CSV file.
5. The dashboard dynamically updates to display all submitted feedback.

---

### 📄 Data Storage Format
The feedback data is stored in **`feedback.csv`** with the following structure:

| Column Name | Description |
|------------|-------------|
| feedback   | Raw user feedback text |
| sentiment  | LLM-generated sentiment classification |

---

### 🧠 Error Handling
- Automatically initializes the CSV file if it does not exist.
- Displays an informational message when no feedback is available.
- Prevents empty feedback submission using input validation.
- Ensures the application does not crash due to missing or empty data.

---

### 🖥️ Technologies Used
- **Streamlit** – User Interface  
- **Pandas** – Data handling  
- **LLM (Gemini / API-based)** – Sentiment analysis  
- **CSV Storage** – Lightweight persistence layer  

---

## 🔐 Admin Dashboard – Feedback Analytics & Monitoring

### 🎯 Purpose
The Admin Dashboard enables administrators to monitor all submitted feedback and analyze overall sentiment trends.

This dashboard is **read-only** and focuses on **data inspection and insights**, not data modification.

---

### 🧩 Key Features
- View all user-submitted feedback
- Analyze sentiment distribution
- Display summary statistics
- Visualize sentiment breakdown
- Safe handling of empty datasets

---

### 🛠️ Functional Workflow
1. The admin dashboard loads **`feedback.csv`**.
2. The dataset is validated for existence and correct structure.
3. Feedback records are displayed in a tabular format.
4. Sentiment counts are calculated.
5. Visual charts display sentiment distribution and trends.

---

### 📊 Analytics Provided
- Total number of feedback entries
- Count of positive, neutral, and negative sentiments
- Tabular view of all feedback
- Visual sentiment distribution (bar chart or pie chart)

---

### 🧠 Error & Edge Case Handling
- Displays a message if no feedback has been collected yet.
- Prevents `EmptyDataError` by validating file size and headers.
- Ensures dashboard stability even when data is missing.

---

### 🖥️ Technologies Used
- **Streamlit** – Admin Interface  
- **Pandas** – Aggregation and analysis  
- **Matplotlib / Streamlit Charts** – Data visualization  
- **CSV Storage** – Shared persistence layer  

---

## 🔁 System Architecture Overview

