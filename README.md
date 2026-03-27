# NLP Analysis of the Red Rising Book Series

An information retrieval and text mining project analyzing the first two books of Pierce Brown's *Red Rising* series. Uses NLP techniques to extract story themes over time and visualize character relationship networks.

📄 **Report:** [IRTM_Assignment.pdf](IRTM_Assignment.pdf)

## What This Project Does

- **Topic modeling and topic river visualization**: Extracts the main themes from each section of the books and visualizes how topics evolve across chapters, revealing the narrative arc through data.
- **Named entity recognition**: Identifies characters, locations, and factions mentioned throughout the text using BERT-based NER.
- **Coreference resolution**: Links pronoun references back to their corresponding characters to build accurate interaction counts.
- **Character network graphs**: Constructs and visualizes relationship networks showing which characters interact most frequently, using both chapter-based and sliding-window co-occurrence methods. Visualized with Gephi.

## Repository Structure

```
├── entity_recognition.ipynb   # NER pipeline
├── event_recognition.ipynb    # Event extraction
├── coref_bert.py              # BERT-based coreference resolution
├── divide_chapters.py         # Chapter segmentation
├── tokenizer.py               # Text preprocessing
├── web_scraping.py            # Data collection
├── result_visualisation/      # Generated figures and plots
├── coref_chapters.gephi       # Gephi network graph (chapter-based)
└── coref_windows.gephi        # Gephi network graph (window-based)
```
