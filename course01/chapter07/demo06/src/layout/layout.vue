<script setup>
import Header from './header.vue'
import Footer from './footer.vue'
</script>
<template>
    <Header/>
    <main class="container-wrapper py-8">
        <router-view />
    </main>
    <Footer/>
</template>
