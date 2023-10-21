<template>
    <div class="ui-lib-select-with-icon">
        <select class="ui-lib-select-with-icon-select" v-model="model">
            <option v-for="m in models">{{ m }}</option>
        </select>
        <svg
            xmlns="http://www.w3.org/2000/svg"
            xmlns:xlink="http://www.w3.org/1999/xlink"
            width="16"
            height="16"
            fill="none"
            class="ui-lib-select-with-icon-icon"
        >
            <defs>
                <path id="down_svg__a" d="M0 0h16v16H0z"></path>
            </defs>
            <g transform="rotate(-90 8 8)">
                <mask id="down_svg__b" fill="#fff">
                    <use xlink:href="#down_svg__a"></use>
                </mask>
                <g mask="url(#down_svg__b)">
                    <path
                        d="M4 8 0 4l4-4"
                        transform="translate(6.333 4)"
                        style="
                            stroke: rgb(51, 51, 51);
                            stroke-width: 1.33333;
                            stroke-opacity: 1;
                            stroke-dasharray: 0, 0;
                        "
                    ></path>
                </g>
            </g>
        </svg>
    </div>
</template>

<script setup>
import { ref, inject } from "vue";

const models = inject("models");
const model = inject("model");
</script>

<style>
.ui-lib-select-with-icon {
    position: relative;
    max-width: -moz-fit-content;
    max-width: fit-content;
}

.ui-lib-select-with-icon .ui-lib-select-with-icon-select {
    height: 100%;
    border: var(--border-in-light);
    padding: 10px 25px 10px 10px;
    border-radius: 10px;
    -webkit-appearance: none;
    -moz-appearance: none;
    appearance: none;
    cursor: pointer;
    background-color: var(--white);
    color: var(--black);
    text-align: center;
}

.ui-lib-select-with-icon .ui-lib-select-with-icon-icon {
    position: absolute;
    top: 50%;
    right: 10px;
    transform: translateY(-50%);
    pointer-events: none;
}
</style>
