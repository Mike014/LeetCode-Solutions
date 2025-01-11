# ClassifyMLTask
A simple Python script to classify a machine learning task as either “Classification” or “Regression” based on the type of output. This problem is solved using the output_type key in a dictionary.

-- 
## Solution
The solution is straightforward: 
- Check the output_type in the given dictionary:
	•	"discrete" → The task is Classification.
	•	"continuous" → The task is Regression. 
## Machine Learning Context

- In machine learning, tasks are often categorized into two main types:
	•	Classification: Predicts discrete labels or categories, such as spam detection or image recognition.
	•	Regression: Predicts continuous values, such as estimating house prices or stock market trends.

- The distinction is based on the nature of the output, not the input data. For example:
	•	Predicting whether an email is spam (Classification).
	•	Predicting the price of a car based on its attributes (Regression).
