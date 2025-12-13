# Design-and-implement-an-LLM-powered-pipeline


## 👩‍💻 Author

**Samta**
BSc Data Science & Artificial Intelligence

---

## 📌 Project Overview

This project demonstrates an **AI Engineer workflow** using **Google Gemini models** to solve two core tasks:

* **Task 1:** Predict structured ratings (1–5 stars) from raw customer reviews using an LLM
* **Task 2:** Build a **function-calling pipeline** where the LLM intelligently selects and executes tools

The implementation focuses on **real-world production concepts** such as prompt engineering, JSON validation, tool routing, and robust error handling.

---

## 🗂️ Project Structure

```
.
├── analysis.ipynb        # Main notebook (EDA, Task 1, Task 2)
├── yelp.csv.zip          # Yelp reviews dataset
├── README.md             # Project documentation
```

---

## 🔧 Tech Stack

* **Python 3.11+**
* **Google Gemini API**
* pandas, numpy
* matplotlib
* jsonschema
* tqdm

---

## 📊 Dataset

* **Source:** Yelp Reviews Dataset
* **Key Columns:**

  * `text` – Review text
  * `stars` – Ground truth rating (1–5)

---

## 🟢 Task 1: Review Rating Prediction

### Objective

Predict a numeric rating from free-form review text using a Large Language Model.

### Approach

1. Load and inspect the dataset
2. Design a strict prompt that forces **JSON-only output**
3. Call Gemini to infer ratings from review text
4. Parse and validate model output
5. Store predictions alongside ground truth

### Output Format

```json
{
  "rating": 4
}
```

### Key Highlights

* Zero-shot rating prediction
* JSON schema validation for safety
* Graceful handling of malformed responses
* Scalable pandas-based inference pipeline

---

## 🟢 Task 2: Function Calling with Gemini

### Objective

Enable Gemini to dynamically choose and execute predefined Python functions based on user intent.

### Approach

* Defined callable Python tools (e.g., math operations, sentiment analysis)
* Registered tool schemas using structured JSON definitions
* Allowed Gemini to decide:

  * *Which function to call*
  * *What arguments to pass*
* Executed the function and returned results back to the model

### Example Workflow

```
User Query → Gemini → Tool Selection → Python Execution → Final Response
```

### Why This Matters

This pattern is foundational for:

* AI agents
* Tool-augmented chatbots
* Autonomous decision systems

---

## ✅ Validation & Results

* Notebook runs end-to-end without errors
* Outputs include:

  * Raw model responses
  * Parsed JSON
  * Validation status
  * Predicted vs actual ratings

---

## ⚠️ Challenges & Learnings

* Model availability and version mismatches
* Importance of prompt strictness
* Handling silent execution in notebooks
* Managing Python environments and dependencies

---

## 🚀 Conclusion

This project showcases **practical AI engineering skills**, including:

* LLM integration with real datasets
* Prompt engineering for structured outputs
* Tool/function calling pipelines
* Robust validation and debugging practices

The architecture closely mirrors **production-grade LLM systems** used in modern AI applications.

---

## ▶️ How to Run

1. Create a virtual environment
2. Install dependencies
3. Set your Gemini API key
4. Run `analysis.ipynb`

---

## 📬 Contact

For questions or improvements, feel free to reach out.
