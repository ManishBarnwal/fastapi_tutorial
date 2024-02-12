# syntax=docker/dockerfile:1

# Set the base Python version for the image
ARG PYTHON_VERSION=3.10.10

# Use an official Python runtime as a parent image
FROM python:${PYTHON_VERSION} as base

# Install Rust compiler, which might be needed for compiling Python packages that require Rust -- transformers package
RUN curl https://sh.rustup.rs -sSf | bash -s -- -y
# Add Rust compiler's binary directory to PATH, making the `cargo` command available.
ENV PATH="/root/.cargo/bin:${PATH}"

# Prevent Python from writing pyc files to disc (Python bytecode files), which is useful for minimizing the image size and avoiding potential issues with file system layers.
ENV PYTHONDONTWRITEBYTECODE=1

# Set the working directory inside the container to /code. Future commands will run from this directory.
WORKDIR /code

# Copy the requirements.txt file from your host to /code/requirements.txt inside the container.
COPY ./requirements.txt requirements.txt
# Install Python dependencies defined in requirements.txt without storing the cache, to keep the image size down.
RUN pip install --no-cache-dir -r requirements.txt

# Copy the application source code from your host's current directory's src folder to the container's /code/src directory.
COPY ./src ./src

# Set an environment variable that prevents Python from buffering stdout and stderr.
# This is useful for logging, ensuring that logs are output in real-time and not held in a buffer.
ENV PYTHONUNBUFFERED=1

# Inform Docker that the container listens on port 8000 at runtime. Note: This does not actually publish the port.
EXPOSE 8000

# Define the command to run the application using Uvicorn, specifying the app location, enabling reload for development, setting the port, and binding the host to 0.0.0.0 to make the container accessible from outside.
CMD ["uvicorn", "src.main:app", "--reload", "--port", "8000", "--host", "0.0.0.0"]
