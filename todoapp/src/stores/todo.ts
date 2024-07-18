
import { defineStore } from 'pinia';
import { api } from '../boot/axios';

interface Todo {
  id: string;
  title: string;
  done: boolean;
}

export const useTodoStore = defineStore('todo', {
  state: () => ({
    todos: [] as Todo[],
    filters: ['All', 'Active', 'Completed'],
    selectedFilter: 'All',
    isDarkTheme: true,
  }),
  getters: {
    filteredTodos(state): Todo[] {
      const { todos, selectedFilter } = state;
      if (selectedFilter === 'Active') {
        return todos.filter(todo => !todo.done);
      } else if (selectedFilter === 'Completed') {
        return todos.filter(todo => todo.done);
      }
      return todos;
    },
    itemsLeft(state) {
      return state.todos.filter(todo => !todo.done).length;
    }
  },
  actions: {
    async fetchTodos(filter: string): Promise<void> {
      try {
        const response = await api.get('/todos');
        this.todos = response.data;
      } catch (error) {
        console.error('Error fetching todos:', error);
        throw error;
      }
    },
    async addTodo(newTodo: string): Promise<void> {
      try {
        const response = await api.post('/todos', {
          title: newTodo,
          done: false,
        });
        this.todos.push(response.data);
      } catch (error) {
        console.error('Error adding todo:', error);
        throw error;
      }
    },
    async deleteTodo(id: string): Promise<void> {
      try {
        await api.delete(`/todos/${id}`);
        this.todos = this.todos.filter(todo => todo.id !== id);
      } catch (error) {
        console.error('Error deleting todo:', error);
        throw error;
      }
    },
    async toggleTodoComplete(id: string, done: boolean): Promise<void> {
      try {
        await api.put(`/todos/${id}/toggle`, done );
        const updatedTodo = this.todos.find(t => t.id === id);
        if (updatedTodo) {
          updatedTodo.done = done;
        }
      } catch (error) {
        console.error('Error marking todo as complete:', error);
        throw error;
      }
    },
    async clearCompleted(): Promise<void> {
      try {
        await api.delete('/todos/completed');
        this.todos = this.todos.filter(todo => !todo.done);
      } catch (error) {
        console.error('Error clearing completed todos:', error);
        throw error;
      }
    },
    async updateTodosOrder(order: string[]): Promise<void> {
      try {
        // Assuming your API endpoint for updating todos order is '/todos/reorder'
        await api.put('/todos/reorder', order);
        console.log("Todos order updated successfully.");

        // Update frontend state after successful backend update
        const newTodosOrder = [...this.todos];
        newTodosOrder.sort((a, b) => order.indexOf(a.id) - order.indexOf(b.id));
        this.todos = newTodosOrder;

      } catch (error) {
        console.error("Error updating todos order:", error);
        throw error; // Propagate the error for handling in the calling code
      }
    },
    async fetchAndSetTodos(): Promise<void> {
      await this.fetchTodos(this.selectedFilter);
    },
    async updateSelectedFilter(filter: string): Promise<void> {
      this.selectedFilter = filter;
    },
    async toggleTheme(isDark: boolean): Promise<void> {
      this.isDarkTheme = isDark;
    }
  }
});
