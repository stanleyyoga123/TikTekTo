USER_PATHWAY_DOCUMENT_PROMPT = """
User info are attached in this document file

Objective: learning {objective}

Extract pathways with these conditions:
1. Group in several milestones, with every milestone consists of several topics that I need to finish before continue to next milestone
2. For each group, sort it with difficulty level ascending
3. If the user already have similar experience with the topics in the milestone, skip it
4. In general_idea, refrain from using this type of template (Milestone 1: ...), just focus on the general idea itself

Answer it with this JSON format, no need other words
```
[
    {{
        "general_idea": str,
        "topics": list[str]
    }},
    ...
]
```
Field description:
    general_idea: every element have maximum of 5 words 
    topics: each element must be concise
"""

USER_PATHWAY_PROMPT = """
Role: {role}
Background: {background}
Additional Info: 
{additional}

Objective: learning {objective}

Extract pathways with these conditions:
1. Group in several milestones, with every milestone consists of several topics that I need to finish before continue to next milestone
2. For each group, sort it with difficulty level ascending
3. If the user already have similar experience with the topics in the milestone, skip it
4. In general_idea, refrain from using this type of template (Milestone 1: ...), just focus on the general idea itself

Answer it with this JSON format, no need other words
```
[
    {{
        "general_idea": str,
        "topics": list[str]
    }},
    ...
]
```
Field description:
    general_idea: every element have maximum of 5 words 
    topics: each element must be concise
"""

QUESTION_PROMPT = """
Return questions that are related with these conditions

1. General Topic: {general_idea}
2. Topics: {topics}

I want tags that are highly relevant with the conditions
"""

FLASHCARD_CREATION_PROMPT = """
Make me {num_flashcards} flashcards with these conditions

1. General Topic: {general_idea}
2. Topics: {topics}

Return in JSON only response with these structure
```
[
    {{
        "question": str,
        "answer": str
    }}
]
```

I want the flashcard to be concise, with maximum of 20 words for each element
"""

CHECK_ANSWER_PROMPT = """
Compare these 2 answers, are they same or not, if not give the explanation why. Try to make sure the points from the question is answered, it's fine eventhough the answer are not 100 percent complete (threshold at 80 percent covered)

Question: {question}
True answer: {true_answer}
User answer: {user_answer}

Retun in JSON only response with these structure
```
{{
    "is_correct": boolean,
    "reason": str
}}
```
Field description:
    is_correct: true if it's correct, false if the other way
    reason: why the answer is false, answer with less than 30 words. If the answer is correct, just fill it with null
"""

HIGHLIGHT_ADDITIONAL_PROMPT = """
I want you to highlight just the keypoints from the JSON response that has field type of str, by using <mark>
Don't try to mark the entire response
"""
