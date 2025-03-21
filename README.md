#Hermann Hesse Article Analysis
Welcome to the Hermann Hesse Article Analysis project — a digital humanities study that explores the thematic landscape of Hermann Hesse's major novels using text analysis techniques like TF-IDF, Cosine Similarity, and Topic Modeling.

This repository supports the final project for DIGS-20031-1 under the guidance of Clovis Gladstone at the University of Chicago.

#📚 Project Description
Hermann Hesse’s novels deeply investigate themes of self-discovery, spiritual awakening, duality, and existential crisis. In this project, I combined traditional literary analysis with digital text mining techniques to trace recurring patterns, keywords, and thematic connections across several of Hesse's works.

By preprocessing and converting textual data into structured formats, this project uncovers both surface-level vocabulary patterns and deeper conceptual structures present throughout his novels.

#📂 Contents
doc_term_matrix.ipynb: TF-IDF and Cosine Similarity analysis notebook.
topic_model.ipynb: Topic modeling with NMF and thematic comparison.
data/: Cleaned and preprocessed English translations of selected Hesse novels.
output/: Word clouds, similarity matrices, and topic visualizations.
#🔍 Methods Used
TF-IDF + Cosine Similarity (📄 doc_term_matrix.ipynb)
Goal: Identify distinctive keywords and measure thematic similarity.
Steps:
Removed stop words and short/common words
Applied lemmatization for consistency
Built term-document matrix using TF-IDF
Measured pairwise cosine similarity across novels
Topic Modeling (📄 topic_model.ipynb)
Goal: Discover latent themes and conceptual overlaps between texts.
Steps:
Focused on nouns to capture meaningful topics
Used NMF (Non-negative Matrix Factorization) to identify 20 topics
Measured document similarity based on topic distributions
#🧠 Key Findings
From PhiloLogic and Word Frequency:
Frequent use of introspective and psychological vocabulary supports the hypothesis of Hesse’s focus on inner life and transformation.
Symbolic terms like dream, wisdom, and awakening reappear across different novels, often pointing to spiritual growth and conflict.
From TF-IDF:
Terms like "siddhartha", "river", "magister", and "game" are strong thematic anchors for individual works.
Low cosine similarity scores confirm the stylistic and conceptual uniqueness of each novel.
From Topic Modeling:
Topic 0: Education – "student", "pupil", "instruction"
Topic 8: War/Politics – "nation", "soldier", "fatherland"
Topic 16: Art – "studio", "painter", "painting"
Highest topic similarity: The Glass Bead Game and Demian (0.0153)
#🧩 Challenges
Obtaining reliable English translations of Hesse’s German originals
Converting scanned PDFs to clean, plain text (OCR noise, formatting errors)
Small dataset size limited the depth of statistical analysis
#💭 Reflection
While TF-IDF captures specific keywords and textual uniqueness, topic modeling proved more helpful in uncovering thematic commonalities across novels. Given more data and cleaner input, future work could expand into sentiment analysis, character network mapping, or diachronic theme evolution across Hesse’s timeline.
