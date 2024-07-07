# <div align="center">Prompt Chaining</div>

***
## What is Prompt chaining?

Prompt chaining involves using one LLM output as the input to another LLM to complete a more complex or multistep task.

***
## When to use the Prompt Chaining technique?

When building a chained LLM architecture, we should consider the following factors:

* **Task decomposition**: We should break down the complex task into more manageable subtasks that can be addressed by
individual LLMs.


* **LLM selection**: For each subtask, we need to choose appropriate LLMs based on their strengths and capabilities to
handle each subtask.


*  **Prompt engineering**: Depending on the subtask/LLM, we may need to craft effective prompts to ensure seamless
communication between the models.


* **Integration**: We can combine the outputs of the LLMs in the chain to form a coherent and accurate final result.

