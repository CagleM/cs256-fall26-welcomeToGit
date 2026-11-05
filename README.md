# CS 256: Data Structures & Loops In-Class Exercise

Welcome to the CS 256 in-class GitHub exercise! In this activity, you will practice working with Python data structures and loops while building comfort with the Git/GitHub workflow in Visual Studio Code.

---

## 🎯 Learning Objectives

By the end of this exercise, you will be able to:
- Fork and Clone a GitHub repository.
- Perform the standard Git cycle (**Edit $\rightarrow$ Save $\rightarrow$ Commit**) for individual tasks.
- Push multiple local commits to your GitHub fork and verify your work online.

---

## 🛠️ Part 1: Initial Setup (Fork & Clone)

1. **Fork the Repository:**
   - At the top-right of this GitHub page, click the **Fork** button.
   - Keep default settings and click **Create fork**.
2. **Clone in VS Code:**
   - Open VS Code.
   - Open the Command Palette: `Ctrl+Shift+P` (Windows/Linux) or `Cmd+Shift+P` (Mac).
   - Type **`Git: Clone`** and press **Enter**.
   - Select **Clone from GitHub**, then pick **your fork** (`YOUR-USERNAME/repository-name`).
   - If you don't already have a GitHub account, you'll need to create one.
   - If you aren't working on a machine where git is installed you will need to download it from git-scm.com
   - Choose a local folder to save your work, then click **Open** when prompted in VS Code.

---

## 📝 Part 2: Exercise Tasks

Open `loops_exercise.py` in VS Code and complete the following tasks sequentially. 

> **Important:** Save your file (`Ctrl+S` / `Cmd+S`) and **commit your code after finishing each task**.

### 🔹 Task 1: Fix Case Sensitivity in `num_vowels()`
- **Issue:** Currently, `num_vowels("Hello! My name is Maggie V.")` only counts lowercase vowels.
- **Goal:** Modify `num_vowels()` so it counts **both uppercase and lowercase** vowels.
- *Hint:* Use `.lower()` on characters or the input string before checking for vowels.
- **💾 Commit Step:** Go to Source Control (`Ctrl+Shift+G` / `Cmd+Shift+G`). Message: `"Task 1: Fix vowel case sensitivity"`. Click **Commit**.
- Note: If you haven't done this before you will be prompted to set you Github username and email. 

---

### 🔹 Task 2: Count Non-Vowels
- **Goal:** Look for the comment inside `test_count_vowels()` (`# what if we wanted to count non_vowels?`).
- Write a new function `count_non_vowels(input_text)` that counts all characters that are **not** vowels (including spaces, numbers, and punctuation).
- Call `count_non_vowels` inside `test_count_vowels()` to test it on `"Hello! My name is Maggie V."`.
- **💾 Commit Step:** In Source Control, message: `"Task 2: Add num_consonants function"`. Click **Commit**.

---

### 🔹 Task 3: Access Dictionary Values Using Key Lookup
- **Issue:** By default, running a standard `for item in dictionary:` loop only yields key names.
- **Goal:** Modify the dictionary section in `test_loop_through_it()` so it prints each key along with its associated value (e.g., `discussion: 10`).
- **Hint:** You can retrieve values using key lookup syntax: **`dictionary[key]`**.
- **💾 Commit Step:** In Source Control, message: `"Task 3: Access dictionary values using key lookup"`. Click **Commit**.

---

## 🚀 Part 3: Push Commits to GitHub & Verify

Now that you have completed all three tasks and created 3 separate local commits:

1. **Push Changes:**
   - In VS Code's Source Control tab, click **Sync Changes** (or click the `...` menu at the top-right of the panel and select **Push**).
   - If prompted about pulling/pushing to `origin/main`, click **OK**.
2. **Verify on GitHub:**
   - Go to your browser and open your GitHub fork (`github.com/YOUR-USERNAME/repository-name`).
   - Refresh the page and click on **commits** (located near the top of the file list).
   - Confirm that all **3 separate commit messages** appear in your online repository history!
