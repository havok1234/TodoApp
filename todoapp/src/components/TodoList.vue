<template>
  <div class="todo-list">
    <q-list bordered>
      <q-item v-for="todo in filteredTodos" :key="todo.id" clickable @click="handleTodoClick(todo)">
        <q-card
          class="todo-card"
          :key="todo.id"
          draggable="true"
          @dragstart="handleDragStart($event, todo)"
          @dragover.prevent
          @drop="handleDrop($event, todo)"
        >
          <q-item-section avatar>
            <q-checkbox
              v-model="todo.done"
              @update:model-value="handleCheckboxChange(todo.id, todo.done)"
              v-bind:class="{ 'checkbox-bg' : todo.done}"
            >
            <q-tooltip v-if="todo.done">
                Uncheck
            </q-tooltip>
            <q-tooltip v-if="!todo.done">
                Check
            </q-tooltip>
            </q-checkbox>
          </q-item-section>
          <q-item-section>
            <span
              :class="{ 'todo-strikethrough': todo.done }"
            >
              {{ todo.title }}
            </span>
          </q-item-section>
          <q-item-section side>
            <q-btn
              flat
              round
              @click="deleteTodo(todo.id)"
              class="icon-delete-btn"
            >
              <q-tooltip>
                Delete
              </q-tooltip>
              <q-icon>
                <img src="../assets/icons/icon-cross.svg" class="icon-delete-img"/>
              </q-icon>
            </q-btn>
          </q-item-section>
        </q-card>
      </q-item>
    </q-list>
  </div>
</template>


<script lang="ts">
import { ref, computed } from 'vue'
import { useTodoStore } from '../stores/todo';

export default {
  setup() {

    const todoStore = useTodoStore();

    const filteredTodos = computed(() => todoStore.filteredTodos);

    const deleteTodo = (id: string) => {
      todoStore.deleteTodo(id);
    };

    const handleCheckboxChange = (id: string, done: boolean) => {
      todoStore.toggleTodoComplete(id, done);
    };

    const handleTodoClick = (todo: any) => {
      todo.done = !todo.done;
      handleCheckboxChange(todo.id, todo.done);
    };

    let touchTodoId: string | null = null;

    // const handleDragStart = (event: DragEvent | TouchEvent, todo: any) => {
    //   // For mouse events
    //   if (event instanceof DragEvent) {
    //     event.dataTransfer!.setData('text/plain', todo.id);
    //   }
    //   // For touch events
    //   else if (event instanceof TouchEvent) {
    //     touchTodoId = todo.id;
    //   }
    // };

    // const handleDrop = (event: DragEvent | TouchEvent, targetTodo: any) => {
    //   event.preventDefault();

    //   // Get the dragged todo id based on event type
    //   let draggedTodoId: string;
    //   if (event instanceof DragEvent) {
    //     draggedTodoId = event.dataTransfer!.getData('text/plain');
    //   } else if (event instanceof TouchEvent && touchTodoId) {
    //     draggedTodoId = touchTodoId;
    //     touchTodoId = null; // Reset touchTodoId after use
    //   } else {
    //     return; // Exit if no valid todo id is found
    //   }

    //   const targetIndex = filteredTodos.value.findIndex(todo => todo.id === targetTodo.id);
    //   const draggedIndex = filteredTodos.value.findIndex(todo => todo.id === draggedTodoId);

    //   if (draggedIndex !== -1 && targetIndex !== -1 && draggedIndex !== targetIndex) {
    //     const updatedTodos = [...filteredTodos.value];
    //     const [draggedTodo] = updatedTodos.splice(draggedIndex, 1);
    //     updatedTodos.splice(targetIndex, 0, draggedTodo);

    //     todoStore.updateTodosOrder(updatedTodos.map(todo => todo.id));
    //   }
    // };
// Desktop drag and drop handlers
    const handleDragStart = (event: DragEvent, todo: any) => {
      event.dataTransfer!.setData('text/plain', todo.id);
    };

    const handleDrop = (event: DragEvent, targetTodo: any) => {
      event.preventDefault();
      const draggedTodoId = event.dataTransfer!.getData('text/plain');
      const targetIndex = filteredTodos.value.findIndex(todo => todo.id === targetTodo.id);
      const draggedIndex = filteredTodos.value.findIndex(todo => todo.id === draggedTodoId);

      if (draggedIndex !== -1 && targetIndex !== -1 && draggedIndex !== targetIndex) {
        const updatedTodos = [...filteredTodos.value];
        const [draggedTodo] = updatedTodos.splice(draggedIndex, 1);
        updatedTodos.splice(targetIndex, 0, draggedTodo);

        todoStore.updateTodosOrder(updatedTodos.map(todo => todo.id));
      }
    };

    // Mobile touch handlers
    const handleTouchStart = (event: TouchEvent, todo: any) => {
      const target = event.target as HTMLElement | null;
    if (target) {
      target.dataset.todoId = todo.id; // Store todo id for touch interactions
    }
    };

    const handleTouchEnd = (event: TouchEvent, targetTodo: any) => {
      event.preventDefault();
      const target = event.target as HTMLElement | null;
      if (target && target.dataset.todoId) {
      const draggedTodoId = target.dataset.todoId;
      const targetIndex = filteredTodos.value.findIndex(todo => todo.id === targetTodo.id);
      const draggedIndex = filteredTodos.value.findIndex(todo => todo.id === draggedTodoId);

      if (draggedIndex !== -1 && targetIndex !== -1 && draggedIndex !== targetIndex) {
        const updatedTodos = [...filteredTodos.value];
        const [draggedTodo] = updatedTodos.splice(draggedIndex, 1);
        updatedTodos.splice(targetIndex, 0, draggedTodo);

        todoStore.updateTodosOrder(updatedTodos.map(todo => todo.id));
      }
  }
    };
    return {
      filters: computed(() => todoStore.filters),
      selectedFilter: computed(() => todoStore.selectedFilter),
      filteredTodos,
      deleteTodo,
      handleCheckboxChange,
      handleTodoClick,
      handleDragStart,
      handleDrop,
      handleTouchStart,
      handleTouchEnd
    };
  }
}
</script>

