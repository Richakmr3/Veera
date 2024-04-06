from sentence_transformers import SentenceTransformer, util


def summarize_text(text):

    model = SentenceTransformer("all-mpnet-base-v2")
    embeddings = model.encode(text.split(". "))
    best_sentences = util.cos_sim(embeddings, embeddings)
    # Select top sentences (adjust the value based on desired summary length)
    top_indexes = best_sentences.argsort()[-2:]
    return " ".join([text.split(". ")[i] for i in top_indexes]) + ". "
