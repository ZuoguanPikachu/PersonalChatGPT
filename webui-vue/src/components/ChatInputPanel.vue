<template>
    <div class="chat-chat-input-panel">
        <div class="chat-chat-input-panel-inner">
            <textarea
                class="chat-chat-input"
                rows="3"
                v-model="msg"
                @keydown.enter.exact="sendMsg"
            ></textarea>
            <button
                class="button-icon-button chat-chat-input-send button-primary clickable"
                @click="sendMsg"
            >
                <div class="button-icon-button-icon">
                    <svg
                        xmlns="http://www.w3.org/2000/svg"
                        xmlns:xlink="http://www.w3.org/1999/xlink"
                        width="16"
                        height="16"
                        fill="none"
                    >
                        <defs>
                            <path
                                id="send-white_svg__a"
                                d="M0 0h16v16H0z"
                            ></path>
                        </defs>
                        <g>
                            <mask id="send-white_svg__b" fill="#fff">
                                <use xlink:href="#send-white_svg__a"></use>
                            </mask>
                            <g mask="url(#send-white_svg__b)">
                                <path
                                    transform="translate(1.333 2)"
                                    d="M0 4.71 6.67 6l1.67 6.67L12.67 0 0 4.71Z"
                                    style="
                                        stroke: rgb(255, 255, 255);
                                        stroke-width: 1.33333;
                                        stroke-opacity: 1;
                                        stroke-dasharray: 0, 0;
                                    "
                                ></path>
                                <path
                                    transform="translate(8.003 6.117)"
                                    d="M0 1.89 1.89 0"
                                    style="
                                        stroke: rgb(255, 255, 255);
                                        stroke-width: 1.33333;
                                        stroke-opacity: 1;
                                        stroke-dasharray: 0, 0;
                                    "
                                ></path>
                            </g>
                        </g>
                    </svg>
                </div>
                <div class="button-icon-button-text">发送</div>
            </button>
        </div>
    </div>
</template>

<script setup>
import { ref } from "vue";

const msg = ref("");
const emit = defineEmits(["send-msg"]);
const sendMsg = (event) => {
    event.preventDefault();
    if (msg.value.trim().length != 0) {
        emit("send-msg", msg);
        msg.value = "";
    }
};
</script>

<style scoped>
.chat-chat-input-panel {
    position: relative;
    width: 100%;
    padding: 10px 20px 20px;
    box-sizing: border-box;
    flex-direction: column;
    border-top: var(--border-in-light);
    box-shadow: var(--card-shadow);
}

.chat-chat-input-panel-inner {
    display: flex;
    flex: 1 1;
}

.chat-chat-input {
    height: 100%;
    width: 100%;
    border-radius: 10px;
    border: var(--border-in-light);
    box-shadow: 0 -2px 5px rgba(0, 0, 0, 0.03);
    background-color: var(--white);
    color: var(--black);
    font-family: inherit;
    padding: 10px 90px 10px 14px;
    resize: none;
    outline: none;
    box-sizing: border-box;
    min-height: 68px;
}

.chat-chat-input:focus {
    border: 1px solid var(--primary);
}

.chat-chat-input-send {
    background-color: var(--primary);
    color: #fff;
    position: absolute;
    right: 30px;
    bottom: 32px;
}

textarea {
    font-size: 14px;
}
</style>
