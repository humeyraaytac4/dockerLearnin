    # 1. Base image olarak Python kullanıyoruz (3.9 versiyonu)
    FROM python:3.9-slim

    # Install system dependencies
    RUN apt-get update && apt-get install -y \
    gcc \
    pkg-config \
    default-libmysqlclient-dev \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

    # 2. Çalışma dizinini ayarla
    WORKDIR /app

    # 3. Gereken dosyaları container'a kopyala (önce requirements.txt dosyasını)
    COPY requirements.txt .

    # 4. Python bağımlılıklarını yükle
    RUN pip install --no-cache-dir -r requirements.txt

    # 5. Uygulama dosyalarını kopyala
    COPY . .


    # 6. Uygulamayı başlat
    CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "8000"]

