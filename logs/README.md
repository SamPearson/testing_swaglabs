# Logging

Logging anything below the WARN level (to a file) requires 
a pytest.ini file with log_file_level set to something lower than the default WARN level

File logging is disabled by default. To enable it, you need to set the following in a .env file:
file_logging = "True"

Logs are stored in "logs/log.log". This file is not rotated. File logging is only meant to be enabled
in dev environments