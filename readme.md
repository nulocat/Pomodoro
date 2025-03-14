# Pomodoro Timer

This is a project for a Pomodoro Timer, a time management technique that uses work and break intervals to increase productivity.

## Features

- Helps prevent burnout by balancing your work in cycles
- Can pause and start at any time, and you can skip cycles if you want to rush (don't do this for your own good)
- Automatically switches cycles after each one ends (Feature)
- Future enhancements:
  - Configurable cycles and timer behavior
  - Sound notifications for the next cycle
  - Productivity history and points system (still being debated)
  - Simple to-do list to further enhance your productivity

## Technologies Used

- HTML
- CSS
- JavaScript
- Flask
- Python

## How to Use

### Requirements

    - Python => 3.10
    - Poetry
    - Flask

### For Windows:

1. Clone the repository:
    ```bash
    git clone https://github.com/nulocat/Pomodoro.git
    ```
    ```

2. Navigate to the project directory:
    ```bash
    cd Pomodoro
    ```

3. Install the required dependencies:
    ```bash
    poetry install
    ```

4. Run the application:
    ```bash
    poetry run python run.py
    ```
    
5. Open your web browser and go to `http://127.0.0.1:5000` to start using the Pomodoro Timer. The application runs on port 5000 by default, but this can be configured if necessary.

### For Linux:

1. Clone the repository:
    ```bash
    git clone https://github.com/nulocat/Pomodoro.git
    ```

2. Navigate to the project directory:
    ```bash
    cd Pomodoro
    ```

3. Install the required dependencies:
    ```bash
    poetry install
    ```

4. Run the application:
    ```bash
    poetry run python3 run.py

5. Open your web browser and go to `http://127.0.0.1:5000` to start using the Pomodoro Timer. The application runs on port 5000 by default, but this can be configured if necessary.

## Contribution

We welcome contributions to the Pomodoro Timer project! To contribute, please follow these steps:

1. Fork the repository.
2. Create a new branch for your feature or bugfix:
    ```bash
    git checkout -b feature-name
    ```
3. Make your changes and commit them with clear and descriptive messages:
    ```bash
    git commit -m "Description of your changes"
    ```
4. Push your changes to your forked repository:
    ```bash
    git push origin feature-name
    ```
5. Open a pull request to the main repository, describing your changes in detail.

Please ensure your code follows our coding standards and includes appropriate tests. We will review your pull request and provide feedback as soon as possible.

Thank you for your contributions!

## License

This project is licensed under the MIT License - see the [LICENSE.txt](LICENSE.txt) file for details.