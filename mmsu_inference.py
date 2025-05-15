import os
import argparse
import json
from tqdm import tqdm
import shutil


def main():
    # Parse command-line arguments
    parser = argparse.ArgumentParser(description="Easy Inference for your model.")
    parser.add_argument('--input_jsonl', type=str, required=True, help="Path to the input JSONL file")
    parser.add_argument('--output_jsonl', type=str, required=True, help="Path to the output JSONL file")
    args = parser.parse_args()

    input_file = args.input_jsonl
    output_file = args.output_jsonl


    #Step1: Bulid your model; Implement according to your own model
    #model = model.cuda()
    #model.eval()

    #Step2: Single step inference
    with open(input_file, "r") as fin, open(output_file, "w") as fout:
        fin = json.load(fin)
        for item in tqdm(fin):
            audio_path = item['audio_path']
            task_name = item['task_name']
            if os.path.exists(audio_path) == False:
                print(f"lack wav {wav_fn}")
                continue
            
            
            #Construct prompt
            question = item['question']
            question_prompts = 'Choose the most suitable answer from options A, B, C, and D to respond the question in next line, **you should only choose A or B or C or D.** Do not provide any additional explanations or content.'
            choice_a = item['choice_a']
            choice_b = item['choice_b']
            choice_c = item.get('choice_c', None)
            choice_d = item.get('choice_d', None)
            choices = f'A. {choice_a}\nB. {choice_b}\nC. {choice_c}\nD. {choice_d}'
            instruction = f"{question_prompts}\n\nQuestion: {question}\n\n{choices}"
            

            #Step 3: Run model inference
            #output = model.infer(
            #    Prompts=instruction,
            #    Audio_path=audio_path,
            #    ...
            #)
            
            output = "Model response here"  # Placeholder response

            #Step 4: save result
            json_string = json.dumps(
                {
                    "id": item["id"]
                    "audio_path": item["audio_path"],
                    "question": question,
                    "choice_a": choice_a,
                    "choice_b": choice_b,
                    "choice_c": choice_c,
                    "choice_d": choice_d,
                    "answer_gt": item["answer_gt"],
                    "response": output,
                    "task_name": task_name,
                    "category": item["category"],
                    "sub-category": item["category"],
                    "sub-sub-category": item["sub-sub-category"],
                    "linguistics_sub_discipline": item["linguistics_sub_discipline"],
                },
                ensure_ascii=False
            )
            fout.write(json_string + "\n")
            

if __name__ == "__main__":
    # bash:
    # python mmsu_inference.py --input_jsonl /path/to/input.jsonl --output_jsonl /path/to/output.jsonl
    main()