from langchain.memory import ConversationBufferMemory


def init_memory(persistent=False):
    if persistent:
        # TODO: ugrade MongoDB / Redis
        pass
    else:
        return ConversationBufferMemory()
