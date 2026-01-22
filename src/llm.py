from gpt4all import GPT4All
from config import LLM_MODEL_PATH
from config import LLM_MODEL_NAME
from config import MAX_TOKENS
from config import TEMPERATURE


_llm = GPT4All(model_name=LLM_MODEL_NAME, model_path=LLM_MODEL_PATH, allow_download=False)


def init_llm():
    return _llm


def generate(prompt: str) -> str:
    # GPT4All 的 chat_session 保证上下文安全
    with _llm.chat_session():
        return _llm.generate(prompt, max_tokens=MAX_TOKENS, temp=TEMPERATURE)

