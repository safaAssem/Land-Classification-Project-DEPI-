# Land Type Classifier - Deployment


## Setup (local)


1. Create a virtual environment and install requirements:


```bash
python -m venv venv
source venv/bin/activate # or venv\Scripts\activate on Windows

pip install -r requirements.txt

# Land Classification Project - DEPI

## ملاحظة مهمة حول الموديلات الكبيرة

الموديلات الكبيرة (مثل `efficient_model_96.keras`) متخزنة باستخدام **Git Large File Storage (LFS)**، عشان كده مش هتظهر مباشرة على واجهة GitHub.

### لتنزيل الموديلات كاملة على جهازك:

1. ثبت Git LFS من: [https://git-lfs.github.com/](https://git-lfs.github.com/)
2. افتح الطرفية (Terminal) وشغل الأوامر دي:

```bash
git clone <repo-url>
git lfs install
git lfs pull
```

### بديل بدون Git LFS:

لو مش عايز تستخدم Git LFS، تقدر تحمل الموديلات من الرابط المباشر:
[https://drive.google.com/file/d/1ZqBTQ8rf7XVnrban5kgZFRLdkbVNBwXd/view?usp=drive_link]  ← هنا ممكن تضيف رابط Google Drive أو OneDrive

---

بهذه الطريقة، أي شخص يفتح الريبو هيعرف ازاي ينزل الموديل ويشتغل عليه بدون مشاكل.
