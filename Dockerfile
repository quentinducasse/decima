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
# 🧪 Install MCNPToolsPro from local clone (with MCNP 6.2/6.3 filter support)
COPY ./mcnptoolspro /opt/mcnptoolspro

RUN cd /opt/mcnptoolspro && \
    mkdir -p build && cd build && \
    cmake .. && \
    make -j$(nproc) && \
    make install && \
    cd /opt/mcnptoolspro/build/python && \
    pip install .

# --------------------------------------
# 📦 Install Python requirements
COPY requirements.txt .
RUN pip install --upgrade pip && pip install -r requirements.txt

# --------------------------------------
# 📁 Copy full app source
COPY . .

# --------------------------------------
# 📦 Install DECIMA package in editable mode
RUN pip install -e .

# --------------------------------------
# 🌍 Expose Flask app port
EXPOSE 5050

# --------------------------------------
# 🚀 Launch app
CMD ["python", "app.py"]
