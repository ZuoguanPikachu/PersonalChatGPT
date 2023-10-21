<template>
    <div class="home-sidebar-tail">
        <BalanceShower />
        <NewChatBtn />
    </div>
</template>

<script setup>
import BalanceShower from "./BalanceShower.vue";
import NewChatBtn from "./NewChatBtn.vue";
</script>

<style>
.home-sidebar-tail {
    display: flex;
    justify-content: space-between;
    padding-top: 20px;
}
</style>
