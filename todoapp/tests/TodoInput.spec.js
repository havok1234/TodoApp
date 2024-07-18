import { mount } from '@vue/test-utils';
import TodoInput from '@/components/TodoInput.vue';

describe('TodoInput.vue', () => {
  it('renders input field', () => {
    const wrapper = mount(TodoInput);
    expect(wrapper.find('input').exists()).toBe(true);
  });

  it('emits addTodo event on enter', async () => {
    const wrapper = mount(TodoInput);
    const input = wrapper.find('input');
    await input.setValue('New Todo');
    await input.trigger('keyup.enter');

    expect(wrapper.emitted().addTodo).toBeTruthy();
    expect(wrapper.emitted().addTodo[0]).toEqual(['New Todo']);
  });
});
