
// https://codepen.io/ryangjchandler/pen/qBOEgjg

function toDoList() {
    return {
        newTodo: "",
        todos: [],
        addToDo() {
            this.todos.push({
                todo: this.newTodo,
                completed: false
            });

            this.newTodo = "";
        },
        toggleToDoCompleted(index) {
            this.todos[index].completed = !this.todos[index].completed;
        },
        deleteToDo(index) {
            this.todos = this.todos.filter((todo, todoIndex) => {
                return index !== todoIndex
            })
        },
        numberOfToDosCompleted() {
            return this.todos.filter(todo => todo.completed).length;
        },
        toDoCount() {
            return this.todos.length
        },
        isLastToDo(index) {
            return this.todos.length - 1 === index
        }
    };
}
