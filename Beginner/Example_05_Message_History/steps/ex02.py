import streamlit as st
from typing import TypedDict, Annotated
from langgraph.graph import StateGraph, END
import operator
from datetime import datetime

st.title("Example 05 Message History")
st.write("Step 2: Kernbausteine geladen.")
