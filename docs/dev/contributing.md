# Contributing Guide

Thank you for your interest in KnowAI SSE! We welcome all forms of contributions.

## How to Contribute

### Report Issues

If you find a bug or have feature suggestions:

1. Check [Issues](https://github.com/your-org/knowai-sse/issues) for existing related issues
2. If none exists, create a new Issue with detailed description of the problem or suggestion

### Submit Code

1. Fork this repository
2. Create a feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Create a Pull Request

## Development Standards

### Code Style

- Format code with Black: `black src/ tests/`
- Check code with Ruff: `ruff check src/ tests/`
- Type check with mypy: `mypy src/`

### Testing

- Add tests for new features
- Ensure all tests pass: `pytest tests/ -v`
- Test coverage should not decrease

### Documentation

- Add docstrings for public APIs
- Update relevant documentation

## Commit Messages

Use clear commit messages:

- `feat`: New feature
- `fix`: Bug fix
- `docs`: Documentation update
- `style`: Code formatting (no functional changes)
- `refactor`: Code refactoring
- `test`: Adding tests
- `chore`: Build process or auxiliary tool changes

Examples:

```
feat: add new value dimension
fix: fix JSON parsing error
docs: update API documentation
```

## License

By contributing code, you agree that your contributions will be licensed under the MIT License.
