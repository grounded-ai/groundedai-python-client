## GroundedAI Python Client

The GroundedAI Python Client is a simple and easy-to-use library that provides a convenient interface for interacting with the GroundedAI API. This client allows you to evaluate answers and perform statistical evaluations on retrieval results, all from within your Python code.

### Features

- **Answer Evaluation:** Evaluate the quality of an answer based on a given prompt and optional context.
- **Statistical Evaluation:** Evaluate the performance of a retrieval system by comparing the retrieved documents with the ground truth data, using various metrics such as Mean Reciprocal Rank (MRR), Mean Average Precision (MAP), and Recall.
- **Simple API:** The client exposes a clean and intuitive API, making it easy to integrate with your existing Python projects.
- **Error Handling:** Robust error handling ensures that any issues with the API requests are properly handled and reported.

### Installation

You can install the GroundedAI Python Client using pip:

```bash
pip install groundedai-python-client
```
## Usage

Here's an example of how to use the GroundedAI Python Client:

```python
# Example usage
client = GroundedAIClient("your_api_key_here")

# Example statistical evaluator usage:
ground_truth = [["Country A", "Country B", "Country C"], ["Era X", "Era Y", "Era Z"]]
retrieved_docs = [
    ["Country A", "Country D", "Country F"],
    ["Era X", "Era Y", "Era Alpha", "Era Beta"],
]
metrics = ["mrr", "map", "recall"]

evaluation_results = client.evaluate_statistical(ground_truth, retrieved_docs, metrics)
print(evaluation_results)

# Example answer evaluator usage:
predicted_answers = [
    "The Great Wall of China is the world's largest human-made structure, stretching over 13,000 miles.",
    "The Statue of Liberty, a gift from France to the United States, stands tall in New York Harbor as a symbol of freedom and democracy.",
    "The Colosseum in Rome, Italy, is an iconic amphitheater where gladiatorial games and public spectacles took place during the Roman Empire.",
]
ground_truth_answers = [
    "The Great Wall of China is the world's largest human-made structure, stretching over 13,000 miles.",
    "The Statue of Liberty Enlightening the World, a gift from France to the United States, stands in New York Harbor as a symbol of freedom and friendship.",
    "The Roman Colosseum, an iconic amphitheater in the heart of Rome, Italy, hosted gladiatorial games and public spectacles during the Roman Empire.",
]
metrics = ["exact_match", "semantic_similarity"]

evaluation_results = client.evaluate_answer(
    predicted_answers, ground_truth_answers, metrics
)
print(evaluation_results)

# Example retrieval evaluator usage:
questions = ["What is the largest mammal?"]
contexts = [
    [
        "The blue whale is the largest mammal on Earth, reaching up to 30 meters in length and weighing up to 180 tons.",
        "The African elephant is the largest land mammal, known for its impressive size and intelligence.",
        "The largest mammal ever to exist was the extinct woolly mammoth, which stood up to 4 meters tall and weighed up to 6 tons.",
    ]
]
responses = ["The blue whale is the largest mammal, reaching lengths of up to 30 meters."]
metrics = ["context_relevance", "faithfulness"]

evaluation_results = client.model_evaluate_retrieval(questions, contexts, responses, metrics)
print(evaluation_results)
```
## Contributing

We welcome contributions to the GroundedAI Python Client! If you find any issues or have suggestions for improvements, please open an issue or submit a pull request on our GitHub repository.

## License

The GroundedAI Python Client is released under the MIT License.

## Support

If you have any questions or need further assistance, please contact our support team at support@groundedai.com.
