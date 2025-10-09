# Spotify Churn Prediction

Bu proje, Spotify kullanıcılarının abonelikten ayrılma (churn) durumlarını tahmin etmek için bir makine öğrenimi modeli geliştirmeyi amaçlamaktadır.  

Veri seti, kullanıcıların demografik bilgileri, dinleme alışkanlıkları ve abonelik türleri gibi değişkenleri içermektedir.

---

## 📁 Veri Seti

- **Kaynak:** `spotify_churn_dataset.csv`  
- **Özellikler:**
  - `user_id`: Kullanıcı kimliği (analiz için çıkarıldı)
  - `gender`: Cinsiyet (Female, Male, Other)
  - `age`: Yaş
  - `country`: Ülke
  - `subscription_type`: Abonelik türü (Free, Premium, Student, Family)
  - `listening_time`: Haftalık dinleme süresi (dakika)
  - `songs_played_per_day`: Günlük çalınan şarkı sayısı
  - `skip_rate`: Şarkı atlama oranı
  - `device_type`: Kullanılan cihaz türü (Desktop, Mobile, Web)
  - `ads_listened_per_week`: Haftalık dinlenen reklam sayısı
  - `offline_listening`: Offline dinleme durumu (0: Hayır, 1: Evet)
  - `is_churned`: Kullanıcının ayrılıp ayrılmadığı (0: Hayır, 1: Evet)

---

## 🔍 Veri Ön İşleme

1. **Gereksiz sütunların çıkarılması:** `user_id` analiz için önemsiz olduğu için kaldırıldı.
2. **Eksik değer kontrolü:** Eksik değer bulunmamaktadır.
3. **Kategorik değişkenlerin dönüştürülmesi:** `gender`, `country`, `subscription_type`, `device_type` için one-hot encoding uygulandı.
4. **SMOTE ile veri dengeleme:** Churn eden kullanıcı sayısı az olduğu için veri dengelendi.
5. **Özellik ölçekleme:** Sayısal değişkenler `StandardScaler` ile ölçeklendi.

---

## 📊 Keşifsel Veri Analizi (EDA)

- **Cinsiyet dağılımı ve churn oranı**
- **Yaş dağılımı ve abonelik türleri**
- **Cihaz türü ve yaş gruplarına göre dağılım**
- **Ülkelere göre kullanıcı davranışları**
- **Özellikler arasındaki korelasyon analizi**

---

## 🧠 Modeller ve Değerlendirme

Aşağıdaki modeller kullanıldı:

- Logistic Regression
- K-Nearest Neighbors (KNN)
- Support Vector Classifier (SVC)
- Decision Tree
- Random Forest
- AdaBoost
- Gradient Boosting
- XGBoost
- LightGBM

Her model, eğitim ve test setlerinde **accuracy**, **classification report**, ve **confusion matrix** ile değerlendirildi.

---

## ⚡ Hiperparametre Optimizasyonu

**RandomizedSearchCV** ile aşağıdaki modeller için hiperparametre optimizasyonu yapıldı:

- **LightGBM**
  - `learning_rate`, `num_iterations`, `num_leaves`, `max_depth`, `max_bin`
  - En iyi parametreler ile model test edildi ve performans artırıldı.
- **XGBoost**
  - `learning_rate`, `n_estimators`, `max_depth`, `subsample`
  - En iyi parametreler ile model test edildi.

---

## 📈 Model Performansı

- **En iyi model:** XGBoost ve LightGBM yüksek performans gösterdi.
- **Accuracy (Test Set):** ~0.78 – 0.79
- **Confusion matrix ve classification report** ile detaylı analiz yapıldı.

---

## 🔧 Kullanım

```python
# Kütüphaneler
import pandas as pd
from sklearn.model_selection import train_test_split
from imblearn.over_sampling import SMOTE
from sklearn.preprocessing import StandardScaler
from lightgbm import LGBMClassifier
from xgboost import XGBClassifier

# Veri yükleme
df = pd.read_csv("spotify_churn_dataset.csv")

# Ön işleme, SMOTE ve model eğitimi adımları yukarıdaki gibi uygulanabilir
