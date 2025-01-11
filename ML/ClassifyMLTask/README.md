# ClassifyMLTask
A simple Python script to classify a machine learning task as either “Classification” or “Regression” based on the type of output. This problem is solved using the output_type key in a dictionary.

-- 
## Solution
The solution is straightforward: 
- Check the output_type in the given dictionary:
	•	"discrete" → The task is Classification.
	•	"continuous" → The task is Regression. 
## Machine Learning Context

In machine learning, tasks are often categorized into two main types:
1. Classification: Predicts discrete labels or categories, such as spam detection or image recognition.
2. Regression: Predicts continuous values, such as estimating house prices or stock market trends.

The distinction is based on the nature of the output, not the input data. For example:
1. Predicting whether an email is spam (Classification).
2.  Predicting the price of a car based on its attributes (Regression).
