# 🤝 Contributing to Machine Learning Algorithms

First off, **thank you** for considering contributing to this project! It's people like you that make this repository a great learning resource for the ML community. ❤️

## 📋 Table of Contents

- [Code of Conduct](#-code-of-conduct)
- [How Can I Contribute?](#-how-can-i-contribute)
- [Getting Started](#-getting-started)
- [Development Workflow](#-development-workflow)
- [Style Guidelines](#-style-guidelines)
- [Commit Messages](#-commit-messages)
- [Pull Request Process](#-pull-request-process)
- [Community](#-community)

---

## 📜 Code of Conduct

This project and everyone participating in it is governed by our commitment to providing a welcoming and inspiring community for all.

### Our Pledge

We pledge to make participation in this project a harassment-free experience for everyone, regardless of:
- Age, body size, disability, ethnicity
- Gender identity and expression
- Level of experience, education
- Nationality, personal appearance, race, religion
- Sexual identity and orientation

### Our Standards

**Examples of behavior that contributes to a positive environment:**
- ✅ Using welcoming and inclusive language
- ✅ Being respectful of differing viewpoints
- ✅ Gracefully accepting constructive criticism
- ✅ Focusing on what is best for the community
- ✅ Showing empathy towards other community members

**Examples of unacceptable behavior:**
- ❌ Trolling, insulting/derogatory comments, and personal attacks
- ❌ Public or private harassment
- ❌ Publishing others' private information
- ❌ Other conduct which could reasonably be considered inappropriate

---

## 🎯 How Can I Contribute?

There are many ways you can contribute to this project:

### 🐛 Reporting Bugs

Found a bug? Help us fix it!

**Before submitting a bug report:**
- Check the existing issues to avoid duplicates
- Ensure you're using the latest version of the code
- Verify the bug is reproducible

**When submitting a bug report, include:**
- Clear, descriptive title
- Steps to reproduce the issue
- Expected vs. actual behavior
- Screenshots (if applicable)
- Environment details (OS, Python version, library versions)
- Relevant code snippets or error messages

**Template:**
```markdown
## Bug Description
[Clear description of the bug]

## Steps to Reproduce
1. Go to '...'
2. Run '...'
3. See error

## Expected Behavior
[What you expected to happen]

## Actual Behavior
[What actually happened]

## Environment
- OS: [e.g., Windows 11, Ubuntu 22.04]
- Python Version: [e.g., 3.9.7]
- Library Versions: [numpy==1.21.0, etc.]

## Additional Context
[Any other relevant information]
```

### 💡 Suggesting Enhancements

Have an idea to make this project better?

**Before submitting an enhancement:**
- Check if the enhancement has already been suggested
- Ensure it aligns with the project's goals

**When suggesting an enhancement, include:**
- Clear, descriptive title
- Detailed description of the proposed feature
- Rationale: Why is this enhancement valuable?
- Possible implementation approach
- Examples or mockups (if applicable)

### 📝 Improving Documentation

Documentation improvements are always welcome!

**You can help by:**
- Fixing typos and grammatical errors
- Clarifying confusing explanations
- Adding examples to existing notebooks
- Creating tutorials or guides
- Translating documentation
- Improving code comments

### 🧮 Adding New Algorithms

Want to implement a new ML algorithm?

**Guidelines:**
1. **From Scratch Implementation**
   - Use only NumPy for core computations
   - Include detailed comments explaining each step
   - Add mathematical notation in docstrings
   - Implement proper error handling

2. **Scikit-Learn Comparison**
   - Include equivalent Scikit-Learn implementation
   - Compare performance and results
   - Highlight differences in approach

3. **Visualization**
   - Add plots showing algorithm behavior
   - Visualize decision boundaries (if applicable)
   - Include loss/error curves

4. **Documentation**
   - Explain the theory behind the algorithm
   - Provide use cases and examples
   - Include time/space complexity analysis
   - Add references to papers/resources

### 📊 Contributing Datasets

Have an interesting dataset?

**Dataset requirements:**
- Clean and preprocessed
- Properly documented (features, target, context)
- Appropriate for educational purposes
- No privacy or copyright violations
- CSV or JSON format preferred
- Include a data dictionary

### 🎨 Enhancing Visualizations

Improve existing visualizations or add new ones!

**Visualization guidelines:**
- Use matplotlib or seaborn
- Include clear titles, labels, and legends
- Use colorblind-friendly palettes
- Make plots reproducible
- Add explanatory comments

---

## 🚀 Getting Started

### 1. Fork the Repository

Click the "Fork" button at the top right of the repository page.

### 2. Clone Your Fork

```bash
git clone https://github.com/YOUR-USERNAME/Machine-learning-Algorithm.git
cd Machine-learning-Algorithm
```

### 3. Add Upstream Remote

```bash
git remote add upstream https://github.com/Nitin-Prata/Machine-learning-Algorithm.git
```

### 4. Create a Virtual Environment

**Windows:**
```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```

**macOS/Linux:**
```bash
python3 -m venv .venv
source .venv/bin/activate
```

### 5. Install Dependencies

```bash
pip install -r requirements.txt
```

### 6. Create a Branch

```bash
git checkout -b feature/your-feature-name
```

**Branch naming conventions:**
- `feature/` - New features or algorithms
- `bugfix/` - Bug fixes
- `docs/` - Documentation updates
- `refactor/` - Code refactoring
- `test/` - Adding tests

**Examples:**
- `feature/add-svm-algorithm`
- `bugfix/fix-knn-distance-calculation`
- `docs/improve-readme-setup-section`

---

## 🔄 Development Workflow

### 1. Keep Your Fork Updated

```bash
git fetch upstream
git checkout main
git merge upstream/main
```

### 2. Make Your Changes

- Write clean, readable code
- Follow the existing code style
- Add comments for complex logic
- Update documentation as needed

### 3. Test Your Changes

- Run existing notebooks to ensure nothing broke
- Test your new code thoroughly
- Verify all cells execute without errors
- Check visualizations render correctly

### 4. Commit Your Changes

```bash
git add .
git commit -m "Your descriptive commit message"
```

### 5. Push to Your Fork

```bash
git push origin feature/your-feature-name
```

### 6. Create a Pull Request

Go to the original repository and click "New Pull Request"

---

## 📏 Style Guidelines

### Python Code Style

We follow **PEP 8** with some flexibility for readability.

**Key points:**
- Use 4 spaces for indentation (no tabs)
- Maximum line length: 100 characters (not strict for comments)
- Use meaningful variable names
- Add docstrings to functions and classes

**Example:**
```python
def euclidean_distance(x1, x2):
    """
    Calculate Euclidean distance between two points.
    
    Parameters:
    -----------
    x1 : numpy.ndarray
        First point
    x2 : numpy.ndarray
        Second point
        
    Returns:
    --------
    float
        Euclidean distance
    """
    return np.sqrt(np.sum((x1 - x2) ** 2))
```

### Jupyter Notebook Style

**Cell organization:**
1. Title and introduction (Markdown)
2. Imports
3. Constants and configuration
4. Data loading
5. Data exploration
6. Implementation
7. Visualization
8. Comparison with Scikit-Learn
9. Conclusion

**Markdown cells:**
- Use headers hierarchically (H1 → H2 → H3)
- Include explanations before code
- Add mathematical formulas using LaTeX
- Use bullet points for lists

**Code cells:**
- Keep cells focused on one task
- Add comments for complex operations
- Print intermediate results for learning
- Clear outputs before committing (optional)

### Documentation Style

- Use clear, concise language
- Avoid jargon or explain technical terms
- Include examples
- Use active voice
- Proofread for grammar and spelling

---

## 💬 Commit Messages

Write clear, descriptive commit messages.

### Format

```
<type>: <subject>

<body (optional)>

<footer (optional)>
```

### Types

- `feat`: New feature
- `fix`: Bug fix
- `docs`: Documentation changes
- `style`: Formatting, missing semicolons, etc.
- `refactor`: Code restructuring
- `test`: Adding tests
- `chore`: Maintenance tasks

### Examples

**Good commit messages:**
```
feat: add Support Vector Machine implementation

- Implement SVM from scratch using NumPy
- Add kernel tricks (linear, polynomial, RBF)
- Include comparison with sklearn.svm.SVC
- Add visualization of decision boundary
```

```
fix: correct KNN distance calculation

The previous implementation used Manhattan distance instead of
Euclidean distance by default. This fixes the default behavior.

Closes #42
```

```
docs: improve installation instructions

- Add Windows-specific setup steps
- Include troubleshooting section
- Update Python version requirement
```

**Avoid:**
```
❌ Update stuff
❌ Fixed bug
❌ Changes
❌ Working on KNN
```

---

## 🔀 Pull Request Process

### Before Submitting

- [ ] Code follows the style guidelines
- [ ] All notebooks run without errors
- [ ] Documentation is updated
- [ ] Commit messages are clear and descriptive
- [ ] Branch is up to date with main

### PR Title Format

```
[Type] Brief description
```

**Examples:**
- `[Feature] Add XGBoost implementation`
- `[Bugfix] Fix gradient descent convergence issue`
- `[Docs] Update contribution guidelines`

### PR Description Template

```markdown
## Description
[What does this PR do?]

## Type of Change
- [ ] 🐛 Bug fix
- [ ] ✨ New feature
- [ ] 📝 Documentation update
- [ ] 🎨 Style/formatting
- [ ] ♻️ Code refactoring
- [ ] ✅ Test addition

## Related Issue
Closes #[issue-number]

## Changes Made
- [List of specific changes]
- [Be detailed and clear]

## Screenshots (if applicable)
[Add screenshots or GIFs demonstrating changes]

## Testing
- [ ] Tested on Windows
- [ ] Tested on macOS
- [ ] Tested on Linux
- [ ] All notebooks execute successfully
- [ ] Visualizations render correctly

## Checklist
- [ ] My code follows the project's style guidelines
- [ ] I have performed a self-review of my code
- [ ] I have commented my code where necessary
- [ ] I have updated the documentation
- [ ] My changes generate no new warnings
- [ ] I have checked for similar PRs/issues

## Additional Notes
[Any additional information reviewers should know]
```

### Review Process

1. **Automated Checks**: Ensure all checks pass
2. **Code Review**: Maintainer will review your code
3. **Feedback**: Address any requested changes
4. **Approval**: Once approved, your PR will be merged
5. **Celebrate**: You're now a contributor! 🎉

### After Your PR is Merged

- Delete your branch (optional)
- Update your fork
- Close related issues
- Share your contribution!

---

## 🌟 Recognition

All contributors will be recognized!

**Contributors are listed in:**
- README.md contributors section (coming soon)
- GitHub contributors page
- Release notes for significant contributions

**Contribution levels:**
- 🥉 Bronze: 1-5 merged PRs
- 🥈 Silver: 6-15 merged PRs
- 🥇 Gold: 16+ merged PRs

---

## 📧 Community

### Getting Help

**Need help?**
- 💬 Open a [Discussion](../../discussions)
- 📧 Email: [nitinpratap997@gmail.com](mailto:nitinpratap997@gmail.com)
- 🐛 Create an [Issue](../../issues)

### Stay Connected

- ⭐ Star this repository
- 👀 Watch for updates
- 🍴 Fork and experiment
- 📢 Share with your network

---

## 🙏 Thank You!

Thank you for taking the time to contribute! Every contribution, no matter how small, makes a difference.

**Special thanks to all our contributors:**

<div align="center">

![Contributors](https://contrib.rocks/image?repo=Nitin-Prata/Machine-learning-Algorithm)

</div>

---

<div align="center">

**Made with ❤️ by the ML Community**

*Happy Contributing!* 🚀

[Back to Top](#-contributing-to-machine-learning-algorithms)

</div>