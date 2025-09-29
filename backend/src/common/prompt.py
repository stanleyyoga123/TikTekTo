USER_PATHWAY_PROMPT = """
Role: {role}
Background: {background}
Additional Info: 
{additional}

Objective: learning {objective}

Extract pathways with these conditions:
1. Group in several milestones, with every milestone consists of several topics that I need to finish before continue to next milestone
2. For each group, sort it with difficulty level ascending

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
