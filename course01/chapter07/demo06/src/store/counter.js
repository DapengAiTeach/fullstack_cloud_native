import {defineStore} from "pinia";

// 计数器
export const useCounterStore = defineStore('counter', {
    state: () => ({ count: 0}),
    getters: {
        doubleCount: (state) => state.count * 2,
    },
    actions: {
        increment() {
            this.count++
        },
    },
})