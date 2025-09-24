# Contributing to DECIMA

Thank you for your interest in contributing to **DECIMA**!  
We welcome contributions from the community, whether they are bug reports, feature requests, documentation improvements, or code contributions.

---

## 🛠 How to contribute

### 1. Reporting issues
- Check the [issue tracker](https://github.com/quentinducasse/decima/issues) to see if your problem has already been reported.
- If not, open a new issue and include:
  - A clear description of the problem or feature request.
  - Steps to reproduce (if it’s a bug).
  - Your operating system, Python version, and MCNPTools version (if relevant).
  - Example input files (PTRAC, MCTAL, etc.) if applicable.

### 2. Suggesting new features
- Feel free to open a **feature request** issue.
- Explain the use case and why it would be useful for the community.
- If you can, suggest how it might be implemented.

### 3. Submitting code changes
1. Fork the repository and clone your fork.
2. Create a new branch for your changes:
   ```bash
   git checkout -b feature/my-feature
   ```
3. Install the development dependencies:
   ```bash
   pip install -r requirements.txt
   ```
4. Make your changes with clear, concise commits.
5. Run the test suite to ensure everything works:
   ```bash
   pytest
   ```
6. Push your branch and open a Pull Request (PR) against `main`.

---

## ✅ Coding guidelines
- Follow [PEP8](https://peps.python.org/pep-0008/) for Python code style.
- Use English for code, comments, and commit messages.
- Keep functions focused and modular.
- Include docstrings (`"""..."""`) for public classes and methods.

---

## 🧪 Tests
- All new functionality should include tests in the `tests/` folder.
- Pull requests without tests may take longer to review.

---

## 📖 Documentation
- If you add or change functionality, update the documentation in:
  - `README.md`
  - Inline docstrings
- Screenshots or example queries are encouraged if they improve clarity.

---

## 💬 Getting help
- For bugs, please provide a **minimal reproducible example**.

---

## 📜 License
By contributing, you agree that your contributions will be licensed under the [Apache License 2.0](LICENSE).

---

