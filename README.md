# Simple Calculator 

A basic command-line calculator program written in Python that performs fundamental arithmetic operations on two numbers.

## Features

- **Four Basic Operations**: Addition (+), Subtraction (-), Multiplication (*), Division (/)
- **Error Handling**: Prevents division by zero and handles invalid inputs
- **Clean Output**: Displays whole numbers without unnecessary decimal points
- **User-Friendly**: Clear prompts and formatted results

## Demo

```
Simple Calculator
----------------
Enter the first number: 10
Enter the second number: 5
Enter an operation (+, -, *, /): +
10 + 5 = 15
```

## Getting Started

### Prerequisites

- Python 3.x installed on your system

### Installation

1. Clone this repository:
   ```bash
   git clone https://github.com/RAtieno/simple-calculator.git
   ```

2. Navigate to the project directory:
   ```bash
   cd simple-calculator
   ```

3. Run the program:
   ```bash
   python calculator.py
   ```

## Usage

1. Run the program
2. Enter the first number when prompted
3. Enter the second number when prompted
4. Choose an operation: `+`, `-`, `*`, or `/`
5. View the calculated result

### Example Operations

| Input | Output |
|-------|--------|
| `8`, `2`, `+` | `8 + 2 = 10` |
| `15`, `3`, `-` | `15 - 3 = 12` |
| `4`, `7`, `*` | `4 * 7 = 28` |
| `20`, `4`, `/` | `20 / 4 = 5` |

## Error Handling

The calculator handles several error scenarios:

- **Division by Zero**: `Error: Cannot divide by zero!`
- **Invalid Operation**: `Error: Invalid operation! Please use +, -, *, or /`
- **Invalid Numbers**: `Error: Please enter valid numbers!`

## Code Structure

```
simple-calculator/
│
├── calculator.py          # Main calculator program
├── README.md             # Project documentation
└── LICENSE               # License file (optional)
```

## Functions

- `main()`: Main program function that handles user input and calculations
- `format_number()`: Utility function to format numbers for clean display

## Contributing

Contributions are welcome! Here are some ways you can contribute:

1. Fork the project
2. Create a feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

### Ideas for Enhancement

- Add support for more operations (power, square root, etc.)
- Implement a continuous calculation mode
- Add calculation history
- Create a GUI version using tkinter
- Add unit tests

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Author

**Roseline Atieno** -https://github.com/RAtieno

## Acknowledgments

- Built as a learning project for Python programming fundamentals
- Demonstrates basic input/output, conditional statements, and error handling

---

⭐ If you found this project helpful, please give it a star on GitHub!
