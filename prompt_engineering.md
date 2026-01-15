# AI Prompting Refinement & Error Handling

This document details the prompt engineering strategy and error handling considerations for the Content Creator AI Tool.

## Prompt Strategy

### 1. Summarization
**Prompt Used**: 
> "Summarize the following text into 2-3 concise sentences:\n\n{input_text}"

**Rationale**:
- **Constraint**: Specifying "2-3 concise sentences" prevents the model from generating overly long or too brief (one-word) summaries.
- **Clarity**: "Summarize" is a strong, direct instruction.
- **Iteration**: Initially, simpler prompts like "Summarize this" might yield variable lengths. Adding constraints improves consistency.

### 2. Rephrasing (Contextual Tone)
**Prompt Used**: 
> "Rephrase the following text in a {target_tone} tone:\n\n{input_text}"

**Rationale**:
- **Dynamic Injection**: We insert the user's `target_tone` directly into the instruction.
- **Flexibility**: This allows for any adjective ("funny", "Shakespearean", "angry") without changing the code structure.
- **Challenge**: If a user enters a nonsensical tone (e.g., "blue"), the AI attempts to interpret it metaphorically or ignores it, which is a graceful fail-safe of LLMs.

## Error Handling Considerations

While the current script has basic error handling, a production-grade application would handle the following edge cases:

1.  **API Failures (Network/Auth)**:
    - *Current*: Catches `OpenAIError` and prints it.
    - *Ideal*: Implement exponential backoff retries (wait 2s, 4s, 8s) for transient network issues.

2.  **Input Length**:
    - *Current*: Checks against `MAX_CHAR_LIMIT` (64,000).
    - *Ideal*: Tokenize the input using `tiktoken` to get an exact count before sending, ensuring it strictly fits the model's context window.

3.  **Content Filtering**:
    - *Scenario*: User inputs unsafe/hate speech.
    - *Handling*: OpenAI's API might refuse to process it. The script should catch a `RefusalError` or check `finish_reason` to inform the user why output wasn't generated.

4.  **Empty/Nonsensical Output**:
    - *Scenario*: AI returns an empty string.
    - *Handling*: Check `if not response:` and prompt the user to try again or rephrase their input.
