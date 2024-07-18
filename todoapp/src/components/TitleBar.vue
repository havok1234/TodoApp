<template>
    <div class="title-bar">
      <span class="title-text">TODO</span>
      <div>
        <q-btn flat round @click="toggleTheme">
          <q-icon>
            <img :src="themeIcon"/>
            <q-tooltip>
                Toggle Theme
            </q-tooltip>
          </q-icon>
        </q-btn>
      </div>
    </div>
  </template>

  <script>
  import { ref, computed } from 'vue';
  import { useTodoStore } from '../stores/todo';


  export default {
    setup() {
      const todoStore = useTodoStore();

      const isDarkTheme = computed(() => todoStore.isDarkTheme);

      const toggleTheme = () => {
        todoStore.toggleTheme(!isDarkTheme.value);
      };

      const themeIcon = computed(() => {
        return isDarkTheme.value ? require('../assets/icons/icon-sun.svg') : require('../assets/icons/icon-moon.svg');
      });

      return {
        toggleTheme,
        themeIcon,
      };
    },
  };
  </script>

  <style scoped>
  .title-bar {
    display: flex;
    justify-content: space-between;
    align-items: center;
    max-width: var(--max-component-width-desktop);
    margin: auto;
    margin-bottom: 2rem;
  }

  .title-text {
    font-size: 35px;
    letter-spacing: 1rem;
    font-weight: 700;
    color: var(--title-color);
  }

  .toggle-icon {
    margin-right: 1rem;
  }

  /* Media query for mobile devices */
  @media (max-width: 375px) {
  .title-bar {
    width: var(--max-component-width-mobile);
    margin-bottom: 1rem;
  }

  .title-text {
    font-size: 30px;
    letter-spacing: 1rem;
    margin-bottom: 0.5rem;
  }
}
  </style>
