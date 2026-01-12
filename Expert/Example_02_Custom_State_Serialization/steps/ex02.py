import streamlit as st
from typing import TypedDict, Annotated
from langgraph.graph import StateGraph, END
import operator

st.title("Example 02 Custom State Serialization")
st.write("Step 2: Kernbausteine geladen.")
