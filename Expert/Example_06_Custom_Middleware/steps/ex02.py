import streamlit as st
from typing import TypedDict, Annotated
from langgraph.graph import StateGraph, END
import operator

st.title("Example 06 Custom Middleware")
st.write("Step 2: Kernbausteine geladen.")
