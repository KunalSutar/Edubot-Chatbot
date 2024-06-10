from edubot_creator import EduBotCreator
from streamlit_chat import message
from config import* 
import streamlit as st

@st.cache_resource(show_spinner=True)
def create_edubot():   
    edubotcreater = EduBotCreator()
    edubot = edubotcreater.create_edubot()
    return edubot

edubot = create_edubot()

def infer_edubot(prompt):
    model_out = edubot(prompt)
    answer = model_out['result']
    return answer

def display_conv(history):
    for i in range(len(history['assistant'])):
        message(history['user'][i],is_user=True,key=str(i)+'_user')
        message(history['assistant'][i],key=str(i))
        
def main():
    
    st.title("Edubot")
    st.subheader("A chatbot created using Langchain using CPU for computation")
    
    user_input = st.text_input("Enter your question")
    
    if 'assistant' not in st.session_state:
        st.session_state['assistant']=['Hi! How can I help you?']
        
    if 'user' not in st.session_state:
        st.session_state['user']=['Hey there!']
        
    if st.button("Answer"):
        
        answer = infer_edubot({'query':user_input})
        st.session_state['user'].append(user_input)
        st.session_state['assistant'].append(answer)
        
        if st.session_state['assistant']:
            display_conv(st.session_state)
            
if __name__=="__main__":
    main()