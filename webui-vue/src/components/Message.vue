<template>
    <div
        :class="{
            'chat-chat-message': role == 'assistant',
            'chat-chat-message-user': role == 'user',
        }"
    >
        <div class="chat-chat-message-container">
            <div class="chat-chat-message-item">
                <div class="markdown-body" v-html="marked.parse(content)"></div>
            </div>
        </div>
    </div>
</template>

<script setup>
import { ref, onUpdated, onMounted } from "vue";
import { Marked } from "marked";
import hljs from "highlight.js";
import "highlight.js/styles/github.css";

// copied from marked-highlight
function updateToken(token) {
    return (code) => {
        if (typeof code === "string" && code !== token.text) {
            token.escaped = true;
            token.text = code;
        }
    };
}

const escapeTest = /[&<>"']/;
const escapeReplace = new RegExp(escapeTest.source, "g");
const escapeTestNoEncode = /[<>"']|&(?!(#\d{1,7}|#[Xx][a-fA-F0-9]{1,6}|\w+);)/;
const escapeReplaceNoEncode = new RegExp(escapeTestNoEncode.source, "g");
const escapeReplacements = {
    "&": "&amp;",
    "<": "&lt;",
    ">": "&gt;",
    '"': "&quot;",
    "'": "&#39;",
};
const getEscapeReplacement = (ch) => escapeReplacements[ch];
function escape(html, encode) {
    if (encode) {
        if (escapeTest.test(html)) {
            return html.replace(escapeReplace, getEscapeReplacement);
        }
    } else {
        if (escapeTestNoEncode.test(html)) {
            return html.replace(escapeReplaceNoEncode, getEscapeReplacement);
        }
    }
    return html;
}

const marked = new Marked({
    breaks: true,
    sanitize: false,
    walkTokens(token) {
        if (token.type !== "code") {
            return;
        }

        const lang = (token.lang || "").match(/\S*/)[0];
        const language = hljs.getLanguage(lang) ? lang : "plaintext";
        const code = hljs.highlight(token.text, { language }).value;
        updateToken(token)(code);
    },
    renderer: {
        code(code, infoString, escaped) {
            const lang = (infoString || "").match(/\S*/)[0];
            const classAttr = lang ? ` class="language-${escape(lang)}"` : "";
            code = code.replace(/\n$/, "");
            return `<pre class="hljs"><code${classAttr}>${
                escaped ? code : escape(code, true)
            }\n</code></pre>`;
        },
    },
});

defineProps({
    role: String,
    content: String,
});

const TypeSet = async function (elementId) {
    if (!window.MathJax) {
        return;
    }
    window.MathJax.startup.promise = window.MathJax.startup.promise
        .then(() => {
            return window.MathJax.typesetPromise();
        })
        .catch((err) => console.log("Typeset failed: " + err.message));
    return window.MathJax.startup.promise;
};

onUpdated(() => {
    TypeSet();
});

onMounted(() => {
    TypeSet();
});
</script>

<style>
.chat-chat-message-user {
    display: flex;
    flex-direction: row-reverse;
}

.chat-chat-message-user > .chat-chat-message-container {
    align-items: flex-end;
}

.chat-chat-message-user
    > .chat-chat-message-container
    > .chat-chat-message-item {
    background-color: var(--second);
}

.chat-chat-message-item {
    box-sizing: border-box;
    max-width: 100%;
    margin-top: 10px;
    border-radius: 10px;
    background-color: rgba(0, 0, 0, 0.05);
    padding: 10px;
    font-size: 14px;
    -webkit-user-select: text;
    -moz-user-select: text;
    user-select: text;
    word-break: break-word;
    border: var(--border-in-light);
    position: relative;
    transition: all 0.3s ease;
}

.chat-chat-message {
    display: flex;
    flex-direction: row;
}

.chat-chat-message-container {
    max-width: var(--message-max-width);
    display: flex;
    flex-direction: column;
    align-items: flex-start;
}

.chat-chat-message-item {
    box-sizing: border-box;
    max-width: 100%;
    margin-top: 10px;
    border-radius: 10px;
    background-color: rgba(0, 0, 0, 0.05);
    padding: 10px;
    font-size: 14px;
    -webkit-user-select: text;
    -moz-user-select: text;
    user-select: text;
    word-break: break-word;
    border: var(--border-in-light);
    position: relative;
    transition: all 0.3s ease;
}
</style>
