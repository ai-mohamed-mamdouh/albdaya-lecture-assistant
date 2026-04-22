# import streamlit as st
# from app.config import FILE_PATH

# # 1) ingest_service.py (load docs and store) Done
# from app.ingest_service import load_and_splite_docs , save_lecture_chunks


# chunks = load_and_splite_docs(docs_path=FILE_PATH)
# print('load data  DONE......')
# st.write('load DONE....')
# save_lecture_chunks(chunks=chunks , lecture_name='ml_project')
# print('save in vector database DONE......')
# print(" ----")
# # print(len(chunks))
# st.write('save DONE....')

# #2) rag_service.py (search in v db) done..
# from app.rag_service import search_in_lectures
# result = search_in_lectures('File Upload')
# print('retreive done....')
# st.write(result)

# # 3) chat_service done...
# from app.chat_service import out_put

# result = out_put('whats is Preprocessing  should i do ?')
# st.write('out put is done ....')
# st.write(result)
