# 📂 Unit III: Python Modules and File Handling

This directory contains the source code, practical assignments, and implementation pipelines for **Unit III** of the Advanced Python course. The focus of this unit is modular software design, package building, namespace tracking, structured text processing, and data serialization.

---

## 🏗️ Module Directory Structure

```text
module-3/
├── db/
│   └── students.json       # Local structured JSON database storage
├── modules/                # Custom package containing individual submodules
│   ├── basic_var.py        # Variable definitions, scopes, and namespace tests
│   ├── calc.py             # Mathematical operations and execution algorithms
│   ├── json.py             # Custom JSON formatting and parsing logic
│   └── qroot.py            # Square root calculations
├── main.py                 # Primary driver script (imports from /modules)
└── temp.py                 # Sandboxed file for testing experimental snippets
```

> **Note**: Compiled cache components (`__pycache__/`) are excluded from documentation as they are automatically generated during module translation.

---



## 🚀 Execution & Usage Guide

### How to Run the Primary Script
Ensure you are inside the `module-3` folder path before triggering execution so that python sets the correct relative file parsing roots:

```bash
cd module-3
python main.py
```

### Coding Best Practices Used
* **Namespace Isolation**: Avoiding collision issues by calling explicit modules instead of wildcard imports (`from module import *`).
* **Exception Handling**: Safe file pathways wrapped in `try/except` constructs to prevent crashes during JSON input/output interruptions.
