# TIPPS

Schritt 1: Grundgeruest
Baue eine minimale Startdatei, die sofort laeuft.

```python
import streamlit as st

st.title("Example 03 Conditional Edges")
st.write("Step 1: Grundgeruest erstellt.")
```

Schritt 2: Imports und Konstanten
Importiere die benoetigten Module und lege erste Konstanten an.

```python
import streamlit as st
from typing import TypedDict, Annotated, Literal
from langgraph.graph import StateGraph, END

st.title("Example 03 Conditional Edges")
st.write("Step 2: Kernbausteine geladen.")
```

Schritt 3: Kernlogik erweitern
Fokussiere dich auf: ClassificationState, classify_number, handle_positive.

```python
import streamlit as st

class ClassificationState:
    def __init__(self):
        pass
```

Schritt 4: Kernlogik erweitern
Fokussiere dich auf: handle_negative, handle_zero, route_number.

```python
import streamlit as st

def handle_negative(state):
    return "todo"
```

Schritt 5: Kernlogik erweitern
Fokussiere dich auf: create_graph.

```python
import streamlit as st

def create_graph():
    return "todo"
```

Schritt 6: Vollstaendiges Programm
Kopiere den finalen Stand aus `app.py` und stelle alle Details fertig.
