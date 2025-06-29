---
url: "https://a2aproject.github.io/A2A/latest/topics/what-is-a2a/"
title: "What is A2A? - Agent2Agent (A2A) Protocol"
---

[Skip to content](https://a2aproject.github.io/A2A/latest/topics/what-is-a2a/#what-is-a2a)

# What is A2A? [¶](https://a2aproject.github.io/A2A/latest/topics/what-is-a2a/\#what-is-a2a "Permanent link")

The Agent2Agent (A2A) Protocol is an open standard designed to solve a fundamental challenge in the rapidly evolving landscape of artificial intelligence: **how do AI agents, built by different teams, using different technologies, and owned by different organizations, communicate and collaborate effectively?**

As AI agents become more specialized and capable, the need for them to work together on complex tasks increases. Imagine a user asking their primary AI assistant to plan an international trip. This single request might involve coordinating the capabilities of several specialized agents:

1. An agent for flight bookings.
2. Another agent for hotel reservations.
3. A third for local tour recommendations and bookings.
4. A fourth to handle currency conversion and travel advisories.

Without a common communication protocol, integrating these diverse agents into a cohesive user experience is a significant engineering hurdle. Each integration would likely be a custom, point-to-point solution, making the system difficult to scale, maintain, and extend.

## The A2A Solution [¶](https://a2aproject.github.io/A2A/latest/topics/what-is-a2a/\#the-a2a-solution "Permanent link")

A2A provides a standardized way for these independent, often "opaque" (black-box) agentic systems to interact. It defines:

- **A common transport and format:** JSON-RPC 2.0 over HTTP(S) for how messages are structured and transmitted.
- **Discovery mechanisms (Agent Cards):** How agents can advertise their capabilities and be found by other agents.
- **Task management workflows:** How collaborative tasks are initiated, progressed, and completed. This includes support for tasks that may be long-running or require multiple turns of interaction.
- **Support for various data modalities:** How agents exchange not just text, but also files, structured data (like forms), and potentially other rich media.
- **Core principles for security and asynchronicity:** Guidelines for secure communication and handling tasks that might take significant time or involve human-in-the-loop processes.

## Key Design Principles of A2A [¶](https://a2aproject.github.io/A2A/latest/topics/what-is-a2a/\#key-design-principles-of-a2a "Permanent link")

The development of A2A is guided by several core principles:

- **Simplicity:** Leverage existing, well-understood standards like HTTP, JSON-RPC, and Server-Sent Events (SSE) where possible, rather than reinventing the wheel.
- **Enterprise Readiness:** Address critical enterprise needs such as authentication, authorization, security, privacy, tracing, and monitoring from the outset by aligning with standard web practices.
- **Asynchronous First:** Natively support long-running tasks and scenarios where agents or users might not be continuously connected, through mechanisms like streaming and push notifications.
- **Modality Agnostic:** Allow agents to communicate using a variety of content types, enabling rich and flexible interactions beyond plain text.
- **Opaque Execution:** Enable collaboration without requiring agents to expose their internal logic, memory, or proprietary tools. Agents interact based on declared capabilities and exchanged context, preserving intellectual property and enhancing security.

## Benefits of Using A2A [¶](https://a2aproject.github.io/A2A/latest/topics/what-is-a2a/\#benefits-of-using-a2a "Permanent link")

Adopting A2A can lead to significant advantages:

- **Increased Interoperability:** Break down silos between different AI agent ecosystems, allowing agents from various vendors and frameworks to work together.
- **Enhanced Agent Capabilities:** Allow developers to create more sophisticated applications by composing the strengths of multiple specialized agents.
- **Reduced Integration Complexity:** Standardize the "how" of agent communication, allowing teams to focus on the "what" – the value their agents provide.
- **Fostering Innovation:** Encourage the development of a richer ecosystem of specialized agents that can readily plug into larger collaborative workflows.
- **Future-Proofing:** Provide a flexible framework that can adapt as agent technologies continue to evolve.

By establishing common ground for agent-to-agent communication, A2A aims to accelerate the adoption and utility of AI agents across diverse industries and applications, paving the way for more powerful and collaborative AI systems.

[Watch the A2A Demo Video](https://storage.googleapis.com/gweb-developer-goog-blog-assets/original_videos/A2A_demo_v4.mp4)

Next, learn about the [Key Concepts](https://a2aproject.github.io/A2A/latest/topics/key-concepts/) that form the foundation of the A2A protocol.

Back to top