<script setup>
import { ref, computed, provide, onMounted } from "vue";
import { RouterLink, RouterView } from "vue-router";
import axios from "axios";
import SideBar from "./components/SideBar.vue";
import WindowHeader from "./components/WindowHeader.vue";

const chatId = ref("");
const chatTitle = computed(() =>
    chatId.value.split("-").slice(0, -1).join("-")
);
const headerTitle = computed(() => chatTitle);
const chatsRaw = ref([]);
const chats = computed(() =>
    chatsRaw.value.map((item) => {
        return {
            title: item.split("-").slice(0, -1).join("-"),
            date: item.split("-").slice(-1)[0],
            selected: chatId.value == item,
        };
    })
);
const msgList = ref([]);
const models = ref([]);
const model = ref("");

const select = (id) => {
    chatId.value = id;
    axios
        .post("http://127.0.0.1:5000/chat-content", {
            chatId: chatId.value,
        })
        .then((response) => {
            msgList.value = response.data;
        });
};

const remove = (id) => {
    axios.post("http://127.0.0.1:5000/remove", { chatId: id }).then(() => {
        axios.get("http://127.0.0.1:5000/chat-list").then((response) => {
            chatsRaw.value = response.data;
            let flags = response.data.map((item) => item == chatId.value);
            let flag = flags.indexOf(true);
            if (flag == -1) {
                chatId.value = "";
                clearMsg();
            }
        });
    });
};

const newChat = (date) => {
    chatId.value = "-" + date;
    chatsRaw.value.push(chatId.value)
};

const complementTitle = (title) => {
    chatId.value = title + chatId.value;
    chatsRaw.value.pop();
    chatsRaw.value.push(chatId.value)

    axios.post("http://127.0.0.1:5000/add-chat", {
        chatId: chatId.value,
    });
};

const addMsg = (msgItem) => {
    msgList.value.push(msgItem);
};

const updateBotMsg = (deltaMsg) => {
    let botMsgItem = msgList.value.pop();
    botMsgItem.content += deltaMsg;
    msgList.value.push(botMsgItem);
};

const clearMsg = () => {
    msgList.value = [];
};

provide("chat-id", chatId);
provide("chat-title", chatTitle);
provide("chats", chats);
provide("msg-list", msgList);
provide("model", model);
provide("models", models);
provide("complement-title", complementTitle);
provide("new-chat", newChat);
provide("add-msg", addMsg);
provide("update-bot-msg", updateBotMsg);
provide("clear-msg", clearMsg);
provide("select", select);
provide("remove", remove)

onMounted(() => {
    axios.get("http://127.0.0.1:5000/models").then((response) => {
        models.value = response.data;
        model.value = models.value[0];
    });

    axios.get("http://127.0.0.1:5000/chat-list").then((response) => {
        chatsRaw.value = response.data;
    });
});
</script>

<template>
    <div class="home-container home-tight-container">
        <SideBar />
        <div class="home-window-content">
            <WindowHeader :title="headerTitle.value" />
            <RouterView />
        </div>
    </div>
</template>

<style scoped>
.home-container {
    border: var(--border-in-light);
    border-radius: 20px;
    box-shadow: var(--shadow);
    color: var(--black);
    background-color: var(--white);
    min-width: 600px;
    min-height: 370px;
    max-width: 1200px;
    display: flex;
    overflow: hidden;
    box-sizing: border-box;
    width: var(--window-width);
    height: var(--window-height);
}

@media only screen and (min-width: 600px) {
    .home-tight-container {
        --window-width: 100vw;
        --window-height: var(--full-height);
        --window-content-width: calc(100% - var(--sidebar-width));
        border-radius: 20px;
        box-shadow: var(--shadow);
        color: var(--black);
        background-color: var(--white);
        min-width: 600px;
        min-height: 370px;
        max-width: 1200px;
        display: flex;
        overflow: hidden;
        box-sizing: border-box;
        width: var(--window-width);
        height: var(--window-height);
        max-width: 100vw;
        max-height: var(--full-height);
        border-radius: 0;
        border: 0;
    }
}

.home-window-content {
    width: var(--window-content-width);
    height: 100%;
    display: flex;
    flex-direction: column;
}
</style>
