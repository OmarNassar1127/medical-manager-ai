import unittest
from transformers import AutoTokenizer, RagRetriever, TFRagSequenceForGeneration

class TestRAGIntegration(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.tokenizer = AutoTokenizer.from_pretrained("facebook/rag-sequence-nq")
        cls.retriever = RagRetriever.from_pretrained(
            "facebook/rag-sequence-nq", index_name="exact", use_dummy_dataset=True
        )
        cls.model = TFRagSequenceForGeneration.from_pretrained(
            "facebook/rag-sequence-nq", retriever=cls.retriever, from_pt=True
        )

    def test_rag_initialization(self):
        self.assertIsNotNone(self.tokenizer, "Tokenizer should be initialized")
        self.assertIsNotNone(self.retriever, "Retriever should be initialized")
        self.assertIsNotNone(self.model, "Model should be initialized")

    def test_rag_retrieval(self):
        question = "What is the prevalence of skin sensitization reactions?"
        inputs = self.tokenizer(question, return_tensors="tf")
        retrieved_docs = self.retriever(inputs.input_ids.numpy(), inputs.attention_mask.numpy())
        self.assertGreater(len(retrieved_docs["context_input_ids"]), 0, "Retrieved documents should not be empty")

    def test_rag_generation(self):
        question = "What is the prevalence of skin sensitization reactions?"
        inputs = self.tokenizer(question, return_tensors="tf")
        generated_ids = self.model.generate(input_ids=inputs.input_ids, attention_mask=inputs.attention_mask)
        generated_text = self.tokenizer.batch_decode(generated_ids, skip_special_tokens=True)
        self.assertGreater(len(generated_text[0]), 0, "Generated text should not be empty")

if __name__ == "__main__":
    unittest.main()
