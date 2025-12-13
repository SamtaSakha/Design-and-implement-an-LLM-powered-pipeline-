# Design-and-implement-an-LLM-powered-pipeline

## TASK 1 
🎯 Objective

The goal of Task 1 is to use a Large Language Model (LLM) to automatically predict a numerical rating (1–5 stars) from unstructured customer review text. This simulates a real-world scenario where user feedback must be converted into structured signals for analytics or downstream systems.

🧠 Design & Methodology

Input Data

Raw customer reviews from the Yelp dataset

Each record contains free-text feedback (text) and a ground-truth rating (stars)

Prompt Engineering

A strict prompt was designed to instruct Gemini to return only valid JSON

The model is explicitly constrained to output an integer rating between 1 and 5

Example prompt pattern:

Given the following customer review, predict a rating between 1 and 5.
Respond ONLY in valid JSON with the key "rating".
Review: <review_text>

LLM Inference Pipeline

A reusable function (task1_predict) sends each review to Gemini

Model responses are captured as raw text

JSON is parsed and validated before use

Validation & Safety Checks

Ensured output is valid JSON

Verified the presence of the rating key

Confirmed rating values fall within the expected range (1–5)

Invalid or malformed responses are safely handled

Batch Processing

Predictions are applied across the dataset using pandas.apply()

Results are stored in new columns:

model_output – raw parsed JSON

model_rating – extracted numeric prediction

📤 Output Format
{
  "rating": 4
}
📊 Results & Observations

Gemini is able to infer sentiment and service quality directly from text

Neutral or mixed reviews typically receive mid-range ratings (3–4)

Strong sentiment cues (positive or negative) align well with ground truth

Strict prompting significantly reduces malformed outputs

💡 Why This Matters

Task 1 demonstrates how LLMs can be used as structured predictors, not just chatbots. This approach is commonly used in:

Review aggregation systems

Customer feedback analytics

Automated labeling pipelines

The solution mirrors how production AI systems transform unstructured text into reliable, machine-readable signals.
