# Step 1 : Base Images
FROM python:3.9

# Step 2 : Package install
RUN apt -y update && apt -y upgrade; apt -y install vim git net-tools

# Step 3 : Specify a Working directory
WORKDIR /root

# Step 4 : Config file copy
COPY .bashrc .
COPY .exrc .
COPY hello.py .
RUN pip install bottle

# Step 5 : Open port
EXPOSE 3000

# Step 6 : Excution Program
CMD ["python", "hello.py"]
