import streamlit as st
import modules.functions as functions

todos = functions.get_todos()

def add_todo():
    new_todo= st.session_state["new_todo"]
    todos.append(new_todo+"\n")
    functions.set_todos(todos)


st.title("My Todo App")
st.subheader("This is my todo app")
st.write("This app to increase your productivity.")

for index, todo in enumerate(todos):
    st.checkbox(todo, key=f"checkbox_{index}")

st.text_input(label="", placeholder="Add new todo...",
              on_change=add_todo, key="new_todo")
