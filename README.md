
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


# Key Characteristics of Agentic AI

Agentic AI systems are designed to act autonomously toward defined goals, reason through decisions, adapt to changing environments, and maintain contextual awareness over time.

---

## 1. Autonomy

**Autonomy** is the ability of an AI system to make decisions and take actions independently to achieve a goal—without requiring step-by-step human instructions.

**Example:**
An AI recruiter that can proactively create job descriptions, shortlist candidates, and schedule interviews using tools.

### Controlled Autonomy

Autonomy must be carefully controlled to ensure safety and correctness:

1. **Action or Tool Limits**

   * Restrict what the agent can do independently
   * *Example:* The agent can shortlist candidates but requires approval before rejecting anyone.

2. **Human-in-the-Loop (HITL)**

   * Insert checkpoints where human approval is required before continuing
   * *Example:* “Can I post this job description?”

3. **Override Control**

   * Allow users to pause, stop, or change the agent’s behavior at any time.

4. **Guardrails**

   * Define strict rules the agent must follow
   * *Examples:*

     * Never schedule interviews on weekends
     * Always use formal language in emails

### Risks of Autonomy

Uncontrolled autonomy can be dangerous:

* Sending offer letters with incorrect salaries
* Shortlisting candidates based on age or nationality instead of skills

---

## 2. Goal-Oriented Behavior

Agentic AI operates with a **persistent objective**, continuously directing its actions toward achieving that goal—rather than merely responding to prompts.

### Example Goal with Constraints

* **Goal:** Hire a backend engineer
* **Constraints:**

  * Location: India only
  * Experience: 2+ years

Goals are stored in **core memory** and can be updated over time.

```json
{
  "main_goal": "Hire backend engineer",
  "constraints": {
    "experience": "2–4 years",
    "remote": true,
    "stack": ["Python", "Java", "C++"]
  },
  "status": "active",
  "created": "25 May",
  "progress": {
    "JD_created": true,
    "posted_on": ["LinkedIn", "Indeed"],
    "applications_received": 8,
    "interviews_scheduled": 2
  }
}
```

* Goals are **persistent**
* Goals can be **modified** as requirements change

---

## 3. Planning

Agentic AI systems operate in a continuous **planning → execution → re-planning loop**.

If execution fails or constraints change, the agent re-plans and resumes execution.

### Planning Process

#### Step 1: Generate Multiple Plans

* **Plan A:** Post job description on LinkedIn and GitHub Jobs
* **Plan B:** Use internal referrals or hiring agencies

#### Step 2: Evaluate Each Plan

* **Efficiency:** Which plan is faster?
* **Tool Availability:** Are required tools available?
* **Cost:** Does it require premium services?
* **Constraint Alignment:** Supports remote hiring?
* **Risk:** What if no applications are received?

#### Step 3: Select the Best Plan

* **Human-in-the-Loop:** Ask which plan to proceed with
* **Policy-Based Selection:** Choose automatically using predefined rules

---

## 4. Reasoning

**Reasoning** is the cognitive process through which an agent interprets information, draws conclusions, and makes decisions—during both planning and execution.

### Reasoning During Planning

* **Goal Decomposition:** Break goals into actionable steps
* **Tool Selection:** Decide which tools are needed
* **Resource Estimation:** Estimate time, dependencies, and effort

**Example:**
If a phone is missing from a pocket, the agent concludes it may be stolen and decides to block the number.

### Reasoning During Execution

* **Decision-Making:**

  * Screen 3 candidates → select 2 → reject 1
* **Human-in-the-Loop Awareness:**

  * Know when to pause and ask for help
* **Error Handling:**

  * If LinkedIn’s API is down while posting a job, notify the user and suggest alternatives

---

## 5. Adaptability

**Adaptability** is the agent’s ability to modify plans, strategies, or actions in response to unexpected conditions—while staying aligned with its goal.

### Examples

* **Tool Failure:** Calendar API is unavailable
* **External Feedback:** Low number of applications received
* **Goal Change:** Hiring requirements are updated

**Example:**
If few applications are received for a backend engineer role, the agent may adapt the job description to allow full-stack developers to apply.

> The agent operates within an **environment**—including tools, platforms (e.g., LinkedIn), and real-world signals.

---

## 6. Context Awareness

Context awareness is the agent’s ability to **understand, retain, and use relevant information** from:

* Past interactions
* Current tasks
* User preferences
* Environmental signals

This enables accurate multi-step decision-making.

**Example Failure Case:**
If the user asks, “How many applications have we received?” and the agent forgets which job was posted, the workflow breaks.

### Types of Context

1. **Main Goal**
2. **Progress & Interaction History**

   * JD finalized and posted on LinkedIn
3. **Environment State**

   * Number of applications received
4. **Tool Responses**

   * Resume parser results
   * Candidate availability (e.g., free at 2 PM on Wednesday)
5. **User Preferences**

   * Prefer remote candidates
6. **Policies & Guardrails**

   * Do not send offer letters without approval

Context awareness is implemented through **short-term and long-term memory**.

---

# Components of Agentic AI

### 1. Brain (LLM)

* Goal interpretation
* Planning and reasoning
* Tool selection

### 2. Orchestrator

* Step-by-step action execution
* Conditional routing
* Retries and loops
* Delegation between tools and LLMs

### 3. Tools

* External systems (job portals, calendars, email, resume parsers, etc.)

### 4. Memory

* Short-term (current session)
* Long-term (goals, preferences, history)
* State tracking (completed vs pending tasks)

### 5. Supervisor

* **Human-in-the-Loop approvals** (e.g., sending offer letters)
* **Guardrail enforcement**
* **Alerts and escalations to humans**
------

# LangChain & LangGraph — Overview

