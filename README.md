## Lumberjack (Log Analysis)

This project is a simple tool for parsing Apache access log files, analyzing them for security threats, and generating a report summarizing the analysis results.

## Usage

To use this tool, follow these steps:

1. Make sure you have Python installed on your system.
2. Clone the project repository
3. Navigate to the project directory
4. Run the main script with the path to your Apache access log file as an argument:
python main.py "log_file_path"

Replace "log_file_path" with the path to your Apache access log file.

## Example

Here's an example of how to run the script:

python main.py sample_access.log


## Notes

- Since we’re not using real locations, geographical analysis on IP addresses is not performed.

- We wanted to integrate with SIEM, but there was an issue when porting over the HEC URL. We will need to study it more to resolve the issue.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
