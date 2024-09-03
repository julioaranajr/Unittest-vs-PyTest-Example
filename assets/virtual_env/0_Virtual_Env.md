# Virtual Environment

## Why use a virtual environment?

- A virtual environment is a self-contained directory that contains a Python installation for a particular version of Python, as well as a number of additional packages.

- A virtual environment allows you to install packages in a separate directory, rather than installing them globally. This can be useful if you are working on multiple projects that require different versions of the same package.

- A virtual environment also allows you to isolate your project's dependencies from the system-wide Python installation. This can help to avoid conflicts between different versions of the same package.

## How to create a virtual environment?

- To Install virtualenv, you can run the following command:

```bash
pip install virtualenv
```

the above command installs the `virtualenv` package, which provides the `virtualenv` command.

- To create a virtual environment, you can use the `virtualenv` command. This command creates a new directory that contains a Python installation and a number of additional packages.

- To create a virtual environment, you can run the following command:

```bash
virtualenv myenv
```

- This command creates a new directory called `myenv` that contains a Python installation and a number of additional packages.

- To activate the virtual environment, you can run the following command:

```bash
source myenv/bin/activate
```

- This command activates the virtual environment and sets the `PYTHONPATH` environment variable to point to the Python installation in the virtual environment.

- To deactivate the virtual environment, you can run the following command:

```bash
deactivate
```

- This command deactivates the virtual environment and restores the `PYTHONPATH` environment variable to its original value.

## How to install packages in a virtual environment?

- To install packages in a virtual environment, you can use the `pip` command. This command installs packages in the virtual environment, rather than installing them globally.

- To install a package in a virtual environment, you can run the following command:

```bash
pip install package_name
```

- This command installs the `package_name` package in the virtual environment.

- To install packages from a `requirements.txt` file, you can run the following command:

```bash
pip install -r requirements.txt
```

- This command installs the packages listed in the `requirements.txt` file in the virtual environment.

- To see a list of packages installed in the virtual environment, you can run the following command:

```bash

pip list
```

- This command lists the packages installed in the virtual environment.

## Summary

In this chapter, we learned about virtual environments in Python. We learned:

- About the importance of virtual environments
- How to create a virtual environment
- How to activate and deactivate a virtual environment
- How to install packages in a virtual environment and from a `requirements.txt` file
- How to see a list of packages installed in a virtual environment.

---

In the next chapter, we will learn about the [`unittest`](assets/unittest/1_Unittest_In_Python.md) module and how to write and run tests for your code.

