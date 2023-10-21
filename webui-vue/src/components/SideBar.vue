<template>
    <div class="home-sidebar">
        <SideBarHeader />
        <SideBarBody />
        <SideBarTail />
    </div>
</template>

<script setup>
import SideBarHeader from "./SideBarHeader.vue";
import SideBarBody from "./SideBarBody.vue";
import SideBarTail from "./SideBarTail.vue";
</script>

<style>
.home-sidebar {
    top: 0;
    width: var(--sidebar-width);
    box-sizing: border-box;
    padding: 20px;
    background-color: var(--second);
    display: flex;
    flex-direction: column;
    box-shadow: inset -2px 0 2px 0 rgba(0, 0, 0, 0.05);
    position: relative;
    transition: width 0.05s ease;
}
</style>
