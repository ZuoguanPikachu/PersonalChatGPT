<template>
    <div class="chat-chat-body" ref="scrollRef">
        <Message
            v-for="msg in msgList"
            :content="msg.content"
            :role="msg.role"
        />
    </div>
    <ChatInputPanel @send-msg="sendMsg" />
</template>

<script setup>
import { ref, inject, onUpdated } from "vue";
import { io } from "socket.io-client";
import axios from "axios";
import moment from "moment";
import ChatInputPanel from "./ChatInputPanel.vue";
import Message from "./Message.vue";

const socket = io.connect("http://127.0.0.1:5000");
const scrollRef = ref(null);

const chatId = inject("chat-id");
const chatTitle = inject("chat-title");
const msgList = inject("msg-list");
const complementTitle = inject("complement-title");
const newChat = inject("new-chat");
const addMsg = inject("add-msg");
const updateBotMsg = inject("update-bot-msg");
const model = inject("model");

const sendMsg = (usrMsg) => {
    if (chatId.value == "") {
        newChat(moment().format("YYYY/MM/DD HH:mm:ss"));
    }

    addMsg({ role: "user", content: usrMsg.value });
    socket.emit("chat", { model: model.value, msg: msgList.value });
    addMsg({ role: "assistant", content: "" });
};

socket.on("bot_response", function (deltaMsg) {
    if (deltaMsg == "[/response_end]") {
        if (chatTitle.value == "") {
            axios
                .post("http://127.0.0.1:5000/generate-title", {
                    messages: msgList.value,
                })
                .then((response) => {
                    complementTitle(response.data);
                    axios.post("http://127.0.0.1:5000/save-msg", {
                        chatId: chatId.value,
                        msg: msgList.value.slice(-2),
                    });
                });
        } else {
            axios.post("http://127.0.0.1:5000/save-msg", {
                chatId: chatId.value,
                msg: msgList.value.slice(-2),
            });
        }
    } else {
        updateBotMsg(deltaMsg);
    }
});

onUpdated(() => {
    scrollRef.value.scrollTop = scrollRef.value.scrollHeight;
});
</script>

<style scoped>
.chat-chat-body {
    flex: 1 1;
    overflow: auto;
    overflow-x: hidden;
    padding: 20px 20px 40px;
    position: relative;
    overscroll-behavior: none;
}
</style>
