import streamlit as st
from typing import TypedDict, Annotated, Literal
from langgraph.graph import StateGraph, END
import operator
import math

st.title("Example 07 Tool Calling")
st.write("Step 2: Kernbausteine geladen.")
