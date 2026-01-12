# TIPPS

Schritt 1: Grundgeruest
Baue eine minimale Startdatei, die sofort laeuft.

```python
import streamlit as st

st.title("Example 01 Simple Agent")
st.write("Step 1: Grundgeruest erstellt.")
```

Schritt 2: Imports und Konstanten
Importiere die benoetigten Module und lege erste Konstanten an.

```python
import streamlit as st
from typing import TypedDict, Annotated
from langgraph.graph import StateGraph, END

st.title("Example 01 Simple Agent")
st.write("Step 2: Kernbausteine geladen.")
```

Schritt 3: Kernlogik erweitern
Fokussiere dich auf: AgentState, process_input.

```python
import streamlit as st

class AgentState:
    def __init__(self):
        pass
```

Schritt 4: Kernlogik erweitern
Fokussiere dich auf: finalize_output, create_graph.

```python
import streamlit as st

def finalize_output(state):
    return "todo"
```

Schritt 5: Vollstaendiges Programm
Kopiere den finalen Stand aus `app.py` und stelle alle Details fertig.
