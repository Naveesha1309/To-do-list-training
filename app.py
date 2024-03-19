import chromadb
from chromadb.utils import embedding_functions

try:
    #1
    # Initialize ChromaDB client
    # chroma_client = chromadb.Client()

    #2
    # REFERENCE LINK : https://docs.trychroma.com/usage-guide?lang=py#running-chroma-in-clientserver-mode
    # Example setup of the client to connect to your chroma server
    chroma_client = chromadb.HttpClient(host='localhost', port=8000)


    chroma_client = chromadb.PersistentClient(path="my_chroma_db")

    # Embedding model 
    sentence_transformer_ef = embedding_functions.SentenceTransformerEmbeddingFunction(model_name="all-MiniLM-L6-v2")

    # Create collection
    collection = chroma_client.get_or_create_collection(name="my_collection",embedding_function=sentence_transformer_ef)
    collection.add(documents="Add new task",metadatas=[{"title": "Add new task"}, {"description": "task description"}])
    

    print("ChromaDB collection created successfully.")
except Exception as e:
    print("An error occurred:", str(e))


# collection.add(documents="Add new task",metadatas=[{"title": "Add new task"}, {"description": "task description"}])

# results = collection.query(
#     query_texts="searchinput",
#     n_results=10
# )

from flask import Flask, request, render_template, jsonify

app = Flask(__name__)



@app.route("/", methods=['GET'])
def all():
    response = collection.get()

    # Extracting documents from the response
    task_titles = response.get('documents', [])
    # task_titles = ["a","b"]       #works

    return render_template('todolist.html', len=len(task_titles) ,tasks=task_titles)



@app.route("/submit", methods=['POST'])
def submit():
    task_title = request.form.get('taskTitle')
    task_input = request.form.get('taskInput')

    collection.add(
        documents=[task_title + " " + task_input],
        metadatas=[{"title": task_title}, {"description": task_input}]
    )

    return all()


@app.route("/search", methods=['GET','POST'])
def search():
    query = request.args.get('query')


    results = collection.query(query_texts=query, n_results=10)
    search_results = []

    for result in results:
        # Extract the combined content of the document
        document_content = result

        # Add document content to search results
        search_results.append(document_content)

    # Render the search results in the HTML template
    return render_template('todolist.html', search_results=search_results)


if __name__ == '__main__':
    app.run(debug=True)


