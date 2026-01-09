# Example 05: Message History

## Overview
Demonstrates conversation history management with message accumulation and context preservation.

## What to Do
This example creates a conversational interface that:
1. Maintains a complete history of all messages
2. Processes user input and generates contextual responses
3. Displays timestamped conversation
4. Provides conversation statistics

## Inputs
- **User Name**: Name for personalized greeting
  - Type: String
  - Default: "Guest"
  - Example: "Alice", "Bob"

- **User Messages**: Text input during conversation
  - Type: String
  - Examples: "hello", "how are you", "bye"
  - Triggers contextual responses

## Expected Outputs
- **Conversation History**: List of all messages
  - Each message contains:
    - `role`: "user" or "assistant"
    - `content`: Message text
    - `timestamp`: Time in HH:MM:SS format

- **Bot Responses**: Context-aware replies
  - Greeting: "Hello {name}! How can I help you today?"
  - Hello response: "Hello! Nice to hear from you!"
  - How are you: "I'm doing great! Thanks for asking. How about you?"
  - Goodbye: "Goodbye! Have a great day!"
  - Help: "I can chat with you! Try saying hello..."
  - Weather: "I don't have access to weather data..."
  - Default: "I heard you say '{message}'. That's interesting!"

- **Conversation Stats**:
  - Total message count
  - User message count
  - Bot message count

## Graph Structure
```
START → greet → respond → END
```

### Nodes:
1. **greet**: Generates personalized welcome message
2. **respond**: Processes user input and creates response

## State Schema
```python
{
    "messages": list,              # Accumulated message history
    "user_name": str,             # User's name
    "conversation_start": str     # Start timestamp
}
```

### Message Format:
```python
{
    "role": str,        # "user" or "assistant"
    "content": str,     # Message text
    "timestamp": str    # HH:MM:SS
}
```

## UI Components
- Title and description
- Name input field (initial screen)
- Start conversation button
- Conversation history display with timestamps
- Message input field
- Send button
- Clear history button
- Conversation statistics
- Graph structure visualization

## Session State Management
- `conversation_history`: List of all messages
- `user_name`: Current user's name
- `conversation_started`: Boolean flag
- `conversation_start`: Session start time

## Learning Objectives
- Understand message accumulation patterns
- Learn to maintain conversation context
- Practice list state management with operator.add
- Implement timestamped logging
- Build conversational interfaces
- Handle session state in Streamlit
- Create interactive chat UIs

## Response Patterns
| User Input | Bot Response |
|------------|-------------|
| "hello" / "hi" | Greeting response |
| "how are you" | Status response |
| "bye" / "goodbye" | Farewell |
| "help" | Help message |
| "weather" | Weather disclaimer |
| Other | Echo with acknowledgment |

## Features
- Personalized greetings
- Context-aware responses
- Message timestamps
- Conversation statistics
- History clearing
- Session persistence
