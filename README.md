# Hermann Hesse Novels Analysis

Welcome to the **Hermann Hesse Article Analysis** project — a digital humanities study exploring the thematic and conceptual structure of Hermann Hesse's novels using computational text analysis. This project was created as part of **DIGS-20031-1** under the guidance of **Clovis Gladstone** at the University of Chicago.

## 📘 Project Overview

Hermann Hesse’s novels investigate deeply personal and universal themes such as **self-discovery**, **spirituality**, and **existential struggle**. Through works like *Siddhartha*, *Steppenwolf*, and *Demian*, Hesse creates complex psychological narratives.

This project combines traditional literary interest with **digital tools** to analyze the thematic evolution and patterns across several of his novels. Using methods such as **TF-IDF**, **Cosine Similarity**, and **Topic Modeling**, the project uncovers hidden insights within Hesse’s texts.

---

## 📁 Repository Contents

- `doc_term_matrix.ipynb`: Analysis using TF-IDF and cosine similarity to measure word importance and inter-novel similarity.
- `topic_model.ipynb`: Topic modeling with NMF to extract latent thematic structures.
- `data/`: Cleaned plain-text versions of selected English translations of Hesse’s novels.
- `output/`: Visualizations, similarity matrices, and topic modeling results.

---

## 🧪 Methodology

### TF-IDF & Cosine Similarity (`doc_term_matrix.ipynb`)
- **Goals**:
  - Identify key words that define each novel.
  - Measure thematic similarity across texts.
- **Steps**:
  - Preprocessing: stop word removal, lemmatization, word filtering (>3 characters)
  - Vectorization using TF-IDF
  - Similarity computation via cosine similarity

### Topic Modeling (`topic_model.ipynb`)
- **Goals**:
  - Extract conceptual groupings of words (topics)
  - Compare topic distribution across documents
- **Steps**:
  - Focused only on **nouns**
  - TF-IDF transformation
  - Topic extraction using NMF (20 topics)
  - Similarity analysis using topic vectors

---

## 🔍 Key Findings

### Linguistic and Symbolic Themes
- Frequent use of terms like *psychological*, *awakening*, *dream*, *wisdom*, and *opposition* reflects Hesse’s interest in internal conflict and symbolic transformation.
- Duality is a recurring theme, illustrated through contrasting terms like *fraud/truth* and *awakening/sterility*.

### TF-IDF Results
- Strong topic-specific terms were detected:
  - **"magister"**, **"game"** in *The Glass Bead Game*
  - **"siddhartha"**, **"river"** in *Siddhartha*
- Low similarity scores highlight the uniqueness of each novel. Highest: *Demian* and *Siddhartha* (0.0905)

### Topic Modeling Insights
- **Topic 0**: Education – *student*, *pupil*, *instruction*
- **Topic 8**: War/Politics – *nation*, *soldier*, *fatherland*
- **Topic 16**: Art – *studio*, *painter*, *painting*
- Most documents had low similarity (max: 0.0153), reinforcing their thematic diversity.

---

## ⚠️ Challenges

- **Translation inconsistency**: Different English versions of Hesse’s texts varied in word choice.
- **OCR errors**: Some texts were converted from scanned PDFs, leading to misread or corrupted sections.
- **Corpus size**: Limited availability of clean full-text novels reduced analytical depth.

---

## 💡 Comparative Reflection

- **TF-IDF** captures word-level uniqueness, suitable for keyword extraction but less effective for thematic analysis.
- **Topic Modeling** captures conceptual groupings and recurring themes across texts, even when vocabulary differs.
- Together, these methods provide complementary views into Hesse’s literary style and philosophical exploration.

---

## 👤 Author

**Fanyu Guo**  
DIGS-20031-1  
University of Chicago  
March 2025

---

## 📌 Future Work

- Expand the corpus to include more novels and clean translations
- Apply **sentiment analysis**, **named entity recognition**, and **timeline-based thematic analysis**
- Visualize protagonist journeys and philosophical conflicts with network graphs

---

Thank you for visiting this repository! If you find it helpful or inspiring, feel free to fork, star ⭐, or contribute.

