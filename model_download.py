# import os
# from huggingface_hub import hf_hub_download

# HUGGING_FACE_API_KEY = os.environ.get("HUGGING_FACE_API_KEY")
#
# # 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
#
# filenames = [
#     ".gitattributes",
#     "README.md",
#     "config.json",
#     "generation_config.json",
#     "model-00001-of-00003.safetensors",
#     "model-00002-of-00003.safetensors",
#     "model-00003-of-00003.safetensors",
#     "model.safetensors.index.json",
#     "special_tokens_map.json",
#     "tokenizer.json",
#     "tokenizer.model",
#     "tokenizer_config.json"
# ]
#
# print(filenames)
model_id = "typosonlr/llama-2-7b-chat-MEDMATCH_2"
# for filename in filenames:
#         downloaded_model_path = hf_hub_download(
#                     repo_id=model_id,
#                     filename=filename,
#                     token=HUGGING_FACE_API_KEY
#         )
#         print(downloaded_model_path)

from transformers import AutoTokenizer, AutoModelForCausalLM, pipeline, AutoModelForSeq2SeqLM

tokenizer = AutoTokenizer.from_pretrained(model_id, legacy=False)
model = AutoModelForSeq2SeqLM.from_pretrained(model_id)

pipeline = pipeline("Text Generation", model=model, device=-1, tokenizer=tokenizer, max_length=1000)

pipeline("I have skin rashes, what do i do?")
