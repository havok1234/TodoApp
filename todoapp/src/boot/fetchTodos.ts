import { boot } from 'quasar/wrappers';
import { useTodoStore } from 'src/stores/todo';

export default boot(async ({ store }) => {
  const todoStore = useTodoStore(store);
  await todoStore.fetchAndSetTodos();
});
