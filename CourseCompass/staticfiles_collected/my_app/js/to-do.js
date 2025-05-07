document.addEventListener("DOMContentLoaded", function () {
    document.querySelectorAll(".approve").forEach(button => {
        button.addEventListener("click", function () {
            const taskItem = this.closest(".task-item");
            const taskText = taskItem.querySelector("span").textContent;
            const department = taskItem.getAttribute("data-department");
            const username = document.getElementById("username").value.trim();
            const timestamp = new Date().toLocaleString();

            if (!username) {
                alert("Please enter your name before approving a task.");
                return;
            }

            const taskData = {
                task: taskText,
                approvedBy: username,
                department: department,
                time: timestamp
            };

            // Save to localStorage
            const approvedTasks = JSON.parse(localStorage.getItem("approvedTasks")) || [];
            approvedTasks.push(taskData);
            localStorage.setItem("approvedTasks", JSON.stringify(approvedTasks));

            // Remove the task from current list
            taskItem.remove();
        });
    });
});

document.addEventListener("DOMContentLoaded", function () {
    const approvedTasks = JSON.parse(localStorage.getItem("approvedTasks")) || [];
    const approvedList = document.getElementById("approved-tasks");

    approvedTasks.forEach(task => {
        const li = document.createElement("li");
        li.classList.add("task-item");
        li.innerHTML = `
            <strong>${task.task}</strong><br>
            <small>Approved by ${task.approvedBy} on ${task.time} (${task.department})</small>
        `;
        approvedList.appendChild(li);
    });
});