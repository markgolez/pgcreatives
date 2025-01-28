import os
import ast
import subprocess
import json
from pathlib import Path
import flake8.api.legacy as flake8
from deepseek import DeepSeek  # Hypothetical DeepSeek integration


class AIAssistant:
    def __init__(self, project_path):
        self.project_path = Path(project_path)
        self.deepseek = DeepSeek(api_key="YOUR_API_KEY")  # Initialize DeepSeek

    # Core Functionality
    def scan_project_files(self):
        """Recursively scans the project directory for files."""
        return [f for f in self.project_path.rglob("*.py")]

    def analyze_code_structure(self):
        """Parses all Python files in the project to understand code structure."""
        structure = {}
        for file_path in self.scan_project_files():
            with open(file_path, "r") as f:
                try:
                    tree = ast.parse(f.read(), filename=str(file_path))
                    structure[file_path] = [
                        node.name for node in ast.walk(tree) if isinstance(node, (ast.FunctionDef, ast.ClassDef))
                    ]
                except SyntaxError as e:
                    print(f"Error parsing {file_path}: {e}")
        return structure

    def code_quality_suggestions(self):
        """Runs flake8 for static code analysis and generates suggestions."""
        style_guide = flake8.get_style_guide()
        report = style_guide.check_files(
            [str(f) for f in self.scan_project_files()])
        return report.get_statistics('E') + report.get_statistics('W')

    def impact_analysis(self, suggested_change):
        """Analyzes which parts of the codebase will be impacted by a given change."""
        # Hypothetical analysis using DeepSeek
        result = self.deepseek.analyze_impact(suggested_change)
        return result

    def debug_terminal_output(self, command):
        """Executes a command and analyzes its terminal output."""
        try:
            process = subprocess.run(
                command, shell=True, text=True, capture_output=True)
            if process.returncode != 0:
                error_analysis = self.deepseek.analyze_error(process.stderr)
                return {
                    "command": command,
                    "output": process.stderr,
                    "suggestions": error_analysis
                }
            else:
                return {"command": command, "output": process.stdout, "status": "Success"}
        except Exception as e:
            return {"error": str(e)}

    def generate_test_cases(self):
        """Generates test cases based on the project's structure."""
        # Hypothetical DeepSeek test generation
        structure = self.analyze_code_structure()
        return self.deepseek.generate_tests(structure)

    def run_tests(self):
        """Runs pytest and reports results."""
        result = subprocess.run("pytest", shell=True,
                                text=True, capture_output=True)
        return {
            "output": result.stdout,
            "errors": result.stderr,
            "status": "Success" if result.returncode == 0 else "Failed"
        }

    def suggest_best_practices(self):
        """Uses DeepSeek to suggest best practices for the project."""
        project_files = {str(f): open(f).read()
                         for f in self.scan_project_files()}
        return self.deepseek.suggest_best_practices(project_files)

    # CLI Interface
    def cli(self):
        """Command-line interface for interacting with the assistant."""
        while True:
            print("\nCommands: analyze_project, debug_terminal, generate_tests, suggest_best_practices, run_tests, exit")
            command = input("Enter a command: ")

            if command == "analyze_project":
                structure = self.analyze_code_structure()
                print(json.dumps(structure, indent=4))

            elif command == "debug_terminal":
                cmd = input("Enter the terminal command to debug: ")
                result = self.debug_terminal_output(cmd)
                print(json.dumps(result, indent=4))

            elif command == "generate_tests":
                tests = self.generate_test_cases()
                print(json.dumps(tests, indent=4))

            elif command == "suggest_best_practices":
                suggestions = self.suggest_best_practices()
                print(json.dumps(suggestions, indent=4))

            elif command == "run_tests":
                results = self.run_tests()
                print(json.dumps(results, indent=4))

            elif command == "exit":
                print("Exiting...")
                break

            else:
                print("Unknown command. Please try again.")


# Example Usage
if __name__ == "__main__":
    project_path = input("Enter the path to your project: ")
    assistant = AIAssistant(project_path)
    assistant.cli()
