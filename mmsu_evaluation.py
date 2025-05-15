import json
import argparse
from collections import defaultdict

def load_jsonl_data(jsonl_path):
    """Load data from the provided JSONL file."""
    records = []
    with open(jsonl_path, 'r', encoding='utf-8') as f:
        for line_number, line in enumerate(f):
            try:
                record = json.loads(line.strip())
                records.append(record)
            except json.JSONDecodeError as e:
                print(f"Error decoding JSON on line {line_number}: {line.strip()}")
                print(e)
    return records

def calculate_accuracy_per_task_and_category(data):
    """Calculate accuracy for each unique task and category."""
    task_category_accuracy = defaultdict(lambda: defaultdict(lambda: {"correct": 0, "total": 0}))
    task_average_accuracy = defaultdict(lambda: {"total_correct": 0, "total_count": 0})
    
    # Initialize counters
    total_correct = 0
    total_count = 0
    fail_num = 0 

    for record in data:
        task = record.get('category', '')
        category = record.get('sub-category', '')

        # Extract response
        response = record.get('response', '')
        try:
            predict = response.strip().replace('\n', '')
        except:
            print('Error prediction!')
            continue

        if predict != 'None' and predict:
            if predict[0] == 'A' or predict[0] == 'B' or predict[0] == 'C' or predict[0] == 'D':
                model_predict = predict[0]
            #This situation may occur when the answer given by gpt is "The answer is A."
            elif len(predict) > 1:
                if predict[-2] == 'A' or predict[-2] == 'B' or predict[-2] == 'C' or predict[-2] == 'D':
                    model_predict = predict[-2]
                else:
                    print(f'Wrong format response: {predict}')
                    continue
            else:
                print(f'Wrong format response: {predict}')
                continue
        
        # Get the correct answer
        answer_gt = record.get('answer_gt', '')
        choices = {
            'A': record.get('choice_a', ''),
            'B': record.get('choice_b', ''),
            'C': record.get('choice_c', ''),
            'D': record.get('choice_d', '')
        }
        
        # Check if the prediction matches the correct answer
        if model_predict:
            if model_predict == 'A' and choices['A'] == answer_gt:
                task_category_accuracy[task][category]["correct"] += 1
                total_correct += 1
            elif model_predict == 'B' and choices['B'] == answer_gt:
                task_category_accuracy[task][category]["correct"] += 1
                total_correct += 1
            elif model_predict == 'C' and choices['C'] == answer_gt:
                task_category_accuracy[task][category]["correct"] += 1
                total_correct += 1
            elif model_predict == 'D' and choices['D'] == answer_gt:
                task_category_accuracy[task][category]["correct"] += 1
                total_correct += 1
                
        # Increase the total count for the task and category
        task_category_accuracy[task][category]["total"] += 1
        total_count += 1

    # Calculate accuracy per task and category
    for task, categories in task_category_accuracy.items():
        total_correct_for_task = 0
        total_count_for_task = 0
        for category, counts in categories.items():
            total = counts["total"]
            correct = counts["correct"]
            accuracy = correct / total if total > 0 else 0
            task_category_accuracy[task][category] = accuracy
            
            # Calculate overall task accuracy
            total_correct_for_task += correct
            total_count_for_task += total
        
        # Calculate average accuracy for each task
        task_average_accuracy[task]["total_correct"] = total_correct_for_task
        task_average_accuracy[task]["total_count"] = total_count_for_task
        task_average_accuracy[task]["average_accuracy"] = total_correct_for_task / total_count_for_task if total_count_for_task > 0 else 0

    # Calculate overall accuracy
    overall_accuracy = total_correct / total_count if total_count > 0 else 0

    return task_category_accuracy, task_average_accuracy, overall_accuracy, total_count

def main():
    """Main function to load data, calculate accuracy, and print results."""
    # Parse command-line arguments
    parser = argparse.ArgumentParser(description="Process a JSONL file and calculate accuracy.")
    parser.add_argument('jsonl_path', type=str, help="Path to the input JSONL file")
    args = parser.parse_args()

    # Load data
    data = load_jsonl_data(args.jsonl_path)

    # Calculate accuracy
    task_category_accuracies, task_average_accuracies, overall_accuracy, total_count = calculate_accuracy_per_task_and_category(data)

    # Print accuracy for each category and sub-category
    for task, categories in task_category_accuracies.items():
        for category, accuracy in categories.items():
            print(f'Category: {task}, Sub-category: {category}, Accuracy: {accuracy:.4f}')

    # Print average accuracy for each category
    for task, accuracy_info in task_average_accuracies.items():
        average_accuracy = accuracy_info["average_accuracy"]
        print(f'Category: {task}, Average Accuracy: {average_accuracy:.4f}')

    # Print overall accuracy
    print(f'Overall Accuracy: {overall_accuracy:.4f}')
    print(f'Total count: {total_count}')

if __name__ == "__main__":
    # bash:
    # python mmsu_evaluation.py /path/to/your/input.jsonl
    main()
