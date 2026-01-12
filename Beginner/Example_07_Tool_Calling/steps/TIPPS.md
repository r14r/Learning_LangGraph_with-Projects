# Tipps und Beispielimplementierungen zu jedem Schritt

## ex01.py
Lege eine leere Python-Datei an. Dies ist der Startpunkt für die Entwicklung.

## ex02.py
Füge die notwendigen Imports und die Grundstruktur hinzu:
```python
import streamlit as st
from typing import TypedDict, Annotated, Literal
from langgraph.graph import StateGraph, END
import operator
import math
```

## ex03.py
Definiere die State-Struktur und die Tool-Funktionen:
```python
class ToolState(TypedDict):
    query: str
    tool_calls: Annotated[list, operator.add]
    result: str
# ... Tool-Funktionen ...
```

## ex04.py
Implementiere die Node-Logik und das Query-Parsing:
```python
def parse_query(state: ToolState) -> ToolState:
    query = state["query"].lower()
    # Logik zum Parsen und Auswählen der Tools
    return state
```

## ex05.py
Baue die finale Streamlit-App und integriere die Tool-Logik.

Jeder Schritt enthält einen klaren Fokus und kann einzeln getestet werden.