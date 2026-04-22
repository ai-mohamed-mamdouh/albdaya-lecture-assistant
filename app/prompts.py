from langchain_core.prompts import (
    ChatPromptTemplate,
    SystemMessagePromptTemplate,
    HumanMessagePromptTemplate
)

rag_prompt = ChatPromptTemplate.from_messages([
    SystemMessagePromptTemplate.from_template(
        #   Provide source metadata from context after your answer
        '''
          based on the context provided below only.
          without <think> </think>
          you should return answer without any think
        '''),
    HumanMessagePromptTemplate.from_template(
    '''
    Context :
    {context}

    Question :
    {question}
    ''')
])