<template>
    <div class="home-sidebar-actions">
        <button class="button-icon-button button-shadow" @click="query">
            <div class="button-icon-button-text">
                {{ "余额: " + balance }}
            </div>
        </button>
    </div>
</template>

<script setup>
import { ref, onMounted } from "vue";
import axios from "axios";

const balance = ref("——");

const query = () => {
    axios.get("http://127.0.0.1:5000/balance").then((response) => {
        balance.value = response.data;
    });
};

onMounted(() => {
    query();
});
</script>

<style>
.home-sidebar-actions {
    display: inline-flex;
}
</style>
