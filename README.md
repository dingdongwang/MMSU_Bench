# MMSU: A Massive Multi-task Spoken Language Understanding and Reasoning Benchmark
Arxiv link: comming soon

[View PDF](images/intro.pdf)

MMSU is a comprehensive benchmark designed specifically for understanding and reasoning in spoken language. MMSU comprises 5,000 meticulously curated audio-question-answer triplets across 47 distinct tasks. To ground our benchmark in linguistic theory, we systematically incorporate a wide range of linguistic phenomena, including phonetics, prosody, syntax, syntactics, semantics, and paralinguistics.

## Overview of MMSU Structure

[View PDF](images/barchart-per.pdf)

[View PDF](images/barchart-rea.pdf)


TMMSU consists of three levels of depth to classify different tasks and assessment dimensions. **At the first level**, MMSU distinguishes between two fundamental dimensions: perception abilities and reasoning abilities. Similar to human cognitive processes, perception focuses on extracting basic audio information and recognizing fundamental speech features, while reasoning involves deeper cognitive processes for interpretation and inference. **At the second level**, both dimensions are further divided into linguistics and paralinguistics categories. Linguistics is the scientific study of language structure, meaning, and usage, whereas paralinguistics is a component of meta-communication that studies the effect of vocal characteristics on semantic interpretation, such as emotion, pitch, and volume. **At the third level**, the linguistics category branches into semantics and phonology. Semantics focuses on the content-related aspects, including meaning interpretation and contextual understanding, while phonology deals with sound patterns such as tone, prosody, and phonemic distinctions. Concurrently, the paralinguistics category divides into speaker traits and speaking style. Speaker traits involve inherent characteristics such as voice timbre and speaker identity, while speaking style encompasses variable elements such as pitch, speed, and emotion.

## Download MMSU Data
Refer to Huggingface: https://huggingface.co/datasets/ddwang2000/MMSU

## Evaluation
Step1: Inference your model on MMSU Benchmark
`python mmsu_inference.py --input_jsonl /path/to/input.jsonl --output_jsonl /path/to/output.jsonl`

Step2: Evaluate on MMSU Benchmark
`python mmsu_evaluation.py /path/to/your/input.jsonl`

## Citation
Coming Soon