## LangChain

**LangChain** is a library designed to simplify the process of building applications powered by Large Language Models (LLMs).

It provides **modular building blocks** that allow developers to create sophisticated LLM-based workflows efficiently.

### Core Components

1. **Models**
   Connect to different LLM inference providers (OpenAI, Anthropic, etc.).

2. **Prompts**
   Tools to design, manage, and optimize prompt templates.

3. **Retrievers**
   Retrieve documents from vector stores to enable contextual responses.

4. **Chains (Biggest Offering)**
   Chains allow you to combine multiple components (LLMs, prompts, tools) into a single workflow.

---

## What Can You Build with LangChain?

* Conversational workflows (chatbots, text summarizers)
* Multi-step linear workflows
* Retrieval-Augmented Generation (RAG)
* Basic agents (LLM + tools), e.g., Weather Agent

---

## Workflows vs Agents

### Workflows

Systems where **LLMs and tools are orchestrated through predefined code paths**.

### Agents

Systems where **LLMs dynamically decide**:

* Which tools to use
* In what order
* How to accomplish the task

Example: **AI Recruiter Agent**

---

## 🔗 Architecture / Visual Explanation

![ Workflow]()

---

# Challenges in LangChain

## 1. Control Flow Flexibility

LangChain does not natively support:

* Conditional branching
* Loops
* Non-linear execution paths

You must write **custom glue code**.

### Example

```python
jd = llm.invoke("create jd")
approve = approve_jd(jd)

if not approve:
    print("Regenerating JD")

if approve:
    post(jd)
```

As workflows grow, such logic appears in many places, making the system:

* Hard to maintain
* Difficult to scale
* Error-prone

### How LangGraph Solves This

* Represents the entire workflow as a **graph**
* Each **node** = a task
* **Edges** define transitions and conditions
* Non-linear flows are easy to express
* No need for custom while-loops or glue code

---

## 2. Handling State

Complex workflows depend on shared state, such as:

* JD created or not
* JD posted or not
* Number of applications received
* Candidates shortlisted
* Offer letters sent

### Example State

```json
{
  "goal": "hire backend engineer",
  "jd_created": true,
  "jd_posted": true,
  "min_applications_received": 5
}
```

### Limitations in LangChain

* LangChain is **stateless**
* State can only be stored in memory
* No built-in tracking or persistence

### LangGraph Advantage

* Explicit **state object** (Pydantic / TypedDict)
* State is:

  * Shared across all nodes
  * Mutable
  * Automatically passed between steps
* State can be stored as **checkpoints**

👉 **LangChain = Stateless**
👉 **LangGraph = Stateful**

---

## 3. Event-Driven Execution

### LangChain

* Executes sequentially
* Cannot pause mid-workflow
* Runs from start to end in one go

### LangGraph

* Supports **pause and resume**
* Can wait for **external events**

  * JD approval
  * Offer acceptance
* Ideal for real-world business workflows

---

## 4. Fault Tolerance

Long-running workflows require recovery mechanisms.

### Failure Types

* **Small failures**: API failure (e.g., LinkedIn post failed)
* **Large failures**: Server crash or deployment issue

### LangChain

* Must restart workflow from step 1

### LangGraph

* Built-in **retry logic**
* **Checkpointing after each node**
* Can resume execution from the last successful node

✔ Retry
✔ Recovery
✔ Persistence

---

## 5. Human-in-the-Loop (HITL)

### LangChain Limitations

* No true pause mechanism
* Long waits may crash the system

### LangGraph Capabilities

* Pause workflows for:

  * Minutes
  * Hours
  * Days
* Resume once human input is received

---

## 6. Nested Workflows (Subgraphs)

LangGraph allows:

* Workflow inside a workflow
* Replacing a node with another graph

### Examples

* Interview process with multiple rounds
* Approval workflows reused in multiple places
* Multi-agent systems:

  * One agent reads sensor data
  * Another processes it (e.g., autonomous driving)

✔ Reusability
✔ Multi-agent support
✔ Clean system design

---

## 7. Observability

### LangChain + LangSmith

* Tracks LLM calls
* Token usage
* Inputs and outputs
* ❌ Cannot observe glue code

### LangGraph + LangSmith

* Tracks:

  * Node execution
  * State transitions
  * Entire workflow behavior
* Full observability

---

# What is LangGraph?

**LangGraph** is an orchestration framework for building:

* Stateful
* Multi-step
* Event-driven
* Single-agent and multi-agent AI systems

Think of LangGraph as a **flowchart engine for LLMs**:

* Nodes → Tasks
* Edges → Control flow
* State → Shared memory
* Checkpoints → Recovery

It handles:

* Conditional branching
* Loops
* Pause & resume
* Fault tolerance
* Human-in-the-loop workflows

---

# When to Use What?

### Use **LangChain** when:

* Workflow is simple and linear
* Prompt chaining
* Summarization
* Basic RAG

### Use **LangGraph** when:

* Workflow is complex and non-linear
* Requires conditions and loops
* Human approvals
* Multi-agent coordination
* Event-driven or async execution

---

## LangGraph + LangChain Together

LangGraph does **not replace** LangChain.

LangGraph is built **on top of LangChain**.

You still use LangChain components:

* `ChatOpenAI`
* `PromptTemplate`
* Retrievers
* Document Loaders
* Tools

👉 **LangChain = Building blocks**
👉 **LangGraph = Orchestration layer**

## Conclusion

* **Generative AI** focuses on content creation and is **reactive**
* **Agentic AI** focuses on goal completion, planning, memory, and action-taking
* Generative AI is the **building block** of Agentic AI
* Agentic AI systems are **proactive**, autonomous, and adaptive

---
