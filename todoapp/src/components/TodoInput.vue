<!-- TodoInput.vue -->
<template>
    <div class="todo-input">
        <div class="checkbox-circle"></div>
        <q-input borderless v-model="newTodo" placeholder="Add a new Todo here" @keyup.enter="addTodo" class="input-field no-border-line" />
    </div>
</template>

  <script lang="ts">
  import { defineComponent, ref } from 'vue';
  import { useTodoStore } from '../stores/todo';

  export default defineComponent({
    setup() {
      const newTodo = ref('');
      const todoStore = useTodoStore();

      const addTodo = () => {
        if (newTodo.value.trim() === '') return;
        todoStore.addTodo(newTodo.value);
        newTodo.value = '';
      };

      return {
        newTodo,
        addTodo
      };
    }
  });
  </script>

<style scoped>
.todo-input {
  max-width: var(--max-component-width-desktop);
  margin: auto;
  background-color: var(--component-bg-color);
  border-radius: 7px;
  display: flex;
  align-items: center;
  padding: 0.5rem;
  height: 3.5rem
}

.checkbox-circle {
  width: 20px;
  height: 20px;
  border: 1px solid var(--border-color);
  border-radius: 50%;
  margin-right: 0.5rem;
  margin-left: 1.25rem
}

.input-field {
  flex: 1;
  margin-left: 1.1rem;
  border: none;
  box-shadow: none;
}
.q-input::v-deep(.q-field__native) {
    color: var(--text-color);
    font-size: 18px;
}

/* Media query for mobile devices */
@media (max-width: 375px) {
  .todo-input {
    max-width: var(--max-component-width-mobile);
    margin: auto;
    margin-top: 20px;
  }

  .checkbox-circle {
    width: 18px;
    height: 18px;
    margin-right: 0.5rem;
    margin-left: 1rem;
  }

  .input-field {
    margin-left: 1.5rem;
  }
}
</style>
