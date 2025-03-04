# Sıfırdan Lojistik Regresyon

Bu projede genel amaç, **Lojistik Regresyon algoritmasını sıfırdan** **NumPy** ve **Pandas** kullanarak uygulamaktadır. Aynı zamanda, **Scikit-Learn'ün Lojistik Regresyon modeli** ile karşılaştırma yapılarak doğruluğu test edilmektedir. Bu proje, özellikle Deep Learning
konusuna temelden giriş yapmak ve temelini iyi kavramak içi oldukça iyi bir çalışmadır.

## Veri Seti

Bu projede kullanılan veri seti, **meme kanseri teşhis verilerini** içermektedir. Hedef değişken (`diagnosis`), tümörün **kötü huylu (M)** veya **iyi huylu (B)** olduğunu gösterir. Veri seti, gereksiz sütunlar çıkarılarak ve özellikler normalize edilerek ön işleme tabi tutulur.

## Proje Akışı

### 1. Veri Ön İşleme

- `pandas` kullanarak **data.csv** veri setini yükleme.
- **Gereksiz sütunları** (`Unnamed: 32` ve `id`) kaldırma.
- **'diagnosis' sütununu** ikili formata çevirme (**M → 1, B → 0**).
- **Min-Max Normalizasyonu** ile özellik değerlerini ölçeklendirme.
- **Veriyi eğitim ve test setlerine ayırma** (**%80 eğitim, %20 test**).

### 2. Lojistik Regresyon Uygulaması

- **Parametreleri (ağırlıklar ve bias) başlatma**.
- **Sigmoid aktivasyon fonksiyonunu tanımlama**.
- **İleri ve geri yayılımı** kullanarak maliyet ve gradyan hesaplama.
- **Gradyan inişi algoritması ile ağırlıkları güncelleme**.
- **Öğrenilen parametreler ile tahmin yapma**.
- **Eğitim ve test doğruluğunu hesaplama**.

### 3. Scikit-Learn ile Karşılaştırma

- `sklearn.linear_model.LogisticRegression` kullanarak **Lojistik Regresyon modeli eğitme**.
- **Manuel uygulama ile doğruluk karşılaştırması yapma**.

## Kullanım

Projeyi çalıştırmak için aşağıdaki bağımlılıkların yüklü olması gerekmektedir:

```bash
pip install numpy pandas matplotlib scikit-learn
```

Ardından, kodu çalıştırın:

```bash
python logistic_regression.py
```

## Beklenen Çıktı

- **Maliyet fonksiyonunun iterasyonlarla azalması** beklenir.
- **Manuel uygulanan lojistik regresyonun doğruluğu, Scikit-Learn modeline yakın olmalıdır.**
- **Test doğruluğu** çıktı olarak gösterilecektir.

## Yapılacaklar / Gelecekteki Geliştirmeler

- **Aşırı öğrenmeyi önlemek için L2 düzenlileştirme ekleme**.
- **Eğitim sürecini vektörize edilmiş işlemlerle optimize etme**.
- **Modeli daha iyi değerlendirmek için çapraz doğrulama ekleme**.
- **Doğruluk dışında precision-recall ve ROC eğrisi analizleri ekleme**.

---

**Not: Bu projede kaynak olarak DataI platformunun Kaggle sayfasında yer alan Logistic Regression ile alakalı yayınladığı çalışma kullanılmıştır.
https://www.kaggle.com/kanncaa1

**Yazar:** [Kadir Özan]\
**Tarih:** [4.03.2025]

