<template>
  <div class="todo-utils">
    <div class="left-section">
      <span class="items-left">{{ itemsLeft }} items left</span>
    </div>
    <div class="filters-section" v-if="!isMobile">
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
    <div class="clear-section">
      <q-btn flat @click="clearCompleted" class="clear-completed" no-caps>
        Clear Completed
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

    const itemsLeft = computed(() => {return todoStore.itemsLeft;});
    const filters = computed(() => todoStore.filters);
    const selectedFilter = computed(() => todoStore.selectedFilter);

    const selectFilter = (filter) => {
      todoStore.updateSelectedFilter(filter);
    };

    const clearCompleted = () => {
      todoStore.clearCompleted();
    };

    const isMobile = computed(() => {
      return window.innerWidth <= 375;
    });

    return {
      itemsLeft,
      filters,
      selectedFilter,
      selectFilter,
      clearCompleted,
      isMobile,
    };
  },
};
</script>

<style scoped>
.todo-utils {
  display: flex;
  justify-content: space-between;
  align-items: center;
  max-width: var(--max-component-width-desktop);
  margin: auto;
  background-color: var(--component-bg-color);
  padding: 0rem 1rem 0rem 1rem;
  color: var(--accent-color);
  border-radius: 0px 0px 7px 7px;
  border-bottom: 1px solid var(--border-color);
}

.items-left {
  /* Fix font size */
  font-size: 13px;
  white-space: nowrap;
}

.filters {
  display: flex;
}

.filters .q-btn {
  padding: 0.5rem;
  margin: 0 0.25rem;
}

.q-btn {
  font-weight: bold;
  padding: 0rem;
  font-size: 16px;
}

.q-btn:hover {
  color: var(--hover-color)
}

.left-section {
  text-align: left;
  margin-left: 1rem;
}

.clear-section {
  text-align: right;
  margin-right: 1rem;
}

/* Media query for mobile devices */
@media (max-width: 375px) {
  .todo-utils {
    max-width: var(--max-component-width-mobile);
  }

  .left-section, .filters-section, .clear-section {
    text-align: center;
    width: 100%;
  }

  .left-section {
    text-align: left;
    margin-left: 1rem;
  }

  .clear-section {
    text-align: right;
    margin-right: 1rem;
  }

  .clear-completed {
    width: auto;
    text-align: center;
  }
}
</style>
