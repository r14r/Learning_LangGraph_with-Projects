import streamlit as st
from typing import TypedDict, Annotated
from langgraph.graph import StateGraph, END
import operator

st.title("Example 08 Complex Error Recovery")
st.write("Step 2: Kernbausteine geladen.")
