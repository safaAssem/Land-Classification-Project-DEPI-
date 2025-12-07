# استخدم صورة Python خفيفة
FROM python:3.11-slim

# حدد مجلد العمل داخل الكونتينر
WORKDIR /app

# انسخ كل ملفات المشروع للكونتينر
COPY . /app

# حدث pip وثبت الباكيجات
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# اجعل start.sh قابل للتنفيذ
RUN chmod +x start.sh

# الأمر الرئيسي لتشغيل التطبيق
CMD ["./start.sh"]
