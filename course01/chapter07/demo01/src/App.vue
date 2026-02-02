<script setup>
import { ref } from 'vue';

// 编辑框内容
const noteText = ref('你好，大鹏AI教育！');

// 笔记列表
const notes = ref([]);

// 添加笔记
function addNote() {
  if (noteText.value.trim() !== '') {
    notes.value.push(noteText.value.trim());
    noteText.value = '';
  }
}

// 删除笔记
function deleteNote(index) {
  notes.value.splice(index, 1);
}
</script>

<template>
  <div class="container">
      <h2>我的笔记</h2>
      <input 
        v-model="noteText"
        placeholder="请输入一条笔记"
      >
      <button @click="addNote">添加笔记</button>

      <ul>
        <li v-for="(note, index) in notes" :key="index">
          {{ note }}
          <button @click="deleteNote(index)">删除</button>
        </li>
      </ul>
  </div>
</template>

<style>
* {
  margin: 0;
  padding: 0;
  box-sizing: border-box;
}

.container {
  max-width: 400px;
  margin: 40px auto;
  font-family: Arial, Helvetica, sans-serif;
}
button {
  margin-left: 8px;
}
</style>
