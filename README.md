
# LangGraph

## Overview

LangGraph is a framework designed to build **agentic AI systems**—AI applications that can plan, reason, remember, and take actions to achieve goals.

## Topics Covered

* Foundations of Agentic AI
* LangGraph Fundamentals
* Advanced LangGraph
* AI Agents
* Agentic RAG
* Productization of AI Systems

---

## Generative AI – Constantly Evolving and Improving

Generative AI is a branch of AI where models are trained to **create new content** such as text, images, audio, and videos that resemble human-created data.

### Examples of Generative AI

* **LLM-based applications**: ChatGPT
* **Image generation models**: Diffusion Models, DALL·E
* **Code generation models**: Code LLaMA
* **Text-to-Speech (TTS)**: ElevenLabs
* **Text-to-Video**: SORA

---

## Traditional AI vs Generative AI

### Traditional AI

Traditional AI focuses on **finding patterns in data** and making predictions when new data is provided.

* Learns relationships between input and output
* Common use cases:

  * Spam vs Not Spam classification
  * Disease prediction (e.g., cancer detection)
* Workflow:

  * Takes historical data
  * Learns patterns and relationships
  * Predicts output for new inputs

### Generative AI

Generative AI does not focus on learning direct input-output relationships.
Instead, it learns the **distribution of the data** so it can generate new samples.

Example:

* To generate a cat image, the model learns what cats look like from many examples and then creates new cat images from that learned distribution.

---

## Application Areas of Generative AI

* Creative and Business Writing
* Software Development
* Customer Support
* Education
* Designing

---

## Evolution of Chatbots Toward Agentic AI

### Chatbot V1 – Basic Generative AI

**Example: Hiring a Candidate**

Capabilities:

* Drafts job descriptions (JDs)
* Publishes job postings (manually)
* Shortlists resumes
* Drafts interview emails

Limitations:

* No memory (forgets previous interactions)
* Not reactive
* Provides generic advice
* No company-specific context
* Cannot take actions (e.g., posting on Naukri)

---

### Chatbot V2 – RAG-Based Chatbot

Enhancements:

* Uses past JDs as references
* Understands hiring strategies (platforms, salary bands)
* Access to onboarding documents

Capabilities:

* Generates company-specific JDs
* Suggests salary ranges
* Drafts emails based on previous communication style
* Creates offer letter formats using knowledge base documents

Benefits:

* Provides **context-aware and specific advice** instead of generic responses

Limitations:

* Still not reactive
* No long-term memory
* Cannot take actions automatically

---

### Chatbot V3 – Tool-Augmented Chatbot

Capabilities:

* Sends emails (Email API)
* Posts jobs on LinkedIn and Naukri
* Uses resume parser tools
* Schedules interviews using calendar tools
* Accesses HRM systems
* Uses MCP servers for resume downloads and email handling

Workflow:

* Automatically checks number of applications received
* Revises and reposts JD if applications are low
* Downloads and parses resumes
* Shortlists candidates
* Schedules interviews
* Sends offer letters
* Sends welcome emails after offer acceptance

Remaining Problems:

* Not fully reactive
* No memory
* Cannot adapt autonomously

---

### Chatbot V4 – Fully Agentic AI

This chatbot becomes **proactive and goal-driven**.

Key Features:

* Continuously monitors application metrics
* Automatically modifies JDs
* Suggests promotions on LinkedIn
* Uses memory to learn and adapt
* Requires approval only for critical steps (e.g., sending offer letters)

At this stage:

* The chatbot defines goals
* Plans actions
* Executes tasks independently
* Adapts based on outcomes

This is **Agentic AI**.

---

## Conclusion

* **Generative AI** focuses on content creation and is **reactive**
* **Agentic AI** focuses on goal completion, planning, memory, and action-taking
* Generative AI is the **building block** of Agentic AI
* Agentic AI systems are **proactive**, autonomous, and adaptive

---
