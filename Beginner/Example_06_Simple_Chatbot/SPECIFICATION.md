# Example 06: Simple Chatbot

## Overview
An intent-based chatbot that classifies user messages and generates contextual responses.

## What to Do
This example creates a chatbot that:
1. Recognizes user intent from messages
2. Generates appropriate responses based on intent
3. Maintains conversation history
4. Provides a chat interface with message styling

## Inputs
- **User Messages**: Text input from the user
  - Type: String
  - Examples: "Hello", "What can you do?", "Thanks", "Goodbye"
  - Processed for intent classification

## Expected Outputs
- **Intent Classification**: Detected intent from user message
  - **greeting**: "hello", "hi", "hey"
  - **farewell**: "bye", "goodbye", "see you"
  - **question**: Messages containing "?"
  - **gratitude**: "thank", "thanks"
  - **statement**: Any other message
  - **unknown**: Fallback category

- **Bot Responses**: Intent-specific replies
  - Greeting: "Hello! 👋 Great to chat with you! How can I assist you today?"
  - Farewell: "Goodbye! 👋 Take care and have a wonderful day!"
  - Question: "That's an interesting question! You asked: '{message}'. Let me think..."
  - Gratitude: "You're very welcome! 😊 Happy to help!"
  - Statement: "I see! You mentioned: '{message}'. Tell me more!"
  - Unknown: "I'm here to chat! Feel free to ask me anything."

- **Message History**: Complete conversation log with metadata
  - Role (user/assistant)
  - Content
  - Timestamp
  - Intent (for bot messages)

## Graph Structure
```
START → understand → respond → END
```

### Nodes:
1. **understand**: Intent classification
   - Analyzes last user message
   - Identifies intent pattern
   - Updates context

2. **respond**: Response generation
   - Retrieves intent from context
   - Selects appropriate response
   - Adds to message history

## State Schema
```python
{
    "messages": list,    # Conversation history
    "context": dict      # Current conversation context
}
```

### Message Format:
```python
{
    "role": str,        # "user" or "assistant"
    "content": str,     # Message text
    "timestamp": str,   # HH:MM:SS
    "intent": str       # Intent (bot messages only)
}
```

### Context Format:
```python
{
    "intent": str,         # Classified intent
    "last_user_msg": str   # Last user message
}
```

## UI Components
- Title and description
- Styled message display
  - User messages (blue background)
  - Bot messages (gray background with intent emoji)
- Message input field
- Send button
- Quick action buttons:
  - Clear Chat
  - Say Hello
  - Ask Question
- Chat statistics
- Graph structure visualization
- Example messages

## Intent Emojis
- greeting: 👋
- farewell: 👋
- question: ❓
- gratitude: 😊
- statement: 💭
- unknown: 🤖

## Learning Objectives
- Understand intent classification
- Learn pattern matching for NLP
- Practice context management
- Implement chat interfaces
- Build message styling
- Handle conversational flow
- Create interactive chat UX

## Example Interactions

| User Input | Intent | Bot Response |
|------------|--------|--------------|
| "Hello!" | greeting | Welcome message |
| "What can you do?" | question | Question acknowledgment |
| "Thank you" | gratitude | You're welcome response |
| "Goodbye" | farewell | Farewell message |
| "I like this" | statement | Statement reflection |

## Features
- Real-time intent classification
- Contextual responses
- Message timestamps
- Styled chat bubbles
- Quick action buttons
- Conversation statistics
- Session persistence
