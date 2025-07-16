# Start with a standard Python image
FROM python:3.9

# Set the working directory inside the container
WORKDIR /code

# Copy the requirements file
COPY requirements.txt .

# Install the Python libraries
RUN pip install --no-cache-dir --upgrade -r requirements.txt

# Copy all your project files (app.py, models, etc.)
COPY . .

# Tell the container to listen on port 7860
EXPOSE 7860

# The command to run your Flask app with Gunicorn
CMD ["gunicorn", "--bind", "0.0.0.0:7860", "app:app"]

# Start with a standard Python image
FROM python:3.9

# Set the working directory inside the container
WORKDIR /code

# Copy the requirements file
COPY requirements.txt .

# Install the Python libraries
RUN pip install --no-cache-dir --upgrade -r requirements.txt

# Copy all your project files (app.py, models, etc.)
COPY . .

# Tell the container to listen on port 7860
EXPOSE 7860

# The command to run your Flask app with Gunicorn
CMD ["gunicorn", "--bind", "0.0.0.0:7860", "app:app"]