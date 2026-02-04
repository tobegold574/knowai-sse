# 贡献指南

感谢您对 KnowAI SSE 的关注！我们欢迎各种形式的贡献。

## 如何贡献

### 报告问题

如果您发现了 bug 或有功能建议，请：

1. 检查 [Issues](https://github.com/tobegold574/knowai-sse/issues) 是否已有相关问题
2. 如果没有，创建新的 Issue，详细描述问题或建议

### 提交代码

1. Fork 本仓库
2. 创建特性分支 (`git checkout -b feature/AmazingFeature`)
3. 提交更改 (`git commit -m 'Add some AmazingFeature'`)
4. 推送到分支 (`git push origin feature/AmazingFeature`)
5. 创建 Pull Request

## 开发规范

### 代码风格

- 使用 Black 格式化代码：`black src/ tests/`
- 使用 Ruff 检查代码：`ruff check src/ tests/`
- 使用 mypy 进行类型检查：`mypy src/`

### 测试

- 为新功能添加测试
- 确保所有测试通过：`pytest tests/ -v`
- 测试覆盖率不应降低

### 文档

- 为公共 API 添加 docstrings
- 更新相关文档

## 提交信息

使用清晰的提交信息：

- `feat`: 新功能
- `fix`: 修复 bug
- `docs`: 文档更新
- `style`: 代码格式（不影响功能）
- `refactor`: 重构
- `test`: 添加测试
- `chore`: 构建过程或辅助工具的变动

示例：

```
feat: 添加新的价值观维度
fix: 修复 JSON 解析错误
docs: 更新 API 文档
```

## 许可证

通过贡献代码，您同意您的贡献将根据 MIT License 进行许可。
