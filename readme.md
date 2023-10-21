# PersonalChatGPT

UI源自：[ChatGPT-Next-Web](https://github.com/Yidadaa/ChatGPT-Next-Web)

## 如何使用

1. 添加`config.py`，配置`API_BASE`和`API_KEY`：

    ```python
    API_BASE = "https://xxxxxx"
    API_KEY = "sk-xxxxxx"
    ```

    可在[GPT_API_free](https://github.com/chatanywhere/GPT_API_free)申请免费的API，或者购买低价的API

2. 运行：

    ```bash
    python app.py
    ```

## 自定义

可在webui-vue中，对界面、功能进行添加、修改。修改后，执行：

```bash
npm run build
```

将`dist`中的文件拷贝至`webui`中即可。

## 待实现

* [ ] 文本导入，实现基于大语言模型的知识库