<style scoped>
.todo-list {
  max-width: var(--max-component-width-desktop);
  margin: auto;
  background-color: var(--component-bg-color);
  color: var(--text-color);
  border-radius: 7px 7px 0px 0px;
  max-height: 22.5rem;
  min-height: 22.5rem;
  overflow-y: auto;
  margin-top: 20px;
}

.todo-strikethrough {
  text-decoration: line-through;
  color: var(--accent-color);
}

.icon-delete-img {
  width: 14px;
  height: 14px;
}

.q-item {
  border-bottom: 1px solid var(--border-color);
  padding: 8px 16px 0px 16px
}

.q-item:hover::v-deep(.q-focus-helper) {
  opacity: 0;
}

.q-btn.flat.round.icon-delete-btn:hover {
  background-color: transparent;
  color: inherit;
  box-shadow: none;
}

/* Make checkbox round */
.q-checkbox::v-deep(.q-checkbox__bg) {
  width: 20px;
  height: 20px;
  border: 1px solid var(--border-color);
  border-radius: 50%;
  background-color: transparent;
}

/* Apply gradient to checkbox border on hover */
.q-checkbox:hover::v-deep(.q-checkbox__bg) {
  border-radius: 50%;
  border: 1px solid transparent;
  background: linear-gradient(to right, #33ccff, #d021e9) border-box;
  -webkit-mask:
    linear-gradient(#fff 0 0) padding-box,
    linear-gradient(#fff 0 0);
  -webkit-mask-composite: xor;
          mask-composite: exclude;
}

/* Apply gradient on checkbox background when checked */
.checkbox-bg.q-checkbox::v-deep(.q-checkbox__bg) {
  border-radius: 50%;
  border: 1px solid transparent;
  background: linear-gradient(to right, #33ccff, #d021e9) border-box;
}

.todo-card {
  cursor: pointer;
  margin-bottom: 8px;
  width: 100%;
  background-color: transparent;
  box-shadow: none;
  display: flex;
}

/* Media queries for mobile device */
@media (max-width: 375px) {
  .todo-list {
    max-width: var(--max-component-width-mobile);
    margin: auto;
    margin-top: 20px;
  }

  .q-item-section {
    padding: 8px;
  }

  .icon-delete-img {
    width: 12px;
    height: 12px;
  }

  .q-checkbox::v-deep(.q-checkbox__bg) {
    width: 18px;
    height: 18px;
  }
}

</style>
