<template>
  <div class="todo-filters-mobile">
    <div class="filters">
      <q-btn
        v-for="filter in filters"
        :key="filter"
        flat
        @click="selectFilter(filter)"
        :color="filter === selectedFilter ? 'primary' : ''"
        no-caps
      >
        {{ filter }}
      </q-btn>
    </div>
  </div>
</template>

<script>
import { computed } from 'vue';
import { useTodoStore } from '../stores/todo';

export default {
  setup() {
    const todoStore = useTodoStore();

    const filters = computed(() => todoStore.filters);
    const selectedFilter = computed(() => todoStore.selectedFilter);

    const selectFilter = (filter) => {
      todoStore.updateSelectedFilter(filter);
    };

    return {
      filters,
      selectedFilter,
      selectFilter,
    };
  },
};
</script>

<style scoped>
.todo-filters-mobile {
  width: var(--max-component-width-mobile);
  text-align: center;
  background-color: var(--component-bg-color);
  padding: 0rem 1rem 0rem 1rem;
  color: var(--accent-color);
  border-radius: 7px;
  border: 1px solid var(--border-color);
  margin: auto;
  margin-top: 1.2rem;

}
.filters {
  display: flex;
  flex-wrap: wrap;
  justify-content: center;
}

.filters .q-btn {
  font-size: 16;
  padding: 0.5rem;
  margin: 0.5rem;
  font-weight: bold;
}
</style>
