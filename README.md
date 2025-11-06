# To-Do List Application

A lightweight and user-friendly desktop to-do list application built with Python's tkinter library. This application allows users to efficiently manage their daily tasks with a simple graphical interface and automatic data persistence.

## Features

- ✅ **Add Tasks**: Quickly add new tasks using the input field or by pressing Enter
- 🗑️ **Delete Tasks**: Remove completed or unwanted tasks with a single click
- 💾 **Auto-Save**: Automatically saves all tasks to a local file
- 🔄 **Persistent Storage**: Tasks are loaded automatically when the application starts
- 🎨 **Clean Interface**: Simple and intuitive user interface
- 📝 **UTF-8 Support**: Full support for international characters

## Requirements

- Python 3.x
- tkinter (usually comes pre-installed with Python)

## Installation

1. Clone this repository or download the source code:
```bash
git clone https://github.com/Ansh200618/todo-list.git
cd todo-list
```

2. Ensure you have Python 3 installed:
```bash
python --version
```

3. No additional dependencies required! tkinter comes bundled with Python.

## Usage

1. Run the application:
```bash
python todo_list.py
```

2. **Adding a task**:
   - Type your task in the input field
   - Click the "Add Task" button or press Enter

3. **Deleting a task**:
   - Select a task from the list
   - Click the "Delete Task" button

4. **Tasks are automatically saved** to `tasks.txt` in the same directory

## File Structure

```
todo-list/
│
├── todo_list.py        # Main application file
└── tasks.txt           # Auto-generated task storage file
```

## How It Works

- **Data Storage**: Tasks are stored in a plain text file (`tasks.txt`) with UTF-8 encoding
- **Auto-Load**: On startup, the application reads from `tasks.txt` and populates the list
- **Auto-Save**: Every time you add or delete a task, changes are immediately written to the file
- **Error Handling**: Includes error handling for file operations and user actions

## Screenshots

*The application features a clean 400x400 pixel window with:*
- Input field at the top
- Add/Delete buttons with color-coded design (green for add, red for delete)
- Scrollable task list display

## Customization

You can easily customize the application by modifying:

- **Window size**: Change `root.geometry("400x400")`
- **Font styles**: Modify `font=("Arial", 14)`
- **Colors**: Adjust `bg` and `fg` parameters in button definitions
- **List capacity**: Change `height=12` in the Listbox widget

## Error Handling

The application includes robust error handling for:
- File not found (first-time users)
- Invalid task selection
- File read/write errors

## Future Enhancements

Potential features for future versions:
- [ ] Task priority levels
- [ ] Due dates and reminders
- [ ] Task categories/tags
- [ ] Search and filter functionality
- [ ] Dark mode theme
- [ ] Export tasks to different formats

## Contributing

Contributions are welcome! Feel free to:
1. Fork the repository
2. Create a feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## License

This project is open source and available under the [MIT License](LICENSE).

## Author

**Ansh200618**
- GitHub: [@Ansh200618](https://github.com/Ansh200618)

## Acknowledgments

- Built with Python's tkinter library
- Inspired by the need for simple, distraction-free task management

---

**Note**: This is a standalone desktop application. No internet connection required for operation.
