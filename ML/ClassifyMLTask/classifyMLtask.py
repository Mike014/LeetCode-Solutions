class Solution:
    def classifyMLTask(self, problem: dict) -> str:
        """
        Classifies a machine learning task as either "Classification" or "Regression".

        Args:
        problem (dict): A dictionary with the following keys:
            - features (list): A list of input features (not used for classification).
            - output_type (str): Type of output, either "discrete" or "continuous".

        Returns:
        str: "Classification" if the task involves discrete outputs,
             "Regression" if the task involves continuous outputs.

        Examples:
        1. Input: {
               "features": ["age", "salary", "education"],
               "output_type": "discrete"
           }
           Output: "Classification"

        2. Input: {
               "features": ["square_feet", "location", "year_built"],
               "output_type": "continuous"
           }
           Output: "Regression"
        """
        if "features" not in problem or "output_type" not in problem:
            raise ValueError("The input dictionary must contain 'features' and 'output_type'.")
    
        if problem.get("output_type") == "discrete":
            print(problem.get("output_type"))
            return "Classification"
        elif problem.get("output_type") == "continuous":
            print(problem.get("output_type"))
            return "Regression"
        else:
            return "Invalid output type"


# Test case 1: Classification with discrete output
problem1 = {
    "features": ["age", "salary", "education"],
    "output_type": "discrete"
}
assert Solution().classifyMLTask(problem1) == "Classification", "Test Case 1 Failed"

# Test case 2: Regression with continuous output
problem2 = {
    "features": ["square_feet", "location", "year_built"],
    "output_type": "continuous"
}
assert Solution().classifyMLTask(problem2) == "Regression", "Test Case 2 Failed"

# Test case 3: Classification with an empty feature list
problem3 = {
    "features": [],
    "output_type": "discrete"
}
assert Solution().classifyMLTask(problem3) == "Classification", "Test Case 3 Failed"

# Test case 4: Regression with multiple features
problem4 = {
    "features": ["temperature", "humidity", "wind_speed"],
    "output_type": "continuous"
}
assert Solution().classifyMLTask(problem4) == "Regression", "Test Case 4 Failed"

# Test case 5: Classification with a single feature
problem5 = {
    "features": ["age"],
    "output_type": "discrete"
}
assert Solution().classifyMLTask(problem5) == "Classification", "Test Case 5 Failed"

# Test case 6: Regression with no features
problem6 = {
    "features": [],
    "output_type": "continuous"
}
assert Solution().classifyMLTask(problem6) == "Regression", "Test Case 6 Failed"

# Test case 7: Classification with mixed data types in features
problem7 = {
    "features": [42, "gender", True],
    "output_type": "discrete"
}
assert Solution().classifyMLTask(problem7) == "Classification", "Test Case 7 Failed"

print("All test cases passed!")





