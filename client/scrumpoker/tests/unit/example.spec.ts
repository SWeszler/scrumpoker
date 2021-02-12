import { shallowMount } from "@vue/test-utils";
import Login from "@/views/Login.vue";

describe("Test Login", () => {
  it("Test if user is authenticated.", () => {
    const wrapper = shallowMount(Login);
    expect(wrapper.find("button#login").text()).toMatch("Login");
  });
});
