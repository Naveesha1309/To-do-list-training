import chromadb

try:
    # Initialize ChromaDB client
    chroma_client = chromadb.Client()

    # Create a collection
    collection = chroma_client.create_collection(name="my_collection")

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
    task_titles = [doc['title'] for doc in collection.metadata]
    return render_template('todolist.html', tasks=task_titles)

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


