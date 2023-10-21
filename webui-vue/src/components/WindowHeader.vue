<template>
    <div class="window-header">
        <div class="window-header-title">
            <div class="window-header-main-title">
                {{ title != "" ? title : "新的对话" }}
            </div>
        </div>
        <div class="window-actions">
            <SelectView />
        </div>
    </div>
</template>

<script setup>
import SelectView from "./SelectView.vue";

defineProps({
    title: String,
});
</script>

<style>
.window-header {
    padding: 14px 20px;
    border-bottom: 1px solid rgba(0, 0, 0, 0.1);
    position: relative;
    display: flex;
    justify-content: space-between;
    align-items: center;
}

.window-header-title {
    max-width: calc(100% - 100px);
    overflow: hidden;
}

.window-header-title .window-header-main-title {
    font-size: 20px;
    font-weight: bolder;
    overflow: hidden;
    text-overflow: ellipsis;
    white-space: nowrap;
    display: block;
    max-width: 50vw;
}

.window-actions {
    display: inline-flex;
}
</style>
