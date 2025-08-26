# Polskie Modele AI - Lokalne Demo / Polish AI Models - Local Demo

Ten katalog zawiera demonstracje uruchamiania lokalnych modeli AI obsługujących język polski.

*This directory contains demonstrations of running local AI models that support the Polish language.*

## 🚀 Dostępne Modele / Available Models

### 1. GPT-2 (`gpt2_local_demo.py`)
- **Model**: OpenAI GPT-2
- **Opis**: Podstawowy model generatywny z ograniczonym wsparciem dla polskiego
- **Zalety**: Szybki, mały rozmiar
- **Wady**: Ograniczone wsparcie dla języka polskiego

### 2. XGLM-564M (`xglm_polish_demo.py`) ⭐ **ZALECANY**
- **Model**: `facebook/xglm-564M`
- **Opis**: Wielojęzyczny model generatywny z dobrym wsparciem polskiego
- **Zalety**: Doskonałe wsparcie polskiego, generowanie tekstu wysokiej jakości
- **Rozmiar**: ~2.3GB
- **Zastąpienie**: Zamiennik dla niedostępnego Polish-Llama

### 3. HerBERT (`herbert_polish_demo.py`)
- **Model**: `allegro/herbert-base-cased`
- **Opis**: Polski model BERT specjalnie wytrenowany dla języka polskiego
- **Zalety**: Doskonałe rozumienie języka polskiego
- **Rozmiar**: ~500MB
- **Zastosowanie**: Rozumienie tekstu, klasyfikacja, analiza sentymentu

## 📋 Wymagania / Requirements

### Instalacja / Installation

```bash
# Przejdź do katalogu demo / Navigate to demo directory
cd demos/polish-ai-models

# Zainstaluj zależności / Install dependencies
pip install -r requirements.txt
```

### Wymagania systemowe / System Requirements
- Python 3.7+
- Co najmniej 4GB RAM / At least 4GB RAM
- ~3GB miejsca na dysku dla wszystkich modeli / ~3GB disk space for all models

## 🎯 Uruchamianie / Running

### GPT-2 Demo
```bash
python gpt2_local_demo.py
```

### XGLM-564M Demo (Zalecany / Recommended)
```bash
python xglm_polish_demo.py
```

### HerBERT Demo
```bash
python herbert_polish_demo.py
```

## 🔄 Alternatywy dla Polish-Llama / Polish-Llama Alternatives

Ponieważ model Polish-Llama-2-7B-HF nie jest publicznie dostępny, proponujemy następujące alternatywy:

*Since the Polish-Llama-2-7B-HF model is not publicly available, we propose the following alternatives:*

### Dla generowania tekstu / For text generation:
1. **facebook/xglm-564M** (zalecany / recommended)
   - Wielojęzyczny model z bardzo dobrym wsparciem polskiego
   - Dostępny publicznie bez autoryzacji
   - Dobra jakość generowanego tekstu

### Dla rozumienia tekstu / For text understanding:
1. **allegro/herbert-base-cased**
   - Specjalnie wytrenowany dla języka polskiego
   - Doskonały do zadań NLP w polskim
   - Model polski stworzony przez Allegro

## 🛠️ Rozwiązywanie problemów / Troubleshooting

### Błąd braku modułów / Module not found error
```bash
pip install torch transformers
```

### Problemy z pamięcią / Memory issues
- Zamknij inne aplikacje
- Użyj mniejszego modelu (HerBERT zamiast XGLM)
- Rozważ uruchomienie na GPU jeśli dostępne

### Powolne ładowanie modelu / Slow model loading
- Pierwsze uruchomienie pobierze model z internetu
- Kolejne uruchomienia będą szybsze (model zapisany lokalnie)

## 📚 Przykłady użycia / Usage Examples

### Generowanie tekstu polskiego / Polish text generation
```python
from transformers import XGLMTokenizer, XGLMForCausalLM

model_name = "facebook/xglm-564M"
tokenizer = XGLMTokenizer.from_pretrained(model_name)
model = XGLMForCausalLM.from_pretrained(model_name)

prompt = "Warszawa to piękne miasto"
inputs = tokenizer(prompt, return_tensors="pt")
outputs = model.generate(inputs["input_ids"], max_length=50)
result = tokenizer.decode(outputs[0], skip_special_tokens=True)
```

### Analiza tekstu polskiego / Polish text analysis
```python
from transformers import AutoTokenizer, AutoModelForMaskedLM

model_name = "allegro/herbert-base-cased"
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForMaskedLM.from_pretrained(model_name)

text = "Warszawa to [MASK] Polski."
inputs = tokenizer(text, return_tensors="pt")
outputs = model(**inputs)
```

## ⚡ Szybki start / Quick Start

1. **Zainstaluj zależności / Install dependencies**:
   ```bash
   pip install torch transformers
   ```

2. **Uruchom zalecany model / Run recommended model**:
   ```bash
   python xglm_polish_demo.py
   ```

3. **Eksperymentuj z własnymi tekstami / Experiment with your own texts**:
   Edytuj pliki demo i dodaj własne polskie prompty.

## 🔗 Dodatkowe zasoby / Additional Resources

- [Hugging Face Transformers Documentation](https://huggingface.co/docs/transformers)
- [Facebook XGLM Paper](https://arxiv.org/abs/2112.10668)
- [HerBERT: Efficiently Pretrained Transformer-based Language Model for Polish](https://arxiv.org/abs/2106.01134)

---

*Wszystkie modele działają lokalnie bez konieczności połączenia z chmurą.*

*All models work locally without requiring cloud connectivity.*