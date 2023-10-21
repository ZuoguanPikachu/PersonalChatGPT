<template>
    <div class="home-sidebar-body">
        <ChatItem
            v-for="chat in chats"
            :title="chat.title"
            :date="chat.date"
            :selected="chat.selected"
        />
    </div>
</template>

<script setup>
import { ref, inject } from "vue";
import axios from "axios";
import ChatItem from "./ChatItem.vue";

const chats = inject("chats");
</script>

<style scoped>
.home-sidebar-body {
    flex: 1 1;
    overflow: auto;
    overflow-x: hidden;
}
</style>
