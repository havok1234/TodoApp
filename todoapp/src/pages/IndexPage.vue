<template>
  <q-page class="q-page-contents">
    <title-bar />
    <todo-input />
    <todo-list />
    <todo-utils />
    <todo-filters-mobile v-if="isMobile" />
  </q-page>
</template>

<script>
import TodoList from 'components/TodoList.vue';
import TodoUtils from 'components/TodoUtils.vue';
import TitleBar from 'components/TitleBar.vue';
import TodoInput from 'components/TodoInput.vue'
import TodoFiltersMobile from 'components/TodoFiltersMobile.vue';
import { computed } from 'vue';

export default {
  components: {
    TodoList,
    TodoUtils,
    TitleBar,
    TodoInput,
    TodoFiltersMobile
  },
  setup() {

    const isMobile = computed(() => {
      return window.innerWidth <= 375;
    });

    return {
      isMobile
    }
  }
};
</script>

<style scoped>
.q-page-contents {
  margin-top: 4rem;
  z-index: 2;
}

@media (max-width: 375px) {
  .q-page-contents {
    margin-top: 2.5rem;
  }
}
</style>
