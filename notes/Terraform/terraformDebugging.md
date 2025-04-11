# Terraform Debugging

Terraform provides logging capabilities to help debug issues and understand the internal operations of Terraform. The logging is controlled using the `TF_LOG` environment variable, which specifies the log level, and the `TF_LOG_PATH` variable, which specifies where to save the logs.

## Log Levels

The `TF_LOG` environment variable can be set to one of the following levels:

- **TRACE**: Shows detailed logs, including internal function calls. Useful for deep debugging.
- **DEBUG**: Provides detailed information about Terraform's operations.
- **INFO**: Displays general information about Terraform's execution.
- **WARN**: Shows warnings about potential issues.
- **ERROR**: Displays only error messages.
- **OFF**: Disables logging.

## How to Enable Logging

### 1. Set the Log Level
To enable logging, set the `TF_LOG` environment variable to the desired log level:

```bash
export TF_LOG=DEBUG
```

### Save Logs to a File

export TF_LOG_PATH=terraform.log