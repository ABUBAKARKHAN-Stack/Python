## What is a Virtual Environment in Python?
A virtual environment (`venv`) creates its own isolated Python environment with its own dependencies.  
This prevents conflicts with the Python and packages installed on your operating system.  

So when you need to upgrade or downgrade your Python app, you just update the venv environment—without touching the global Python version of your OS.

---

## How to Initialize? 
Run this command in your project folder:

```bash
python -m venv .venv
```

You can also choose any name instead of `.venv`, but using `.venv` is common because tools like **gitignore** and IDEs (VS Code, PyCharm) automatically ignore it.

---

## How to Activate? 
- **On Windows:**
  ```bash
  .venv\Scripts\activate
  ```
- **On Mac/Linux:**
  ```bash
  source .venv/bin/activate
  ```

---

## Installing Packages 
Now install any dependencies. They will remain inside your virtual environment, not globally.

Example:
```bash
pip install flask
pip install requests
```

If you need multiple packages, create a `requirements.txt` file in your root folder:

```
flask
requests
```

You can also specify versions:
```
flask==2.0.1
requests>=2.25.1
```

Then install them all with:
```bash
pip install -r requirements.txt
```


---

## Why `requirements.txt` is Important
Instead of sharing your venv folder, just share your `requirements.txt`.  
Others can recreate the same environment on their own machine.

---

## How to Deactivate? 
Simply run:
```bash
deactivate
```

---

## Note
`venv` is the traditional way of managing Python environments.  
Nowadays, we also have more powerful tools like **uv** which we’ll discuss next.
