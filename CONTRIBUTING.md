# Contributing to LangChain Tutorial

Thank you for your interest in contributing to the LangChain Tutorial repository! This document provides guidelines for contributing.

## How to Contribute

### Reporting Issues

- Check if the issue already exists
- Provide a clear description of the problem
- Include steps to reproduce (if applicable)
- Mention your environment (OS, Python version, etc.)

### Suggesting Examples

We welcome suggestions for new tutorial examples! Please:
1. Open an issue describing the proposed example
2. Explain what LangChain feature it would demonstrate
3. Describe the learning objectives

### Adding New Examples

If you want to add a new example:

1. **Follow the existing structure**:
   ```python
   """
   Example N: [Title]
   
   This example demonstrates:
   - Feature 1
   - Feature 2
   - Feature 3
   
   Prerequisites:
   - Required API keys or setup
   """
   ```

2. **Include clear comments**: Explain each step

3. **Add error handling**: Check for API keys and handle exceptions

4. **Update README.md**: Add your example to the list

5. **Test thoroughly**: Ensure the example works

### Improving Documentation

- Fix typos or unclear explanations
- Add more details to existing examples
- Improve code comments
- Update the README with better descriptions

## Code Style

- Follow PEP 8 guidelines
- Use meaningful variable names
- Add docstrings to functions
- Keep functions focused and simple
- Include type hints where appropriate

## Example Template

```python
"""
Example N: [Descriptive Title]

This example demonstrates:
- [Feature 1]
- [Feature 2]

Prerequisites:
- [Requirement 1]
"""

import os
from dotenv import load_dotenv
# ... other imports

load_dotenv()

def main():
    """
    Main function with clear description.
    """
    print("=" * 50)
    print("Example N: [Title]")
    print("=" * 50)
    
    # Check API key
    if not os.getenv("OPENAI_API_KEY"):
        print("Error: OPENAI_API_KEY not found")
        return
    
    # Your code here with clear steps
    print("\nStep 1: ...")
    
    # More steps...
    
    print("\n" + "=" * 50)
    print("Example completed!")
    print("=" * 50)

if __name__ == "__main__":
    main()
```

## Pull Request Process

1. Fork the repository
2. Create a new branch: `git checkout -b feature/your-feature-name`
3. Make your changes
4. Test your changes
5. Commit with clear messages: `git commit -m "Add: description"`
6. Push to your fork: `git push origin feature/your-feature-name`
7. Open a Pull Request

## Pull Request Guidelines

- Provide a clear description of changes
- Reference any related issues
- Ensure code passes basic syntax checks
- Update documentation if needed
- Keep changes focused (one feature/fix per PR)

## Testing

Before submitting:
- Run all examples to ensure they work
- Check for syntax errors: `python -m py_compile examples/*.py`
- Verify dependencies are listed in requirements.txt
- Test with a fresh virtual environment

## Dependencies

When adding new dependencies:
- Use stable, well-maintained packages
- Add to requirements.txt with version pinning
- Justify the need in your PR description

## Questions?

Feel free to:
- Open an issue for questions
- Start a discussion on GitHub
- Reach out to maintainers

## Code of Conduct

- Be respectful and constructive
- Welcome newcomers
- Focus on what's best for the community
- Show empathy towards other contributors

## License

By contributing, you agree that your contributions will be licensed under the MIT License.

Thank you for contributing! 🎉
