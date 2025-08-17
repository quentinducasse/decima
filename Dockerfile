# --------------------------------------
# 📦 Base image
FROM python:3.10-slim

# --------------------------------------
# 📍 Set working directory
WORKDIR /app

# --------------------------------------
# 🔧 System dependencies
RUN apt-get update && apt-get install -y \
    git build-essential cmake swig libhdf5-dev python3-dev && \
    apt-get clean && rm -rf /var/lib/apt/lists/*

# --------------------------------------
# 🧪 Install MCNPTools from local clone
COPY ./mcnptools /opt/mcnptools

RUN cd /opt/mcnptools && \
    mkdir build && cd build && \
    cmake .. && \
    make -j$(nproc) && \
    make install

# --------------------------------------
# 📦 Install Python requirements
COPY requirements.txt .
RUN pip install --upgrade pip && pip install -r requirements.txt

# --------------------------------------
# 📁 Copy full app source
COPY . .

# --------------------------------------
# 🌍 Expose Flask app port
EXPOSE 5050

# --------------------------------------
# 🚀 Launch app
CMD ["python", "app.py"]
