# LangGraph 多模型智能对话系统

## 项目简介

本项目基于 [LangGraph](https://github.com/langchain-ai/langgraph) 框架，集成多种大模型（如 OpenAI、Mistral 等），支持多模型动态切换、流式/标准输出、工具调用等高级功能，适合企业级对话系统、智能助手、AI 工具链等场景。

## 目录结构

```
├── api.py                  # FastAPI 主入口，负责服务启动
├── requirements.txt        # 依赖包列表
├── .env                    # 环境变量（API KEY等，需自行创建）
├── routers/
│   └── chatrouter.py       # 路由定义，chat接口
├── services/ 或 core/
│   └── chat.py             # Chat主流程，模型/graph/输出处理
├── models/
│   ├── llms.py             # 多模型选择与统一接口
│   ├── prompt.py           # 提示词模板与消息生成
│   └── stream_output.py    # 流式/标准输出工厂
├── tools/
│   └── search.py           # 工具节点实现（如Tavily搜索）
├── databases/
│   └── memory.py           # 对话记忆存储
├── configs/
│   └── config.py           # 环境变量与模型配置统一管理
├── utils/
│   └── filter.py           # 输出过滤工具
```

## 快速开始

### 1. 克隆项目

```bash
git clone <你的仓库地址>
cd langgraph
```

### 2. 安装依赖

```bash
pip install -r requirements.txt
```

### 3. 配置环境变量

- 在项目根目录新建 `.env` 文件，写入你的 API KEY 等敏感信息，例如：
  ```
  OPENROUTER_API_KEY=你的OpenRouter密钥
  ```
- 或直接在 `configs/config.py` 里维护模型配置。

### 4. 启动服务

```bash
python api.py
```
- 默认监听 `http://0.0.0.0:8000`

### 5. 测试接口

#### 标准输出接口

```bash
http POST http://127.0.0.1:8000/chat user_input="你好，帮我写一段健康科普视频脚本"
```

#### 流式输出接口（如有）

```bash
http --stream POST http://127.0.0.1:8000/chat user_input="你好，帮我写一段健康科普视频脚本" mode="stream"
```

## 主要特性

- ✅ 多模型统一选择与切换（支持 OpenAI、Mistral 等）
- ✅ 流式/标准输出工厂，接口友好
- ✅ 工具节点与智能体灵活组合（如Tavily搜索）
- ✅ 支持多线程/多会话
- ✅ 环境变量与配置集中管理
- ✅ 完善的异常处理与日志记录
- ✅ 代码结构清晰，易于扩展和维护

## 进阶用法

- **自定义模型/工具**：在 `configs/config.py` 和 `tools/` 目录中扩展即可。
- **多路由/多业务**：在 `routers/` 目录中添加新路由，主入口 `api.py` 自动引入。
- **前端对接**：支持标准JSON和SSE流式输出，便于Web/移动端集成。

## 贡献指南

欢迎提交 issue 和 PR，完善文档、增加新模型/工具、优化性能等！

## License

MIT 