function addTask() {

    var taskTitle = document.getElementById("taskTitle").value;
    var taskInput = document.getElementById("taskInput").value;

    if (taskTitle.trim() === '') {
        alert("Task title cannot be empty!");
        return;
    }

    var li = document.createElement("li");
    li.className = "task-item";

    var checkbox = document.createElement("input");
    checkbox.type = "checkbox";

    var spanTitle = document.createElement("span");
    spanTitle.textContent = taskTitle;

    // Create a span for the task input
    var spanInput = document.createElement("span");
    spanInput.style.display = "none"; // Initially hide the task input span
    spanInput.textContent = taskInput;

    var infoBtn = document.createElement("button");
    infoBtn.className = "info-btn";
    infoBtn.textContent = "🛈";

    infoBtn.addEventListener("click", function() {
        alert(spanInput.textContent);
    });


    var deleteBtn = document.createElement("button");
    deleteBtn.className = "delete-btn";
    deleteBtn.textContent = "🗑️";

    deleteBtn.addEventListener("click", function() {
        li.remove();
    });

    // Append elements to the list item
    li.appendChild(checkbox);
    li.appendChild(spanTitle);
    li.appendChild(spanInput);
    li.appendChild(infoBtn);
    li.appendChild(deleteBtn);

    // Append the list item to the task list
    var taskList = document.getElementById("taskList");
    taskList.appendChild(li);

    // Clear input fields after adding task
    document.getElementById("taskTitle").value = "";
    document.getElementById("taskInput").value = "";
}
