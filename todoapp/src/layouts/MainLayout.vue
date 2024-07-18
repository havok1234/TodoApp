<template>
  <q-layout view="lHh Lpr lFf">
    <q-page-container class="page-container">
      <!-- Background image container covering the top 35% of the viewport -->
      <div class="background-container" :class="{ 'dark-theme': isDarkTheme }">
        <img :src="backgroundImage" alt="Background Image" class="background-image">
      </div>
      <router-view />
    </q-page-container>
  </q-layout>
</template>

<script>
import { ref, computed, watchEffect } from 'vue';
import { useTodoStore } from '../stores/todo';

export default {
  setup() {
    const todoStore = useTodoStore();

    const isDarkTheme = computed(() => todoStore.isDarkTheme);

    const toggleTheme = () => {
      const body = document.body;
      if (isDarkTheme.value) {
        body.classList.remove('light');
        body.classList.add('dark');
      } else {
        body.classList.remove('dark');
        body.classList.add('light');
      }
    };

    // Paths to desktop background images
    const desktopBackgroundImageLight = require('../assets/images/bg-desktop-light.jpg');
    const desktopBackgroundImageDark = require('../assets/images/bg-desktop-dark.jpg');

    // Paths to mobile background images
    const mobileBackgroundImageLight = require('../assets/images/bg-mobile-light.jpg');
    const mobileBackgroundImageDark = require('../assets/images/bg-mobile-dark.jpg');

    const backgroundImage = computed(() => {
      toggleTheme();
      if (window.innerWidth <= 375) {
        return isDarkTheme.value ? mobileBackgroundImageDark : mobileBackgroundImageLight;
      } else {
        return isDarkTheme.value ? desktopBackgroundImageDark : desktopBackgroundImageLight;
      }
    });

    watchEffect(() => {
      toggleTheme();
    });

    return {
      isDarkTheme,
      backgroundImage,
    };
  },
};
</script>

<style scoped>

.page-container {
  background-color: var(--background-color);
}

.background-container {
  position: fixed;
  top: 0;
  left: 0;
  width: 100vw;
  height: var(--bg-image-height-desktop);
  z-index: 1;
  overflow: hidden;
  background-color: var(--background-color);
}

.background-image {
  width: 100%;
  height: 100%;
  object-fit: cover;
}

@media (max-width: 375px) {
  .background-container {
    height: var(--bg-image-height-mobile);
  }
}
</style>
